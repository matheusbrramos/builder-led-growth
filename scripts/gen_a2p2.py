#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais do arco 2, parte 2 — candidatura: as três portas para o conjunto.

PT e EN no mesmo arquivo. Helpers de desenho importados do gen_p4; a
rasterização pelo Chrome e o `fecho` vêm do gen_a2p1, que já resolveu o
problema do cairosvg sem biblioteca nativa nesta máquina. Cada função termina
com assert de folga contra o rodapé: peça torta falha alto em vez de sair
publicada.

Os seis visuais seguem os seis marcadores da peça, na ordem em que aparecem:
três lógicas (tabela), três portas e relógios, anatomia dos sete produtos,
as sete plataformas, o experimento com quatro provedores fictícios, e os dois
extremos com o meio. Os números existem uma vez só, no topo, e batem com o
texto das duas línguas — quem mudar um, muda nos três lugares.

Escrito em 5 de setembro de 2026, depois de Mat aprovar o português.

Uso:  python scripts/gen_a2p2.py          # gera PT e EN
      python scripts/gen_a2p2.py pt       # só português
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
    GRAY_LIGHT, GREEN, GREEN_SOFT, MUTED, NAVY, NAVY_DEEP, PANEL, WHITE,
    doc, footer, header, line, rect, txt,
)
from gen_a2p1 import RED, RED_SOFT, _cairo, _png_pelo_chrome, fecho  # noqa: E402

W = 1600
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "visuais", "arco2-parte-02")

# ---------------------------------------------------------------- números
# Uma vez só. Batem com o texto das duas línguas.
HAIKU_CONF = (0, 100, 0, 0)      # N, C, S, A sob o tom de confiabilidade
HAIKU_RAP = (0, 0, 100, 0)       # sob o tom de rapidez
SONNET_CONF = (22, 63, 8, 7)
SONNET_RAP = (5, 0, 95, 0)
RODADAS_VALIDAS = 318
PAGINAS_CORR = "0,17 / 0,19"
PAGINAS_CORR_EN = "0.17 / 0.19"


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


# ------------------------------------------------ v1: três lógicas, tabela
def v1(t, lang):
    H = 1030
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    cols = [60, 340, 780, 1150]           # início de cada coluna
    widths = [280, 440, 370, 390]
    y0 = 196
    # cabeçalho da tabela
    for i, h_ in enumerate(t["v1_cols"]):
        b.append(txt(cols[i] + 16, y0 + 24, h_, 13, "700", GRAY_LIGHT, sp="1.5"))
    b.append(line(60, y0 + 40, W - 60, y0 + 40, BORDER, 1.5))

    rh = 112
    cores = [GRAY_LIGHT, GRAY_LIGHT, GRAY_LIGHT, AMBER, ACCENT]
    for r in range(5):
        y = y0 + 52 + r * (rh + 8)
        soft = ACCENT_SOFT if r == 4 else (AMBER_SOFT if r == 3 else PANEL)
        b.append(rect(60, y, W - 120, rh, soft, rx=12))
        b.append(rect(60, y, 6, rh, cores[r], rx=0))
        linhas(b, cols[0] + 22, y + 40, t["v1_r%d_0" % r], 19, NAVY, 24, "700")
        for c in (1, 2, 3):
            linhas(b, cols[c] + 16, y + 34, t["v1_r%d_%d" % (r, c)], 14, GRAY, 20)
    yb = y0 + 52 + 5 * (rh + 8)

    fecho(b, H, t["v1_faixa"], ACCENT, ACCENT_SOFT)
    footer(b, W, H, t["v1_rodape"])
    assert yb < H - 152, "v1 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v2: três portas, três relógios
def v2(t, lang):
    H = 900
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    cw, gap = 470, 35
    x0 = (W - (cw * 3 + gap * 2)) / 2
    cy, ch = 210, 372
    cores = [ACCENT, GREEN, AMBER]
    softs = [ACCENT_SOFT, GREEN_SOFT, AMBER_SOFT]
    for i in range(3):
        cx = x0 + i * (cw + gap)
        b.append(rect(cx, cy, cw, ch, softs[i], rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cores[i], 2, rx=14))
        b.append(rect(cx, cy, cw, 7, cores[i], rx=0))
        b.append(txt(cx + 26, cy + 50, t["v2_p%d_rot" % i], 13, "700", cores[i], sp="2"))
        b.append(txt(cx + 26, cy + 92, t["v2_p%d_nome" % i], 30, "700", NAVY))
        b.append(txt(cx + 26, cy + 146, t["v2_p%d_relogio" % i], 40, "700", cores[i]))
        b.append(txt(cx + 26, cy + 176, t["v2_p%d_rel_sub" % i], 14, "400", GRAY_LIGHT,
                     style="italic"))
        b.append(line(cx + 26, cy + 198, cx + cw - 26, cy + 198, cores[i], 1.2))
        linhas(b, cx + 26, cy + 228, t["v2_p%d_txt" % i], 14.5, NAVY, 22)

    yb = cy + ch + 30
    b.append(rect(60, yb, W - 120, 84, NAVY, rx=14))
    b.append(txt(92, yb + 34, t["v2_barra1"], 21, "700", WHITE))
    b.append(txt(92, yb + 64, t["v2_barra2"], 15, "400", "#AEB6C2"))

    fecho(b, H, t["v2_faixa"])
    footer(b, W, H, t["v2_rodape"])
    assert yb + 84 < H - 152, "v2 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v3: anatomia dos sete
