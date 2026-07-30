#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Visuais da parte 2 — Builder-Led Growth. PT-BR."""
import cairosvg, os, math

OUT = os.path.dirname(os.path.abspath(__file__))
FONT = "Liberation Sans, Arial, sans-serif"

NAVY = "#16213E"
GRAY = "#5B6472"
GRAY_LIGHT = "#8B93A1"
BG = "#FFFFFF"
PANEL = "#F7F8FA"
BORDER = "#DEE2E7"
ACCENT = "#2F5D8A"
ACCENT_SOFT = "#E7EEF4"
AMBER = "#B8792E"
AMBER_SOFT = "#F5EBDD"
MUTED = "#C7CDD5"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=16, weight="400", fill=NAVY, anchor="start", style="normal", family=FONT):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" fill="{fill}" '
            f'text-anchor="{anchor}">{esc(s)}</text>')


def lines(x, y, arr, size=14, weight="400", fill=GRAY, lh=21, anchor="start", style="normal"):
    return "\n".join(txt(x, y + i * lh, l, size, weight, fill, anchor, style) for i, l in enumerate(arr))


def rect(x, y, w, h, fill, stroke=None, sw=1, rx=10):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}/>'


def line(x1, y1, x2, y2, stroke=BORDER, w=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{w}"{d}/>'


def circle(cx, cy, r, fill, stroke=None, sw=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}/>'


def doc(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="{BG}"/>{body}</svg>')


def header(b, kicker, title, sub, h):
    b.append(rect(0, 0, 10, h, ACCENT, rx=0))
    b.append(txt(60, 66, kicker, 14, "700", ACCENT))
    b.append(txt(60, 104, title, 30, "700", NAVY))
    b.append(txt(60, 136, sub, 17, "400", GRAY, style="italic"))


def footer(b, w, h, note):
    b.append(line(60, h - 66, w - 60, h - 66, BORDER, 1))
    b.append(txt(60, h - 40, note, 12.5, "400", GRAY_LIGHT))


def save(name, svg, scale=2):
    p = os.path.join(OUT, f"{name}.svg")
    open(p, "w", encoding="utf-8").write(svg)
    cairosvg.svg2png(url=p, write_to=os.path.join(OUT, f"{name}.png"), scale=scale)
    print("ok:", name)


# ---------------------------------------------------------------- 1. três entradas
def v1():
    W, H = 1600, 860
    b = []
    header(b, "O QUE COMPETE NA DECISÃO DE UM AGENTE", "As três entradas",
           "Poder, velocidade de influência e prazo de retorno não coincidem", H)

    cols = [
        {
            "n": "1", "t": ["Conhecimento", "paramétrico"],
            "d": ["O que o modelo aprendeu no", "treino e carrega nos pesos.",
                  "Responde mesmo sem acesso", "à internet."],
            "poder": 1.0, "vel": 0.12,
            "prazo": "18 a 36 meses",
            "ex": "Explica o shadcn/ui: volume de", "ex2": "código público virou default"
        },
        {
            "n": "2", "t": ["Recuperação", "em tempo real"],
            "d": ["O que o agente busca durante", "a tarefa: docs, resultados de",
                  "busca, arquivos do repo,", "llms.txt."],
            "poder": 0.55, "vel": 0.85,
            "prazo": "semanas",
            "ex": "Só alcança quem já sabe", "ex2": "procurar por você"
        },
        {
            "n": "3", "t": ["Atrito", "de execução"],
            "d": ["O que acontece quando o", "agente tenta usar. DSL própria,",
                  "passos manuais, custo de", "token do schema."],
            "poder": 0.75, "vel": 0.7,
            "prazo": "sprint",
            "ex": "Só age depois de vencidas", "ex2": "as duas primeiras batalhas"
        },
    ]

    cw, gap, x0 = 468, 26, 60
    by, bh = 195, 545
    for i, c in enumerate(cols):
        x = x0 + i * (cw + gap)
        b.append(rect(x, by, cw, bh, PANEL, BORDER, 1))
        b.append(circle(x + 40, by + 46, 20, ACCENT))
        b.append(txt(x + 40, by + 53, c["n"], 18, "700", "#FFFFFF", "middle"))
        b.append(lines(x + 26, by + 100, c["t"], 20, "700", NAVY, 26))
        b.append(lines(x + 26, by + 168, c["d"], 14, "400", GRAY, 21))

        # barras
        bx, bw = x + 26, cw - 52
        yb = by + 275
        for label, val, col in [("poder relativo", c["poder"], ACCENT), ("velocidade de influência", c["vel"], AMBER)]:
            b.append(txt(bx, yb, label, 12.5, "400", GRAY_LIGHT))
            b.append(rect(bx, yb + 10, bw, 18, "#EEF0F3", rx=5))
            b.append(rect(bx, yb + 10, max(8, bw * val), 18, col, rx=5))
            yb += 56

        b.append(line(bx, by + bh - 128, x + cw - 26, by + bh - 128, BORDER, 1))
        b.append(txt(bx, by + bh - 100, "prazo de retorno", 12.5, "400", GRAY_LIGHT))
        b.append(txt(bx, by + bh - 72, c["prazo"], 22, "700", NAVY))
        b.append(txt(bx, by + bh - 40, c["ex"], 12.5, "400", GRAY_LIGHT, style="italic"))
        b.append(txt(bx, by + bh - 22, c["ex2"], 12.5, "400", GRAY_LIGHT, style="italic"))

    footer(b, W, H, "Tratar as três como uma só coisa — \"otimizar para IA\" — é o que faz times investirem seis meses no lugar errado.")
    return doc(W, H, "\n".join(b))


# ---------------------------------------------------------------- 2. funil
def v2():
    W, H = 1600, 900
    b = []
    header(b, "O FUNIL BUILDER-LED GROWTH", "Três estágios, três mecanismos",
           "Cada estágio é decidido por uma entrada diferente — e se perde de um jeito diferente", H)

    st = [
        {"n": "01", "t": "Candidatura",
         "q": "O modelo sabe que você existe,\ncom precisão para citar certo?",
         "mec": "Conhecimento paramétrico",
         "perda": "Ser citado com erro:\nnome de pacote errado, método\ninexistente, versão descontinuada",
         "dado": "16% → 54%",
         "dadol": "acerto do GPT-4 com dados estruturados"},
        {"n": "02", "t": "Recomendação",
         "q": "Entre os candidatos,\no agente escolhe você?",
         "mec": "Recuperação + sinal de comunidade",
         "perda": "Ausência do conteúdo\ncomparativo de terceiros que\nresponde pela maior fatia",
         "dado": "32,5% vs <5%",
         "dadol": "terceiros vs. página própria"},
        {"n": "03", "t": "Adoção",
         "q": "A recomendação virou\nintegração funcionando?",
         "mec": "Atrito de execução",
         "perda": "Passos manuais no meio do\nfluxo. Nenhuma métrica de\nmarketing acusa a perda",
         "dado": "o estágio cego",
         "dadol": "\"fui recomendado\" já foi cumprido"},
    ]

    x0, cw, gap = 60, 468, 26
    by, bh = 200, 520
    for i, s in enumerate(st):
        x = x0 + i * (cw + gap)
        hl = (i == 2)
        b.append(rect(x, by, cw, bh, ACCENT_SOFT if hl else PANEL, ACCENT if hl else BORDER, 2 if hl else 1))
        b.append(rect(x, by, cw, 6, ACCENT if hl else MUTED, rx=0))
        b.append(txt(x + 26, by + 48, s["n"], 30, "700", ACCENT if hl else GRAY_LIGHT))
        b.append(txt(x + 100, by + 48, s["t"], 24, "700", NAVY))

        b.append(txt(x + 26, by + 96, "A PERGUNTA", 11.5, "700", GRAY_LIGHT))
        b.append(lines(x + 26, by + 122, s["q"].split("\n"), 15.5, "400", NAVY, 23))

        b.append(txt(x + 26, by + 200, "MECANISMO DOMINANTE", 11.5, "700", GRAY_LIGHT))
        b.append(txt(x + 26, by + 226, s["mec"], 15, "700", ACCENT))

        b.append(txt(x + 26, by + 272, "COMO SE PERDE AQUI", 11.5, "700", GRAY_LIGHT))
        b.append(lines(x + 26, by + 298, s["perda"].split("\n"), 14, "400", GRAY, 21))

        b.append(line(x + 26, by + bh - 96, x + cw - 26, by + bh - 96, BORDER, 1))
        b.append(txt(x + 26, by + bh - 58, s["dado"], 24, "700", ACCENT))
        b.append(txt(x + 26, by + bh - 30, s["dadol"], 12.5, "400", GRAY_LIGHT, style="italic"))

        if i < 2:
            cy = by + bh / 2
            ax = x + cw + 3
            b.append(f'<path d="M{ax},{cy} l14,0 m-5,-5 l5,5 l-5,5" stroke="{GRAY_LIGHT}" stroke-width="2" fill="none"/>')

    # faixa do limite
    fy = by + bh + 34
    b.append(rect(60, fy, W - 120, 74, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, fy + 32, "O LIMITE DA TESE", 12.5, "700", AMBER))
    b.append(txt(88, fy + 58, "O BLG decide quem entra. Quem decide se permanece é a economia humana — o limite da tese é o boleto.", 17, "400", NAVY))

    footer(b, W, H, "Fontes: Digidop (dados estruturados) · Connor Kimball (origem das citações) · análise completa no artigo.")
    return doc(W, H, "\n".join(b))


# ---------------------------------------------------------------- 3. duas forças do preço
def v3():
    W, H = 1600, 800
    b = []
    header(b, "PRECIFICAÇÃO SOB BLG", "As duas forças a equilibrar",
           "O tier gratuito deixa de ser topo de funil e vira ingresso — sem deixar de precisar gerar receita", H)

    bw, bh, by = 620, 330, 205
    xl, xr = 60, W - 60 - bw

    # esquerda
    b.append(rect(xl, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xl, by, bw, 6, ACCENT, rx=0))
    b.append(txt(xl + 30, by + 52, "FORÇA 1 — INGRESSO", 12.5, "700", ACCENT))
    b.append(lines(xl + 30, by + 92, ["A máquina precisa poder", "tentar sem pedir autorização"], 22, "700", NAVY, 30))
    b.append(lines(xl + 30, by + 172, [
        "Um agente que bate num paywall precisa parar,",
        "avisar o humano e esperar. A interrupção quebra o",
        "fluxo e transfere a decisão para quem estava",
        "fazendo outra coisa — abrindo espaço para o agente",
        "escolher a ferramenta que não exigiu parada."], 14, "400", GRAY, 21))
    b.append(txt(xl + 30, by + bh - 26, "Sem tier gratuito, você não está no jogo.", 14.5, "700", ACCENT))

    # direita
    b.append(rect(xr, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xr, by, bw, 6, AMBER, rx=0))
    b.append(txt(xr + 30, by + 52, "FORÇA 2 — SUFICIÊNCIA", 12.5, "700", AMBER))
    b.append(lines(xr + 30, by + 92, ["O gratuito não pode", "resolver o problema inteiro"], 22, "700", NAVY, 30))
    b.append(lines(xr + 30, by + 172, [
        "O freemium do PLG converte porque o humano cria",
        "hábito, bate no limite e sente dor. A máquina não",
        "sente atrito como incômodo, não cria apego e tem",
        "paciência infinita para esperar o limite resetar.",
        "O mecanismo de conversão por dor não transfere."], 14, "400", GRAY, 21))
    b.append(txt(xr + 30, by + bh - 26, "Já existe técnica publicada de empilhar free tiers.", 14.5, "700", AMBER))

    # setas em oposição
    cy = by + bh / 2
    mx = W / 2
    b.append(f'<path d="M{mx-42},{cy} l-30,0 m5,-5 l-5,5 l5,5" stroke="{GRAY_LIGHT}" stroke-width="2.5" fill="none"/>')
    b.append(f'<path d="M{mx+42},{cy} l30,0 m-5,-5 l5,5 l-5,5" stroke="{GRAY_LIGHT}" stroke-width="2.5" fill="none"/>')

    # alavancas
    ly = by + bh + 40
    b.append(rect(60, ly, W - 120, 118, ACCENT_SOFT, ACCENT, 1.5))
    b.append(txt(88, ly + 34, "AS ALAVANCAS QUE RESOLVEM A TENSÃO", 12.5, "700", ACCENT))
    items = [
        "Custo do crédito proporcional ao custo de servir",
        "Cota calibrada por unidade de trabalho, não de calendário",
        "Limite de concorrência, além de limite de volume",
        "Caminho de receita trafegável pela máquina",
    ]
    for i, it in enumerate(items):
        cx = 88 + (i % 2) * 740
        cyy = ly + 66 + (i // 2) * 30
        b.append(circle(cx + 5, cyy - 5, 4, ACCENT))
        b.append(txt(cx + 20, cyy, it, 15, "400", NAVY))

    footer(b, W, H, "O detalhe menos copiado: limitar concorrência permite ser generoso em volume sem servir de infraestrutura de produção.")
    return doc(W, H, "\n".join(b))


# ---------------------------------------------------------------- 4. onde medir
def v4():
    W, H = 1600, 840
    b = []
    header(b, "MEDIÇÃO", "Onde se mede cada estágio",
           "Candidatura mede o passado do modelo. Comunidade mede o futuro dele.", H)

    zones = [
        {"t": "DENTRO DO MODELO", "e": "Candidatura", "c": ACCENT,
         "m": ["Share of Model — % das respostas", "da categoria que citam você",
               "", "Taxa de acerto de citação —", "quando cita, acerta pacote,", "instalação e método?"],
         "n": "Mede o que o modelo já sabe:\num corpus fechado meses atrás."},
        {"t": "NA COMUNIDADE", "e": "Recomendação", "c": AMBER,
         "m": ["Presença nas 15-20 comparações", "mais buscadas da categoria",
               "Dependentes no GitHub (Used by)", "Downloads comparados a 3 rivais",
               "Inclusão em scaffolds e starters", "Levantamentos anuais e listas"],
         "n": "Mede o material do qual a\nrecomendação futura vai se alimentar."},
        {"t": "DENTRO DO PRODUTO", "e": "Adoção", "c": "#2F7D5D",
         "m": ["O evento que só acontece quando", "a integração funcionou de verdade",
               "", "Não é download. Não é install.", "Não é cadastro. É a primeira", "chamada com dados reais."],
         "n": "Separa \"fui recomendado\" de\n\"estou sendo usado\"."},
    ]

    x0, cw, gap = 60, 468, 26
    by, bh = 200, 520
    for i, z in enumerate(zones):
        x = x0 + i * (cw + gap)
        b.append(rect(x, by, cw, bh, PANEL, BORDER, 1))
        b.append(rect(x, by, cw, 6, z["c"], rx=0))
        b.append(txt(x + 26, by + 50, z["t"], 12.5, "700", z["c"]))
        b.append(txt(x + 26, by + 86, z["e"], 26, "700", NAVY))
        b.append(line(x + 26, by + 110, x + cw - 26, by + 110, BORDER, 1))
        b.append(lines(x + 26, by + 146, z["m"], 14.5, "400", GRAY, 24))
        b.append(line(x + 26, by + bh - 92, x + cw - 26, by + bh - 92, BORDER, 1))
        b.append(lines(x + 26, by + bh - 60, z["n"].split("\n"), 13.5, "400", GRAY_LIGHT, 20, style="italic"))

    footer(b, W, H, "Medir recomendação perguntando ao agente é medir candidatura de novo — o modelo só devolve o que já sabia.")
    return doc(W, H, "\n".join(b))


# ---------------------------------------------------------------- 5. quadro consolidado
def v5():
    W, H = 1600, 780
    b = []
    header(b, "QUADRO CONSOLIDADO", "O que cada métrica responde — e o que não responde",
           "O erro mais comum é reportar menção em IA como se fosse adoção", H)

    rows = [
        ["Candidatura", "Dentro do modelo", "Share of Model", "Não diz se a citação está correta"],
        ["Candidatura", "Dentro do modelo", "Taxa de acerto de citação", "Não diz se você é o escolhido"],
        ["Recomendação", "Na comunidade", "Presença em comparativos", "Não diz se a integração funciona"],
        ["Recomendação", "Na comunidade", "Dependentes, downloads, scaffolds", "Não diz se o uso é recorrente"],
        ["Adoção", "Dentro do produto", "Primeira chamada bem-sucedida", "Não diz se o cliente permanece"],
        ["Atravessa os 3", "Dentro do produto", "Taxa de adoção arquitetural", "Não diz por que o agente escolheu"],
    ]
    heads = ["ESTÁGIO", "ONDE MEDIR", "MÉTRICA", "O QUE ELA NÃO RESPONDE"]
    colx = [60, 300, 590, 1030]
    ty = 205

    b.append(rect(60, ty - 30, W - 120, 44, ACCENT_SOFT, rx=6))
    for i, h in enumerate(heads):
        b.append(txt(colx[i] + 16, ty, h, 12.5, "700", ACCENT))

    ry = ty + 46
    for i, r in enumerate(rows):
        if i % 2 == 0:
            b.append(rect(60, ry - 26, W - 120, 62, PANEL, rx=6))
        for j, cell in enumerate(r):
            wt = "700" if j == 2 else "400"
            fl = NAVY if j == 2 else GRAY
            sz = 15.5 if j == 2 else 14.5
            st = "italic" if j == 3 else "normal"
            b.append(txt(colx[j] + 16, ry, cell, sz, wt, fl, style=st))
        ry += 62

    b.append(rect(60, ry + 6, W - 120, 70, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, ry + 38, "O PRIMEIRO NÚMERO A LEVANTAR", 12.5, "700", AMBER))
    b.append(txt(88, ry + 62, "Se você não sabe qual proporção dos recursos do seu produto é criada por agente, não sabe se o BLG já é relevante para você.", 15.5, "400", NAVY))

    footer(b, W, H, "Referências: Supabase (60%+ dos bancos via ferramentas de IA) · Vercel (de <3% para mais da metade dos deploys).")
    return doc(W, H, "\n".join(b))


if __name__ == "__main__":
    save("p2-tres-entradas-pt", v1())
    save("p2-funil-tres-estagios-pt", v2())
    save("p2-duas-forcas-preco-pt", v3())
    save("p2-onde-medir-cada-estagio-pt", v4())
    save("p2-quadro-metricas-completo-pt", v5())
    print("done")
