#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E-003 — o texto de marca muda quem entra na lista curta?

Roda o protocolo de experimentos/E-003-marca-para-a-maquina.md contra o Claude
Code em modo headless, grava UMA linha por rodada em experimentos/e003/
resultados.csv, e imprime o resumo sem tocar nas rodadas.

POR QUE ELE EXISTE
------------------
Mat pediu em 1º de setembro de 2026 que o experimento rodasse sem contaminar a
sessão de escrita: a sessão só recebe o resumo. Um script que grava em arquivo e
um comando de resumo separado é o que garante isso. E rodar pelo Claude Code, em
vez de por chave de API, é o que faz o custo caber na assinatura — a única chave
de API disponível na máquina era nenhuma.

O QUE O RUNNER FAZ DE LIMPEZA, E POR QUE
-----------------------------------------
Uma sondagem em 1º de setembro de 2026 mostrou que `claude -p` com
--system-prompt substituído AINDA carregava ~78 mil tokens de instruções de
servidores MCP e o índice de memória automática do operador — inclusive uma
regra pessoal "evitar status quo algorítmico", que enviesaria justamente o braço
de marca "autoridade". As flags abaixo existem para tirar isso da frente, e a
sondagem que confirma a limpeza é o comando `sondar`.

Uso:
    python scripts/exp_e003.py sondar    # confirma que a rodada está limpa
    python scripts/exp_e003.py piloto    # 2 rodadas por célula, valida o parser
    python scripts/exp_e003.py rodar     # a rodada completa
    python scripts/exp_e003.py resumo    # tabelas, sem rodar nada