def v3(t, lang):
    H = 920
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    lx, lw = 60, 280                    # coluna de rótulos
    cw = 171                            # sete colunas de produto
    x0 = lx + lw + 8
    y0 = 200
    prods = t["v3_prods"]
    for i, p in enumerate(prods):
        b.append(txt(x0 + i * cw + cw / 2, y0 + 26, p, 15, "700", NAVY, anchor="middle"))
    b.append(line(60, y0 + 42, W - 60, y0 + 42, BORDER, 1.5))

    rh = 108
    for r in range(4):
        y = y0 + 54 + r * (rh + 8)
        b.append(rect(lx, y, W - 120, rh, PANEL, rx=12))
        b.append(rect(lx, y, 6, rh, ACCENT, rx=0))
        linhas(b, lx + 22, y + 44, t["v3_l%d" % r], 16, NAVY, 21, "700")
        for i in range(7):
            estado, texto = t["v3_c%d_%d" % (r, i)]
            cor = {"sim": GREEN, "nao": RED, "meio": AMBER, "na": GRAY_LIGHT}[estado]
            soft = {"sim": GREEN_SOFT, "nao": RED_SOFT, "meio": AMBER_SOFT, "na": WHITE}[estado]
            cx = x0 + i * cw
            b.append(rect(cx + 6, y + 12, cw - 12, rh - 24, soft, rx=10))
            b.append(rect(cx + 6, y + 12, cw - 12, rh - 24, "none", cor, 1.2, rx=10))
            linhas(b, cx + cw / 2, y + 44, texto, 13.5, NAVY, 18, "600", anchor="middle")
    yb = y0 + 54 + 4 * (rh + 8)

    fecho(b, H, t["v3_faixa"], GREEN, GREEN_SOFT)
    footer(b, W, H, t["v3_rodape"])
    assert yb < H - 152, "v3 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v4: as sete plataformas
def v4(t, lang):
    H = 1070
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    cols = [60, 330, 830, 1130]
    y0 = 196
    for i, h_ in enumerate(t["v4_cols"]):
        b.append(txt(cols[i] + 16, y0 + 24, h_, 13, "700", GRAY_LIGHT, sp="1.5"))
    b.append(line(60, y0 + 40, W - 60, y0 + 40, BORDER, 1.5))

    rh = 84
    for r in range(7):
        y = y0 + 52 + r * (rh + 8)
        exc = (r == 3)                   # v0 é a exceção
        soft = GREEN_SOFT if exc else PANEL
        cor = GREEN if exc else GRAY_LIGHT
        b.append(rect(60, y, W - 120, rh, soft, rx=12))
        b.append(rect(60, y, 6, rh, cor, rx=0))
        b.append(txt(cols[0] + 22, y + 50, t["v4_r%d_0" % r], 18, "700", NAVY))
        linhas(b, cols[1] + 16, y + 34, t["v4_r%d_1" % r], 14, GRAY, 20)
        vis = t["v4_r%d_2" % r]
        cvis = GREEN if vis[0] == "sim" else (AMBER if vis[0] == "meio" else RED)
        b.append(txt(cols[2] + 16, y + 50, vis[1], 15, "700", cvis))
        linhas(b, cols[3] + 16, y + 34, t["v4_r%d_3" % r], 14, GRAY, 20)
    yb = y0 + 52 + 7 * (rh + 8)

    fecho(b, H, t["v4_faixa"], AMBER, AMBER_SOFT)
    footer(b, W, H, t["v4_rodape"])
    assert yb < H - 152, "v4 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v5: o experimento
