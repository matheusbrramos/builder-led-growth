#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais do arco 2, parte 4 — recomendação: como separar a tática que dura da
que vai ser consertada.

PT e EN no mesmo arquivo. Helpers de desenho importados do gen_p4; a
rasterização pelo Chrome e o `fecho` vêm do gen_a2p1, como no gen_a2p3. Cada
função termina com assert de folga contra o rodapé: peça torta falha alto em
vez de sair publicada.

Os cinco visuais seguem os cinco marcadores da peça, na ordem em que aparecem:
as três decisões do harness, a estratificação por porte de marca, o critério em
três perguntas, os três decaimentos, e a grade de horizonte por durabilidade.
Os números existem uma vez só, no topo, e batem com o texto das duas línguas —
quem mudar um, muda nos três lugares.

TODOS os números abaixo foram lidos na fonte primária em 16 de setembro de 2026.
Dois que circulavam nos dossiês NÃO estão aqui porque não existem na fonte a que
eram atribuídos: as faixas de acurácia por tamanho de catálogo e os percentuais
de efeito de posição. A correção está registrada como C-047 no repositório de
trabalho.

Escrito em 16 de setembro de 2026, junto com a peça.

Uso:  python scripts/gen_a2p4.py          # gera PT e EN
      python scripts/gen_a2p4.py pt       # só português
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import cairosvg  # noqa: F401
except Exception:
    import types
    sys.modules["cairosvg"] = types.ModuleType("cairosvg")

from gen_p4 import (  # noqa: E402
    ACCENT, ACCENT_LIGHT, ACCENT_SOFT, AMBER, AMBER_SOFT, BORDER, GRAY,
    GRAY_LIGHT, GREEN, GREEN_SOFT, NAVY, NAVY_DEEP, PANEL, WHITE,
    doc, footer, header, line, rect, txt,
)
from gen_a2p1 import RED, RED_SOFT, _cairo, _png_pelo_chrome, fecho  # noqa: E402

W = 1600
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "visuais", "arco2-parte-04")

# ---------------------------------------------------------------- números
# Uma vez só. Batem com o texto das duas línguas.
MENU_TUDO = "32,1%"          # ToolMenuBench, arXiv 2606.15508, 13/jun/2026
MENU_FILTRADO = "85,7%"
MENU_TUDO_EN = "32.1%"
MENU_FILTRADO_EN = "85.7%"
MENU_TOKENS = 98             # % a menos de tokens com filtragem causal mínima

RAG_SEM = "13,62%"           # RAG-MCP, arXiv 2505.03275, 6/mai/2025
RAG_COM = "43,13%"
RAG_SEM_EN = "13.62%"
RAG_COM_EN = "43.13%"
RAG_TOKENS = 50              # % a menos de tokens de prompt

K_EMBED = "1,4"              # arXiv 2605.24660, 23/mai/2026, mesmos dados BFCL
K_BM25 = "7,4"
K_EMBED_EN = "1.4"
K_BM25_EN = "7.4"
K_FATOR = 5                  # vezes mais candidatos

LIDER_CONSISTENCIA = 80      # arXiv 2605.30207, 28/mai/2026
MEIO_TROCA = 75
JACCARD = "0,12 a 0,20"
JACCARD_EN = "0.12 to 0.20"
AUDIT_RODADAS = "2.000"
AUDIT_RODADAS_EN = "2,000"

LIB_DESNECESSARIA = 45       # Twist et al., Findings of ACL 2026 (v4)
PYTHON_DOMINANTE = 58
MODELOS_TWIST = 8

MODELOS_BIAS = 7             # BiasBusters, arXiv 2510.00307, ICLR 2026

E003_MENOR = 100             # experimento da casa, 1/set/2026
E003_MAIOR_MIN = 63
E003_MAIOR_MAX = 95

GHOST_DATA = "16 de julho de 2026"
GHOST_DATA_EN = "16 July 2026"


def salvar(nome, svg, scale=2):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "%s.svg" % nome)
    open(p, "w", encoding="utf-8").write(svg)
    png = os.path.join(OUT, "%s.png" % nome)
    cs = _cairo()
    if cs is not None:
        cs.svg2png(url=p, write_to=png, scale=scale)
    else:
        m = re.search(r'width="(\d+)" height="(\d+)"', svg)
        w, h = int(m.group(1)), int(m.group(2))
        if not _png_pelo_chrome(p, png, w, h, scale, svg=svg):
            raise SystemExit(
                "Nao consegui gerar o PNG de %s. O cairosvg nao roda aqui e nao\n"
                "achei o Chrome para rasterizar. O SVG foi escrito." % nome)
    print("ok:", os.path.relpath(png, RAIZ))


def linhas(b, x, y, texto, size=14, fill=GRAY, lh=20, weight="400", anchor="start"):
    for j, l in enumerate(texto.split("\n")):
        b.append(txt(x, y + j * lh, l, size, weight, fill, anchor=anchor))


