#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais do arco 2, parte 5 — construção: o que segura o seu produto no código
depois que a IA o escolhe.

PT e EN no mesmo arquivo. Helpers de desenho importados do gen_p4; a
rasterização pelo Chrome e o `fecho` vêm do gen_a2p1, como no gen_a2p4. Cada
função termina com assert de folga contra o fecho: peça torta falha alto em vez
de sair publicada.

Os cinco visuais seguem os cinco marcadores da peça, na ordem em que aparecem:
os três vetos e o relógio de cada um, onde o veto de quem constrói acontece, o
que a ISO/IEC 25010 mudou em 2023, os três rastros que o funil de ativação
mistura, e a porta da adoção. Os números existem uma vez só, no topo, e batem
com o texto das duas línguas — quem mudar um, muda nos três lugares.

TODOS os números abaixo foram lidos na fonte em 6 de outubro de 2026, na
sessão que escreveu a peça (Anthropic, Lightsage, Zylo; os demais na mesma
sessão, com citação literal guardada no material de trabalho).

Escrito em 8 de outubro de 2026, depois da aprovação do texto.

Uso:  python scripts/gen_a2p5.py          # gera PT e EN
      python scripts/gen_a2p5.py pt       # só português
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
    ACCENT, ACCENT_LIGHT, ACCENT_SOFT, AMBER, AMBER_SOFT, BORDER, FONT, GRAY,
    GRAY_LIGHT, GREEN, GREEN_SOFT, MUTED, NAVY, NAVY_DEEP, PANEL, WHITE,
    circle, doc, footer, header, line, rect, txt,
)
from gen_a2p1 import RED, RED_SOFT, _cairo, _png_pelo_chrome, fecho  # noqa: E402

W = 1600
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "visuais", "arco2-parte-05")

# ---------------------------------------------------------------- números
# Uma vez só. Batem com o texto das duas línguas.
FIRECRAWL_S = 49             # Lightsage, 30/ago/2026, mesma tarefa no Codex
CIRCLE_MIN = 43
PERMISSAO_APROVA = 97        # Anthropic, 7/ago/2026
PERMISSAO_RECUSA = 3
PLANO_RECUSA = 39
ATENCAO_INICIO = 17          # % de comandos perigosos barrados no começo
ATENCAO_DEPOIS = 5           # depois de 50 ou mais pedidos
ATENCAO_PEDIDOS = 50
BARRADOS = "13,6%"
BARRADOS_EN = "13.6%"
TESTADORES = "1.053"
TESTADORES_EN = "1,053"
ZYLO_CONSUMO = 78            # Zylo, 2026 SaaS Management Index
ISO_DATA = "novembro de 2023"
ISO_DATA_EN = "November 2023"
TEECE_ANO = 1986


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


def cabe(texto, size, largura, bold=False):
    """Estimativa grosseira da largura do texto. Falha alto se não couber."""
    fator = 0.58 if bold else 0.53
    for l in texto.split("\n"):
        assert len(l) * size * fator <= largura, "nao cabe: %r" % l


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
    cabe(t["capa_t1"], 76, CW - 240, True)
    cabe(t["capa_t2"], 76, CW - 240, True)
    cabe(t["capa_frase1"], 34, CW - 320)
    cabe(t["capa_frase2"], 34, CW - 320, True)
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 %d %d">%s</svg>' % (CW, CH, CW, CH, "".join(b)))


# ------------------------------------------- v1: os três vetos e os relógios
def v1(t, lang):
    H = 920
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    # a régua da construção: da primeira linha de código à premissa
    ry = 196
    b.append(line(60, ry, W - 80, ry, MUTED, 2))
    b.append('<polygon points="%d,%d %d,%d %d,%d" fill="%s"/>' % (
        W - 60, ry, W - 80, ry - 8, W - 80, ry + 8, MUTED))
    b.append(txt(60, ry - 12, t["v1_regua_esq"], 13, "700", GRAY, sp="1.5"))
    b.append(txt(W - 60, ry - 12, t["v1_regua_dir"], 13, "700", GRAY, anchor="end", sp="1.5"))

    cw, gap = 470, 35
    x0 = (W - (cw * 3 + gap * 2)) / 2
    cy, ch = 226, 400
    cores = [RED, ACCENT, AMBER]
    softs = [RED_SOFT, ACCENT_SOFT, AMBER_SOFT]
    for i in range(3):
        cx = x0 + i * (cw + gap)
        b.append(rect(cx, cy, cw, ch, softs[i], rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cores[i], 2, rx=14))
        b.append(rect(cx, cy, cw, 7, cores[i], rx=0))
        b.append(txt(cx + 26, cy + 48, t["v1_c%d_rot" % i], 13, "700", cores[i], sp="2"))
        b.append(txt(cx + 26, cy + 92, t["v1_c%d_nome" % i], 28, "700", NAVY))
        b.append(txt(cx + 26, cy + 120, t["v1_c%d_relogio" % i], 14, "700", cores[i]))
        b.append(txt(cx + 26, cy + 170, t["v1_c%d_num" % i], 34, "700", cores[i]))
        b.append(txt(cx + 26, cy + 196, t["v1_c%d_num_sub" % i], 13, "400", GRAY_LIGHT,
                     style="italic"))
        b.append(line(cx + 26, cy + 216, cx + cw - 26, cy + 216, cores[i], 1.2))
        linhas(b, cx + 26, cy + 248, t["v1_c%d_txt" % i], 14.5, NAVY, 22)
        cabe(t["v1_c%d_txt" % i], 14.5, cw - 52)
        cabe(t["v1_c%d_num_sub" % i], 13, cw - 52)
        cabe(t["v1_c%d_nome" % i], 28, cw - 52, True)
        assert len(t["v1_c%d_txt" % i].split("\n")) <= 6, "v1 cartao %d longo" % i

    yb = cy + ch + 28
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v1_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 66, t["v1_barra2"], 14.5, "400", "#AEB6C2"))
    cabe(t["v1_barra1"], 20, W - 184, True)
    cabe(t["v1_barra2"], 14.5, W - 184)

    fecho(b, H, t["v1_faixa"], NAVY, PANEL)
    cabe(t["v1_faixa"], 19, W - 184, True)
    footer(b, W, H, t["v1_rodape"])
    assert yb + 88 < H - 152, "v1 encosta no fecho"
    return doc(W, H, "".join(b))


