#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais da peça avulsa do arco 2 — comércio agêntico.

Seis figuras mais a capa, PT e EN, escritas direto em `visuais/arco2-comercio-agentico/`.
Os nomes de arquivo são os que os marcadores `[IMAGEM n/6]` das duas peças já
declaram — quem manda aqui é o texto, e o gerador obedece.

POR QUE O RASTERIZADOR VEM IMPORTADO, E NÃO COPIADO
---------------------------------------------------
O `gen_a2p1.py` resolveu, em 11 de agosto de 2026, dois problemas desta máquina
que nada têm a ver com desenho: o `cairosvg` importa e não roda no Windows, e o
Chrome headless precisa de `--user-data-dir` próprio ou termina em silêncio sem
escrever arquivo nenhum. Copiar aquelas cem linhas para cá criaria duas cópias da
mesma cura, e a segunda envelheceria sem ninguém notar. Importar deixa uma só.

O gen_a2p1 instala o substituto vazio de `cairosvg` ANTES de importar o gen_p4,
então importá-lo primeiro é o que faz o resto passar nesta máquina.

O `assert` de folga contra o rodapé fica em toda figura, pela mesma razão das
peças anteriores: peça torta falha alto, em vez de sair publicada.

Uso:  python scripts/gen_comercio_agentico.py          # PT e EN
      python scripts/gen_comercio_agentico.py pt       # só português
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gen_a2p1 import _cairo, _png_pelo_chrome            # noqa: E402
from gen_p4 import (                                     # noqa: E402
    ACCENT, ACCENT_LIGHT, ACCENT_SOFT, AMBER, AMBER_SOFT, BORDER, GRAY,
    GRAY_LIGHT, GREEN, GREEN_SOFT, MUTED, NAVY, NAVY_DEEP, PANEL, WHITE,
    arrow, doc, footer, header, line, rect, txt,
)

W = 1600
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "visuais", "arco2-comercio-agentico")

RED = "#9C4A3C"
RED_SOFT = "#F5E6E2"

# ---------------------------------------------------------------- números
# Existem uma vez só, e batem com o texto das duas línguas. Trocar um número no
# artigo e esquecer o visual foi o defeito que o verificar-paridade.py passou a
# cobrar entre as línguas; entre texto e imagem quem cobra é esta lista curta.
TETO_DECIDIR = 11
ESTREITAR_CASA = 31
ESTREITAR_ELETRO = 28
GARTNER_N = 322

LEGIBILIDADE = [
    ("cosmeticos", 63, ACCENT),
    ("eletronicos", 56, ACCENT),
    ("vestuario", 51, AMBER),
    ("mercearia", 48, AMBER),
    ("moveis", 47, RED),
]
NAO_CAPTURADO = (30, 40)

ADOBE_CRESCIMENTO = 138
ADOBE_ACUMULADO = "1.324"
ADOBE_CONVERSAO = 54
ADOBE_TEMPO = 53
ADOBE_PAGINAS = 23

PROPORCAO = (1, 3, 5)


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
                "Nao consegui gerar o PNG de %s. O cairosvg nao roda aqui (falta a\n"
                "biblioteca nativa Cairo) e nao achei o Chrome para rasterizar.\n"
                "O SVG foi escrito e esta correto — falta so o PNG." % nome)
    print("ok:", os.path.relpath(png, RAIZ))


def fecho(b, H, texto, cor=NAVY, soft=None):
    y = H - 152
    b.append(rect(60, y, W - 120, 62, soft or PANEL, rx=12))
    b.append(rect(60, y, 6, 62, cor, rx=0))
    b.append(txt(92, y + 39, texto, 19, "700", cor))


# ------------------------------------------------ v1: os dois funis
def v1(t, lang):
    """Marketing contra BLG, lado a lado.

    O que precisa ficar claro a olho, e e a frase que fecha a secao: num deles
    quem anda e o cliente, no outro quem anda e o produto. Por isso o token que
    se move e desenhado dentro de cada funil, com legenda propria.
    """
    H = 930
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    py, ph = 250, 400
    pw = 660
    for k in (0, 1):
        px = 120 if k == 0 else W - 120 - pw
        cor = GRAY_LIGHT if k == 0 else ACCENT
        soft = PANEL if k == 0 else ACCENT_SOFT
        pcx = px + pw / 2
        b.append(rect(px, py, pw, ph, soft, rx=14))
        b.append(rect(px, py, pw, ph, "none", cor, 2, rx=14))
        b.append(txt(pcx, py + 44, t["v1_%d_tit" % k], 16, "700", cor,
                     anchor="middle", sp="2"))

        # Tres degraus estreitando: a boca larga e o bico fino, que e a razao
        # de a figura se chamar funil.
        larguras = (510, 420, 352)
        for i in range(3):
            lw = larguras[i]
            ly = py + 92 + i * 84
            b.append(rect(pcx - lw / 2, ly, lw, 66, WHITE, cor, 1.5, rx=10))
            b.append(txt(pcx, ly + 30, t["v1_%d_e%d" % (k, i)], 21, "700", NAVY,
                         anchor="middle"))
            b.append(txt(pcx, ly + 52, t["v1_%d_m%d" % (k, i)], 13.5, "400", GRAY,
                         anchor="middle"))

        # Quem anda pelo funil, nomeado embaixo de cada um.
        qy = py + ph - 30
        b.append(rect(px + 30, qy - 26, pw - 60, 44, cor, rx=10, op="0.14"))
        b.append(txt(pcx, qy + 4, t["v1_%d_quem" % k], 17, "700", NAVY,
                     anchor="middle"))

    yb = py + ph + 34
    b.append(rect(60, yb, W - 120, 82, NAVY, rx=14))
    b.append(txt(W / 2, yb + 36, t["v1_barra1"], 24, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 64, t["v1_barra2"], 15.5, "400", "#AEB6C2",
                 anchor="middle"))

    fecho(b, H, t["v1_faixa"])
    footer(b, W, H, t["v1_rodape"])
    assert yb + 82 < H - 152, "v1 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v2: as tres etapas em comercio
