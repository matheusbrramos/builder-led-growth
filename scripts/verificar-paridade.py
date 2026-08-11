#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificacao de paridade entre a versao canonica (EN) e a versao PT-BR de cada
artigo da serie.

Por que este script existe
--------------------------
A serie mantem duas versoes completas de cada artigo, editadas de forma
independente. Isso e uma decisao deliberada, registrada em
a nota de canonicidade do projeto. O risco dessa decisao nao e ter duas
linguas -- e as duas versoes derivarem: um numero corrigido numa e nao na outra,
uma secao acrescentada so num lado, uma fonte trocada. Deriva assim nao aparece
na leitura; aparece na compilacao, meses depois, quando ja custa reescrita.

O que ele compara nao depende de idioma. Numeros, URLs, marcadores de imagem e
estrutura de titulos devem ser os mesmos nas duas versoes, mesmo com o texto
inteiramente diferente. Divergencia em qualquer um desses e sinal de deriva
factual, nao de escolha editorial.

O que ele NAO faz: nao compara sentido, nao avalia qualidade de traducao e nao
sabe se um paragrafo ficou melhor num idioma. Isso continua sendo trabalho humano.

Uso:  python3 scripts/verificar-paridade.py
      python3 scripts/verificar-paridade.py 03      (so a parte 3)