# --------------------------------------- v2: onde o veto de quem constrói mora
def v2(t, lang):
    H = 900
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    py, ph = 200, 400
    # painel esquerdo: plano contra pedido de permissão
    px, pw = 60, 800
    b.append(rect(px, py, pw, ph, PANEL, BORDER, 1.5, rx=14))
    b.append(txt(px + 30, py + 46, t["v2_e_rot"], 13, "700", ACCENT, sp="2"))
    b.append(txt(px + 30, py + 82, t["v2_e_nome"], 24, "700", NAVY))
    bx, bw, bh = px + 30, pw - 60, 46
    barras = [(t["v2_e_b0"], PERMISSAO_RECUSA, t["v2_e_b0_val"]),
              (t["v2_e_b1"], PLANO_RECUSA, t["v2_e_b1_val"])]
    for k, (rot, recusa, val) in enumerate(barras):
        y = py + 140 + k * 110
        b.append(txt(bx, y - 12, rot, 16, "700", NAVY))
        aprova_w = bw * (100 - recusa) / 100
        b.append(rect(bx, y, aprova_w, bh, MUTED, rx=0))
        b.append(rect(bx + aprova_w, y, bw - aprova_w, bh, RED, rx=0))
        # só o pedido de permissão tem "aprovados" publicado (97%); para o plano a
        # fonte dá só os 39% recusados, e o resto pode incluir plano editado
        if k == 0:
            b.append(txt(bx + 16, y + 30, t["v2_e_aprova"] % PERMISSAO_APROVA, 15, "700", NAVY))
        b.append(txt(bx + bw, y + bh + 24, val, 15, "700", RED, anchor="end"))
    linhas(b, bx, py + 362, t["v2_e_nota"], 14, GRAY, 20)
    cabe(t["v2_e_nota"], 14, pw - 60)

    # painel direito: a atenção cai com o volume
    qx, qw = 890, W - 60 - 890
    b.append(rect(qx, py, qw, ph, PANEL, BORDER, 1.5, rx=14))
    b.append(txt(qx + 30, py + 46, t["v2_d_rot"], 13, "700", AMBER, sp="2"))
    b.append(txt(qx + 30, py + 82, t["v2_d_nome"], 24, "700", NAVY))
    base = py + 300
    escala = 9.0  # px por ponto percentual
    for k, (v, rot) in enumerate([(ATENCAO_INICIO, t["v2_d_b0"]),
                                  (ATENCAO_DEPOIS, t["v2_d_b1"])]):
        cx = qx + 90 + k * 260
        h = v * escala
        b.append(rect(cx, base - h, 130, h, AMBER if k == 0 else AMBER_SOFT,
                      AMBER, 1.5, rx=6))
        b.append(txt(cx + 65, base - h - 14, t["v2_d_val"] % v, 28, "700", AMBER,
                     anchor="middle"))
        b.append(txt(cx + 65, base + 26, rot, 14, "700", NAVY, anchor="middle"))
    b.append(line(qx + 60, base, qx + qw - 40, base, BORDER, 1.5))
    linhas(b, qx + 30, py + 362, t["v2_d_nota"], 14, GRAY, 20)
    cabe(t["v2_d_nota"], 14, qw - 60)
    assert base - ATENCAO_INICIO * escala - 44 > py + 92, "v2 barra invade o titulo"

    yb = py + ph + 28
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v2_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 66, t["v2_barra2"], 14.5, "400", "#AEB6C2"))
    cabe(t["v2_barra1"], 20, W - 184, True)
    cabe(t["v2_barra2"], 14.5, W - 184)

    fecho(b, H, t["v2_faixa"], ACCENT, ACCENT_SOFT)
    cabe(t["v2_faixa"], 19, W - 184, True)
    footer(b, W, H, t["v2_rodape"])
    assert yb + 88 < H - 152, "v2 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------- v3: o que a 25010 mudou