def v2(t, lang):
    """O que se mede e com que ferramenta, etapa a etapa.

    A regra de 15 de agosto de 2026 — nao presumir que o leitor entendeu — pede
    a CONTA concreta e a FERRAMENTA pelo nome de mercado em toda etapa. Aqui isso
    e o corpo do visual, e nao a legenda.
    """
    H = 940
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    colx = [60, 570, 1080]
    cw = 460
    cores = [GREEN, AMBER, ACCENT]
    softs = [GREEN_SOFT, AMBER_SOFT, ACCENT_SOFT]
    cy, ch = 250, 372

    for i in range(3):
        cx = colx[i]
        b.append(rect(cx, cy, cw, ch, softs[i], rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cores[i], 2, rx=14))
        b.append(rect(cx, cy, cw, 7, cores[i], rx=0))
        b.append(txt(cx + 30, cy + 62, t["v2_e%d" % i], 32, "700", NAVY))
        b.append(txt(cx + 30, cy + 92, t["v2_e%d_sub" % i], 14.5, "400", GRAY,
                     style="italic"))

        b.append(line(cx + 30, cy + 120, cx + cw - 30, cy + 120, cores[i], 1.5))
        b.append(txt(cx + 30, cy + 148, t["v2_mede_rot"], 12.5, "700", cores[i],
                     sp="1.5"))
        for j, l in enumerate(t["v2_e%d_mede" % i].split("\n")):
            b.append(txt(cx + 30, cy + 178 + j * 23, l, 15, "400", NAVY))

        b.append(txt(cx + 30, cy + 276, t["v2_ferr_rot"], 12.5, "700", cores[i],
                     sp="1.5"))
        for j, l in enumerate(t["v2_e%d_ferr" % i].split("\n")):
            b.append(txt(cx + 30, cy + 306 + j * 23, l, 15, "400", GRAY))

        if i < 2:
            b.append(arrow(cx + cw + 14, cy + ch / 2, cx + cw + 42, cy + ch / 2,
                           MUTED, 3))

    # A etapa do meio encolhendo: a barra mostra o que a frase afirma.
    yb = cy + ch + 32
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 34, t["v2_barra1"], 22, "700", WHITE))
    b.append(txt(92, yb + 62, t["v2_barra2"], 15, "400", "#AEB6C2"))
    for i, f in enumerate((0.34, 0.16, 0.03)):
        bx = 1010 + i * 180
        b.append(rect(bx, yb + 26, 150, 40, "#24365C", rx=8))
        b.append(rect(bx, yb + 26, 150 * f, 40, AMBER, rx=8))
        b.append(txt(bx + 75, yb + 80, t["v2_enc%d" % i], 12.5, "400", "#AEB6C2",
                     anchor="middle"))

    fecho(b, H, t["v2_faixa"])
    footer(b, W, H, t["v2_rodape"])
    assert yb + 88 < H - 152, "v2 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v3: legibilidade por categoria
def v3(t, lang):
    """As barras da Adobe, com a ressalva colada nelas.

    A escala vai a 100 de proposito, e nao ao maximo da serie: o argumento e
    quanto FALTA para a maquina ler a pagina inteira, e uma escala cortada
    esconderia justamente isso.
    """
    H = 930
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    x0, bw = 380, 940
    y0, bh, gap = 254, 54, 26
    for i, (chave, valor, cor) in enumerate(LEGIBILIDADE):
        y = y0 + i * (bh + gap)
        b.append(txt(x0 - 24, y + 36, t["v3_cat_%s" % chave], 18, "700", NAVY,
                     anchor="end"))
        b.append(rect(x0, y, bw, bh, PANEL, BORDER, 1, rx=8))
        b.append(rect(x0, y, bw * valor / 100.0, bh, cor, rx=8))
        b.append(txt(x0 + bw * valor / 100.0 + 18, y + 36, "%d%%" % valor, 24,
                     "700", cor))
        # A parte que a maquina nao alcanca fica hachurada, e nao vazia: vazio
        # le-se como "nao medido", e isto foi medido.
        b.append(txt(x0 + bw - 16, y + 34, t["v3_resto"], 13, "400", GRAY_LIGHT,
                     anchor="end"))

    yn = y0 + len(LEGIBILIDADE) * (bh + gap) + 12
    b.append(rect(60, yn, W - 120, 80, AMBER_SOFT, rx=14))
    b.append(rect(60, yn, 6, 80, AMBER, rx=0))
    b.append(txt(96, yn + 34, t["v3_nota1"], 19, "700", NAVY))
    b.append(txt(96, yn + 62, t["v3_nota2"], 15, "400", GRAY))

    fecho(b, H, t["v3_faixa"])
    footer(b, W, H, t["v3_rodape"])
    assert yn + 80 < H - 152, "v3 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v4: o teto da delegacao