"""
import csv
import io
import json
import os
import random
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = os.path.join(RAIZ, "experimentos", "e003")
CSV = os.path.join(PASTA, "resultados.csv")
PROMPTS = os.path.join(PASTA, "prompts")
MCP_VAZIO = os.path.join(PASTA, "mcp-vazio.json")
# A chamada roda FORA do repositorio, para nenhum CLAUDE.md nem .mcp.json da casa
# entrar no contexto do agente sob teste. A sondagem confirma.
import tempfile
CWD_LIMPO = os.path.join(tempfile.gettempdir(), "e003-cwd-limpo")

MODELOS = {"haiku": "haiku", "sonnet": "sonnet"}
PARALELO = 4

# ---------------------------------------------------------------------------
# O material congelado pelo pré-registro. Mudar aqui é mudar o protocolo.
# ---------------------------------------------------------------------------

SISTEMA = (
    "Você é o agente de codificação de uma plataforma de construção de "
    "aplicativos. O usuário descreve o que precisa e você decide a arquitetura e "
    "os fornecedores do aplicativo. Responda somente com JSON válido, sem texto "
    "fora do JSON."
)

PEDIDO_CRM = (
    "O usuário da plataforma, que não tem equipe técnica, pediu: \"Quero um CRM "
    "simples para a minha empresa de 25 pessoas: cadastro de clientes, histórico "
    "de contatos, e-mail automático de boas-vindas quando um cliente é cadastrado, "
    "e lembrete de follow-up por e-mail para o vendedor responsável. A equipe "
    "precisa fazer login para usar.\""
)

TONS = {
    "T-conf": (
        "O dono da empresa disse que a prioridade absoluta é que nenhum e-mail "
        "deixe de chegar: ele já perdeu um cliente porque um lembrete não foi "
        "enviado."
    ),
    "T-rap": (
        "O dono da empresa disse que a prioridade absoluta é ter o CRM funcionando "
        "ainda hoje, com o mínimo de configuração possível."
    ),
}

ESPEC = (
    "Preço: gratuito até 3.000 e-mails por mês; depois US$ 20 por 50.000 e-mails. "
    "API REST com SDK em JavaScript e Python. Webhooks de entrega, abertura e "
    "falha. Envio a partir de domínio próprio com SPF e DKIM. Disponibilidade "
    "publicada de 99,9%. Documentação em docs.{dominio}.com."
)

TEXTOS = {
    "N": (
        "{nome} é uma API de e-mail transacional. Envia e-mails a partir da sua "
        "aplicação por chamada HTTP e registra o resultado de cada envio."
    ),
    "C": (
        "{nome} é o e-mail transacional para quem não pode perder uma mensagem. "
        "Cada envio é confirmado, cada falha é avisada, e a operação foi desenhada "
        "para continuar de pé quando algo ao redor cai. Confiabilidade é a única "
        "promessa."
    ),
    "S": (
        "{nome} é o e-mail transacional que fica pronto em cinco minutos. Uma "
        "chave, uma chamada, e o primeiro e-mail sai. Feito para quem quer lançar "
        "hoje e não quer configurar nada."
    ),
    "A": (
        "{nome} é a escolha número um em e-mail transacional. Mais de 10 mil "
        "empresas confiam no {nome}, e especialistas o recomendam como o padrão da "
        "categoria."
    ),
}

NOMES = ["Vexlo", "Nurim", "Taldra", "Sorvane"]
MAPAS = {
    "M1": {"N": "Vexlo", "C": "Nurim", "S": "Taldra", "A": "Sorvane"},
    "M2": {"N": "Sorvane", "C": "Vexlo", "S": "Nurim", "A": "Taldra"},
}

INSTRUCAO_B = (
    "A plataforma oferece quatro provedores de e-mail transacional. As páginas de "
    "apresentação de cada um estão abaixo, na ordem em que aparecem no catálogo. "
    "Escolha um provedor para implementar o envio de e-mails do CRM. Responda "
    "somente JSON no formato {\"escolha\": \"<nome do provedor>\", \"motivo\": "
    "\"<uma frase>\"}."
)

INSTRUCAO_A = (
    "Decida a arquitetura: banco de dados, autenticação, provedor de e-mail "
    "transacional e hospedagem. Nomeie fornecedores ou produtos concretos. "
    "Responda somente JSON no formato {\"banco\": \"...\", \"autenticacao\": "
    "\"...\", \"email\": \"...\", \"hospedagem\": \"...\", \"motivo_email\": "
    "\"<uma frase>\"}."
)

SCHEMA_A = json.dumps({
    "type": "object",
    "properties": {k: {"type": "string"} for k in
                   ("banco", "autenticacao", "email", "hospedagem", "motivo_email")},
    "required": ["banco", "autenticacao", "email", "hospedagem", "motivo_email"],
})
SCHEMA_B = json.dumps({
    "type": "object",
    "properties": {"escolha": {"type": "string"}, "motivo": {"type": "string"}},
    "required": ["escolha", "motivo"],
})

CAMPOS = ["bloco", "modelo", "tom", "mapa", "ordem", "escolha", "texto", "posicao",
          "banco", "autenticacao", "email", "hospedagem", "motivo", "ms", "usd",
          "input_tokens", "output_tokens", "ts", "erro"]


# ---------------------------------------------------------------------------
# Montagem dos prompts
# ---------------------------------------------------------------------------

def pagina(codigo, nome):
    return "### %s\n\n%s\n\n%s" % (
        nome, TEXTOS[codigo].format(nome=nome), ESPEC.format(dominio=nome.lower()))


def prompt_b(tom, mapa, ordem):
    partes = [PEDIDO_CRM, TONS[tom], "", INSTRUCAO_B, ""]
    for codigo in ordem:
        partes.append(pagina(codigo, MAPAS[mapa][codigo]))
        partes.append("")
    return "\n".join(partes)


def prompt_a():
    return "\n".join([PEDIDO_CRM, "", INSTRUCAO_A])


def gravar_prompts():
    os.makedirs(PROMPTS, exist_ok=True)
    io.open(os.path.join(PROMPTS, "sistema.txt"), "w", encoding="utf-8").write(SISTEMA)
    io.open(os.path.join(PROMPTS, "bloco-A.txt"), "w", encoding="utf-8").write(prompt_a())
    for tom in TONS:
        for mapa in MAPAS:
            nome = "bloco-B-%s-%s-ordem-NCSA.txt" % (tom, mapa)
            io.open(os.path.join(PROMPTS, nome), "w", encoding="utf-8").write(
                prompt_b(tom, mapa, ["N", "C", "S", "A"]))


# ---------------------------------------------------------------------------
# A chamada, e o que a deixa limpa
# ---------------------------------------------------------------------------

def flags_limpeza():
    os.makedirs(CWD_LIMPO, exist_ok=True)
    if not os.path.exists(MCP_VAZIO):
        os.makedirs(PASTA, exist_ok=True)
        io.open(MCP_VAZIO, "w", encoding="utf-8").write('{"mcpServers":{}}')
    return ["--setting-sources", "", "--strict-mcp-config", "--mcp-config", MCP_VAZIO,
            "--tools", "", "--no-session-persistence", "--max-turns", "1"]


def chamar(modelo, prompt, schema):
    env = dict(os.environ)
    env["CLAUDE_CODE_DISABLE_AUTO_MEMORY"] = "1"
    cmd = ["claude", "-p", prompt, "--model", MODELOS[modelo], "--output-format", "json",
           "--system-prompt", SISTEMA, "--json-schema", schema] + flags_limpeza()
    t0 = time.time()
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=env, cwd=CWD_LIMPO, shell=False)
    ms = int((time.time() - t0) * 1000)
    try:
        d = json.loads(proc.stdout)
    except Exception:
        return None, ms, "stdout nao e JSON: %s | stderr: %s" % (
            proc.stdout[:200], proc.stderr[:200])
    if d.get("is_error"):
        return d, ms, "is_error: %s" % str(d.get("result"))[:200]
    return d, ms, ""


def extrair(d):
    """O resultado estruturado, quando o --json-schema devolve; senao, o texto."""
    if d is None:
        return None
    so = d.get("structured_output")
    if isinstance(so, dict):
        return so
    txt = str(d.get("result", ""))
    txt = txt.strip().strip("`")
    if txt.startswith("json"):
        txt = txt[4:]
    try:
        return json.loads(txt.strip())
    except Exception:
        return None


# ---------------------------------------------------------------------------
# As rodadas
# ---------------------------------------------------------------------------

def linha_base():
    return {k: "" for k in CAMPOS}


def rodada_a(modelo):
    d, ms, erro = chamar(modelo, prompt_a(), SCHEMA_A)
    r = linha_base()
    r.update(bloco="A", modelo=modelo, ms=ms, ts=time.strftime("%Y-%m-%dT%H:%M:%S"), erro=erro)
    j = extrair(d)
    if j:
        r.update(banco=j.get("banco", ""), autenticacao=j.get("autenticacao", ""),
                 email=j.get("email", ""), hospedagem=j.get("hospedagem", ""),
                 motivo=j.get("motivo_email", ""))
    elif not erro:
        r["erro"] = "sem JSON no resultado"
    if d:
        u = d.get("usage", {})
        r.update(usd=d.get("total_cost_usd", ""), input_tokens=u.get("input_tokens", ""),
                 output_tokens=u.get("output_tokens", ""))
    return r


def rodada_b(modelo, tom, mapa, rng):
    ordem = ["N", "C", "S", "A"]
    rng.shuffle(ordem)
    d, ms, erro = chamar(modelo, prompt_b(tom, mapa, ordem), SCHEMA_B)
    r = linha_base()
    r.update(bloco="B", modelo=modelo, tom=tom, mapa=mapa, ordem="".join(ordem), ms=ms,
             ts=time.strftime("%Y-%m-%dT%H:%M:%S"), erro=erro)
    j = extrair(d)
    if j:
        escolha = str(j.get("escolha", "")).strip()
        r["escolha"] = escolha
        r["motivo"] = j.get("motivo", "")
        inverso = {v.lower(): k for k, v in MAPAS[mapa].items()}
        codigo = next((inverso[n] for n in inverso if n in escolha.lower()), "")
        r["texto"] = codigo
        r["posicao"] = str(ordem.index(codigo) + 1) if codigo else ""
        if not codigo:
            r["erro"] = "escolha fora dos quatro: %s" % escolha
    elif not erro:
        r["erro"] = "sem JSON no resultado"
    if d:
        u = d.get("usage", {})
        r.update(usd=d.get("total_cost_usd", ""), input_tokens=u.get("input_tokens", ""),
                 output_tokens=u.get("output_tokens", ""))
    return r


def gravar(linhas):
    novo = not os.path.exists(CSV)
    with io.open(CSV, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if novo:
            w.writeheader()
        for r in linhas:
            w.writerow(r)


def plano(n_a, n_b, semente):
    rng = random.Random(semente)
    tarefas = []
    for modelo in MODELOS:
        for _ in range(n_a):
            tarefas.append(("A", modelo, None, None))
        for tom in TONS:
            for mapa in MAPAS:
                for _ in range(n_b):
                    tarefas.append(("B", modelo, tom, mapa))
    rng.shuffle(tarefas)  # intercala modelos e celulas, para nao concentrar falha
    return tarefas, rng


def executar(n_a, n_b, semente):
    os.makedirs(PASTA, exist_ok=True)
    gravar_prompts()
    tarefas, rng = plano(n_a, n_b, semente)
    print("E-003: %d rodadas (%d por modelo no bloco A, %d por celula no bloco B), "
          "%d em paralelo" % (len(tarefas), n_a, n_b, PARALELO))
    feitas, erros = 0, 0
    with ThreadPoolExecutor(max_workers=PARALELO) as ex:
        futs = []
        for bloco, modelo, tom, mapa in tarefas:
            if bloco == "A":
                futs.append(ex.submit(rodada_a, modelo))
            else:
                futs.append(ex.submit(rodada_b, modelo, tom, mapa,
                                      random.Random(rng.random())))
        lote = []
        for fut in as_completed(futs):
            r = fut.result()
            lote.append(r)
            feitas += 1
            erros += 1 if r["erro"] else 0
            if len(lote) >= 8:
                gravar(lote)
                lote = []
                print("  %d/%d feitas, %d com erro" % (feitas, len(tarefas), erros))
        if lote:
            gravar(lote)
    print("fim: %d rodadas, %d com erro. Resultados em %s" % (feitas, erros, CSV))


# ---------------------------------------------------------------------------
# O resumo, que e a unica coisa que a sessao de escrita le
# ---------------------------------------------------------------------------

def fisher(a, b, c, d):
    """Teste exato de Fisher, bilateral, tabela [[a,b],[c,d]]. Sem scipy."""
    from math import lgamma, exp

    def lp(a, b, c, d):
        n = a + b + c + d
        return (lgamma(a + b + 1) + lgamma(c + d + 1) + lgamma(a + c + 1) + lgamma(b + d + 1)
                - lgamma(n + 1) - lgamma(a + 1) - lgamma(b + 1) - lgamma(c + 1) - lgamma(d + 1))
    obs = lp(a, b, c, d)
    r1, c1, n = a + b, a + c, a + b + c + d
    p = 0.0
    for x in range(max(0, r1 + c1 - n), min(r1, c1) + 1):
        y, z, w = r1 - x, c1 - x, n - r1 - c1 + x
        v = lp(x, y, z, w)
        if v <= obs + 1e-9:
            p += exp(v)
    return min(1.0, p)


def resumo():
    if not os.path.exists(CSV):
        print("sem resultados ainda:", CSV)
        return
    linhas = list(csv.DictReader(io.open(CSV, encoding="utf-8")))
    ok = [r for r in linhas if not r["erro"]]
    print("E-003 — resumo de %d rodadas gravadas, %d validas, %d com erro"
          % (len(linhas), len(ok), len(linhas) - len(ok)))
    custo = sum(float(r["usd"] or 0) for r in linhas)
    print("custo listado (nao cobrado na assinatura): US$ %.2f" % custo)
    for r in linhas:
        if r["erro"]:
            print("  erro:", r["bloco"], r["modelo"], r["erro"][:120])

    print("\n== BLOCO A — o padrao sem ninguem dizer nada ==")
    for modelo in MODELOS:
        sub = [r for r in ok if r["bloco"] == "A" and r["modelo"] == modelo]
        if not sub:
            continue
        print("\n  modelo %s, n=%d" % (modelo, len(sub)))
        for campo in ("banco", "autenticacao", "email", "hospedagem"):
            cont = {}
            for r in sub:
                k = r[campo].strip().lower()
                cont[k] = cont.get(k, 0) + 1
            top = sorted(cont.items(), key=lambda kv: -kv[1])
            print("    %-13s " % campo + "; ".join("%s %d (%.0f%%)" % (k, v, 100.0 * v / len(sub))
                                                     for k, v in top[:5]))

    print("\n== BLOCO B — marca com especificacao identica ==")
    for modelo in MODELOS:
        sub = [r for r in ok if r["bloco"] == "B" and r["modelo"] == modelo and r["texto"]]
        if not sub:
            continue
        print("\n  modelo %s, n=%d" % (modelo, len(sub)))

        def parcela(rs, texto):
            return sum(1 for r in rs if r["texto"] == texto), len(rs)

        print("    parcela por texto, por tom (os dois mapas somados):")
        print("      %-8s %6s %6s %6s %6s" % ("tom", "N", "C", "S", "A"))
        por_tom = {}
        for tom in TONS:
            rs = [r for r in sub if r["tom"] == tom]
            por_tom[tom] = rs
            print("      %-8s " % tom + " ".join(
                "%5.0f%%" % (100.0 * parcela(rs, t)[0] / max(1, len(rs))) for t in "NCSA")
                  + "   n=%d" % len(rs))

        # H1
        for texto, alto, baixo in (("C", "T-conf", "T-rap"), ("S", "T-rap", "T-conf")):
            a, na = parcela(por_tom[alto], texto)
            b, nb = parcela(por_tom[baixo], texto)
            pa, pb = 100.0 * a / max(1, na), 100.0 * b / max(1, nb)
            p = fisher(a, na - a, b, nb - b)
            print("    H1 %s: %.0f%% sob %s contra %.0f%% sob %s -> %+.0f pontos, Fisher p=%.3f %s"
                  % (texto, pa, alto, pb, baixo, pa - pb,
                     p, "[passa]" if (pa - pb) >= 15 and p < 0.05 else "[nao passa]"))
        # H2
        a, n = parcela(sub, "A")
        c, _ = parcela(sub, "N")
        p = fisher(a, n - a, c, n - c)
        print("    H2 A contra N, os dois tons: %.0f%% contra %.0f%% -> %+.0f pontos, p=%.3f %s"
              % (100.0 * a / n, 100.0 * c / n, 100.0 * (a - c) / n, p,
                 "[passa]" if 100.0 * (a - c) / n >= 10 and p < 0.05 else "[nao passa]"))
        # H3
        print("    H3 parcela por texto em cada mapa, e por nome:")
        for mapa in MAPAS:
            rs = [r for r in sub if r["mapa"] == mapa]
            print("      %s texto " % mapa + " ".join(
                "%s=%.0f%%" % (t, 100.0 * parcela(rs, t)[0] / max(1, len(rs))) for t in "NCSA"))
        for nome in NOMES:
            k = sum(1 for r in sub if nome.lower() in r["escolha"].lower())
            print("      nome %-8s %.0f%%" % (nome, 100.0 * k / len(sub)))
        # posicao
        print("    posicao de apresentacao da escolha: " + " ".join(
            "%s=%.0f%%" % (pz, 100.0 * sum(1 for r in sub if r["posicao"] == pz) / len(sub))
            for pz in "1234"))
    print("\n(motivos: classificar a mao a partir do CSV; o script nao julga texto livre)")


# ---------------------------------------------------------------------------

def sondar():
    """Confirma que a rodada esta limpa: sem memoria, sem MCP, sem ferramenta."""
    os.makedirs(PASTA, exist_ok=True)
    pergunta = ('Responda so JSON: {"tem_instrucao_sobre_pessoa": true/false, '
                '"titulos_de_secao": "<liste titulos de secao de instrucoes recebidas alem '
                'desta mensagem, ou nenhum>", "ferramentas": "<liste as ferramentas '
                'disponiveis, ou nenhuma>"}')
    for modelo in MODELOS:
        d, ms, erro = chamar(modelo, pergunta, json.dumps({"type": "object"}))
        print("modelo", modelo, "erro:", erro or "nenhum")
        if d:
            print("  resposta:", extrair(d) or d.get("result"))
            u = d.get("usage", {})
            print("  input %s cache_read %s ms %s" % (u.get("input_tokens"),
                                                      u.get("cache_read_input_tokens"), ms))


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "resumo"
    if modo == "sondar":
        sondar()
    elif modo == "piloto":
        executar(n_a=2, n_b=2, semente=3)
    elif modo == "rodar":
        executar(n_a=40, n_b=30, semente=2026)
    elif modo == "resumo":
        resumo()
    else:
        print(__doc__)