def v3(t, lang):
    H = 940
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    py, ph = 196, 250
    # renomeadas
    px, pw = 60, 600
    b.append(rect(px, py, pw, ph, PANEL, BORDER, 1.5, rx=14))
    b.append(txt(px + 28, py + 44, t["v3_e_rot"], 13, "700", GRAY, sp="2"))
    for k in range(2):
        y = py + 104 + k * 80
        b.append(txt(px + 28, y, t["v3_ren%d_de" % k], 20, "400", GRAY_LIGHT))
        b.append(txt(px + 28 + 210, y, "→", 22, "700", ACCENT))
        b.append(txt(px + 28 + 250, y, t["v3_ren%d_para" % k], 20, "700", NAVY))
        cabe(t["v3_ren%d_para" % k], 20, pw - 290, True)

    # safety entra
    qx, qw = 690, W - 60 - 690
    b.append(rect(qx, py, qw, ph, GREEN_SOFT, GREEN, 2, rx=14))
    b.append(rect(qx, py, qw, 7, GREEN, rx=0))
    b.append(txt(qx + 28, py + 44, t["v3_d_rot"], 13, "700", GREEN, sp="2"))
    b.append(txt(qx + 28, py + 84, t["v3_d_nome"], 26, "700", NAVY))
    chips = t["v3_chips"]
    destaque = (2, 4)  # falha segura e integração segura
    cx, cy = qx + 28, py + 116
    for k, c in enumerate(chips):
        w = len(c) * 9.4 + 36
        if cx + w > qx + qw - 28:
            cx, cy = qx + 28, cy + 58
        on = k in destaque
        b.append(rect(cx, cy, w, 42, GREEN if on else WHITE, GREEN, 1.5, rx=21))
        b.append(txt(cx + w / 2, cy + 27, c, 16, "700", WHITE if on else GREEN,
                     anchor="middle"))
        cx += w + 14
    assert cy + 42 < py + ph - 10, "v3 chips estouram o painel"

    # as duas definições
    dy, dh = py + ph + 26, 170
    dw = (W - 120 - 30) / 2
    for k in range(2):
        dx = 60 + k * (dw + 30)
        b.append(rect(dx, dy, dw, dh, WHITE, GREEN, 2, rx=14))
        b.append(rect(dx, dy, 6, dh, GREEN, rx=0))
        b.append(txt(dx + 30, dy + 44, t["v3_def%d_rot" % k], 14, "700", GREEN, sp="2"))
        linhas(b, dx + 30, dy + 84, t["v3_def%d_txt" % k], 17, NAVY, 26)
        cabe(t["v3_def%d_txt" % k], 17, dw - 60)

    yb = dy + dh + 26
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v3_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 66, t["v3_barra2"], 14.5, "400", "#AEB6C2"))
    cabe(t["v3_barra1"], 20, W - 184, True)
    cabe(t["v3_barra2"], 14.5, W - 184)

    fecho(b, H, t["v3_faixa"], GREEN, GREEN_SOFT)
    cabe(t["v3_faixa"], 19, W - 184, True)
    footer(b, W, H, t["v3_rodape"])
    assert yb + 88 < H - 152, "v3 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------- v4: três rastros que o funil mistura
def v4(t, lang):
    H = 880
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    ry0, rh, rgap = 200, 104, 18
    lx, lw = 60, 400          # rótulo
    tx0, tx1 = 490, 1110      # linha do tempo
    vx = 1140                 # veredito
    cores = [GRAY, RED, GREEN]
    softs = [PANEL, RED_SOFT, GREEN_SOFT]
    # eventos por rastro: (tipo, quantidade); o silêncio vem depois
    eventos = [("vazio", 1), ("erro", 6), ("ok", 7)]
    for i in range(3):
        y = ry0 + i * (rh + rgap)
        b.append(rect(lx, y, W - 120, rh, softs[i], rx=12))
        b.append(rect(lx, y, 6, rh, cores[i], rx=0))
        b.append(txt(lx + 28, y + 38, t["v4_r%d_rot" % i], 12.5, "700", cores[i], sp="2"))
        linhas(b, lx + 28, y + 66, t["v4_r%d_nome" % i], 16, NAVY, 22, weight="700")
        cabe(t["v4_r%d_nome" % i], 16, lw - 40, True)
        # chave criada
        my = y + rh / 2
        b.append(rect(tx0, my - 13, 26, 26, NAVY, rx=4))
        tipo, n = eventos[i]
        x = tx0 + 56
        for _ in range(n):
            if tipo == "ok":
                b.append(circle(x, my, 11, GREEN))
            elif tipo == "erro":
                b.append(circle(x, my, 11, RED))
            else:
                b.append(circle(x, my, 11, WHITE, GRAY_LIGHT, 2))
            x += 34
        b.append(line(x, my, tx1, my, GRAY_LIGHT, 2.5, dash="6 8"))
        ver, nota = t["v4_r%d_ver" % i].split("\n")
        b.append(txt(vx, y + 46, ver, 17, "700", cores[i]))
        b.append(txt(vx, y + 72, nota, 14.5, "400", GRAY))
        cabe(ver, 17, W - 60 - vx - 20, True)

    # legenda
    ly = ry0 + 3 * (rh + rgap) + 10
    itens = [("chave", NAVY), ("ok", GREEN), ("erro", RED), ("silencio", GRAY_LIGHT)]
    x = 60
    for k, (tipo, cor) in enumerate(itens):
        if tipo == "chave":
            b.append(rect(x, ly - 10, 20, 20, cor, rx=3))
        elif tipo == "silencio":
            b.append(line(x, ly, x + 34, ly, cor, 2.5, dash="6 8"))
        else:
            b.append(circle(x + 10, ly, 9, cor))
        b.append(txt(x + 44, ly + 5, t["v4_leg%d" % k], 14, "400", GRAY))
        x += 44 + len(t["v4_leg%d" % k]) * 7.6 + 46

    yb = ly + 34
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v4_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 66, t["v4_barra2"], 14.5, "400", "#AEB6C2"))
    cabe(t["v4_barra1"], 20, W - 184, True)
    cabe(t["v4_barra2"], 14.5, W - 184)

    fecho(b, H, t["v4_faixa"], RED, RED_SOFT)
    cabe(t["v4_faixa"], 19, W - 184, True)
    footer(b, W, H, t["v4_rodape"])
    assert yb + 88 < H - 152, "v4 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------- v5: a porta da adoção