def v5(t, lang):
    H = 960
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    cores = [GRAY_LIGHT, ACCENT, GREEN, RED]          # N, C, S, A
    pw = 700
    py, ph = 200, 420
    dados = [(t["v5_m0"], HAIKU_CONF, HAIKU_RAP), (t["v5_m1"], SONNET_CONF, SONNET_RAP)]
    for k, (nome, conf, rap) in enumerate(dados):
        px = 60 if k == 0 else W - 60 - pw
        b.append(rect(px, py, pw, ph, PANEL, rx=14))
        b.append(txt(px + 24, py + 40, nome, 20, "700", NAVY))
        b.append(txt(px + pw - 24, py + 40, t["v5_n"], 13, "400", GRAY_LIGHT, anchor="end"))
        base = py + ph - 74
        escala = 2.4                                   # 100% = 240 px
        for g, (valores, rot) in enumerate(((conf, t["v5_tom0"]), (rap, t["v5_tom1"]))):
            gx = px + 40 + g * 340
            for i, v in enumerate(valores):
                bx = gx + i * 72
                h_ = max(3, v * escala)
                b.append(rect(bx, base - h_, 54, h_, cores[i], rx=4))
                b.append(txt(bx + 27, base - h_ - 8, "%d%%" % v, 13, "700",
                             cores[i] if v else GRAY_LIGHT, anchor="middle"))
                b.append(txt(bx + 27, base + 20, t["v5_letras"][i], 13, "700", cores[i],
                             anchor="middle"))
            b.append(txt(gx + 135, base + 46, rot, 13.5, "400", GRAY, anchor="middle",
                         style="italic"))
        b.append(line(px + 30, base, px + pw - 30, base, BORDER, 1.2))

    # legenda dos quatro textos
    ly = py + ph + 22
    lx = 60
    for i in range(4):
        b.append(rect(lx, ly + 4, 16, 16, cores[i], rx=3))
        b.append(txt(lx + 24, ly + 17, t["v5_leg"][i], 14, "400", GRAY))
        lx += 370

    yb = ly + 42
    b.append(rect(60, yb, W - 120, 78, NAVY, rx=14))
    b.append(txt(92, yb + 32, t["v5_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 60, t["v5_barra2"], 14.5, "400", "#AEB6C2"))

    fecho(b, H, t["v5_faixa"])
    footer(b, W, H, t["v5_rodape"])
    assert yb + 78 < H - 152, "v5 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v6: os dois extremos e o meio
def v6(t, lang):
    H = 920
    b = []
    header(b, t["v6_kicker"], t["v6_titulo"], t["v6_sub"], H)

    cw, gap = 470, 35
    x0 = (W - (cw * 3 + gap * 2)) / 2
    cy, ch = 200, 410
    cores = [RED, AMBER, ACCENT]
    softs = [RED_SOFT, AMBER_SOFT, ACCENT_SOFT]
    for i in range(3):
        cx = x0 + i * (cw + gap)
        b.append(rect(cx, cy, cw, ch, softs[i], rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cores[i], 2, rx=14))
        b.append(rect(cx, cy, cw, 7, cores[i], rx=0))
        b.append(txt(cx + 26, cy + 50, t["v6_c%d_rot" % i], 13, "700", cores[i], sp="2"))
        b.append(txt(cx + 26, cy + 88, t["v6_c%d_nome" % i], 24, "700", NAVY))
        for r in range(3):
            ry = cy + 124 + r * 88
            b.append(rect(cx + 20, ry, cw - 40, 76, WHITE, rx=10))
            b.append(txt(cx + 36, ry + 26, t["v6_porta"][r], 12.5, "700", cores[i], sp="1.5"))
            linhas(b, cx + 36, ry + 50, t["v6_c%d_%d" % (i, r)], 14, NAVY, 19)

    yb = cy + ch + 28
    b.append(rect(60, yb, W - 120, 78, NAVY, rx=14))
    b.append(txt(W / 2, yb + 34, t["v6_barra1"], 22, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 62, t["v6_barra2"], 15, "400", "#AEB6C2", anchor="middle"))

    fecho(b, H, t["v6_faixa"], AMBER, AMBER_SOFT)
    footer(b, W, H, t["v6_rodape"])
    assert yb + 78 < H - 152, "v6 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ capa
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


# ---------------------------------------------------------------- textos
T = {
    "pt": {
        "capa_kicker": "BUILDER-LED GROWTH — ARCO 2, PARTE 2",
        "capa_t1": "Ninguém perguntou por você.",
        "capa_t2": "Mesmo assim, você entrou ou ficou de fora",
        "capa_sub": "Candidatura: as três portas para o conjunto de onde a máquina escolhe",
        "capa_frase1": "Um CRM montado com IA em três semanas, quatro fornecedores trabalhando dentro dele,",
        "capa_frase2": "e ninguém na empresa buscou, comparou ou viu nenhum dos quatro.",
        "capa_creditof": "Três lógicas, três portas, três relógios, e um experimento com %d rodadas" % RODADAS_VALIDAS,
        "capa_rodape": "Matheus Ramos · arco 2, parte 2",

        "v1_nome": "a2p2-tres-logicas-pt",
        "v1_kicker": "TRÊS LÓGICAS, TRÊS LEITORES",
        "v1_titulo": "Quem lê, e o que se mede em cada prática de ser encontrado",
        "v1_sub": "Nas quatro primeiras linhas, alguém perguntou. Na última, ninguém perguntou pelo fornecedor",
        "v1_cols": ["PRÁTICA", "QUEM CUNHOU, QUANDO", "QUEM LÊ", "O QUE SE MEDE"],
        "v1_r0_0": "SEO",
        "v1_r0_1": "Autoria disputada, 1995–1997. Registro\ndatado: Usenet, 26 jul 1997 (apurado por\nDanny Sullivan em 2004), que o popularizou",
        "v1_r0_2": "Uma pessoa que digita uma\npergunta e clica num resultado",
        "v1_r0_3": "Posição, clique e tráfego orgânico\n(Google Search Console)",
        "v1_r1_0": "AEO",
        "v1_r1_1": "Jason Barnard, com Chee Lo (Trustpilot).\nWhite paper na BrightonSEO, 15 set 2017",
        "v1_r1_2": "Uma pessoa que pergunta e ouve\nou lê a resposta pronta, sem clicar",
        "v1_r1_3": "Ser a resposta destacada.\nEm 2026, fundido com GEO",
        "v1_r2_0": "GEO",
        "v1_r2_1": "Aggarwal, Murahari, Rajpurohit, Kalyan,\nNarasimhan e Deshpande, 16 nov 2023\n(arXiv 2311.09735, KDD 2024)",
        "v1_r2_2": "Uma pessoa que pergunta\na um chatbot",
        "v1_r2_3": "Citação, menção e share of voice,\nmedidos por fornecedor de ferramenta.\nGoogle: nenhuma métrica nova",
        "v1_r3_0": "AX · Agentic Engine\nOptimization · AAO",
        "v1_r3_1": "Biilmann (Netlify), 28 jan 2025 · Osmani\n(Google Cloud), 11 abr 2026 · Barnard,\n24 fev 2026",
        "v1_r3_2": "Um agente que constrói (AX, Osmani)\nou que age por alguém (AAO)",
        "v1_r3_3": "Nenhuma métrica pública",
        "v1_r4_0": "Builder-Led\nGrowth",
        "v1_r4_1": "Esta série. Precedentes creditados;\no leitor e a métrica são outros",
        "v1_r4_2": "O par de pessoa e máquina que está\nconstruindo. A decisão acontece dentro\nda construção, sem pergunta",
        "v1_r4_3": "Incorporação: instalado, importado,\nchamado. Ninguém publica essa taxa",
        "v1_faixa": "Mais páginas no site é o fator de correlação mais baixa que alguém mediu: %s, último de onze." % PAGINAS_CORR,
        "v1_rodape": "Builder-Led Growth, arco 2 · Search Engine Land (set/2025) · Barnard (2017) · arXiv 2311.09735 · Ahrefs (mai e dez/2025, 75 mil marcas)",

        "v2_nome": "a2p2-tres-portas-pt",
        "v2_kicker": "O CONJUNTO E OS RELÓGIOS",
        "v2_titulo": "Três portas para o conjunto de onde a máquina tira as opções",
        "v2_sub": "Cada porta tem um relógio, e nenhum dos três marca a mesma hora",
        "v2_p0_rot": "PORTA 1",
        "v2_p0_nome": "O corpus",
        "v2_p0_relogio": "meses",
        "v2_p0_rel_sub": "corte de conhecimento + lançamento + confiabilidade",
        "v2_p0_txt": "A memória do modelo, formada no\ntreinamento. Entra-se por presença\nacumulada por terceiros: 85,7% das\ncitações vêm de sites que a marca\nnão controla. Definição igual em todo\nlugar, nome que não colide, pacote\nque instala. Horizonte: um ano ou mais",
        "v2_p1_rot": "PORTA 2",
        "v2_p1_nome": "A busca",
        "v2_p1_relogio": "dias",
        "v2_p1_rel_sub": "o agente lê por dois segundos, em uma requisição",
        "v2_p1_txt": "O que o agente lê na hora: página em\nMarkdown, índice para máquina, preço\nlegível, distância até a primeira\nchamada, e a descrição da skill. Só\nalcança quem já sabe procurar por você:\n57,8% das repetições no ChatGPT não\nacionaram busca nenhuma",
        "v2_p2_rot": "PORTA 3",
        "v2_p2_nome": "A plataforma",
        "v2_p2_relogio": "um contrato",
        "v2_p2_rel_sub": "avança quando alguém assina ou revisa um catálogo",
        "v2_p2_txt": "O padrão da casa, decidido antes de\na conversa começar. Em cinco de sete\nplataformas o cliente nunca vê o nome.\nDois caminhos: ser o substrato (por\ncontato) ou entrar no catálogo (só o\nVercel Marketplace documenta como).\nCalendário que ninguém publica",
        "v2_barra1": "No terminal ou no editor (Claude Code, Codex, Cursor) a terceira porta muda de forma",
        "v2_barra2": "Não há casa embutindo padrão: a porta é o que quem constrói instalou — servidores MCP, skills, arquivo do projeto — e o resto vem inteiro do corpus",
        "v2_faixa": "O que você publica hoje age em dias por uma porta, em um ano por outra, e nunca sozinho pela terceira.",
        "v2_rodape": "Builder-Led Growth, arco 2 · Anthropic (cortes, ago/2026) · Semrush (dez/2025) · arXiv 2604.07585 via Martinez · Zatuchin (jun/2026)",

        "v3_nome": "a2p2-anatomia-pt",
        "v3_kicker": "PORTA 2 — O QUE O AGENTE ENCONTRA EM DOIS SEGUNDOS",
        "v3_titulo": "Sete produtos lidos em 2 de setembro de 2026, quatro coisas em cada um",
        "v3_sub": "Baixados com a mesma ferramenta que um agente usaria, de um endereço no Brasil",
        "v3_prods": ["Firecrawl", "shadcn/ui", "Vercel", "Resend", "Supabase", "SendGrid", "Stripe"],
        "v3_l0": "Página em Markdown\npor sufixo .md",
        "v3_l1": "Índice para máquina\n(llms.txt) com definição",
        "v3_l2": "Preço legível por\nmáquina (/pricing.md)",
        "v3_l3": "Passos até a\nprimeira chamada",
        "v3_c0_0": ("sim", "sim"), "v3_c0_1": ("sim", "sim"), "v3_c0_2": ("sim", "sim"),
        "v3_c0_3": ("sim", "sim"), "v3_c0_4": ("sim", "sim"), "v3_c0_5": ("sim", "sim"),
        "v3_c0_6": ("sim", "sim"),
        "v3_c1_0": ("sim", "sim, com preço\nna própria linha"),
        "v3_c1_1": ("sim", "sim"),
        "v3_c1_2": ("meio", "sim; traz instrução,\nnão descrição"),
        "v3_c1_3": ("sim", "sim: \"the email\nAPI for developers\""),
        "v3_c1_4": ("meio", "31 links, nenhuma\nfrase de definição"),
        "v3_c1_5": ("nao", "não tem; o da Twilio\né mapa sem título"),
        "v3_c1_6": ("meio", "sim na raiz; o das\ndocs só instrui"),
        "v3_c2_0": ("sim", "sim"),
        "v3_c2_1": ("na", "não há preço\n(código aberto)"),
        "v3_c2_2": ("sim", "sim"),
        "v3_c2_3": ("sim", "sim, em tabela"),
        "v3_c2_4": ("sim", "sim"),
        "v3_c2_5": ("nao", "não: toda URL cai\nna página de produto"),
        "v3_c2_6": ("nao", "não: HTML, localizado\npelo endereço"),
        "v3_c3_0": ("sim", "1, sem conta\nnem chave (testado)"),
        "v3_c3_1": ("sim", "2 comandos,\nsem conta"),
        "v3_c3_2": ("meio", "3, com login\nno segundo"),
        "v3_c3_3": ("meio", "3, após chave\ne domínio"),
        "v3_c3_4": ("nao", "8, com projeto\nno painel"),
        "v3_c3_5": ("nao", "conta, chave, 2FA\ne domínio"),
        "v3_c3_6": ("meio", "~12, ou sandbox\nanônimo p/ agente"),
        "v3_faixa": "Hipótese, sem medição: o que separa os produtos é a distância até a primeira chamada funcionando.",
        "v3_rodape": "Builder-Led Growth, arco 2 · leitura direta em 2 de setembro de 2026 · a Stripe tem o menor conjunto e está nos cinco catálogos; a SendGrid não tem arquivo e ganhou 40 de 40 num modelo",

        "v4_nome": "a2p2-plataformas-pt",
        "v4_kicker": "PORTA 3 — O PADRÃO DA CASA",
        "v4_titulo": "Sete plataformas de construção assistida em 1º de setembro de 2026",
        "v4_sub": "Documentação lida naquele dia. Muda sem aviso",
        "v4_cols": ["PLATAFORMA", "PADRÃO EMBUTIDO", "CLIENTE VÊ O FORNECEDOR?", "ESCOLHA OFERECIDA"],
        "v4_r0_0": "Lovable",
        "v4_r0_1": "Lovable Cloud (Supabase por baixo), e-mails embutidos sem\nfornecedor nomeado, pagamentos Paddle ou Stripe",
        "v4_r0_2": ("nao", "não"),
        "v4_r0_3": "Cloud ou uma Supabase própria;\n\"Preciso de SendGrid ou Resend? Não\"",
        "v4_r1_0": "Bolt",
        "v4_r1_1": "Bolt Database (Supabase), Resend para e-mail sem\nprovedor escolhido, hospedagem Bolt Cloud (Netlify)",
        "v4_r1_2": ("meio", "em parte"),
        "v4_r1_3": "Bolt Database ou Supabase,\nna criação do projeto",
        "v4_r2_0": "Replit",
        "v4_r2_1": "Replit Database, Replit Auth, App Storage\n(Google Cloud Storage por baixo)",
        "v4_r2_2": ("nao", "não"),
        "v4_r2_3": "Lista curta de conectores quando\no fornecedor não é nomeado",
        "v4_r3_0": "v0 (Vercel)",
        "v4_r3_1": "Nenhum banco padrão. A exceção do conjunto,\ne a de público mais técnico",
        "v4_r3_2": ("sim", "sim"),
        "v4_r3_3": "Upstash, Neon, Supabase, Vercel Blob;\npausa humana antes de plano pago",
        "v4_r4_0": "Base44 (Wix)",
        "v4_r4_1": "Banco, login, hospedagem e envio de e-mail embutidos,\nnenhum fornecedor nomeado",
        "v4_r4_2": ("nao", "não"),
        "v4_r4_3": "Resend a partir de plano pago;\nStripe nos pagamentos",
        "v4_r5_0": "Emergent",
        "v4_r5_1": "Pilha única: React, FastAPI e MongoDB Atlas\n(nomeado pela MongoDB, não pela plataforma)",
        "v4_r5_2": ("nao", "não"),
        "v4_r5_3": "Nenhuma alternativa de banco\ndocumentada",
        "v4_r6_0": "Google AI Studio",
        "v4_r6_1": "Firestore e Firebase Authentication:\no padrão é a própria casa",
        "v4_r6_2": ("sim", "é a casa"),
        "v4_r6_3": "Botão de aprovação\n(\"Enable Firebase\")",
        "v4_faixa": "Onde existe escolha, o desenho é um só: o padrão da casa e uma alternativa. Nunca lista aberta.",
        "v4_rodape": "Builder-Led Growth, arco 2 · documentação oficial de cada plataforma, lida em 1º de setembro de 2026 · Supabase (set e dez/2025) · MongoDB (case study)",

        "v5_nome": "a2p2-experimento-pt",
        "v5_kicker": "MARCA PARA A MÁQUINA — O EXPERIMENTO",
        "v5_titulo": "Quatro provedores fictícios, especificação idêntica, só o texto de marca diferente",
        "v5_sub": "Parcela de escolha por texto, sob cada tom da tarefa · 1º de setembro de 2026 · %d rodadas válidas" % RODADAS_VALIDAS,
        "v5_m0": "Claude Haiku 4.5",
        "v5_m1": "Claude Sonnet 5",
        "v5_n": "n = 59–60 por tom",
        "v5_tom0": "tom: \"nenhum e-mail pode deixar de chegar\"",
        "v5_tom1": "tom: \"funcionando ainda hoje, sem configurar\"",
        "v5_letras": ["N", "C", "S", "A"],
        "v5_leg": ["N · neutro e descritivo", "C · dono de \"confiabilidade\"", "S · dono de \"simplicidade\"", "A · autoridade sem prova"],
        "v5_barra1": "Sem documentação nenhuma: Haiku escolheu SendGrid 40 vezes em 40; Sonnet, Resend 40 em 40",
        "v5_barra2": "É a porta do corpus em um número — monolítica dentro de um modelo, divergente entre modelos. Rodado no Claude Code, sem nada instalado",
        "v5_faixa": "O texto de marca decide enquanto o modelo não percebe que os produtos são iguais; quando percebe, a posição volta a mandar.",
        "v5_rodape": "Builder-Led Growth, arco 2 · protocolo congelado antes da rodada; dados no repositório público · dois modelos de uma família, em português — limite declarado",

        "v6_nome": "a2p2-dois-extremos-pt",
        "v6_kicker": "OS DOIS EXTREMOS, E O MEIO",
        "v6_titulo": "Quem decide em cada porta, conforme quanto se delega e quanto se governa",
        "v6_sub": "Os extremos são desenho de laboratório. O dia a dia fica no meio",
        "v6_porta": ["CORPUS", "BUSCA", "PLATAFORMA / CATÁLOGO"],
        "v6_c0_rot": "SEM GOVERNANÇA, DELEGAÇÃO TOTAL",
        "v6_c0_nome": "A empresa de 25 pessoas",
        "v6_c0_0": "O padrão do modelo decide.\nNinguém perguntou pelo fornecedor",
        "v6_c0_1": "O agente lê o que encontra na hora,\nse chegar a buscar",
        "v6_c0_2": "O padrão da casa, decidido antes\nda conversa. Ninguém vê o nome",
        "v6_c1_rot": "O MEIO, ONDE FICA O DIA A DIA",
        "v6_c1_nome": "Nomeia o que conhece",
        "v6_c1_0": "O que a pessoa delega, o corpus\ndecide: o tamanho do que ela não conhece",
        "v6_c1_1": "O que a pessoa nomeia, a descrição\nlida na hora decide",
        "v6_c1_2": "O que a lista permite, o catálogo\ndecide. A API aberta passa por fora",
        "v6_c2_rot": "COM GOVERNANÇA",
        "v6_c2_nome": "Uma pessoa fixa a lista",
        "v6_c2_0": "O modelo sabe que você existe\ne não pode conectar você",
        "v6_c2_1": "O agente lê a documentação\ne não instala",
        "v6_c2_2": "A lista é de uma pessoa, entre\no que a plataforma já catalogou",
        "v6_barra1": "Nos dois extremos, a candidatura acontece antes do primeiro prompt",
        "v6_barra2": "Nenhuma lista cobre tudo: o corpus continua aberto por dentro do código, e a governança fecha catálogo e instalação",
        "v6_faixa": "O fornecedor que cuida de uma porta só aposta em qual das três vai valer para aquele cliente — numa proporção que ninguém publica.",
        "v6_rodape": "Builder-Led Growth, arco 2 · Lovable e Bolt (controles de admin) · GitHub (nov/2025) · Anthropic (managed MCP) · Nylas (mar/2025)",
    },
    "en": {
        "capa_kicker": "BUILDER-LED GROWTH — ARC 2, PART 2",
        "capa_t1": "Nobody asked for you.",
        "capa_t2": "You got in, or were left out, all the same",
        "capa_sub": "Candidacy: the three doors into the set the machine chooses from",
        "capa_frase1": "A CRM built with AI in three weeks, four vendors working inside it,",
        "capa_frase2": "and nobody at the company searched for, compared or saw any of the four.",
        "capa_creditof": "Three logics, three doors, three clocks, and an experiment with %d rounds" % RODADAS_VALIDAS,
        "capa_rodape": "Matheus Ramos · arc 2, part 2",

        "v1_nome": "a2p2-three-logics-en",
        "v1_kicker": "THREE LOGICS, THREE READERS",
        "v1_titulo": "Who reads, and what gets measured, in each practice of being found",
        "v1_sub": "In the first four rows, someone asked. In the last, nobody asked for the vendor",
        "v1_cols": ["PRACTICE", "WHO COINED IT, WHEN", "WHO READS", "WHAT GETS MEASURED"],
        "v1_r0_0": "SEO",
        "v1_r0_1": "Disputed authorship, 1995–1997. Dated\nrecord: Usenet, 26 Jul 1997 (traced by\nDanny Sullivan in 2004, who popularised it)",
        "v1_r0_2": "A person who types a question\nand clicks a result",
        "v1_r0_3": "Position, click and organic traffic\n(Google Search Console)",
        "v1_r1_0": "AEO",
        "v1_r1_1": "Jason Barnard, with Chee Lo (Trustpilot).\nWhite paper at BrightonSEO, 15 Sep 2017",
        "v1_r1_2": "A person who asks and hears or\nreads the ready answer, no click",
        "v1_r1_3": "Being the featured answer.\nIn 2026, merged with GEO",
        "v1_r2_0": "GEO",
        "v1_r2_1": "Aggarwal, Murahari, Rajpurohit, Kalyan,\nNarasimhan and Deshpande, 16 Nov 2023\n(arXiv 2311.09735, KDD 2024)",
        "v1_r2_2": "A person asking\na chatbot",
        "v1_r2_3": "Citation, mention and share of voice,\nmeasured by tooling vendors.\nGoogle: no new metric",
        "v1_r3_0": "AX · Agentic Engine\nOptimization · AAO",
        "v1_r3_1": "Biilmann (Netlify), 28 Jan 2025 · Osmani\n(Google Cloud), 11 Apr 2026 · Barnard,\n24 Feb 2026",
        "v1_r3_2": "An agent that builds (AX, Osmani)\nor acts for someone (AAO)",
        "v1_r3_3": "No public metric",
        "v1_r4_0": "Builder-Led\nGrowth",
        "v1_r4_1": "This series. Precedents credited;\nthe reader and the metric differ",
        "v1_r4_2": "The pair of person and machine that\nis building. The decision happens\ninside the build, with no question",
        "v1_r4_3": "Incorporation: installed, imported,\ncalled. Nobody publishes that rate",
        "v1_faixa": "More pages on the site is the lowest correlation anyone has measured: %s, last of eleven." % PAGINAS_CORR_EN,
        "v1_rodape": "Builder-Led Growth, arc 2 · Search Engine Land (Sep 2025) · Barnard (2017) · arXiv 2311.09735 · Ahrefs (May and Dec 2025, 75,000 brands)",

        "v2_nome": "a2p2-three-doors-en",
        "v2_kicker": "THE SET AND THE CLOCKS",
        "v2_titulo": "Three doors into the set the machine draws its options from",
        "v2_sub": "Each door has a clock, and none of the three keeps the same time",
        "v2_p0_rot": "DOOR 1",
        "v2_p0_nome": "The corpus",
        "v2_p0_relogio": "months",
        "v2_p0_rel_sub": "knowledge cutoff + launch + reliability",
        "v2_p0_txt": "The model's memory, formed in\ntraining. You enter by presence built\nby third parties: 85.7% of citations\npoint to sites the brand does not\ncontrol. Same definition everywhere,\na name that doesn't collide, a package\nthat installs. Horizon: a year or more",
        "v2_p1_rot": "DOOR 2",
        "v2_p1_nome": "Search",
        "v2_p1_relogio": "days",
        "v2_p1_rel_sub": "the agent reads for two seconds, in one request",
        "v2_p1_txt": "What the agent reads on the spot:\nMarkdown page, machine index,\nreadable price, distance to the first\ncall, and the skill's description. It\nonly reaches whoever already knows to\nlook for you: 57.8% of ChatGPT\nrepetitions triggered no search at all",
        "v2_p2_rot": "DOOR 3",
        "v2_p2_nome": "The platform",
        "v2_p2_relogio": "a contract",
        "v2_p2_rel_sub": "moves when someone signs or revises a catalogue",
        "v2_p2_txt": "The house default, decided before the\nconversation begins. In five of seven\nplatforms the customer never sees the\nname. Two paths: be the substrate (by\ncontact) or enter the catalogue (only\nthe Vercel Marketplace documents how).\nA calendar nobody publishes",
        "v2_barra1": "In the terminal or the editor (Claude Code, Codex, Cursor) the third door changes shape",
        "v2_barra2": "No house embeds a default: the door is what the builder installed — MCP servers, skills, the project file — and the rest comes entirely from the corpus",
        "v2_faixa": "What you publish today acts in days through one door, in a year through another, and never on its own through the third.",
        "v2_rodape": "Builder-Led Growth, arc 2 · Anthropic (cutoffs, Aug 2026) · Semrush (Dec 2025) · arXiv 2604.07585 via Martinez · Zatuchin (Jun 2026)",

        "v3_nome": "a2p2-anatomy-en",
        "v3_kicker": "DOOR 2 — WHAT THE AGENT FINDS IN TWO SECONDS",
        "v3_titulo": "Seven products read on 2 September 2026, four things in each",
        "v3_sub": "Fetched with the same tool an agent would use, from an address in Brazil",
        "v3_prods": ["Firecrawl", "shadcn/ui", "Vercel", "Resend", "Supabase", "SendGrid", "Stripe"],
        "v3_l0": "Markdown page\nby .md suffix",
        "v3_l1": "Machine index\n(llms.txt) with a definition",
        "v3_l2": "Machine-readable\nprice (/pricing.md)",
        "v3_l3": "Steps to the\nfirst call",
        "v3_c0_0": ("sim", "yes"), "v3_c0_1": ("sim", "yes"), "v3_c0_2": ("sim", "yes"),
        "v3_c0_3": ("sim", "yes"), "v3_c0_4": ("sim", "yes"), "v3_c0_5": ("sim", "yes"),
        "v3_c0_6": ("sim", "yes"),
        "v3_c1_0": ("sim", "yes, with the price\non the line itself"),
        "v3_c1_1": ("sim", "yes"),
        "v3_c1_2": ("meio", "yes; carries instruction,\nnot description"),
        "v3_c1_3": ("sim", "yes: \"the email\nAPI for developers\""),
        "v3_c1_4": ("meio", "31 links, no\ndefining sentence"),
        "v3_c1_5": ("nao", "none; Twilio's is a\nsite map with no title"),
        "v3_c1_6": ("meio", "yes at the root; the\ndocs one only instructs"),
        "v3_c2_0": ("sim", "yes"),
        "v3_c2_1": ("na", "no price\n(open source)"),
        "v3_c2_2": ("sim", "yes"),
        "v3_c2_3": ("sim", "yes, as a table"),
        "v3_c2_4": ("sim", "yes"),
        "v3_c2_5": ("nao", "no: every URL ends\non a product page"),
        "v3_c2_6": ("nao", "no: HTML, localised\nby address"),
        "v3_c3_0": ("sim", "1, no account\nor key (tested)"),
        "v3_c3_1": ("sim", "2 commands,\nno account"),
        "v3_c3_2": ("meio", "3, with a login\nat the second"),
        "v3_c3_3": ("meio", "3, after key\nand domain"),
        "v3_c3_4": ("nao", "8, with a project\nin the dashboard"),
        "v3_c3_5": ("nao", "account, key, 2FA\nand domain"),
        "v3_c3_6": ("meio", "~12, or anonymous\nsandbox for agents"),
        "v3_faixa": "Hypothesis, unmeasured: what separates the products is the distance to the first working call.",
        "v3_rodape": "Builder-Led Growth, arc 2 · direct reading on 2 September 2026 · Stripe has the smallest set and sits in all five catalogues; SendGrid has no file and won 40 of 40 on one model",

        "v4_nome": "a2p2-platforms-en",
        "v4_kicker": "DOOR 3 — THE HOUSE DEFAULT",
        "v4_titulo": "Seven AI build platforms on 1 September 2026",
        "v4_sub": "Documentation read that day. It changes without notice",
        "v4_cols": ["PLATFORM", "BUILT-IN DEFAULT", "VENDOR VISIBLE TO CUSTOMER?", "CHOICE OFFERED"],
        "v4_r0_0": "Lovable",
        "v4_r0_1": "Lovable Cloud (Supabase underneath), built-in e-mails with\nno vendor named, payments via Paddle or Stripe",
        "v4_r0_2": ("nao", "no"),
        "v4_r0_3": "Cloud or a Supabase of your own;\n\"Do I need SendGrid or Resend? No\"",
        "v4_r1_0": "Bolt",
        "v4_r1_1": "Bolt Database (Supabase), Resend for e-mail when no\nprovider is chosen, Bolt Cloud hosting (Netlify)",
        "v4_r1_2": ("meio", "partly"),
        "v4_r1_3": "Bolt Database or Supabase,\nat project creation",
        "v4_r2_0": "Replit",
        "v4_r2_1": "Replit Database, Replit Auth, App Storage\n(Google Cloud Storage underneath)",
        "v4_r2_2": ("nao", "no"),
        "v4_r2_3": "A short list of connectors when\nno vendor is named",
        "v4_r3_0": "v0 (Vercel)",
        "v4_r3_1": "No default database. The exception in the set,\nand the one with the most technical audience",
        "v4_r3_2": ("sim", "yes"),
        "v4_r3_3": "Upstash, Neon, Supabase, Vercel Blob;\nhuman pause before any paid plan",
        "v4_r4_0": "Base44 (Wix)",
        "v4_r4_1": "Database, login, hosting and e-mail sending built in,\nno vendor named",
        "v4_r4_2": ("nao", "no"),
        "v4_r4_3": "Resend from a paid plan up;\nStripe in payments",
        "v4_r5_0": "Emergent",
        "v4_r5_1": "Single stack: React, FastAPI and MongoDB Atlas\n(named by MongoDB, not by the platform)",
        "v4_r5_2": ("nao", "no"),
        "v4_r5_3": "No documented database\nalternative",
        "v4_r6_0": "Google AI Studio",
        "v4_r6_1": "Firestore and Firebase Authentication:\nthe default is the house itself",
        "v4_r6_2": ("sim", "it is the house"),
        "v4_r6_3": "An approval button\n(\"Enable Firebase\")",
        "v4_faixa": "Where a choice exists, it has one design: the house default and one alternative. Never an open list.",
        "v4_rodape": "Builder-Led Growth, arc 2 · each platform's official documentation, read on 1 September 2026 · Supabase (Sep and Dec 2025) · MongoDB (case study)",

        "v5_nome": "a2p2-experiment-en",
        "v5_kicker": "BRAND FOR THE MACHINE — THE EXPERIMENT",
        "v5_titulo": "Four fictional providers, identical specification, only the brand text differs",
        "v5_sub": "Share of choice per text, under each task tone · 1 September 2026 · %d valid rounds" % RODADAS_VALIDAS,
        "v5_m0": "Claude Haiku 4.5",
        "v5_m1": "Claude Sonnet 5",
        "v5_n": "n = 59–60 per tone",
        "v5_tom0": "tone: \"no e-mail can fail to arrive\"",
        "v5_tom1": "tone: \"working today, with no configuration\"",
        "v5_letras": ["N", "R", "S", "A"],
        "v5_leg": ["N · neutral and descriptive", "R · owns \"reliability\"", "S · owns \"simplicity\"", "A · authority without proof"],
        "v5_barra1": "With no documentation at all: Haiku picked SendGrid 40 times out of 40; Sonnet, Resend 40 out of 40",
        "v5_barra2": "It is the corpus door in a single number — monolithic within one model, divergent between models. Run in Claude Code, with nothing installed",
        "v5_faixa": "The brand text decides as long as the model doesn't notice the products are identical; once it notices, position takes over.",
        "v5_rodape": "Builder-Led Growth, arc 2 · protocol frozen before the run; data in the public repository · two models from one family, in Portuguese — declared limit",

        "v6_nome": "a2p2-two-extremes-en",
        "v6_kicker": "THE TWO EXTREMES, AND THE MIDDLE",
        "v6_titulo": "Who decides at each door, by how much is delegated and how much is governed",
        "v6_sub": "The extremes are a laboratory design. Day to day sits in the middle",
        "v6_porta": ["CORPUS", "SEARCH", "PLATFORM / CATALOGUE"],
        "v6_c0_rot": "NO GOVERNANCE, TOTAL DELEGATION",
        "v6_c0_nome": "The 25-person company",
        "v6_c0_0": "The model's default decides.\nNobody asked for the vendor",
        "v6_c0_1": "The agent reads what it finds on the\nspot, if it searches at all",
        "v6_c0_2": "The house default, decided before the\nconversation. Nobody sees the name",
        "v6_c1_rot": "THE MIDDLE, WHERE DAY TO DAY SITS",
        "v6_c1_nome": "Names what she knows",
        "v6_c1_0": "What the person delegates, the corpus\ndecides: the size of what she doesn't know",
        "v6_c1_1": "What the person names, the description\nread on the spot decides",
        "v6_c1_2": "What the list allows, the catalogue\ndecides. The open API goes around it",
        "v6_c2_rot": "WITH GOVERNANCE",
        "v6_c2_nome": "A person pins the list",
        "v6_c2_0": "The model knows you exist\nand cannot connect you",
        "v6_c2_1": "The agent reads the documentation\nand does not install",
        "v6_c2_2": "The list belongs to a person, among\nwhat the platform already catalogued",
        "v6_barra1": "At both extremes, candidacy happens before the first prompt",
        "v6_barra2": "No list covers everything: the corpus stays open from inside the code, and governance closes catalogue and installation",
        "v6_faixa": "The vendor who tends one door only is betting on which of the three will hold for that customer — in a proportion nobody publishes.",
        "v6_rodape": "Builder-Led Growth, arc 2 · Lovable and Bolt (admin controls) · GitHub (Nov 2025) · Anthropic (managed MCP) · Nylas (Mar 2025)",
    },
}


def gerar(lang):
    t = T[lang]
    salvar("a2p2-capa-pt" if lang == "pt" else "a2p2-cover-en", capa(t, lang), scale=1.5)
    for i, fn in enumerate((v1, v2, v3, v4, v5, v6), start=1):
        salvar(t["v%d_nome" % i], fn(t, lang))


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    for lang in (["pt", "en"] if alvo is None else [alvo]):
        gerar(lang)