# --------------------------------------------------------------------- capa
def capa(t, lang):
    CW, CH = 1920, 1080
    b = ['<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (CW, CH, NAVY_DEEP)]
    for i in range(9):
        x = 1180 + i * 92
        b.append('<line x1="%d" y1="0" x2="%d" y2="%d" stroke="%s" '
                 'stroke-opacity="0.10" stroke-width="2"/>' % (x, x - 240, CH, ACCENT))
    b.append(txt(120, 186, t["capa_kicker"], 26, "700", ACCENT_LIGHT, sp="4"))
    b.append(line(120, 214, 470, 214, ACCENT, 3))
    b.append(txt(120, 322, t["capa_t1"], 76, "700", WHITE))
    b.append(txt(120, 412, t["capa_t2"], 76, "700", WHITE))
    b.append(txt(120, 476, t["capa_sub"], 30, "400", "#AEB6C2"))
    qy = 574
    b.append(rect(120, qy, CW - 240, 250, AMBER, rx=16, op="0.13"))
    b.append(rect(120, qy, CW - 240, 250, "none", AMBER, 2, rx=16))
    b.append(rect(120, qy, 7, 250, AMBER, rx=0))
    b.append(txt(172, qy + 84, t["capa_frase1"], 34, "400", "#E8DCC8"))
    b.append(txt(172, qy + 146, t["capa_frase2"], 34, "700", WHITE))
    b.append(txt(172, qy + 206, t["capa_creditof"], 22, "400", "#AEB6C2", style="italic"))
    b.append(line(120, CH - 90, CW - 120, CH - 90, ACCENT, 1.5))
    b.append(txt(120, CH - 48, t["capa_rodape"], 22, "400", "#AEB6C2"))
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 %d %d">%s</svg>' % (CW, CH, CW, CH, "".join(b)))


# ------------------------------------------- v1: as três decisões do harness
def v1(t, lang):
    H = 900
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    cw, gap = 470, 35
    x0 = (W - (cw * 3 + gap * 2)) / 2
    cy, ch = 210, 390
    cores = [ACCENT, GREEN, AMBER]
    softs = [ACCENT_SOFT, GREEN_SOFT, AMBER_SOFT]
    for i in range(3):
        cx = x0 + i * (cw + gap)
        b.append(rect(cx, cy, cw, ch, softs[i], rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cores[i], 2, rx=14))
        b.append(rect(cx, cy, cw, 7, cores[i], rx=0))
        b.append(txt(cx + 26, cy + 50, t["v1_c%d_rot" % i], 13, "700", cores[i], sp="2"))
        b.append(txt(cx + 26, cy + 96, t["v1_c%d_nome" % i], 30, "700", NAVY))
        b.append(txt(cx + 26, cy + 142, t["v1_c%d_num" % i], 34, "700", cores[i]))
        b.append(txt(cx + 26, cy + 168, t["v1_c%d_num_sub" % i], 13, "400", GRAY_LIGHT,
                     style="italic"))
        b.append(line(cx + 26, cy + 188, cx + cw - 26, cy + 188, cores[i], 1.2))
        linhas(b, cx + 26, cy + 220, t["v1_c%d_txt" % i], 14.5, NAVY, 22)

    yb = cy + ch + 28
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v1_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 66, t["v1_barra2"], 14.5, "400", "#AEB6C2"))

    fecho(b, H, t["v1_faixa"], ACCENT, ACCENT_SOFT)
    footer(b, W, H, t["v1_rodape"])
    assert yb + 88 < H - 152, "v1 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------- v2: a estratificação
def v2(t, lang):
    H = 880
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    pw, ph = 630, 380
    py = 206
    cores = [GREEN, RED]
    softs = [GREEN_SOFT, RED_SOFT]
    for k in range(2):
        px = 60 if k == 0 else W - 60 - pw
        b.append(rect(px, py, pw, ph, softs[k], rx=14))
        b.append(rect(px, py, pw, ph, "none", cores[k], 2, rx=14))
        b.append(rect(px, py, pw, 7, cores[k], rx=0))
        b.append(txt(px + 28, py + 50, t["v2_p%d_rot" % k], 13, "700", cores[k], sp="2"))
        b.append(txt(px + 28, py + 96, t["v2_p%d_nome" % k], 30, "700", NAVY))
        b.append(txt(px + 28, py + 168, t["v2_p%d_num" % k], 62, "700", cores[k]))
        b.append(txt(px + 28, py + 198, t["v2_p%d_num_sub" % k], 14, "400", GRAY_LIGHT,
                     style="italic"))
        b.append(line(px + 28, py + 220, px + pw - 28, py + 220, cores[k], 1.2))
        linhas(b, px + 28, py + 252, t["v2_p%d_txt" % k], 14.5, NAVY, 22)

    # o miolo, entre os dois painéis
    mx = 60 + pw + 22
    mw = W - 120 - pw * 2 - 44
    b.append(rect(mx, py + 96, mw, 190, PANEL, rx=12))
    b.append(rect(mx, py + 96, mw, 5, NAVY, rx=0))
    linhas(b, mx + mw / 2, py + 138, t["v2_meio_rot"], 12.5, NAVY, 18, "700",
           anchor="middle")
    linhas(b, mx + mw / 2, py + 196, t["v2_meio_txt"], 14, GRAY, 21, anchor="middle")

    yb = py + ph + 26
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v2_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 66, t["v2_barra2"], 14.5, "400", "#AEB6C2"))

    fecho(b, H, t["v2_faixa"], RED, RED_SOFT)
    footer(b, W, H, t["v2_rodape"])
    assert yb + 88 < H - 152, "v2 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------- v3: o critério em três perguntas