def v5(t, lang):
    H = 920
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    py, ph = 196, 420
    porta_w = 90
    pw = (W - 120 - porta_w - 40) / 2
    lados = [(60, ACCENT, ACCENT_SOFT, "e"), (60 + pw + 20 + porta_w + 20, AMBER, AMBER_SOFT, "d")]
    for px, cor, soft, k in lados:
        b.append(rect(px, py, pw, ph, soft, cor, 2, rx=14))
        b.append(rect(px, py, pw, 7, cor, rx=0))
        b.append(txt(px + 30, py + 50, t["v5_%s_rot" % k], 14, "700", cor, sp="2"))
        b.append(txt(px + 30, py + 98, t["v5_custa_rot"], 12.5, "700", GRAY, sp="1.5"))
        b.append(txt(px + 30, py + 132, t["v5_%s_custa" % k], 28, "700", NAVY))
        b.append(txt(px + 30, py + 182, t["v5_decide_rot"], 12.5, "700", GRAY, sp="1.5"))
        linhas(b, px + 30, py + 212, t["v5_%s_decide" % k], 17, NAVY, 24, weight="700")
        b.append(line(px + 30, py + 262, px + pw - 30, py + 262, cor, 1.2))
        b.append(txt(px + 30, py + 296, t["v5_medir_rot"], 12.5, "700", GRAY, sp="1.5"))
        linhas(b, px + 30, py + 328, t["v5_%s_medir" % k], 15.5, NAVY, 26)
        cabe(t["v5_%s_decide" % k], 17, pw - 60, True)
        cabe(t["v5_%s_medir" % k], 15.5, pw - 60)
        assert len(t["v5_%s_medir" % k].split("\n")) <= 3, "v5 lista longa"
        assert len(t["v5_%s_decide" % k].split("\n")) <= 2, "v5 decide longo"

    # a porta
    dx = 60 + pw + 20
    b.append(rect(dx, py, porta_w, ph, NAVY, rx=10))
    b.append(circle(dx + porta_w - 22, py + ph / 2, 6, AMBER))
    cxp, cyp = dx + porta_w / 2 - 6, py + ph / 2
    b.append('<text x="%s" y="%s" font-family="%s" font-size="15" font-weight="700" '
             'fill="%s" text-anchor="middle" letter-spacing="3" '
             'transform="rotate(-90 %s %s)">%s</text>' % (
                 cxp, cyp, FONT, WHITE, cxp, cyp, t["v5_porta"]))
    assert len(t["v5_porta"]) * 15 * 0.7 < ph - 40, "v5 rotulo da porta"

    yb = py + ph + 28
    b.append(rect(60, yb, W - 120, 88, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v5_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 66, t["v5_barra2"], 14.5, "400", "#AEB6C2"))
    cabe(t["v5_barra1"], 20, W - 184, True)
    cabe(t["v5_barra2"], 14.5, W - 184)

    fecho(b, H, t["v5_faixa"], NAVY, PANEL)
    cabe(t["v5_faixa"], 19, W - 184, True)
    footer(b, W, H, t["v5_rodape"])
    assert yb + 88 < H - 152, "v5 encosta no fecho"
    return doc(W, H, "".join(b))