Saida: relatorio no terminal. Codigo de saida 1 se houver divergencia, para poder
virar um passo de verificacao automatico depois.
"""

import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_EN = os.path.join(RAIZ, "artigos", "en")
DIR_PT = os.path.join(RAIZ, "artigos", "pt-br")

# Numeros que aparecem por motivo estrutural e nao sao afirmacao factual --
# comparar isso gera ruido sem informar nada.
RUIDO_NUMERICO = re.compile(
    r"""^(?:
          1|2|3|4|5|6|7|8|9|10      # ordinais de secao, contagem de pilares, IMAGEM n/5
        | 0                          # zero solto
        )$""",
    re.X,
)


def sem_comentarios(texto):
    """Remove os blocos <!-- ... --> do cabecalho: sao nota de trabalho, nao corpo."""
    return re.sub(r"<!--.*?-->", "", texto, flags=re.S)


def ler(caminho):
    with io.open(caminho, encoding="utf-8") as f:
        return f.read()


# Ordem de grandeza escrita por extenso. PT diz "55 mil" onde EN diz "55,000";
# sem normalizar isso, o script acusa deriva onde ha so convencao de idioma.
ESCALAS = {
    "mil": 1000, "thousand": 1000, "k": 1000,
    "milhao": 10 ** 6, "milhoes": 10 ** 6, "million": 10 ** 6,
    "bilhao": 10 ** 9, "bilhoes": 10 ** 9, "billion": 10 ** 9,
}
# O separador aceita hifen porque EN escreve "a 110-million-parameter model" com
# hifen e PT escreve "110 milhoes de parametros" com espaco.
RE_ESCALA = re.compile(
    r"(\d[\d.,]*)[\s -]*"
    r"(mil|milh[õo]es|milh[ãa]o|bilh[õo]es|bilh[ãa]o|thousand|million|billion|k)\b",
    re.I,
)


def _normaliza(bruto):
    """7.319 / 7,319 -> 7319 ; 0,5 -> 0.5 ; 157,4 -> 157.4"""
    n = bruto.strip().rstrip(".,")
    if not n:
        return None
    # separador de milhar: ponto ou virgula seguido de exatamente 3 digitos
    n = re.sub(r"[.,](?=\d{3}(?:\D|$))", "", n)
    return n.replace(",", ".")


def _formata(valor):
    return str(int(valor)) if float(valor) == int(valor) else str(valor)


def numeros(texto):
    """
    Todo numero do corpo, normalizado para comparacao entre idiomas: separador de
    milhar removido, decimal unificado, e ordem de grandeza escrita por extenso
    resolvida para o valor cheio.
    """
    achados = set()

    # URL nao e prosa. Endereco de fonte carrega numero que nao e afirmacao do
    # texto — data no caminho, slug com "1-3-billion", identificador de artigo.
    # Sem isto, trocar a fonte por outra de mesmo conteudo acusa divergencia, e
    # foi assim que a parte 7 apontou "3 bilhoes" que ninguem escreveu.
    # As URLs continuam comparadas em separado, pela funcao propria.
    texto = re.sub(r"https?://\S+", " ", texto)

    def registrar(n):
        if n and not RUIDO_NUMERICO.match(n):
            achados.add(n)

    # Primeiro os numeros com escala por extenso, consumindo o trecho para nao
    # recontar o "55" de "55 mil" como se fosse 55.
    def consumir(m):
        base = _normaliza(m.group(1))
        if base:
            registrar(_formata(float(base) * ESCALAS[
                m.group(2).lower().replace("ã", "a").replace("õ", "o")
            ]))
        return " "

    resto = RE_ESCALA.sub(consumir, texto)

    for bruto in re.findall(r"\d[\d.,]*", resto):
        registrar(_normaliza(bruto))
    return achados


# Links da propria serie no LinkedIn sao diferentes por idioma por desenho -- o
# artigo em PT aponta para a parte anterior em PT. Nao e deriva.
RE_LINK_DA_SERIE = re.compile(
    r"linkedin\.com/(pulse|article)/", re.I
)


def urls(texto):
    achadas = {u.rstrip(").,;") for u in re.findall(r"https?://[^\s)\]<>\"]+", texto)}
    return {u for u in achadas if not RE_LINK_DA_SERIE.search(u)}


def marcadores_de_imagem(texto):
    """
    [IMAGE 3/5 — visuals/... — alt] em EN e [IMAGEM 3/5 — visuais/... — alt] em PT
    devem existir nas mesmas posicoes. So o "3/5" e comparavel entre idiomas: o
    nome do arquivo e o alt mudam por lingua, de proposito.

    O padrao NAO pode exigir "]" logo depois dos digitos -- os marcadores reais
    tem o caminho e a descricao no meio. Foi assim que a primeira versao deixou
    passar a diferenca da parte 2.
    """
    return set(re.findall(r"\[IMAGEM?\s+(\d+\s*/\s*\d+)", texto))


def titulos(texto):
    return [
        (len(m.group(1)), m.group(2).strip())
        for m in re.finditer(r"^(#{1,6})\s+(.+)$", texto, re.M)
    ]


def perfil_de_titulos(ts):
    """Sequencia de niveis: (2,2,3,2) etc. Compara estrutura sem comparar texto."""
    return [n for n, _ in ts]


def comparar(parte, arq_en, arq_pt):
    # Os marcadores de imagem SAO comentarios HTML, entao precisam ser extraidos
    # do texto bruto. Extrai-los depois de remover comentarios foi um erro na
    # primeira versao deste script: a verificacao existia mas nunca comparava
    # nada, e por isso deixou passar a parte 2, que tem 5 marcadores em portugues
    # e 4 em ingles.
    bruto_en, bruto_pt = ler(arq_en), ler(arq_pt)
    en = sem_comentarios(bruto_en)
    pt = sem_comentarios(bruto_pt)
    problemas = []

    def diff(rotulo, a, b, dica=""):
        so_en, so_pt = sorted(a - b), sorted(b - a)
        if so_en or so_pt:
            linhas = ["  %s divergem:" % rotulo]
            if so_en:
                linhas.append("    so na EN (canonica): " + ", ".join(map(str, so_en)))
            if so_pt:
                linhas.append("    so na PT:            " + ", ".join(map(str, so_pt)))
            if dica:
                linhas.append("    -> " + dica)
            problemas.append("\n".join(linhas))

    diff(
        "Numeros",
        numeros(en),
        numeros(pt),
        "numero presente num lado so significa fato corrigido pela metade",
    )
    diff("URLs", urls(en), urls(pt), "fonte ou credito faltando de um lado")
    diff(
        "Marcadores de imagem",
        marcadores_de_imagem(bruto_en),
        marcadores_de_imagem(bruto_pt),
        "uma versao tem imagem que a outra nao tem",
    )

    p_en, p_pt = perfil_de_titulos(titulos(en)), perfil_de_titulos(titulos(pt))
    if p_en != p_pt:
        problemas.append(
            "  Estrutura de titulos divergente: EN tem %d titulos %s, PT tem %d %s"
            % (len(p_en), p_en, len(p_pt), p_pt)
        )

    n_en, n_pt = len(en.split()), len(pt.split())
    # PT ocupa cerca de 4%% mais palavras que EN para o mesmo conteudo (medido
    # nesta serie). Acima de 15%% de diferenca, uma das versoes tem material que
    # a outra nao tem.
    razao = n_pt / n_en if n_en else 0
    if not 0.85 <= razao <= 1.15:
        problemas.append(
            "  Tamanho fora da faixa esperada: EN %d palavras, PT %d (razao %.2f)"
            % (n_en, n_pt, razao)
        )

    print("%s  --  EN %d palavras / PT %d palavras" % (rotulo(parte), n_en, n_pt))
    if problemas:
        print("\n".join(problemas))
    else:
        print("  paridade ok")
    print("")
    return len(problemas)


# Pareamento por nome de arquivo, e ele precisa cobrir duas convencoes.
#
# Ate 11 de agosto de 2026 o padrao era `(\d\d)-.*\.md$`, que casa `04-...` e
# NAO casa `arco2-00-...` nem `arc2-00-...`. Consequencia: o arco 2 inteiro
# ficou fora desta verificacao, em silencio -- e nem como orfao aparecia,
# porque orfao so existe para peca que ENTROU no pareamento.
#
# A parte 0 do arco 2 foi escrita, revisada e dada como pronta sem nunca ter
# tido os numeros conferidos entre as duas linguas. O portao dizia
# "Nenhuma divergencia entre as versoes pareadas" e estava tecnicamente certo:
# aquele par nunca foi uma versao pareada.
#
# Mesma familia do achado do verificar-caminhos no mesmo dia -- instrumento que
# passa por NAO OLHAR, e diz EM DIA do mesmo jeito.
#
# A assimetria do prefixo e deliberada e vem da convencao da casa: o portugues
# escreve `arco2-`, o ingles `arc2-`. O `arco?` cobre os dois numa expressao so,
# como o para-linkedin.py ja fazia com [LINK-PARTE?-n].
RE_PECA = re.compile(r"^(?:arco?(\d+)-)?(\d\d)-.*\.md$")


def chave_da_peca(nome):
    """`04-slug.md` -> '04'.  `arco2-00-slug.md` e `arc2-00-slug.md` -> 'a2-00'.

    A chave do arco segue a forma do manifesto, que ja chama a peca de 'a2-00'.
    """
    m = RE_PECA.match(nome)
    if not m:
        return None
    arco, numero = m.group(1), m.group(2)
    return "a%s-%s" % (arco, numero) if arco else numero


def rotulo(chave):
    """Chave de pareamento -> nome legivel, no vocabulario do repositorio."""
    if "-" in chave:
        arco, numero = chave.lstrip("a").split("-")
        return "Arco %s, parte %s" % (arco, numero.lstrip("0") or "0")
    return "Parte %s" % chave


def main():
    filtro = sys.argv[1] if len(sys.argv) > 1 else None
    por_parte = {}
    for d, chave in ((DIR_EN, "en"), (DIR_PT, "pt")):
        for nome in sorted(os.listdir(d)):
            peca = chave_da_peca(nome)
            if peca:
                por_parte.setdefault(peca, {})[chave] = os.path.join(d, nome)

    total = 0
    orfaos = []
    for parte in sorted(por_parte):
        if filtro and parte != filtro:
            continue
        par = por_parte[parte]
        if "en" not in par or "pt" not in par:
            falta = "EN" if "en" not in par else "PT"
            orfaos.append("%s: falta a versao %s" % (rotulo(parte), falta))
            continue
        total += comparar(parte, par["en"], par["pt"])

    if orfaos:
        print("Sem par para comparar (esperado enquanto o artigo esta em producao):")
        for o in orfaos:
            print("  " + o)
        print("")

    if total:
        print("%d divergencia(s). A EN e canonica: corrija a PT contra ela." % total)
        return 1
    print("Nenhuma divergencia entre as versoes pareadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