def v4(t, lang):
    """Decidir contra estreitar, com a ressalva de metodo no corpo.

    A regra da casa manda a ressalva de rigor vir JUNTO do numero, nunca em
    rodape — entao o n, o campo e o fato de ser autodeclaracao ficam dentro do
    cartao, no mesmo olhar que ve o numero.
    """
    H = 880
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    dados = [
        (TETO_DECIDIR, t["v4_0_tit"], t["v4_0_txt"], RED, RED_SOFT),
        (ESTREITAR_CASA, t["v4_1_tit"], t["v4_1_txt"], GREEN, GREEN_SOFT),
        (ESTREITAR_ELETRO, t["v4_2_tit"], t["v4_2_txt"], ACCENT, ACCENT_SOFT),
    ]
    cw, gap = 460, 50
    x0 = (W - (cw * 3 + gap * 2)) / 2
    cy, ch = 250, 285
    escala = 300.0                      # altura de 100%, para a barra ser lida

    for i, (v, tit, sub, cor, soft) in enumerate(dados):
        cx = x0 + i * (cw + gap)
        b.append(rect(cx, cy, cw, ch, soft, rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cor, 2, rx=14))
        b.append(rect(cx, cy, cw, 6, cor, rx=0))
        b.append(txt(cx + 28, cy + 92, "%d%%" % v, 62, "700", cor))
        # A barrinha ao lado do numero: 11 contra 31 e uma diferenca que o olho
        # precisa ver, e nao so ler.
        bx, bwid = cx + cw - 76, 44
        b.append(rect(bx, cy + 40, bwid, escala * 0.34, WHITE, cor, 1.5, rx=6))
        alt = escala * 0.34 * v / 100.0
        b.append(rect(bx, cy + 40 + escala * 0.34 - alt, bwid, alt, cor, rx=6))
        b.append(txt(cx + 28, cy + 132, tit, 17, "700", NAVY))
        for j, l in enumerate(sub.split("\n")):
            b.append(txt(cx + 28, cy + 172 + j * 23, l, 14.5, "400", GRAY))

    yb = cy + ch + 34
    b.append(rect(60, yb, W - 120, 82, NAVY, rx=14))
    b.append(txt(W / 2, yb + 36, t["v4_barra1"], 25, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 64, t["v4_barra2"], 15, "400", "#AEB6C2",
                 anchor="middle"))

    fecho(b, H, t["v4_faixa"])
    footer(b, W, H, t["v4_rodape"])
    assert yb + 82 < H - 152, "v4 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v5: a porta
def v5(t, lang):
    """Navegador contra servidor, que e o criterio real do Nono Circuito.

    O caminho dos pacotes e o argumento inteiro, entao ele e desenhado: no lado
    protegido a linha passa pelo computador da pessoa; no outro ela vai direto.
    """
    H = 900
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    pw, ph, py = 660, 344, 250
    for k in (0, 1):
        px = 120 if k == 0 else W - 120 - pw
        cor = GREEN if k == 0 else RED
        soft = GREEN_SOFT if k == 0 else RED_SOFT
        pcx = px + pw / 2
        b.append(rect(px, py, pw, ph, soft, rx=14))
        b.append(rect(px, py, pw, ph, "none", cor, 2, rx=14))
        b.append(txt(pcx, py + 44, t["v5_%d_tit" % k], 16, "700", cor,
                     anchor="middle", sp="2"))
        b.append(txt(pcx, py + 84, t["v5_%d_gesto" % k], 27, "700", NAVY,
                     anchor="middle"))

        # Os tres nos do caminho. No lado protegido o do meio esta aceso.
        nos = (t["v5_%d_n0" % k], t["v5_%d_n1" % k], t["v5_%d_n2" % k])
        nw, ny = 180, py + 126
        sx = pcx - (nw * 3 + 40) / 2
        for i, nome in enumerate(nos):
            nx = sx + i * (nw + 20)
            aceso = (i == 1 and k == 0)
            b.append(rect(nx, ny, nw, 72, WHITE, cor, 2 if aceso else 1, rx=10))
            if aceso:
                b.append(rect(nx, ny, nw, 5, cor, rx=0))
            for j, l in enumerate(nome.split("\n")):
                b.append(txt(nx + nw / 2, ny + 34 + j * 20, l, 14.5,
                             "700" if aceso else "400", NAVY if aceso else GRAY,
                             anchor="middle"))
            if i < 2:
                b.append(arrow(nx + nw + 2, ny + 36, nx + nw + 18, ny + 36, cor, 2))

        # No lado hospedado a linha PULA o computador da pessoa, e o desvio e o
        # que a corte olhou.
        if k == 1:
            b.append(line(sx + 95, ny + 88, sx + 2 * (nw + 20) + 95, ny + 88,
                          cor, 2.5, dash="8 6"))
            b.append(txt(pcx, ny + 112, t["v5_1_desvio"], 14, "700", cor,
                         anchor="middle"))

        for j, l in enumerate(t["v5_%d_txt" % k].split("\n")):
            b.append(txt(pcx, py + 272 + j * 24, l, 15.5, "400", GRAY,
                         anchor="middle"))

    yb = py + ph + 30
    b.append(rect(60, yb, W - 120, 82, NAVY, rx=14))
    b.append(txt(W / 2, yb + 36, t["v5_barra1"], 24, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 64, t["v5_barra2"], 15, "400", "#AEB6C2",
                 anchor="middle"))

    fecho(b, H, t["v5_faixa"])
    footer(b, W, H, t["v5_rodape"])
    assert yb + 82 < H - 152, "v5 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v6: o 1:3:5