def v3(t, lang):
    H = 940
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    # os dois lados do critério
    pw, ph = 730, 176
    py = 200
    for k in range(2):
        px = 60 if k == 0 else W - 60 - pw
        cor = RED if k == 0 else GREEN
        soft = RED_SOFT if k == 0 else GREEN_SOFT
        b.append(rect(px, py, pw, ph, soft, rx=14))
        b.append(rect(px, py, pw, ph, "none", cor, 2, rx=14))
        b.append(txt(px + 28, py + 44, t["v3_l%d_rot" % k], 13, "700", cor, sp="2"))
        b.append(txt(px + 28, py + 88, t["v3_l%d_nome" % k], 27, "700", NAVY))
        linhas(b, px + 28, py + 124, t["v3_l%d_txt" % k], 14.5, GRAY, 21)

    # as três perguntas
    qw, gap = 470, 35
    x0 = (W - (qw * 3 + gap * 2)) / 2
    qy, qh = py + ph + 34, 268
    for i in range(3):
        qx = x0 + i * (qw + gap)
        b.append(rect(qx, qy, qw, qh, PANEL, rx=14))
        b.append(rect(qx, qy, qw, qh, "none", BORDER, 1.5, rx=14))
        b.append(rect(qx, qy, 6, qh, ACCENT, rx=0))
        b.append(txt(qx + 26, qy + 44, t["v3_q%d_rot" % i], 12.5, "700", ACCENT, sp="1.5"))
        linhas(b, qx + 26, qy + 82, t["v3_q%d_perg" % i], 17.5, NAVY, 25, "700")
        b.append(line(qx + 26, qy + 168, qx + qw - 26, qy + 168, BORDER, 1.2))
        linhas(b, qx + 26, qy + 198, t["v3_q%d_txt" % i], 13.5, GRAY, 19)

    yb = qy + qh + 24
    b.append(rect(60, yb, W - 120, 62, AMBER_SOFT, rx=12))
    b.append(rect(60, yb, 6, 62, AMBER, rx=0))
    b.append(txt(92, yb + 38, t["v3_alerta"], 17, "700", NAVY))

    fecho(b, H, t["v3_faixa"], GREEN, GREEN_SOFT)
    footer(b, W, H, t["v3_rodape"])
    assert yb + 62 < H - 152, "v3 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v4: os três decaimentos
def v4(t, lang):
    H = 900
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    cw, gap = 470, 35
    x0 = (W - (cw * 3 + gap * 2)) / 2
    cy, ch = 210, 400
    cores = [AMBER, ACCENT, RED]
    softs = [AMBER_SOFT, ACCENT_SOFT, RED_SOFT]
    # a barra de velocidade: quanto mais cheia, mais rápido o decaimento
    velocidade = [0.45, 0.25, 1.0]
    for i in range(3):
        cx = x0 + i * (cw + gap)
        b.append(rect(cx, cy, cw, ch, softs[i], rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cores[i], 2, rx=14))
        b.append(rect(cx, cy, cw, 7, cores[i], rx=0))
        b.append(txt(cx + 26, cy + 50, t["v4_c%d_rot" % i], 13, "700", cores[i], sp="2"))
        b.append(txt(cx + 26, cy + 96, t["v4_c%d_nome" % i], 28, "700", NAVY))
        b.append(txt(cx + 26, cy + 132, t["v4_c%d_relogio" % i], 15, "400", GRAY_LIGHT,
                     style="italic"))
        # velocidade
        b.append(txt(cx + 26, cy + 174, t["v4_vel_rot"], 11.5, "700", GRAY_LIGHT, sp="1.5"))
        b.append(rect(cx + 26, cy + 186, cw - 52, 12, WHITE, rx=6))
        b.append(rect(cx + 26, cy + 186, (cw - 52) * velocidade[i], 12, cores[i], rx=6))
        b.append(line(cx + 26, cy + 224, cx + cw - 26, cy + 224, cores[i], 1.2))
        linhas(b, cx + 26, cy + 256, t["v4_c%d_txt" % i], 14.5, NAVY, 22)

    yb = cy + ch + 26
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v4_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 66, t["v4_barra2"], 14.5, "400", "#AEB6C2"))

    fecho(b, H, t["v4_faixa"], RED, RED_SOFT)
    footer(b, W, H, t["v4_rodape"])
    assert yb + 88 < H - 152, "v4 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------- v5: a grade de horizonte por durabilidade
def v5(t, lang):
    H = 1150
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    lx, lw = 60, 186          # coluna dos rótulos de linha
    cx0, cw, cgap = 262, 635, 20
    cy0, chh, rgap = 254, 272, 64

    # cabeçalhos de coluna
    for j in range(2):
        cx = cx0 + j * (cw + cgap)
        cor = GREEN if j == 0 else RED
        b.append(rect(cx, 204, cw, 38, cor, rx=8))
        b.append(txt(cx + cw / 2, 229, t["v5_col%d" % j], 15, "700", WHITE,
                     anchor="middle", sp="1.5"))

    for i in range(2):
        cy = cy0 + i * (chh + rgap)
        # rótulo de linha
        b.append(rect(lx, cy, lw, chh, PANEL, rx=12))
        b.append(rect(lx, cy, 6, chh, NAVY, rx=0))
        linhas(b, lx + 22, cy + 56, t["v5_lin%d" % i], 19, NAVY, 25, "700")
        linhas(b, lx + 22, cy + 132, t["v5_lin%d_sub" % i], 13, GRAY_LIGHT, 18)
        for j in range(2):
            cx = cx0 + j * (cw + cgap)
            k = i * 2 + j
            cor = GREEN if j == 0 else RED
            soft = GREEN_SOFT if j == 0 else RED_SOFT
            b.append(rect(cx, cy, cw, chh, soft, rx=12))
            b.append(rect(cx, cy, cw, chh, "none", cor, 1.8, rx=12))
            b.append(txt(cx + 24, cy + 44, t["v5_q%d_rot" % k], 19, "700", cor))
            b.append(line(cx + 24, cy + 64, cx + cw - 24, cy + 64, cor, 1.2))
            linhas(b, cx + 24, cy + 94, t["v5_q%d_txt" % k], 14, NAVY, 21)

    # a seta de financiamento: desce DENTRO da coluna que sobrevive ao conserto,
    # do quadrante rapido e duravel para o lento e duravel. Posta na calha entre
    # as duas linhas para nao ser lida como se apontasse para a coluna vermelha.
    ax = cx0 + cw / 2
    b.append(line(ax, cy0 + chh + 12, ax, cy0 + chh + rgap - 20, ACCENT, 4))
    b.append('<polygon points="%d,%d %d,%d %d,%d" fill="%s"/>' % (
        ax, cy0 + chh + rgap - 6, ax - 13, cy0 + chh + rgap - 26,
        ax + 13, cy0 + chh + rgap - 26, ACCENT))
    b.append(txt(ax + 26, cy0 + chh + rgap - 20, t["v5_seta"], 13, "700", ACCENT, sp="1.5"))

    yb = cy0 + chh * 2 + rgap + 26
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v5_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 66, t["v5_barra2"], 14.5, "400", "#AEB6C2"))

    fecho(b, H, t["v5_faixa"], ACCENT, ACCENT_SOFT)
    footer(b, W, H, t["v5_rodape"])
    assert yb + 88 < H - 152, "v5 encosta no fecho"
    return doc(W, H, "".join(b))