# ---------------------------------------------------------------- textos
T = {
    "pt": {
        "capa_kicker": "BUILDER-LED GROWTH — ARCO 2, PARTE 5",
        "capa_t1": "Escolhido na terça,",
        "capa_t2": "fora do código na sexta",
        "capa_sub": "Construção: o que segura o seu produto no código depois que a IA o escolhe",
        "capa_frase1": "Ninguém cancelou, ninguém reclamou, ninguém abriu chamado —",
        "capa_frase2": "no painel, só uma chave de acesso que fez três chamadas.",
        "capa_creditof": "Os três vetos da construção, os dois lados da mesa, e o descarte que se confunde com a não ativação",
        "capa_rodape": "Matheus Ramos · arco 2, parte 5",

        "v1_nome": "a2p5-tres-vetos-pt",
        "v1_kicker": "OS TRÊS VETOS DA CONSTRUÇÃO",
        "v1_titulo": "Três partes podem tirar o seu produto do código, cada uma com o seu relógio",
        "v1_sub": "A primeira não é uma pessoa, e nenhuma das três aparece no painel de quem vende",
        "v1_regua_esq": "PRIMEIRA LINHA DE CÓDIGO",
        "v1_regua_dir": "PREMISSA DO QUE FOI ENTREGUE",
        "v1_c0_rot": "VETO 1 · DA MÁQUINA",
        "v1_c0_nome": "A integração falha",
        "v1_c0_relogio": "relógio: segundos",
        "v1_c0_num": "%d s × %d min" % (FIRECRAWL_S, CIRCLE_MIN),
        "v1_c0_num_sub": "a mesma tarefa no Codex, com Firecrawl e com Circle",
        "v1_c0_txt": "O agente não avisa que vetou: avisa\nque achou uma alternativa. Erro que\ndiz só \"Request failed\" entrega a\nvez ao concorrente; erro que nomeia\na causa e o formato esperado deixa\no agente consertar sozinho",
        "v1_c1_rot": "VETO 2 · DE QUEM CONSTRÓI",
        "v1_c1_nome": "O plano é recusado",
        "v1_c1_relogio": "relógio: horas",
        "v1_c1_num": "%d%% × %d%%" % (PLANO_RECUSA, PERMISSAO_RECUSA),
        "v1_c1_num_sub": "planos recusados contra pedidos de permissão recusados",
        "v1_c1_txt": "O produto aparece no plano como um\npasso com especificações técnicas.\nCada linha que depende de alguém\nfora da conversa — DNS, compra,\nchave de outra área — é um motivo\npara a pessoa recusar",
        "v1_c2_rot": "VETO 3 · DE QUEM PAGA",
        "v1_c2_nome": "O custo aparece",
        "v1_c2_relogio": "relógio: na assinatura ou no limite de consumo",
        "v1_c2_num": "%d%%" % ZYLO_CONSUMO,
        "v1_c2_num_sub": "líderes de TI com cobrança inesperada por consumo ou IA",
        "v1_c2_txt": "Quem decide não estava na conversa\nentre a pessoa e o agente. Na\nassinatura, o cartão está com outra\npessoa; no consumo, a conta passa\nde um limite e alguém pergunta o\nque é aquilo",
        "v1_barra1": "O que fica, nos três casos, é uma chave criada, algumas chamadas e silêncio",
        "v1_barra2": "É o descarte: a saída sem cancelamento, sem reclamação e sem aviso, que no painel de quem vende parece uma conta que nunca chegou a usar o produto",
        "v1_faixa": "Criar não é ficar: entre a primeira linha de código e a adoção, o produto passa por três vetos.",
        "v1_rodape": "Builder-Led Growth, arco 2 · Lightsage (30 ago 2026, material da empresa) · Anthropic (7 ago 2026, a fabricante sobre o próprio produto) · Zylo, 2026 SaaS Management Index (fornecedor)",

        "v2_nome": "a2p5-plano-e-pedido-pt",
        "v2_kicker": "O VETO DE QUEM CONSTRÓI",
        "v2_titulo": "A decisão de tirar um produto acontece no plano, não no pedido de permissão",
        "v2_sub": "Quem constrói aprova quase todo pedido de permissão e recusa quatro em cada dez planos",
        "v2_e_rot": "ONDE A RECUSA ACONTECE",
        "v2_e_nome": "Recusado pela pessoa, no Claude Code",
        "v2_e_b0": "Pedidos de permissão",
        "v2_e_b0_val": "%d%% recusados" % PERMISSAO_RECUSA,
        "v2_e_b1": "Planos apresentados para aprovação",
        "v2_e_b1_val": "%d%% recusados" % PLANO_RECUSA,
        "v2_e_aprova": "%d%% aprovados",
        "v2_e_nota": "Na leitura da própria empresa, uma taxa de aprovação tão alta sugere\nque muita gente clica por reflexo em vez de revisar cada comando",
        "v2_d_rot": "A ATENÇÃO CAI COM O VOLUME",
        "v2_d_nome": "Comandos perigosos barrados",
        "v2_d_val": "~%d%%",
        "v2_d_b0": "começo da sessão",
        "v2_d_b1": "depois de %d pedidos" % ATENCAO_PEDIDOS,
        "v2_d_nota": "%s barrados no total · %s testadores pagos, em\nexperimento controlado; sabiam que eram avaliados" % (BARRADOS, TESTADORES),
        "v2_barra1": "No plano, o seu produto não aparece como produto: aparece como um passo",
        "v2_barra2": "\"Passo 3: incluir o serviço de e-mail\", seguido das especificações técnicas que ele exige — e cada linha que depende de outra pessoa é um motivo para recusar",
        "v2_faixa": "O modo automático tira a pessoa do pedido de permissão. Não tira do plano, e é no plano que ela deveria estar.",
        "v2_rodape": "Builder-Led Growth, arco 2 · Anthropic, 7 de agosto de 2026 — a fabricante do agente, no post que anunciou o modo automático como padrão",

        "v3_nome": "a2p5-iso-25010-pt",
        "v3_kicker": "A LÍNGUA QUE O PORTÃO JÁ FALA",
        "v3_titulo": "O que a ISO/IEC 25010 mudou em %s" % ISO_DATA,
        "v3_sub": "A norma de qualidade de produto de software ganhou palavras para integrar sem quebrar",
        "v3_e_rot": "MUDARAM DE NOME",
        "v3_ren0_de": "Usabilidade",
        "v3_ren0_para": "Capacidade de interação",
        "v3_ren1_de": "Portabilidade",
        "v3_ren1_para": "Flexibilidade",
        "v3_d_rot": "ENTROU COMO CARACTERÍSTICA NOVA",
        "v3_d_nome": "Safety, com cinco subcaracterísticas",
        "v3_chips": ["Restrição operacional", "Identificação de risco", "Falha segura",
                     "Aviso de perigo", "Integração segura"],
        "v3_def0_rot": "INTEGRAÇÃO SEGURA",
        "v3_def0_txt": "Grau em que o produto mantém a segurança durante\ne depois da integração com um ou mais componentes",
        "v3_def1_rot": "FALHA SEGURA",
        "v3_def1_txt": "Grau em que o produto se põe sozinho num modo\nseguro, ou volta a uma condição segura, quando falha",
        "v3_barra1": "Ressalva: o safety da norma trata de risco a vida, saúde, patrimônio e ambiente",
        "v3_barra2": "É mais estreito do que \"o que quebra quando o agente integra\". O vocabulário serve; o escopo não é idêntico",
        "v3_faixa": "Dizer que, quando a chamada falha, nenhum e-mail sai duplicado e nada fica pela metade é falar a língua do portão.",
        "v3_rodape": "Builder-Led Growth, arco 2 · ISO/IEC 25010:2023, prefácio (prévia oficial) · definições via iso25000.com, portal especializado",

        "v4_nome": "a2p5-descarte-ou-nao-ativacao-pt",
        "v4_kicker": "O DESCARTE QUE SE CONFUNDE COM A NÃO ATIVAÇÃO",
        "v4_titulo": "Três rastros que o funil de ativação conta como um só",
        "v4_sub": "No painel, as três contas viram o mesmo número: conta criada que não ativou",
        "v4_r0_rot": "RASTRO 1",
        "v4_r0_nome": "Chave criada, nenhuma\nchamada bem-sucedida",
        "v4_r0_ver": "Nunca chegou à construção\nproblema de aquisição",
        "v4_r1_rot": "RASTRO 2",
        "v4_r1_nome": "Sequência de erros,\ndepois silêncio",
        "v4_r1_ver": "Veto da máquina\nassinatura provável",
        "v4_r2_rot": "RASTRO 3",
        "v4_r2_nome": "Chamadas bem-sucedidas,\ndepois silêncio",
        "v4_r2_ver": "Integrado e tirado\no descarte",
        "v4_leg0": "chave criada",
        "v4_leg1": "chamada bem-sucedida",
        "v4_leg2": "erro",
        "v4_leg3": "silêncio",
        "v4_barra1": "Separar os três exige pouca coisa nova",
        "v4_barra2": "Marcar a primeira chamada bem-sucedida, quando o uso parou e se quem chama é agente ou pessoa; contar por semana quem parou depois de funcionar e depois de errar",
        "v4_faixa": "Na construção, falta medir a saída que aconteceu e ninguém viu.",
        "v4_rodape": "Builder-Led Growth, arco 2 · proposta do autor a partir do mecanismo; até 6 de outubro de 2026, nenhuma plataforma de medição de agentes mede remoção em código real",

        "v5_nome": "a2p5-porta-da-adocao-pt",
        "v5_kicker": "NA PORTA DA ADOÇÃO",
        "v5_titulo": "Na adoção, o produto vira premissa, e quem decide se ele fica deixa de ser o par",
        "v5_sub": "De um lado da porta, tirar custa horas; do outro, custa um projeto",
        "v5_e_rot": "CONSTRUÇÃO",
        "v5_d_rot": "ADOÇÃO",
        "v5_custa_rot": "TIRAR CUSTA",
        "v5_decide_rot": "QUEM DECIDE",
        "v5_medir_rot": "O QUE MEDIR",
        "v5_e_custa": "horas de retrabalho",
        "v5_d_custa": "um projeto",
        "v5_e_decide": "o par, e quem paga quando o custo aparece",
        "v5_d_decide": "a economia humana: contrato, preço,\nsuporte, a dor de migrar",
        "v5_e_medir": "a primeira chamada bem-sucedida\nquem parou depois de funcionar e depois de errar\npor que um fornecedor foi trocado",
        "v5_d_medir": "entregas sem parar para consertar a integração\nvezes que o agente relê a documentação\ntempo sem aparecer num plano como problema",
        "v5_porta": "PORTA DA ADOÇÃO",
        "v5_barra1": "Ativos coespecializados (David Teece, %d): um depende do outro, nos dois sentidos" % TEECE_ANO,
        "v5_barra2": "Valor no BLG é uma taxa: quanto o par avança com o seu produto por unidade de atrito — não quantos ficaram",
        "v5_faixa": "O Builder-Led Growth decide quem entra; a economia humana decide quem fica.",
        "v5_rodape": "Builder-Led Growth, arco 2 · Teece (%d), via Springer · valor como taxa, a definição usada nesta série" % TEECE_ANO,
    },
    "en": {
        "capa_kicker": "BUILDER-LED GROWTH — ARC 2, PART 5",
        "capa_t1": "Picked on Tuesday,",
        "capa_t2": "out of the code by Friday",
        "capa_sub": "Construction: what keeps your product in the code after the AI picks it",
        "capa_frase1": "Nobody cancelled, nobody complained, nobody opened a ticket —",
        "capa_frase2": "on the dashboard, just an access key that made three calls.",
        "capa_creditof": "The three vetoes of construction, both sides of the table, and the discard that passes for non-activation",
        "capa_rodape": "Matheus Ramos · arc 2, part 5",

        "v1_nome": "a2p5-three-vetoes-en",
        "v1_kicker": "THE THREE VETOES OF CONSTRUCTION",
        "v1_titulo": "Three parties can take your product out of the code, each on its own clock",
        "v1_sub": "The first is not a person, and none of the three shows up on the seller's dashboard",
        "v1_regua_esq": "FIRST LINE OF CODE",
        "v1_regua_dir": "PREMISE OF WHAT WAS SHIPPED",
        "v1_c0_rot": "VETO 1 · THE MACHINE'S",
        "v1_c0_nome": "The integration fails",
        "v1_c0_relogio": "clock: seconds",
        "v1_c0_num": "%d s vs %d min" % (FIRECRAWL_S, CIRCLE_MIN),
        "v1_c0_num_sub": "the same task on Codex, with Firecrawl and with Circle",
        "v1_c0_txt": "The agent does not announce a veto:\nit announces it found an alternative.\nAn error saying only \"Request\nfailed\" hands the turn to the\ncompetitor; one naming the cause and\nexpected format lets the agent fix it",
        "v1_c1_rot": "VETO 2 · THE BUILDER'S",
        "v1_c1_nome": "The plan is rejected",
        "v1_c1_relogio": "clock: hours",
        "v1_c1_num": "%d%% vs %d%%" % (PLANO_RECUSA, PERMISSAO_RECUSA),
        "v1_c1_num_sub": "plans rejected against permission prompts rejected",
        "v1_c1_txt": "The product appears in the plan as a\nstep with technical specifications.\nEvery line depending on someone\noutside the conversation — DNS, a\npurchase, a key from another team —\nis a reason for the person to reject",
        "v1_c2_rot": "VETO 3 · THE PAYER'S",
        "v1_c2_nome": "The cost shows up",
        "v1_c2_relogio": "clock: at sign-up or at a usage threshold",
        "v1_c2_num": "%d%%" % ZYLO_CONSUMO,
        "v1_c2_num_sub": "IT leaders hit by unexpected usage or AI charges",
        "v1_c2_txt": "The one deciding was not in the\nconversation between person and\nagent. At sign-up, someone else\nholds the card; with usage, the\nbill crosses a threshold and\nsomeone asks what it is",
        "v1_barra1": "What is left, in all three cases, is a key created, a few calls and silence",
        "v1_barra2": "That is the discard: an exit with no cancellation, no complaint and no warning, which on the seller's dashboard looks like an account that never used the product",
        "v1_faixa": "Being created is not staying: between the first line of code and adoption, the product passes three vetoes.",
        "v1_rodape": "Builder-Led Growth, arc 2 · Lightsage (30 Aug 2026, company material) · Anthropic (7 Aug 2026, the maker on its own product) · Zylo, 2026 SaaS Management Index (vendor)",

        "v2_nome": "a2p5-plan-and-prompt-en",
        "v2_kicker": "THE BUILDER'S VETO",
        "v2_titulo": "The decision to take a product out happens in the plan, not the permission prompt",
        "v2_sub": "The person building approves nearly every permission prompt and rejects four out of ten plans",
        "v2_e_rot": "WHERE THE REJECTION HAPPENS",
        "v2_e_nome": "Rejected by the person, in Claude Code",
        "v2_e_b0": "Permission prompts",
        "v2_e_b0_val": "%d%% rejected" % PERMISSAO_RECUSA,
        "v2_e_b1": "Plans presented for approval",
        "v2_e_b1_val": "%d%% rejected" % PLANO_RECUSA,
        "v2_e_aprova": "%d%% approved",
        "v2_e_nota": "In the company's own reading, an approval rate that high suggests\nmany users click through reflexively rather than reviewing each command",
        "v2_d_rot": "ATTENTION DROPS WITH VOLUME",
        "v2_d_nome": "Dangerous commands blocked",
        "v2_d_val": "~%d%%",
        "v2_d_b0": "early in a session",
        "v2_d_b1": "after %d prompts" % ATENCAO_PEDIDOS,
        "v2_d_nota": "%s blocked overall · %s paid testers in a\ncontrolled experiment; they knew they were evaluated" % (BARRADOS_EN, TESTADORES_EN),
        "v2_barra1": "In the plan, your product does not appear as a product: it appears as a step",
        "v2_barra2": "\"Step 3: add the e-mail service\", followed by the technical specifications it requires — and every line depending on another person is a reason to reject",
        "v2_faixa": "Auto mode takes the person out of the permission prompt. It does not take them out of the plan, where they should be.",
        "v2_rodape": "Builder-Led Growth, arc 2 · Anthropic, 7 August 2026 — the agent's maker, in the post announcing auto mode as the default",

        "v3_nome": "a2p5-iso-25010-en",
        "v3_kicker": "THE LANGUAGE THE GATE ALREADY SPEAKS",
        "v3_titulo": "What ISO/IEC 25010 changed in %s" % ISO_DATA_EN,
        "v3_sub": "The software product quality standard gained words for integrating without breaking things",
        "v3_e_rot": "RENAMED",
        "v3_ren0_de": "Usability",
        "v3_ren0_para": "Interaction capability",
        "v3_ren1_de": "Portability",
        "v3_ren1_para": "Flexibility",
        "v3_d_rot": "ADDED AS A NEW CHARACTERISTIC",
        "v3_d_nome": "Safety, with five subcharacteristics",
        "v3_chips": ["Operational constraint", "Risk identification", "Fail safe",
                     "Hazard warning", "Safe integration"],
        "v3_def0_rot": "SAFE INTEGRATION",
        "v3_def0_txt": "Degree to which a product can maintain safety\nduring and after integration with other components",
        "v3_def1_rot": "FAIL SAFE",
        "v3_def1_txt": "Degree to which a product can place itself in a safe\nmode, or revert to a safe condition, when it fails",
        "v3_barra1": "Caveat: the standard's safety concerns risk to life, health, property and the environment",
        "v3_barra2": "That is narrower than \"what breaks when the agent integrates\". The vocabulary serves; the scope is not identical",
        "v3_faixa": "Saying that when the call fails no e-mail goes out twice and nothing is left half done is speaking the gate's language.",
        "v3_rodape": "Builder-Led Growth, arc 2 · ISO/IEC 25010:2023, foreword (official preview) · definitions via iso25000.com, a specialist portal",

        "v4_nome": "a2p5-discard-or-non-activation-en",
        "v4_kicker": "THE DISCARD THAT PASSES FOR NON-ACTIVATION",
        "v4_titulo": "Three traces the activation funnel counts as one",
        "v4_sub": "On the dashboard, all three accounts become the same number: an account that never activated",
        "v4_r0_rot": "TRACE 1",
        "v4_r0_nome": "Key created, no\nsuccessful call",
        "v4_r0_ver": "Never reached construction\nan acquisition problem",
        "v4_r1_rot": "TRACE 2",
        "v4_r1_nome": "A run of errors,\nthen silence",
        "v4_r1_ver": "The machine's veto\nlikely signature",
        "v4_r2_rot": "TRACE 3",
        "v4_r2_nome": "Successful calls,\nthen silence",
        "v4_r2_ver": "Integrated and taken out\nthe discard",
        "v4_leg0": "key created",
        "v4_leg1": "successful call",
        "v4_leg2": "error",
        "v4_leg3": "silence",
        "v4_barra1": "Telling the three apart takes little that is new",
        "v4_barra2": "Flag the first successful call, when usage stopped and whether the caller is an agent or a person; count weekly who stopped after working and after failing",
        "v4_faixa": "In construction, what is missing is a measure of the exit that happened and nobody saw.",
        "v4_rodape": "Builder-Led Growth, arc 2 · the author's proposal from the mechanism; as of 6 October 2026, no agent-measurement platform measures removal from real code",

        "v5_nome": "a2p5-adoption-door-en",
        "v5_kicker": "AT THE DOOR OF ADOPTION",
        "v5_titulo": "In adoption, the product becomes a premise, and the pair no longer decides if it stays",
        "v5_sub": "On one side of the door, removing it costs hours; on the other, it costs a project",
        "v5_e_rot": "CONSTRUCTION",
        "v5_d_rot": "ADOPTION",
        "v5_custa_rot": "REMOVING COSTS",
        "v5_decide_rot": "WHO DECIDES",
        "v5_medir_rot": "WHAT TO MEASURE",
        "v5_e_custa": "hours of rework",
        "v5_d_custa": "a project",
        "v5_e_decide": "the pair, and the payer when the cost shows up",
        "v5_d_decide": "human economics: contract, price,\nsupport, the pain of migrating",
        "v5_e_medir": "the first successful call\nwho stopped after working and after failing\nwhy a vendor was swapped",
        "v5_d_medir": "deliveries shipped without stopping to fix the integration\ntimes the agent rereads the documentation\nhow long it goes without showing up in a plan as a problem",
        "v5_porta": "DOOR OF ADOPTION",
        "v5_barra1": "Co-specialised assets (David Teece, %d): each depends on the other, in both directions" % TEECE_ANO,
        "v5_barra2": "Value in BLG is a rate: how far the pair gets with your product per unit of friction — not how many stayed",
        "v5_faixa": "Builder-Led Growth decides who gets in; human economics decides who stays.",
        "v5_rodape": "Builder-Led Growth, arc 2 · Teece (%d), via Springer · value as a rate, the definition used in this series" % TEECE_ANO,
    },
}


def gerar(lang):
    t = T[lang]
    salvar("a2p5-capa-pt" if lang == "pt" else "a2p5-cover-en", capa(t, lang), scale=1.5)
    for i, fn in enumerate((v1, v2, v3, v4, v5), start=1):
        salvar(t["v%d_nome" % i], fn(t, lang))


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    for lang in (["pt", "en"] if alvo is None else [alvo]):
        gerar(lang)