def v6(t, lang):
    """O padrao que funciona contra a distribuicao invertida.

    As duas pilhas usam a MESMA altura total, porque o argumento nao e gastar
    mais: e gastar nas mesmas proporcoes. Alturas diferentes leriam como
    orcamento maior, que nao e o que a pesquisa diz.
    """
    H = 930
    b = []
    header(b, t["v6_kicker"], t["v6_titulo"], t["v6_sub"], H)

    faixas = [
        (t["v6_f0"], ACCENT, ACCENT_SOFT),
        (t["v6_f1"], AMBER, AMBER_SOFT),
        (t["v6_f2"], GREEN, GREEN_SOFT),
    ]
    total = float(sum(PROPORCAO))
    proporcoes = [
        [p / total for p in PROPORCAO],                    # o padrao que funciona
        [p / total for p in reversed(PROPORCAO)],          # a inversao
    ]

    pw, ph, py = 660, 400, 250
    for k in (0, 1):
        px = 120 if k == 0 else W - 120 - pw
        pcx = px + pw / 2
        borda = GREEN if k == 0 else RED
        b.append(rect(px, py, pw, ph, WHITE, borda, 2, rx=14))
        b.append(txt(pcx, py + 42, t["v6_%d_tit" % k], 16, "700", borda,
                     anchor="middle", sp="2"))
        b.append(txt(pcx, py + 78, t["v6_%d_forma" % k], 30, "700", NAVY,
                     anchor="middle"))

        sy, altura_total = py + 110, 246
        y = sy
        for i, (rot, cor, soft) in enumerate(faixas):
            fr = proporcoes[k][i]
            h = altura_total * fr
            b.append(rect(px + 40, y, pw - 80, h, soft, rx=8))
            b.append(rect(px + 40, y, 6, h, cor, rx=0))
            b.append(txt(px + 70, y + h / 2 + 6, rot, 16.5, "700", NAVY))
            b.append(txt(px + pw - 70, y + h / 2 + 6, "%d" % (PROPORCAO[i] if k == 0
                                                              else tuple(reversed(PROPORCAO))[i]),
                         26, "700", cor, anchor="end"))
            y += h + 6

    yb = py + ph + 30
    b.append(rect(60, yb, W - 120, 82, NAVY, rx=14))
    b.append(txt(W / 2, yb + 36, t["v6_barra1"], 24, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 64, t["v6_barra2"], 15, "400", "#AEB6C2",
                 anchor="middle"))

    fecho(b, H, t["v6_faixa"])
    footer(b, W, H, t["v6_rodape"])
    assert yb + 82 < H - 152, "v6 encosta no fecho"
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
    b.append(txt(120, 322, t["capa_t1"], 72, "700", WHITE))
    b.append(txt(120, 412, t["capa_t2"], 72, "700", WHITE))
    b.append(txt(120, 476, t["capa_sub"], 30, "400", "#AEB6C2"))

    qy = 574
    b.append(rect(120, qy, CW - 240, 250, AMBER, rx=16, op="0.13"))
    b.append(rect(120, qy, CW - 240, 250, "none", AMBER, 2, rx=16))
    b.append(rect(120, qy, 7, 250, AMBER, rx=0))
    b.append(txt(172, qy + 84, t["capa_frase1"], 34, "400", "#E8DCC8"))
    b.append(txt(172, qy + 146, t["capa_frase2"], 34, "700", WHITE))
    b.append(txt(172, qy + 206, t["capa_creditof"], 22, "400", "#AEB6C2",
                 style="italic"))

    b.append(line(120, CH - 90, CW - 120, CH - 90, ACCENT, 1.5))
    b.append(txt(120, CH - 48, t["capa_rodape"], 22, "400", "#AEB6C2"))
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 %d %d">%s</svg>' % (CW, CH, CW, CH, "".join(b)))