# ---------------------------------------------------------------- textos
T = {
    "pt": {
        "capa_kicker": "BUILDER-LED GROWTH — ARCO 2, PARTE 4",
        "capa_t1": "A tática que mais funciona hoje",
        "capa_t2": "costuma ser a que menos dura",
        "capa_sub": "Recomendação: como separar a tática que dura da que vai ser consertada",
        "capa_frase1": "Você entrou na lista, o concorrente também, e o agente pegou o outro —",
        "capa_frase2": "o motivo que ele escreveu falava do texto, não do produto.",
        "capa_creditof": "Três decisões de harness, três decaimentos, e a grade de horizonte por durabilidade",
        "capa_rodape": "Matheus Ramos · arco 2, parte 4",

        "v1_nome": "a2p4-harness-pt",
        "v1_kicker": "O HARNESS — ANTES DE O MODELO OPINAR",
        "v1_titulo": "Três decisões de engenharia estreitam o conjunto antes da escolha",
        "v1_sub": "Quem toma as três não é o mercado, e nunca vai comparar o seu produto com o do concorrente",
        "v1_c0_rot": "DECISÃO 1",
        "v1_c0_nome": "Catálogo",
        "v1_c0_num": "%s → %s" % (MENU_TUDO, MENU_FILTRADO),
        "v1_c0_num_sub": "sucesso de tarefa, de tudo exposto a menu filtrado",
        "v1_c0_txt": "Sete modelos, três tamanhos de menu\ne seis métodos de filtragem, com\n%d%% menos tokens no menu mínimo.\nEstar no catálogo grande pode valer\nmenos que estar no menu pequeno:\no catálogo grande derruba a chance\nde qualquer um ser escolhido direito" % MENU_TOKENS,
        "v1_c1_rot": "DECISÃO 2",
        "v1_c1_nome": "Recuperação",
        "v1_c1_num": "%s vs %s" % (K_EMBED, K_BM25),
        "v1_c1_num_sub": "candidatos vistos, embeddings contra BM25, mesmos dados",
        "v1_c1_txt": "%d vezes mais candidatos sobre o\nmesmo conjunto de dados, com a mesma\npergunta. Nada mudou no mercado nem\nno produto: mudou um componente de\nbusca. Expor o catálogo inteiro dá\n%s de acurácia; buscar antes dá\n%s, com %d%% menos tokens" % (K_FATOR, RAG_SEM, RAG_COM, RAG_TOKENS),
        "v1_c2_rot": "DECISÃO 3",
        "v1_c2_nome": "Ordem",
        "v1_c2_num": "%d modelos" % MODELOS_BIAS,
        "v1_c2_num_sub": "sobre APIs reais agrupadas por função equivalente",
        "v1_c2_txt": "Os modelos ou fixam num único\nfornecedor ou favorecem\ndesproporcionalmente as ferramentas\nque aparecem mais cedo no contexto.\nÉ o exemplo mais limpo de tática\nque funciona hoje e não vai durar —\nporque isso se chama viés",
        "v1_barra1": "Quem escreve o harness define catálogo, ordem e recuperação — e em parte também é produto selecionável",
        "v1_barra2": "Descrição de posição, não de conduta: o precedente é loja de aplicativo e sistema operacional, com a diferença de a camada aqui ser opaca e probabilística",
        "v1_faixa": "O tamanho da lista curta em que você disputa não é propriedade do seu mercado: é decisão de quem montou o agente.",
        "v1_rodape": "Builder-Led Growth, arco 2 · Babu e Iyer (jun/2026, preprint) · Gan e Sun (mai/2025, preprint) · Repantis et al. (mai/2026, preprint) · Blankenstein et al. (ICLR 2026)",

        "v2_nome": "a2p4-estratificacao-pt",
        "v2_kicker": "O QUE DECIDE ENTRE OS QUE SOBRARAM",
        "v2_titulo": "A mesma pergunta, compradores diferentes, e o conjunto só se mexe para quem não lidera",
        "v2_sub": "%s execuções sobre 10 perfis de comprador, 8 perguntas e 3 configurações de modelo — a primeira pergunta do desenho é \"best CRM software\"" % AUDIT_RODADAS,
        "v2_p0_rot": "LÍDER DE CATEGORIA",
        "v2_p0_nome": "Resistente ao perfil",
        "v2_p0_num": "%d%%" % LIDER_CONSISTENCIA,
        "v2_p0_num_sub": "de consistência de marca de um comprador para o outro",
        "v2_p0_txt": "Quem já é o padrão da categoria\nquase não é disputado. A memória\ndo modelo o sustenta, e exposição\nrepetida a um mesmo endereço de API\nno pré-treino amplifica o viés a\nfavor daquele fornecedor",
        "v2_p1_rot": "MARCA DE MEIO DE MERCADO",
        "v2_p1_nome": "Troca de lugar",
        "v2_p1_num": "%d%%" % MEIO_TROCA,
        "v2_p1_num_sub": "do conjunto trocado conforme o perfil de quem pergunta muda",
        "v2_p1_txt": "Três em cada quatro vezes que\nalguém com outro contexto faz a\nmesma pergunta, você sai do\nconjunto. Não por mérito, não por\ncomparação: porque o seu lugar\nnunca foi firme",
        "v2_meio_rot": "PERFIL DE COMPRADOR\nNO PROMPT",
        "v2_meio_txt": "derruba a similaridade\nentre os conjuntos\nem %s ponto\n(índice de Jaccard)" % JACCARD,
        "v2_barra1": "O texto move a escolha quando o modelo não tem outra coisa para usar — e move menos quanto mais ele já tem formado",
        "v2_barra2": "Com especificações idênticas, a marca dona da palavra do pedido foi escolhida em %d%% das rodadas no modelo menor e entre %d%% e %d%% no maior (medição própria, 1º de setembro de 2026)" % (E003_MENOR, E003_MAIOR_MIN, E003_MAIOR_MAX),
        "v2_faixa": "Bibliotecas populares usadas em até %d%% dos casos em que não eram necessárias; Python dominante em %d%% das tarefas onde não é a melhor escolha." % (LIB_DESNECESSARIA, PYTHON_DOMINANTE),
        "v2_rodape": "Builder-Led Growth, arco 2 · Jack, Lehman, Maloney e Xu (mai/2026, preprint de auditoria) · Twist et al. (Findings of ACL 2026, %d modelos) · Blankenstein et al. (ICLR 2026)" % MODELOS_TWIST,

        "v3_nome": "a2p4-implementacao-ou-estrutura-pt",
        "v3_kicker": "O CRITÉRIO — A ESPINHA DA PEÇA",
        "v3_titulo": "Tática que explora a implementação decai; tática que explora a estrutura fica",
        "v3_sub": "Viés de posição é defeito, e defeito é consertado. Alinhamento semântico entre pedido e descrição não é defeito, e não vai ser corrigido",
        "v3_l0_rot": "EXPLORA A IMPLEMENTAÇÃO ATUAL",
        "v3_l0_nome": "Decai quando consertam",
        "v3_l0_txt": "A tática de otimizar para a posição e a correção que a destrói\nnasceram no mesmo artigo, com poucas páginas de distância:\nfiltrar para o subconjunto relevante e amostrar uniformemente",
        "v3_l1_rot": "EXPLORA A ESTRUTURA DO JOGO",
        "v3_l1_nome": "Sobrevive à mudança",
        "v3_l1_txt": "Alinhamento semântico entre o que o usuário pediu e o metadado\nda ferramenta é o fator mais forte da seleção. Corrigir a ordem\ntorna o alinhamento MAIS decisivo, não menos",
        "v3_q0_rot": "PERGUNTA 1",
        "v3_q0_perg": "Quem construiu o\nmecanismo chamaria\nisso de defeito?",
        "v3_q0_txt": "Se sim, você está com prazo de\nvalidade. Viés de posição,\ndegradação por catálogo grande e\nsensibilidade a formatação são\ndefeitos, e há equipes pagas\npara consertá-los",
        "v3_q1_rot": "PERGUNTA 2",
        "v3_q1_perg": "A vantagem some se\ntodo mundo fizer\nigual?",
        "v3_q1_txt": "Se sim, é vantagem de escassez,\nnão de estrutura. Ela dura\nenquanto poucos souberem, e o\nrelógio dela é o da difusão da\nnotícia, não o do seu roteiro\nde produto",
        "v3_q2_rot": "PERGUNTA 3",
        "v3_q2_perg": "A tática continua\nfazendo sentido se o\nmecanismo virar outro?",
        "v3_q2_txt": "Descrever com precisão o que o\nproduto faz vale para busca,\npara agente, para catálogo de\nplataforma e para a pessoa que\nlê a documentação. Vale no dia\nem que nada disso existir assim",
        "v3_alerta": "Ninguém publicou quanto tempo dura a vantagem de uma tática: o critério serve para decidir, não para prever data.",
        "v3_faixa": "Uma ferramenta escolhida porque a descrição dela é inequívoca continua sendo escolhida depois do conserto.",
        "v3_rodape": "Builder-Led Growth, arco 2 · Blankenstein et al., BiasBusters (ICLR 2026) — o achado, a ressalva e a própria correção estão no mesmo artigo",

        "v4_nome": "a2p4-tres-decaimentos-pt",
        "v4_kicker": "OS TRÊS DECAIMENTOS",
        "v4_titulo": "Três caminhos de uma tática decair",
        "v4_sub": "Dois todo mundo prevê. O terceiro chega sem aviso: a plataforma absorve a tática e entrega a todo mundo de uma vez",
        "v4_vel_rot": "VELOCIDADE DO DECAIMENTO",
        "v4_c0_rot": "CAMINHO 1",
        "v4_c0_nome": "O defeito consertado",
        "v4_c0_relogio": "relógio: o ciclo de versão do harness",
        "v4_c0_txt": "Previsível: o grupo que mediu o\nviés propôs a correção no mesmo\ntrabalho. A data é que ninguém\nanuncia: a tática para de render\nsem que nada tenha mudado do\nseu lado",
        "v4_c1_rot": "CAMINHO 2",
        "v4_c1_nome": "O concorrente copiando",
        "v4_c1_relogio": "relógio: o ritmo do que é acumulável",
        "v4_c1_txt": "O mais lento dos três, e o único\nque a literatura de estratégia já\ntratava antes de qualquer agente.\nTem freio conhecido: copiar custa,\ne quanto mais a tática depender de\nacúmulo, mais devagar a cópia anda",
        "v4_c2_rot": "CAMINHO 3",
        "v4_c2_nome": "A plataforma absorvendo",
        "v4_c2_relogio": "relógio: um lançamento de produto de terceiro",
        "v4_c2_txt": "Nenhum concorrente agiu, nenhum\ndefeito foi consertado. Em %s\no Ghost passou a gerar o llms.txt\ne a servir Markdown por URL, como\nrecurso nativo — desligado por\npadrão, e ligado em Configurações" % GHOST_DATA,
        "v4_barra1": "A absorção não é automática: é uma caixa de seleção, e cada site perde a vantagem na data em que o seu administrador clicou",
        "v4_barra2": "Para quem vendia a tática como serviço, o mercado não encolheu de uma vez: encolheu em pedaços, sem aviso e sem curva",
        "v4_faixa": "O que a plataforma consegue gerar por você, ela vai gerar — e no dia em que gerar, entrega a todo mundo junto.",
        "v4_rodape": "Builder-Led Growth, arco 2 · Ghost, registro de mudanças (%s) · First Round, llms.txt conferido em 16 de setembro de 2026 · a data de ativação do site não é pública" % GHOST_DATA,

        "v5_nome": "a2p4-grade-pt",
        "v5_kicker": "O QUE FAZER PRIMEIRO",
        "v5_titulo": "Horizonte e durabilidade são dois eixos, não um",
        "v5_sub": "Horizonte responde quando o efeito aparece; durabilidade responde se ele sobrevive ao mecanismo mudar",
        "v5_col0": "SOBREVIVE AO CONSERTO",
        "v5_col1": "DECAI QUANDO CONSERTAM",
        "v5_lin0": "Efeito\nrápido",
        "v5_lin0_sub": "dias a semanas",
        "v5_lin1": "Efeito\nlento",
        "v5_lin1_sub": "meses, ou o treino\nseguinte do modelo",
        "v5_q0_rot": "Fazer primeiro",
        "v5_q0_txt": "Descrição inequívoca no lugar onde o agente lê\nUma única definição do produto, com as mesmas palavras\nComeçar sem falar com uma pessoa\nDocumentação canônica num endereço só\nMedir e publicar o atrito do par\n\nMelhor relação entre esforço e permanência do arco",
        "v5_q1_rot": "Usar sabendo, com a validade anotada",
        "v5_q1_txt": "Posição no catálogo\nSer poucas ferramentas em vez de muitas\nQualquer coisa que explore viés de seleção\nFormato que só o harness de hoje lê assim\n\nÉ onde mora quase todo o conteúdo corrente sobre\no assunto. O erro não é executar: é não marcar o prazo",
        "v5_q2_rot": "O investimento real",
        "v5_q2_txt": "Presença acumulada no corpus\nMaterial comparativo escrito por terceiro\nVirar o jeito padrão de resolver o problema\nEntrar no registro corporativo de fornecedores\nCertificação\n\nO único quadrante que precisa de defesa orçamentária",
        "v5_q3_rot": "Evitar",
        "v5_q3_txt": "Custa meses e morre com a mudança.\n\nNão tem uso.",
        "v5_seta": "FINANCIA",
        "v5_barra1": "Financiar o lento com o rápido: o primeiro quadrante produz efeito no custo de aquisição dentro do trimestre que a empresa mede",
        "v5_barra2": "Quem tenta aprovar o investimento lento sem o rápido na frente está pedindo fé; quem executa só o rápido está construindo uma vantagem que expira",
        "v5_faixa": "A legibilidade vira commodity. A consistência não — nenhum gerador produz a mesma definição repetida por anos.",
        "v5_rodape": "Builder-Led Growth, arco 2 · a coluna da direita é feita de propriedades do mecanismo de hoje; a da esquerda, do produto e do que se sabe dele",
    },
    "en": {
        "capa_kicker": "BUILDER-LED GROWTH — ARC 2, PART 4",
        "capa_t1": "The tactic that works best today",
        "capa_t2": "tends to be the one that lasts least",
        "capa_sub": "Recommendation: telling the tactic that lasts from the one that gets patched",
        "capa_frase1": "You made it onto the list, so did your competitor, and the agent took the other —",
        "capa_frase2": "the reason it wrote down described the text, not the product.",
        "capa_creditof": "Three harness decisions, three decays, and the horizon-by-durability grid",
        "capa_rodape": "Matheus Ramos · arc 2, part 4",

        "v1_nome": "a2p4-harness-en",
        "v1_kicker": "THE HARNESS — BEFORE THE MODEL HAS AN OPINION",
        "v1_titulo": "Three engineering decisions narrow the set before the choice",
        "v1_sub": "The people making all three are not the market, and will never compare your product with your competitor's",
        "v1_c0_rot": "DECISION 1",
        "v1_c0_nome": "Catalogue",
        "v1_c0_num": "%s → %s" % (MENU_TUDO_EN, MENU_FILTRADO_EN),
        "v1_c0_num_sub": "task success, from everything exposed to a filtered menu",
        "v1_c0_txt": "Seven models, three menu sizes and\nsix filtering methods, with %d%% fewer\ntokens on the minimum menu. Being in\nthe large catalogue can be worth less\nthan being in the small menu: the\nlarge catalogue drives down the odds\nof anyone being picked properly" % MENU_TOKENS,
        "v1_c1_rot": "DECISION 2",
        "v1_c1_nome": "Retrieval",
        "v1_c1_num": "%s vs %s" % (K_EMBED_EN, K_BM25_EN),
        "v1_c1_num_sub": "candidates seen, embeddings versus BM25, same data",
        "v1_c1_txt": "%d times as many candidates over the\nsame dataset, with the same question.\nNothing changed in the market or in\nthe product: a search component\nchanged. Exposing the whole catalogue\ngives %s accuracy; searching first\ngives %s, with %d%% fewer tokens" % (K_FATOR, RAG_SEM_EN, RAG_COM_EN, RAG_TOKENS),
        "v1_c2_rot": "DECISION 3",
        "v1_c2_nome": "Order",
        "v1_c2_num": "%d models" % MODELOS_BIAS,
        "v1_c2_num_sub": "over real APIs grouped by equivalent function",
        "v1_c2_txt": "The models either fixate on a single\nprovider or disproportionately favour\nthe tools appearing earlier in the\ncontext. It is the cleanest example\nof a tactic that works today and will\nnot last — because what it exploits\nis called bias",
        "v1_barra1": "Whoever writes the harness defines catalogue, order and retrieval — and is, in part, also a selectable product",
        "v1_barra2": "A description of position, not of conduct: the precedent is app stores and operating systems, with the difference that this layer is opaque and probabilistic",
        "v1_faixa": "The size of the shortlist you compete in is not a property of your market: it is a decision made by whoever assembled the agent.",
        "v1_rodape": "Builder-Led Growth, arc 2 · Babu and Iyer (Jun 2026, preprint) · Gan and Sun (May 2025, preprint) · Repantis et al. (May 2026, preprint) · Blankenstein et al. (ICLR 2026)",

        "v2_nome": "a2p4-stratification-en",
        "v2_kicker": "WHAT DECIDES AMONG THOSE LEFT",
        "v2_titulo": "Same question, different buyers, and the set only moves for whoever does not lead",
        "v2_sub": "%s runs across 10 buyer personas, 8 prompts and 3 model configurations — the design's first prompt is \"best CRM software\"" % AUDIT_RODADAS_EN,
        "v2_p0_rot": "CATEGORY LEADER",
        "v2_p0_nome": "Persona-resistant",
        "v2_p0_num": "%d%%" % LIDER_CONSISTENCIA,
        "v2_p0_num_sub": "same-brand consistency from one buyer to the next",
        "v2_p0_txt": "Whoever is already the category\ndefault is barely contested. The\nmodel's memory holds them up, and\nrepeated exposure to a single API\nendpoint in pre-training amplifies\nthe bias in that provider's favour",
        "v2_p1_rot": "MID-MARKET BRAND",
        "v2_p1_nome": "Swapped out",
        "v2_p1_num": "%d%%" % MEIO_TROCA,
        "v2_p1_num_sub": "of the set swapped as the asking persona changes",
        "v2_p1_txt": "Three out of every four times\nsomeone with a different context\nasks the same question, you drop\nout of the set. Not on merit, not\nby comparison: because your place\nwas never firm",
        "v2_meio_rot": "A BUYER PERSONA\nIN THE PROMPT",
        "v2_meio_txt": "drops the similarity\nbetween the sets\nby %s points\n(Jaccard index)" % JACCARD_EN,
        "v2_barra1": "Text moves the choice when the model has nothing else to work with — and moves it less the more the model already holds",
        "v2_barra2": "With identical specifications, the brand owning the word the request asked for was chosen in %d%% of runs on the smaller model and between %d%% and %d%% on the larger (own measurement, 1 September 2026)" % (E003_MENOR, E003_MAIOR_MIN, E003_MAIOR_MAX),
        "v2_faixa": "Popular libraries used in up to %d%% of cases where they were not required; Python dominant in %d%% of tasks where it is not the right choice." % (LIB_DESNECESSARIA, PYTHON_DOMINANTE),
        "v2_rodape": "Builder-Led Growth, arc 2 · Jack, Lehman, Maloney and Xu (May 2026, audit preprint) · Twist et al. (Findings of ACL 2026, %d models) · Blankenstein et al. (ICLR 2026)" % MODELOS_TWIST,

        "v3_nome": "a2p4-implementation-or-structure-en",
        "v3_kicker": "THE CRITERION — THE SPINE OF THE PIECE",
        "v3_titulo": "A tactic exploiting the implementation decays; one exploiting the structure lasts",
        "v3_sub": "Position bias is a defect, and defects get patched. Semantic alignment between request and description is not a defect, and will not be corrected",
        "v3_l0_rot": "EXPLOITS THE CURRENT IMPLEMENTATION",
        "v3_l0_nome": "Decays when patched",
        "v3_l0_txt": "The tactic of optimising for position and the correction that\ndestroys it were born in the same paper, a few pages apart:\nfilter to the relevant subset, then sample uniformly",
        "v3_l1_rot": "EXPLOITS THE STRUCTURE OF THE GAME",
        "v3_l1_nome": "Survives the change",
        "v3_l1_txt": "Semantic alignment between what the user asked for and the\ntool's metadata is the strongest driver of selection. Fixing the\nordering makes alignment MORE decisive, not less",
        "v3_q0_rot": "QUESTION 1",
        "v3_q0_perg": "Would whoever built\nthe mechanism call\nthis a defect?",
        "v3_q0_txt": "If yes, you are on borrowed time.\nPosition bias, degradation under a\nlarge catalogue and sensitivity to\nprompt formatting are defects, and\nthere are teams paid to fix them",
        "v3_q1_rot": "QUESTION 2",
        "v3_q1_perg": "Does the advantage\nvanish if everyone\ndoes the same?",
        "v3_q1_txt": "If yes, it is an advantage of\nscarcity, not of structure. It\nlasts as long as few people know,\nand its clock is the spread of the\nnews, not your product roadmap",
        "v3_q2_rot": "QUESTION 3",
        "v3_q2_perg": "Does it still make\nsense if the mechanism\nbecomes something else?",
        "v3_q2_txt": "Describing precisely what a product\ndoes holds for search, for agents,\nfor a platform catalogue and for the\nperson reading the docs. It holds on\nthe day none of those exist this way",
        "v3_alerta": "Nobody has published how long a tactic's advantage lasts: the criterion is good for deciding, not for predicting a date.",
        "v3_faixa": "A tool chosen because its description is unambiguous keeps being chosen after the patch.",
        "v3_rodape": "Builder-Led Growth, arc 2 · Blankenstein et al., BiasBusters (ICLR 2026) — the finding, the caveat and the correction itself are in the same paper",

        "v4_nome": "a2p4-three-decays-en",
        "v4_kicker": "THE THREE DECAYS",
        "v4_titulo": "Three paths for a tactic to decay",
        "v4_sub": "Everyone sees two coming. The third arrives unannounced: the platform absorbs the tactic and hands it to everybody at once",
        "v4_vel_rot": "SPEED OF THE DECAY",
        "v4_c0_rot": "PATH 1",
        "v4_c0_nome": "The patched defect",
        "v4_c0_relogio": "clock: the harness release cycle",
        "v4_c0_txt": "Predictable: the group that measured\nthe bias proposed the fix in the\nsame work. Only the date goes\nunannounced: the tactic stops paying\nwith nothing having changed on\nyour side",
        "v4_c1_rot": "PATH 2",
        "v4_c1_nome": "The competitor copying",
        "v4_c1_relogio": "clock: the pace of what can be accumulated",
        "v4_c1_txt": "The slowest of the three, and the\nonly one strategy literature already\nhandled before any agent existed. It\nhas a known brake: copying costs, and\nthe more a tactic depends on what is\naccumulated, the slower the copy moves",
        "v4_c2_rot": "PATH 3",
        "v4_c2_nome": "The platform absorbing",
        "v4_c2_relogio": "clock: somebody else's product launch",
        "v4_c2_txt": "No competitor acted, no defect was\npatched. On %s Ghost began\ngenerating llms.txt and serving\nMarkdown by URL as a native feature —\nshipped off by default, and turned\non in Settings" % GHOST_DATA_EN,
        "v4_barra1": "Absorption is not automatic: it is a checkbox, and each site loses the advantage on the date its administrator clicked",
        "v4_barra2": "For anyone selling the tactic as a service, the market did not shrink all at once: it shrank in pieces, with no warning and no curve",
        "v4_faixa": "Whatever a platform can generate for you, it will generate — and on the day it does, it hands it to everybody at once.",
        "v4_rodape": "Builder-Led Growth, arc 2 · Ghost changelog (%s) · First Round llms.txt checked on 16 September 2026 · the site's activation date is not public" % GHOST_DATA_EN,

        "v5_nome": "a2p4-grid-en",
        "v5_kicker": "WHAT TO DO FIRST",
        "v5_titulo": "Horizon and durability are two axes, not one",
        "v5_sub": "Horizon answers when the effect shows up; durability answers whether it survives the mechanism changing",
        "v5_col0": "SURVIVES THE PATCH",
        "v5_col1": "DECAYS WHEN PATCHED",
        "v5_lin0": "Fast\neffect",
        "v5_lin0_sub": "days to weeks",
        "v5_lin1": "Slow\neffect",
        "v5_lin1_sub": "months, or the model's\nnext training run",
        "v5_q0_rot": "Do this first",
        "v5_q0_txt": "Unambiguous description where the agent reads\nA single definition of the product, in the same words\nLetting someone start without talking to a person\nCanonical documentation at one address\nMeasuring and publishing the pair's friction\n\nBest ratio of effort to permanence in the arc",
        "v5_q1_rot": "Use knowingly, with the expiry written down",
        "v5_q1_txt": "Position in the catalogue\nBeing few tools rather than many\nAnything exploiting selection bias\nA format only today's harness reads that way\n\nWhere nearly all current commentary lives. The mistake\nis not executing: it is not marking the expiry",
        "v5_q2_rot": "The real investment",
        "v5_q2_txt": "Accumulated corpus presence\nComparative material written by a third party\nBecoming the default way to solve the problem\nGetting into the corporate vendor registry\nCertification\n\nThe only quadrant that needs a budget defence",
        "v5_q3_rot": "Avoid",
        "v5_q3_txt": "Costs months and dies with the change.\n\nNo use.",
        "v5_seta": "FUNDS",
        "v5_barra1": "Fund the slow with the fast: the first quadrant produces an effect on acquisition cost inside the quarter the company measures",
        "v5_barra2": "Anyone trying to approve the slow investment without the fast one in front is asking for faith; anyone executing only the fast one builds an advantage that expires",
        "v5_faixa": "Legibility becomes a commodity. Consistency does not — no generator produces the same definition repeated over years.",
        "v5_rodape": "Builder-Led Growth, arc 2 · the right-hand column is made of properties of today's mechanism; the left-hand one, of the product and what is known of it",
    },
}


def gerar(lang):
    t = T[lang]
    salvar("a2p4-capa-pt" if lang == "pt" else "a2p4-cover-en", capa(t, lang), scale=1.5)
    for i, fn in enumerate((v1, v2, v3, v4, v5), start=1):
        salvar(t["v%d_nome" % i], fn(t, lang))


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    for lang in (["pt", "en"] if alvo is None else [alvo]):
        gerar(lang)