# ---------------------------------------------------------------- textos
T = {
    "pt": {
        "capa_kicker": "BUILDER-LED GROWTH — COMÉRCIO AGÊNTICO",
        "capa_t1": "A loja deixou de ser destino.",
        "capa_t2": "Virou fonte de dados",
        "capa_sub": "O funil do BLG onde ele é curto o bastante para ser visto inteiro",
        "capa_frase1": "No funil de marketing quem se move é o cliente.",
        "capa_frase2": "No funil do BLG o que se move é o produto, e quem o move é o par.",
        "capa_creditof": "R$ 100 milhões numa conversa, 11% de teto na delegação, e um registro que não é seu",
        "capa_rodape": "Matheus Ramos · arco 2 · peça avulsa",

        "v1_nome": "ca-comparacao-pt",
        "v1_kicker": "DOIS FUNIS LADO A LADO",
        "v1_titulo": "O mesmo desenho, e não é a mesma coisa que anda dentro",
        "v1_sub": "Um descreve onde a pessoa está; o outro, onde o seu produto está",
        "v1_0_tit": "FUNIL DE MARKETING",
        "v1_0_e0": "Descoberta",
        "v1_0_m0": "alcance, impressão, visita",
        "v1_0_e1": "Consideração",
        "v1_0_m1": "lead, clique, carrinho montado",
        "v1_0_e2": "Decisão",
        "v1_0_m2": "conversão, ticket, custo de aquisição",
        "v1_0_quem": "quem anda: o cliente",
        "v1_1_tit": "FUNIL DO BUILDER-LED GROWTH",
        "v1_1_e0": "Candidatura",
        "v1_1_m0": "você está no conjunto de onde se escolhe",
        "v1_1_e1": "Construção",
        "v1_1_m1": "a decisão fechou, e tirar é barato",
        "v1_1_e2": "Adoção",
        "v1_1_m2": "virou premissa, e tirar custa um projeto",
        "v1_1_quem": "quem anda: o produto, empurrado pelo par",
        "v1_barra1": "Em nenhum dos dois o consumidor escolhe fornecedor",
        "v1_barra2": "Quem passa pelo funil do BLG é quem constrói: a plataforma, o meio de pagamento, o varejista que precisa ser escolhido",
        "v1_faixa": "Na resposta do agente a pessoa vê o que sobrou da curadoria, sem saber o que foi descartado.",
        "v1_rodape": "Builder-Led Growth, arco 2 · funil de marketing: St. Elmo Lewis (1898), AIDA (1921), o desenho de funil (1924)",

        "v2_nome": "ca-funil-pt",
        "v2_kicker": "AS TRÊS ETAPAS EM COMÉRCIO",
        "v2_titulo": "O que se mede em cada uma, e com que ferramenta",
        "v2_sub": "A conta concreta, e não a categoria — nenhuma delas é tráfego",
        "v2_mede_rot": "O QUE SE MEDE",
        "v2_ferr_rot": "COM QUE FERRAMENTA",
        "v2_e0": "Candidatura",
        "v2_e0_sub": "estar no conjunto de onde o agente tira as opções",
        "v2_e0_mede": "Presença na resposta.\nTrinta perguntas da sua\ncategoria, com repetição:\nem quantas você aparece",
        "v2_e0_ferr": "AEO e GEO, documentação\ncanônica, feed de produto,\nperfil de capacidade",
        "v2_e1": "Construção",
        "v2_e1_sub": "a decisão fechou sobre você, e tirar custa um clique",
        "v2_e1_mede": "Taxa de substituição entre\na decisão e o pagamento:\nquantas vezes o agente\ntrocou antes de fechar",
        "v2_e1_ferr": "Completude do dado de\nproduto, preço e estoque\ncorretos, tempo de resposta",
        "v2_e2": "Adoção",
        "v2_e2_sub": "você virou premissa, e tirar custa um projeto",
        "v2_e2_mede": "A fatia de recompra que NÃO\nreabre a comparação: dos\npedidos de noventa dias,\nquantos não compararam nada",
        "v2_e2_ferr": "Camada de memória:\nassinatura, pagamento\nguardado, um clique",
        "v2_barra1": "A etapa do meio é curta, e encolhe até sumir conforme a delegação sobe",
        "v2_barra2": "Uma recompra de um clique vai de candidatura direto a adoção: a janela em que um concorrente entraria não abre",
        "v2_enc0": "delegação baixa",
        "v2_enc1": "delegação média",
        "v2_enc2": "um clique",
        "v2_faixa": "Em software você trabalha para ser encontrado. Em comércio, para ser admitido.",
        "v2_rodape": "Builder-Led Growth, arco 2 · o Cart Mandate do padrão de 11 de janeiro de 2026 nomeia o objeto da etapa do meio",

        "v3_nome": "ca-legibilidade-pt",
        "v3_kicker": "QUANTO A MÁQUINA CONSEGUE LER",
        "v3_titulo": "Perto de metade do que a loja escreve não chega a quem decide",
        "v3_sub": "Adobe, sobre mais de um trilhão de visitas · a escala vai a 100% porque o argumento é o que falta",
        "v3_cat_cosmeticos": "Cosméticos",
        "v3_cat_eletronicos": "Eletrônicos",
        "v3_cat_vestuario": "Esportivos e vestuário",
        "v3_cat_mercearia": "Mercearia",
        "v3_cat_moveis": "Móveis e decoração",
        "v3_resto": "o que a máquina não alcança",
        "v3_nota1": "Mesmo nos setores que vão melhor, de %d%% a %d%% do conteúdo das páginas de maior valor não é capturado"
                    % NAO_CAPTURADO,
        "v3_nota2": "Ninguém escreveu uma página ruim de propósito: elas foram escritas para uma pessoa olhar, por um time que não sabia que o próximo leitor seria um programa",
        "v3_faixa": "A conta é de uma tarde: vinte páginas, os fatos que decidem a compra, e um modelo respondendo só com aquela página.",
        "v3_rodape": "Builder-Led Growth, arco 2 · Adobe Analytics, via Digital Commerce 360 (17 de junho de 2026) · medição de fornecedor, parte interessada",

        "v4_nome": "ca-teto-pt",
        "v4_kicker": "O TETO DA DELEGAÇÃO DO CONSUMIDOR",
        "v4_titulo": "Estreitar as opções, sim; decidir a compra, quase não",
        "v4_sub": "A disposição declarada, e a ressalva de método vem junto do número",
        "v4_0_tit": "deixar a IA DECIDIR a compra",
        "v4_0_txt": "É TETO, não média, e ocorre nas\ncategorias de menor risco\nGartner, campo em jan/2026, n=%d\nautodeclaração, sem margem publicada" % GARTNER_N,
        "v4_1_tit": "deixar a IA ESTREITAR as opções",
        "v4_1_txt": "Produto de limpeza e casa,\na categoria de maior aceitação\nGartner, campo em jan/2026, n=%d\nautodeclaração, sem margem publicada" % GARTNER_N,
        "v4_2_tit": "estreitar, em eletrônico pessoal",
        "v4_2_txt": "Categoria de risco percebido maior,\ne a aceitação cai junto\nGartner, campo em jan/2026, n=%d\nautodeclaração, sem margem publicada" % GARTNER_N,
        "v4_barra1": "Quem está construindo autonomia total está construindo para %d%% do mercado" % TETO_DECIDIR,
        "v4_barra2": "Numa compra delegada a transação é o compromisso: você descobre se foi bom depois de já ter pago",
        "v4_faixa": "Ganha o produto que faz a delegação parecer reversível, não o que automatiza mais.",
        "v4_rodape": "Builder-Led Growth, arco 2 · a ansiedade que trava a troca é de Bob Moesta, na teoria do trabalho a ser feito",

        "v5_nome": "ca-porta-pt",
        "v5_kicker": "O CRITÉRIO DO NONO CIRCUITO, EM 4 DE AGOSTO DE 2026",
        "v5_titulo": "Não é o quanto o agente é autônomo, é por onde os pacotes passam",
        "v5_sub": "O desenho que parecia mais invasivo é o que ficou protegido",
        "v5_0_tit": "AGENTE NO NAVEGADOR",
        "v5_0_gesto": "instrumento da pessoa",
        "v5_0_n0": "a pessoa",
        "v5_0_n1": "o computador\ndela",
        "v5_0_n2": "o servidor\nda loja",
        "v5_0_txt": "Quem acessou foi o usuário, com a ajuda do agente.\nA ferramenta não acessa; a pessoa acessa usando a ferramenta",
        "v5_1_tit": "AGENTE HOSPEDADO",
        "v5_1_gesto": "pode ser ator próprio",
        "v5_1_n0": "a pessoa",
        "v5_1_n1": "o computador\ndela",
        "v5_1_n2": "o servidor\nda loja",
        "v5_1_desvio": "os sistemas do agente falam direto com a plataforma",
        "v5_1_txt": "É o desenho de quase toda plataforma de comércio agêntico,\ne cai do outro lado da linha que a corte traçou",
        "v5_barra1": "Onde o seu agente roda deixou de ser só uma decisão de arquitetura",
        "v5_barra2": "Se recusar o agente na porta não é direito garantido, preparar-se para ele deixa de ser opção e vira condição",
        "v5_faixa": "A Amazon obteve liminar em 10 de março de 2026, e o Nono Circuito reverteu em 4 de agosto.",
        "v5_rodape": "Builder-Led Growth, arco 2 · caso 26-1444 · leitura da opinião publicada, não aconselhamento jurídico",

        "v6_nome": "ca-135-pt",
        "v6_kicker": "ONDE O DINHEIRO ESTÁ INDO",
        "v6_titulo": "O padrão que funciona, e a inversão que a maioria pratica",
        "v6_sub": "Mesma altura total nos dois lados: o que muda é a proporção, não o orçamento",
        "v6_f0": "Tecnologia de agentes",
        "v6_f1": "Redesenho de processo",
        "v6_f2": "Capacitação e adoção",
        "v6_0_tit": "AS TRANSFORMAÇÕES QUE DÃO CERTO",
        "v6_0_forma": "1 : 3 : 5",
        "v6_1_tit": "O QUE A MAIORIA DAS EMPRESAS FAZ",
        "v6_1_forma": "5 : 3 : 1",
        "v6_barra1": "A fronteira entre marketing e engenharia dissolveu",
        "v6_barra2": "Quando quem lê é a máquina, o artefato de engenharia e a peça de marketing são o mesmo objeto",
        "v6_faixa": "Se o seu investimento está invertido, o atraso na adoção é seu.",
        "v6_rodape": "Builder-Led Growth, arco 2 · McKinsey, agosto de 2026 · estudo de ambiente corporativo; levá-lo ao varejo é conjectura declarada",
    },
    "en": {
        "capa_kicker": "BUILDER-LED GROWTH — AGENTIC COMMERCE",
        "capa_t1": "The shop stopped being a destination.",
        "capa_t2": "It became a data source",
        "capa_sub": "The BLG funnel where it is short enough to be seen whole",
        "capa_frase1": "In the marketing funnel what moves is the customer.",
        "capa_frase2": "In the BLG funnel what moves is the product, and what moves it is the pair.",
        "capa_creditof": "R$ 100 million inside a conversation, an 11% ceiling on delegation, and a record that isn't yours",
        "capa_rodape": "Matheus Ramos · arc 2 · standalone piece",

        "v1_nome": "ca-comparacao-en",
        "v1_kicker": "TWO FUNNELS SIDE BY SIDE",
        "v1_titulo": "The same drawing, and not the same thing walking inside it",
        "v1_sub": "One describes where the person is; the other, where your product is",
        "v1_0_tit": "THE MARKETING FUNNEL",
        "v1_0_e0": "Discovery",
        "v1_0_m0": "reach, impressions, visits",
        "v1_0_e1": "Consideration",
        "v1_0_m1": "leads, clicks, carts assembled",
        "v1_0_e2": "Decision",
        "v1_0_m2": "conversion, order value, acquisition cost",
        "v1_0_quem": "who walks: the customer",
        "v1_1_tit": "THE BUILDER-LED GROWTH FUNNEL",
        "v1_1_e0": "Candidacy",
        "v1_1_m0": "you are in the set the choice is made from",
        "v1_1_e1": "Construction",
        "v1_1_m1": "the decision closed, and removing you is cheap",
        "v1_1_e2": "Adoption",
        "v1_1_m2": "you became a premise; removal costs a project",
        "v1_1_quem": "who walks: the product, pushed by the pair",
        "v1_barra1": "In neither of them does the consumer pick a vendor",
        "v1_barra2": "The one walking the BLG funnel is whoever builds: the platform, the payments company, the retailer who needs to be chosen",
        "v1_faixa": "In the agent's answer the person sees what survived the curation, without knowing what was discarded.",
        "v1_rodape": "Builder-Led Growth, arc 2 · marketing funnel: St. Elmo Lewis (1898), AIDA (1921), the funnel drawing (1924)",

        "v2_nome": "ca-funil-en",
        "v2_kicker": "THE THREE STAGES IN COMMERCE",
        "v2_titulo": "What gets measured at each one, and with which tool",
        "v2_sub": "The concrete calculation, not the category — none of them is traffic",
        "v2_mede_rot": "WHAT GETS MEASURED",
        "v2_ferr_rot": "WITH WHICH TOOL",
        "v2_e0": "Candidacy",
        "v2_e0_sub": "being in the set the agent draws its options from",
        "v2_e0_mede": "Presence in the answer.\nThirty questions from your\ncategory, repeated: how many\nof them you show up in",
        "v2_e0_ferr": "AEO and GEO, canonical\ndocumentation, product feed,\ncapability profile",
        "v2_e1": "Construction",
        "v2_e1_sub": "the decision closed around you; removal costs one click",
        "v2_e1_mede": "Substitution rate between\nthe decision and payment:\nhow many times the agent\nswapped before closing",
        "v2_e1_ferr": "Product data completeness,\ncorrect price and stock,\nresponse time",
        "v2_e2": "Adoption",
        "v2_e2_sub": "you became a premise; removal costs a project",
        "v2_e2_mede": "The share of repurchase that\ndoes NOT reopen the comparison:\nof ninety days of orders, how\nmany compared nothing",
        "v2_e2_ferr": "The memory layer:\nsubscription, stored\npayment, one click",
        "v2_barra1": "The middle stage is short, and it shrinks until it disappears as delegation rises",
        "v2_barra2": "A one-click repurchase goes from candidacy straight to adoption: the window a competitor would enter through never opens",
        "v2_enc0": "low delegation",
        "v2_enc1": "mid delegation",
        "v2_enc2": "one click",
        "v2_faixa": "In software you work to be found. In commerce, to be admitted.",
        "v2_rodape": "Builder-Led Growth, arc 2 · the Cart Mandate in the 11 January 2026 standard names the object of the middle stage",

        "v3_nome": "ca-legibilidade-en",
        "v3_kicker": "HOW MUCH THE MACHINE CAN READ",
        "v3_titulo": "Close to half of what the shop writes never reaches the decider",
        "v3_sub": "Adobe, over more than a trillion visits · the scale runs to 100% because the argument is what's missing",
        "v3_cat_cosmeticos": "Cosmetics",
        "v3_cat_eletronicos": "Electronics",
        "v3_cat_vestuario": "Sporting goods and apparel",
        "v3_cat_mercearia": "Grocery",
        "v3_cat_moveis": "Furniture and home decor",
        "v3_resto": "what the machine can't reach",
        "v3_nota1": "Even in the sectors doing best, %d%% to %d%% of the content on the highest-value pages is not captured"
                    % NAO_CAPTURADO,
        "v3_nota2": "Nobody wrote a bad page on purpose: they were written for a person to look at, by a team that didn't know the next reader would be a program",
        "v3_faixa": "The calculation is an afternoon's work: twenty pages, the facts that decide the purchase, and a model answering from that page alone.",
        "v3_rodape": "Builder-Led Growth, arc 2 · Adobe Analytics, via Digital Commerce 360 (17 June 2026) · vendor measurement, interested party",

        "v4_nome": "ca-teto-en",
        "v4_kicker": "THE CEILING ON CONSUMER DELEGATION",
        "v4_titulo": "Narrowing the options, yes; deciding the purchase, barely",
        "v4_sub": "Declared willingness, with the method caveat sitting next to the number",
        "v4_0_tit": "letting AI DECIDE the purchase",
        "v4_0_txt": "A CEILING, not an average, and it\noccurs in the lowest-risk categories\nGartner, fielded Jan 2026, n=%d\nself-report, no margin published" % GARTNER_N,
        "v4_1_tit": "letting AI NARROW the options",
        "v4_1_txt": "Cleaning and household products,\nthe most accepting category\nGartner, fielded Jan 2026, n=%d\nself-report, no margin published" % GARTNER_N,
        "v4_2_tit": "narrowing, in personal electronics",
        "v4_2_txt": "Higher perceived risk category,\nand acceptance falls with it\nGartner, fielded Jan 2026, n=%d\nself-report, no margin published" % GARTNER_N,
        "v4_barra1": "Anyone building for full autonomy is building for %d%% of the market" % TETO_DECIDIR,
        "v4_barra2": "In a delegated purchase the transaction is the commitment: you find out whether it was any good after you have already paid",
        "v4_faixa": "The product that wins is the one that makes delegation feel reversible, not the one that automates most.",
        "v4_rodape": "Builder-Led Growth, arc 2 · the anxiety that blocks a switch is Bob Moesta's, in jobs-to-be-done theory",

        "v5_nome": "ca-porta-en",
        "v5_kicker": "THE NINTH CIRCUIT CRITERION, 4 AUGUST 2026",
        "v5_titulo": "It is not how autonomous the agent is, it is where the packets travel",
        "v5_sub": "The design that looked more invasive is the one that ended up protected",
        "v5_0_tit": "AGENT IN THE BROWSER",
        "v5_0_gesto": "the person's instrument",
        "v5_0_n0": "the person",
        "v5_0_n1": "their own\ncomputer",
        "v5_0_n2": "the shop's\nserver",
        "v5_0_txt": "The party who accessed was the user, with the agent's help.\nThe tool doesn't access; the person accesses using the tool",
        "v5_1_tit": "HOSTED AGENT",
        "v5_1_gesto": "may be an actor in its own right",
        "v5_1_n0": "the person",
        "v5_1_n1": "their own\ncomputer",
        "v5_1_n2": "the shop's\nserver",
        "v5_1_desvio": "the agent's systems speak straight to the platform",
        "v5_1_txt": "It is the design of nearly every agentic commerce platform,\nand it falls on the other side of the line the court drew",
        "v5_barra1": "Where your agent runs stopped being only an architecture decision",
        "v5_barra2": "If refusing the agent at the door is not a guaranteed right, preparing for it stops being an option and becomes a condition",
        "v5_faixa": "Amazon obtained an injunction on 10 March 2026, and the Ninth Circuit reversed on 4 August.",
        "v5_rodape": "Builder-Led Growth, arc 2 · case 26-1444 · a reading of the published opinion, not legal advice",

        "v6_nome": "ca-135-en",
        "v6_kicker": "WHERE THE MONEY IS GOING",
        "v6_titulo": "The pattern that works, and the inversion most companies practise",
        "v6_sub": "Same total height on both sides: what changes is the proportion, not the budget",
        "v6_f0": "Agent technology",
        "v6_f1": "Process redesign",
        "v6_f2": "Enablement and adoption",
        "v6_0_tit": "TRANSFORMATIONS THAT WORK",
        "v6_0_forma": "1 : 3 : 5",
        "v6_1_tit": "WHAT MOST COMPANIES DO",
        "v6_1_forma": "5 : 3 : 1",
        "v6_barra1": "The boundary between marketing and engineering dissolved",
        "v6_barra2": "When the reader is a machine, the engineering artefact and the marketing piece are the same object",
        "v6_faixa": "If your investment is inverted, the adoption lag is yours.",
        "v6_rodape": "Builder-Led Growth, arc 2 · McKinsey, August 2026 · a corporate-environment study; carrying it to retail is declared conjecture",
    },
}


def gerar(lang):
    t = T[lang]
    salvar("ca-capa-pt" if lang == "pt" else "ca-cover-en", capa(t, lang), scale=1.5)
    for i, fn in enumerate((v1, v2, v3, v4, v5, v6), start=1):
        salvar(t["v%d_nome" % i], fn(t, lang))


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    for lang in (["pt", "en"] if alvo is None else [alvo]):
        gerar(lang)
