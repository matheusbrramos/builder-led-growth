#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais do arco 2, parte 3 — compliance: como entrar na lista de onde a IA pode
escolher.

PT e EN no mesmo arquivo. Helpers de desenho importados do gen_p4; a
rasterização pelo Chrome e o `fecho` vêm do gen_a2p1, como no gen_a2p2. Cada
função termina com assert de folga contra o rodapé: peça torta falha alto em
vez de sair publicada.

Os cinco visuais seguem os cinco marcadores da peça, na ordem em que aparecem:
os três cortadores, as duas listas, por que o portão sobe, o portão lido por
máquina, e a idade da regra. Os números existem uma vez só, no topo, e batem
com o texto das duas línguas — quem mudar um, muda nos três lugares.

Escrito em 16 de setembro de 2026, depois de Mat aprovar o português.

Uso:  python scripts/gen_a2p3.py          # gera PT e EN
      python scripts/gen_a2p3.py pt       # só português
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
OUT = os.path.join(RAIZ, "visuais", "arco2-parte-03")

# ---------------------------------------------------------------- números
# Uma vez só. Batem com o texto das duas línguas.
GOVERNADO = 30            # Black Duck e UserEvidence, jun/2026, n=831
NAO_GOVERNADO = 70
MONITORAMENTO_LIMITADO = 44
SEM_VISIBILIDADE = 47     # Protiviti, mai/2026
NHI_GOVERNANCA = 10       # Okta, Businesses at Work 2026
NHI_PREOCUPACAO = 58
SAAS_NEGOCIO = 81         # Zylo, jan/2026
SAAS_TI = 15
SAAS_CARTAO = 4
SAAS_CARTAO_CRESC = 267
PAC_COMERCIAL = "5,2%"    # Spracklen et al., USENIX Security 2025
PAC_ABERTO = "21,7%"
PAC_COMERCIAL_EN = "5.2%"
PAC_ABERTO_EN = "21.7%"
PAC_2026 = "4,62% – 6,10%"      # Churilov, mai/2026
PAC_2026_EN = "4.62% – 6.10%"
NOMES_INVENTADOS = "205.474"
NOMES_INVENTADOS_EN = "205,474"
SUSPEITAM = 69            # Gartner, n=302, 2025
CONTA_PESSOAL = 35        # Sonar, jan/2026
QUESTIONARIO_IA = 77      # UpGuard, out/2024 (comprador)
RESPOSTAS_ACEITAS = 98    # UpGuard (fornecedor)
VANTA_ACEITACAO = 95
CHATBOT_INICIO = 51       # G2, mar/2026, n=1.076
CHATBOT_COMPARA = 41
VALIDAM_VENDEDOR = 69     # Gartner, n=645
COMPRAS_DECIDE = 53       # Forrester, jan/2026
CONTROLES_AICM = 247


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


# ------------------------------------------------ v1: os três cortadores
def v1(t, lang):
    H = 900
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    cw, gap = 470, 35
    x0 = (W - (cw * 3 + gap * 2)) / 2
    cy, ch = 210, 380
    cores = [ACCENT, AMBER, RED]
    softs = [ACCENT_SOFT, AMBER_SOFT, RED_SOFT]
    for i in range(3):
        cx = x0 + i * (cw + gap)
        b.append(rect(cx, cy, cw, ch, softs[i], rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cores[i], 2, rx=14))
        b.append(rect(cx, cy, cw, 7, cores[i], rx=0))
        b.append(txt(cx + 26, cy + 50, t["v1_c%d_rot" % i], 13, "700", cores[i], sp="2"))
        b.append(txt(cx + 26, cy + 94, t["v1_c%d_nome" % i], 30, "700", NAVY))
        b.append(txt(cx + 26, cy + 138, t["v1_c%d_com" % i], 22, "700", cores[i]))
        b.append(line(cx + 26, cy + 162, cx + cw - 26, cy + 162, cores[i], 1.2))
        linhas(b, cx + 26, cy + 194, t["v1_c%d_txt" % i], 14.5, NAVY, 22)

    yb = cy + ch + 30
    b.append(rect(60, yb, W - 120, 84, NAVY, rx=14))
    b.append(txt(92, yb + 34, t["v1_barra1"], 21, "700", WHITE))
    b.append(txt(92, yb + 64, t["v1_barra2"], 15, "400", "#AEB6C2"))

    fecho(b, H, t["v1_faixa"])
    footer(b, W, H, t["v1_rodape"])
    assert yb + 84 < H - 152, "v1 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v2: as duas listas
def v2(t, lang):
    H = 900
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    pw, ph = 630, 400
    py = 200
    cores = [NAVY, ACCENT]
    softs = [PANEL, ACCENT_SOFT]
    for k in range(2):
        px = 60 if k == 0 else W - 60 - pw
        b.append(rect(px, py, pw, ph, softs[k], rx=14))
        b.append(rect(px, py, pw, ph, "none", cores[k], 2, rx=14))
        b.append(txt(px + 26, py + 46, t["v2_l%d_rot" % k], 13, "700", cores[k], sp="2"))
        b.append(txt(px + 26, py + 90, t["v2_l%d_nome" % k], 30, "700", NAVY))
        b.append(txt(px + 26, py + 124, t["v2_l%d_quem" % k], 15, "400", GRAY_LIGHT,
                     style="italic"))
        b.append(line(px + 26, py + 146, px + pw - 26, py + 146, cores[k], 1.2))
        for r in range(3):
            ry = py + 166 + r * 74
            b.append(rect(px + 20, ry, pw - 40, 62, WHITE, rx=10))
            b.append(txt(px + 36, ry + 24, t["v2_l%d_r%d_rot" % (k, r)], 12, "700",
                         cores[k], sp="1.5"))
            b.append(txt(px + 36, ry + 46, t["v2_l%d_r%d_txt" % (k, r)], 14, "400", NAVY))
    # seta entre as duas listas
    ax = 60 + pw + 10
    ay = py + ph / 2
    b.append(line(ax, ay, W - 60 - pw - 10, ay, ACCENT, 4))
    b.append('<polygon points="%d,%d %d,%d %d,%d" fill="%s"/>' % (
        W - 60 - pw - 8, ay, W - 60 - pw - 30, ay - 14, W - 60 - pw - 30, ay + 14, ACCENT))
    linhas(b, W / 2, ay - 44, t["v2_seta"], 12.5, ACCENT, 18, "700", anchor="middle")

    yb = py + ph + 26
    b.append(rect(60, yb, W - 120, 92, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v2_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 68, t["v2_barra2"], 14.5, "400", "#AEB6C2"))

    fecho(b, H, t["v2_faixa"], ACCENT, ACCENT_SOFT)
    footer(b, W, H, t["v2_rodape"])
    assert yb + 92 < H - 152, "v2 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v3: por que o portão sobe
def v3(t, lang):
    H = 840
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    tw, gap = 340, 26
    x0 = (W - (tw * 4 + gap * 3)) / 2
    ty, th = 204, 330
    cores = [GRAY_LIGHT, RED, AMBER, ACCENT]
    softs = [PANEL, RED_SOFT, AMBER_SOFT, ACCENT_SOFT]
    for i in range(4):
        tx = x0 + i * (tw + gap)
        b.append(rect(tx, ty, tw, th, softs[i], rx=14))
        b.append(rect(tx, ty, tw, 7, cores[i], rx=0))
        b.append(txt(tx + 22, ty + 46, t["v3_t%d_rot" % i], 12.5, "700", cores[i], sp="1.5"))
        b.append(txt(tx + 22, ty + 116, t["v3_t%d_num" % i], 50, "700", NAVY))
        b.append(txt(tx + 22, ty + 146, t["v3_t%d_sub" % i], 13.5, "400", GRAY_LIGHT,
                     style="italic"))
        b.append(line(tx + 22, ty + 166, tx + tw - 22, ty + 166, cores[i], 1.2))
        linhas(b, tx + 22, ty + 196, t["v3_t%d_txt" % i], 14, NAVY, 20)

    yb = ty + th + 28
    b.append(rect(60, yb, W - 120, 84, NAVY, rx=14))
    b.append(txt(W / 2, yb + 36, t["v3_barra1"], 22, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 64, t["v3_barra2"], 14.5, "400", "#AEB6C2", anchor="middle"))

    fecho(b, H, t["v3_faixa"], RED, RED_SOFT)
    footer(b, W, H, t["v3_rodape"])
    assert yb + 84 < H - 152, "v3 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v4: o portão lido por máquina
def v4(t, lang):
    H = 880
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    pw, ph = 560, 360
    py = 204
    mid_w = 300
    xs = [60, W - 60 - pw]
    cores = [GREEN, ACCENT]
    softs = [GREEN_SOFT, ACCENT_SOFT]
    for k in range(2):
        px = xs[k]
        b.append(rect(px, py, pw, ph, softs[k], rx=14))
        b.append(rect(px, py, pw, ph, "none", cores[k], 2, rx=14))
        b.append(txt(px + 26, py + 46, t["v4_s%d_rot" % k], 13, "700", cores[k], sp="2"))
        b.append(txt(px + 26, py + 88, t["v4_s%d_nome" % k], 26, "700", NAVY))
        b.append(txt(px + 26, py + 160, t["v4_s%d_num" % k], 54, "700", cores[k]))
        b.append(txt(px + 26, py + 190, t["v4_s%d_num_sub" % k], 14, "400", GRAY_LIGHT,
                     style="italic"))
        b.append(line(px + 26, py + 212, px + pw - 26, py + 212, cores[k], 1.2))
        linhas(b, px + 26, py + 242, t["v4_s%d_txt" % k], 14.5, NAVY, 22)
    # o meio: a pessoa decide
    mx = (W - mid_w) / 2
    b.append(rect(mx, py + 40, mid_w, ph - 80, WHITE, rx=14))
    b.append(rect(mx, py + 40, mid_w, ph - 80, "none", AMBER, 2, rx=14))
    b.append(txt(mx + mid_w / 2, py + 86, t["v4_m_rot"], 12.5, "700", AMBER, anchor="middle",
                 sp="1.5"))
    b.append(txt(mx + mid_w / 2, py + 156, t["v4_m_num"], 54, "700", NAVY, anchor="middle"))
    linhas(b, mx + mid_w / 2, py + 192, t["v4_m_txt"], 14, GRAY, 20, anchor="middle")
    # setas dos dois lados para o meio
    ay = py + ph / 2
    b.append(line(60 + pw + 8, ay, mx - 8, ay, GRAY_LIGHT, 3))
    b.append(line(mx + mid_w + 8, ay, W - 60 - pw - 8, ay, GRAY_LIGHT, 3))

    yb = py + ph + 26
    b.append(rect(60, yb, W - 120, 92, NAVY, rx=14))
    b.append(txt(92, yb + 36, t["v4_barra1"], 20, "700", WHITE))
    b.append(txt(92, yb + 68, t["v4_barra2"], 14.5, "400", "#AEB6C2"))

    fecho(b, H, t["v4_faixa"], GREEN, GREEN_SOFT)
    footer(b, W, H, t["v4_rodape"])
    assert yb + 92 < H - 152, "v4 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v5: a idade da regra
def v5(t, lang):
    H = 840
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    pw, gap = 720, 40
    x0 = (W - (pw * 2 + gap)) / 2
    py, ph = 204, 340
    cores = [ACCENT, GRAY_LIGHT]
    softs = [ACCENT_SOFT, PANEL]
    for k in range(2):
        px = x0 + k * (pw + gap)
        b.append(rect(px, py, pw, ph, softs[k], rx=14))
        b.append(rect(px, py, pw, ph, "none", cores[k], 2, rx=14))
        b.append(rect(px, py, pw, 7, cores[k], rx=0))
        b.append(txt(px + 26, py + 50, t["v5_r%d_rot" % k], 13, "700", cores[k], sp="2"))
        b.append(txt(px + 26, py + 94, t["v5_r%d_nome" % k], 28, "700", NAVY))
        b.append(txt(px + 26, py + 128, t["v5_r%d_forca" % k], 16, "400", GRAY_LIGHT,
                     style="italic"))
        b.append(line(px + 26, py + 150, px + pw - 26, py + 150, cores[k], 1.2))
        b.append(txt(px + 26, py + 186, t["v5_r%d_resp" % k], 12.5, "700", cores[k], sp="1.5"))
        linhas(b, px + 26, py + 214, t["v5_r%d_txt" % k], 14.5, NAVY, 22)

    yb = py + ph + 28
    b.append(rect(60, yb, W - 120, 84, NAVY, rx=14))
    b.append(txt(W / 2, yb + 36, t["v5_barra1"], 22, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 64, t["v5_barra2"], 14.5, "400", "#AEB6C2", anchor="middle"))

    fecho(b, H, t["v5_faixa"], AMBER, AMBER_SOFT)
    footer(b, W, H, t["v5_rodape"])
    assert yb + 84 < H - 152, "v5 encosta no fecho"
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
        "capa_kicker": "BUILDER-LED GROWTH — ARCO 2, PARTE 3",
        "capa_t1": "Ninguém recusou você.",
        "capa_t2": "Você nunca esteve na lista",
        "capa_sub": "Compliance: como entrar na lista de onde a IA pode escolher",
        "capa_frase1": "Um CRM montado com IA numa empresa de 2.500 pessoas, e o serviço de e-mail",
        "capa_frase2": "decidido seis meses antes do primeiro prompt, por quem nunca vai comparar fornecedores.",
        "capa_creditof": "Três cortadores, duas listas, uma norma lida por máquina, e a idade da regra",
        "capa_rodape": "Matheus Ramos · arco 2, parte 3",

        "v1_nome": "a2p3-tres-cortadores-pt",
        "v1_kicker": "ADMISSIBILIDADE — ANTES DA PREFERÊNCIA",
        "v1_titulo": "Três coisas cortam o conjunto antes de a máquina escolher",
        "v1_sub": "Um produto reprovado aqui não é concorrente fraco: é ausente, e o agente nunca soube que ele existia",
        "v1_c0_rot": "CORTADOR 1",
        "v1_c0_nome": "Uma pessoa",
        "v1_c0_com": "com uma lista",
        "v1_c0_txt": "Escreve de onde o agente pode\npuxar fornecedores, a partir do que\na empresa já tem contrato, do que a\nplataforma já cataloga e do que a\nsegurança já revisou. Nunca compara\nprodutos de e-mail. Escreve seis\nmeses antes do primeiro prompt",
        "v1_c1_rot": "CORTADOR 2",
        "v1_c1_nome": "Uma norma",
        "v1_c1_com": "com um processo",
        "v1_c1_txt": "ISO/IEC 42001 vale para quem usa IA,\nnão só para quem desenvolve. O Anexo\nA manda existir um processo sobre\nfornecedor, não uma exigência. O\nportão é tão concreto quanto o\ncomprador o fizer — e um comprador\nnomeado já o fez",
        "v1_c2_rot": "CORTADOR 3",
        "v1_c2_nome": "O seu passado",
        "v1_c2_com": "no corpus",
        "v1_c2_txt": "A issue, a resposta no fórum e o\nartigo com a solução alternativa,\npublicados no dia de um defeito de\n2024. O código foi corrigido em\nhoras; o material sobrevive por anos,\ne é ele que o modelo de 2025 lê.\nÉ o único que o fornecedor controla",
        "v1_barra1": "Antes das cinco forças de Porter falta uma pergunta: quem decide o conjunto, e com que critério?",
        "v1_barra2": "Do lado de quem constrói agentes o estágio se chama tool eligibility (Zhu, mai/2026); do lado de quem compra, homologação de fornecedores (Wright e Barbour, 1977)",
        "v1_faixa": "Perder uma venda deixa rastro. Ser cortado do conjunto não deixa nenhum.",
        "v1_rodape": "Builder-Led Growth, arco 2 · Porter (HBR, 1979) · Zhu (mai/2026) · Wright e Barbour (1977) · ISO/IEC 42001:2023, Anexo A",

        "v2_nome": "a2p3-duas-listas-pt",
        "v2_kicker": "QUEM CORTA: A PESSOA, E AS DUAS LISTAS",
        "v2_titulo": "A lista de compras alimenta a lista do agente, e ninguém compara produtos em nenhuma",
        "v2_sub": "A segunda quase não existe ainda; a maioria das empresas está no meio, onde a lista existe e não fecha tudo",
        "v2_l0_rot": "LISTA 1",
        "v2_l0_nome": "A lista de compras",
        "v2_l0_quem": "escrita por compras, segurança e jurídico — ninguém que vá usar o serviço",
        "v2_l0_r0_rot": "O QUE ELA PERGUNTA",
        "v2_l0_r0_txt": "Tem relatório de auditoria? Onde guarda o dado? O que faz com ele?",
        "v2_l0_r1_rot": "O QUE ELA NÃO PERGUNTA",
        "v2_l0_r1_txt": "Se o serviço de e-mail entrega melhor que o concorrente",
        "v2_l0_r2_rot": "QUANTO ELA ALCANÇA",
        "v2_l0_r2_txt": "%d%% do gasto em SaaS é das unidades de negócio; TI, %d%%; cartão, %d%%" % (SAAS_NEGOCIO, SAAS_TI, SAAS_CARTAO),
        "v2_l1_rot": "LISTA 2",
        "v2_l1_nome": "A lista do agente",
        "v2_l1_quem": "escrita por quem administra a plataforma ou o editor",
        "v2_l1_r0_rot": "ONDE ELA MORA",
        "v2_l1_r0_txt": "Copilot, Claude Code, Cursor (Enterprise), Codex: servidor MCP por identidade",
        "v2_l1_r1_rot": "O QUE A DOCUMENTAÇÃO AVISA",
        "v2_l1_r1_txt": "\"Não é uma fronteira de segurança\" (Cursor); a API aberta passa por fora",
        "v2_l1_r2_rot": "QUANTAS EMPRESAS A TÊM",
        "v2_l1_r2_txt": "%d%% têm governança para identidades não humanas; %d%%: preocupação nº 1" % (NHI_GOVERNANCA, NHI_PREOCUPACAO),
        "v2_seta": "A PRIMEIRA\nALIMENTA A SEGUNDA",
        "v2_barra1": "Governança plena em %d%% das equipes de engenharia; %d%% das grandes empresas sem visibilidade completa" % (GOVERNADO, SEM_VISIBILIDADE),
        "v2_barra2": "Black Duck e UserEvidence (jun/2026, n=831, fornecedor de segurança) · Protiviti (mai/2026, consultoria) · Zylo (jan/2026, base própria) · Okta (2026)",
        "v2_faixa": "O fornecedor de e-mail que já está no contrato da nuvem entra na lista do agente sem que ninguém compare nada.",
        "v2_rodape": "Builder-Led Growth, arco 2 · Cursor e OpenAI (documentação oficial, set/2026) · Zylo · Okta · Black Duck · Protiviti",

        "v3_nome": "a2p3-portao-sobe-pt",
        "v3_kicker": "POR QUE O PORTÃO SOBE",
        "v3_titulo": "A ausência de governança produz o risco que vai justificá-la",
        "v3_sub": "Direção sem medida: nenhum levantamento repete a mesma pergunta em dois anos. O mecanismo, sim, tem número",
        "v3_t0_rot": "ONDE ESTÁ A MAIORIA",
        "v3_t0_num": "%d%%" % NAO_GOVERNADO,
        "v3_t0_sub": "governança parcial ou informal",
        "v3_t0_txt": "%d%% plenamente governado, %d%%\nestruturado com monitoramento\nlimitado, o resto informal ou\nindividual. Empresas com mais\nde 500 pessoas, n=831" % (GOVERNADO, MONITORAMENTO_LIMITADO),
        "v3_t1_rot": "O PACOTE QUE NÃO EXISTE",
        "v3_t1_num": PAC_COMERCIAL,
        "v3_t1_sub": "a %s conforme o modelo, 2025" % PAC_ABERTO,
        "v3_t1_txt": "%s nomes únicos inventados\nem 576 mil amostras. Em 2026,\n%s nos modelos de\nfronteira; 127 nomes que cinco\nmodelos inventam igual" % (NOMES_INVENTADOS, PAC_2026),
        "v3_t2_rot": "O QUE A EMPRESA NÃO VÊ",
        "v3_t2_num": "%d%%" % SUSPEITAM,
        "v3_t2_sub": "suspeitam de uso proibido de IA",
        "v3_t2_txt": "Líderes de segurança, n=302\n(Gartner, 2025). Entre\ndesenvolvedores, %d%% acessam\nIA por conta pessoal\n(Sonar, jan/2026)" % CONTA_PESSOAL,
        "v3_t3_rot": "QUEM CADASTROU O AGENTE",
        "v3_t3_num": "%d%%" % NHI_GOVERNANCA,
        "v3_t3_sub": "com governança de identidade para agentes",
        "v3_t3_txt": "A empresa sabe que tem agentes\nrodando, não sabe quantos, e\nnão sabe o que eles podem\nconectar (Okta, 2026)",
        "v3_barra1": "O incidente chega à mesa de alguém, e a resposta é escrever a lista",
        "v3_barra2": "Quem escreve tem nome e cargo, quase nunca é um comitê: presidente, conselho executivo, quem administra a plataforma",
        "v3_faixa": "Quem vende para essa empresa hoje está vendendo para uma lista que ainda não foi escrita.",
        "v3_rodape": "Builder-Led Growth, arco 2 · Black Duck (jun/2026) · Spracklen et al. (USENIX Security 2025) · Churilov (mai/2026) · Gartner via Infosecurity (nov/2025) · Sonar · Okta",

        "v4_nome": "a2p3-lido-por-maquina-pt",
        "v4_kicker": "O PORTÃO LIDO POR MÁQUINA",
        "v4_titulo": "O questionário que o fornecedor responde com IA é lido pela IA do comprador",
        "v4_sub": "Produto vendido desde outubro de 2024, não previsão. A pessoa entra depois, para decidir sobre o que as duas máquinas concordaram",
        "v4_s0_rot": "LADO DO FORNECEDOR",
        "v4_s0_nome": "A IA responde o questionário",
        "v4_s0_num": "%d%%" % RESPOSTAS_ACEITAS,
        "v4_s0_num_sub": "das sugestões aceitas (UpGuard); %d%% de aceitação (Vanta)" % VANTA_ACEITACAO,
        "v4_s0_txt": "Lê o próprio relatório de auditoria\n(SOC 2, ISO 27001) e responde o\nquestionário de cada comprador,\ndezenas de vezes por ano. Os\npercentuais são das próprias\nempresas que vendem a ferramenta",
        "v4_s1_rot": "LADO DO COMPRADOR",
        "v4_s1_nome": "A IA lê o relatório",
        "v4_s1_num": "%d%%" % QUESTIONARIO_IA,
        "v4_s1_num_sub": "de um questionário de 100+ perguntas preenchido a partir do SOC 2",
        "v4_s1_txt": "Agentes que \"leem evidência do\nfornecedor, respondem controles\ncom citações\" e apontam o que\naprovar ou escalar (Whistic).\nPrimeira pergunta de IA de um\ncomprador: você treina com meu dado?",
        "v4_m_rot": "A DECISÃO",
        "v4_m_num": "%d%%" % VALIDAM_VENDEDOR,
        "v4_m_txt": "dos compradores validam\no que a IA disse com\num vendedor (Gartner,\nn=645). A pessoa decide;\na máquina prepara",
        "v4_barra1": "Na lista curta do comprador humano: %d%% começam por chatbot, e comparar fornecedores é o uso nº 1 (%d%%)" % (CHATBOT_INICIO, CHATBOT_COMPARA),
        "v4_barra2": "G2 (mar/2026, n=1.076, site de avaliações) · compras é decisor em %d%% dos ciclos, desde o início (Forrester, jan/2026)" % COMPRAS_DECIDE,
        "v4_faixa": "Certificação substitui o questionário, não o processo. O que a máquina lê é em parte o que você publica, em parte o que você entrega sob NDA.",
        "v4_rodape": "Builder-Led Growth, arco 2 · UpGuard (out/2024) · Whistic · Vanta · GitLab (manual público) · G2 (abr/2026) · Gartner (mai/2026, lido em cópia) · Forrester (jan/2026)",

        "v5_nome": "a2p3-idade-da-regra-pt",
        "v5_kicker": "O QUE SE PROVA, A QUEM",
        "v5_titulo": "A idade da regra diz qual argumento funciona",
        "v5_sub": "Compliance não é a ansiedade: é a resposta institucional a ela. E envelhece para hábito",
        "v5_r0_rot": "REGRA NOVA",
        "v5_r0_nome": "A lista escrita há seis meses",
        "v5_r0_forca": "ainda é ansiedade — alguém lembra qual susto a criou",
        "v5_r0_resp": "RESPONDE A",
        "v5_r0_txt": "Evidência, prova e reversibilidade.\nÉ aqui que a conformidade conferível\nfaz diferença: o link para a atestação\nreal, o relatório de auditoria, a\npágina de status, o registro público\ndo questionário",
        "v5_r1_rot": "REGRA VELHA",
        "v5_r1_nome": "O fornecedor no contrato há cinco anos",
        "v5_r1_forca": "já é hábito — ninguém no time lembra o medo, só o passo",
        "v5_r1_resp": "SÓ CEDE A",
        "v5_r1_txt": "Convivência, troca pequena e o caminho\nque não exige desfazer nada. Quem chega\ncom relatório de auditoria contra uma\nregra de cinco anos fala com a\nansiedade de alguém que já foi embora",
        "v5_barra1": "Declarar conformidade é tática que decai. Tornar a conformidade conferível é tática que fica.",
        "v5_barra2": "Afirmação num arquivo é afirmação não verificada: se todo fornecedor escrever que atende a norma, o leitor de máquina passa a ignorar",
        "v5_faixa": "Critério não testado, dito como tal: raciocínio sobre as quatro forças de Moesta e Spiek, sem medição.",
        "v5_rodape": "Builder-Led Growth, arco 2 · Moesta e Spiek (The Four Forces) · Cloud Security Alliance, AI-CAIQ (jun/2026, %d controles) · Microsoft SSPA (abr/2025)" % CONTROLES_AICM,
    },
    "en": {
        "capa_kicker": "BUILDER-LED GROWTH — ARC 2, PART 3",
        "capa_t1": "Nobody turned you down.",
        "capa_t2": "You were never on the list",
        "capa_sub": "Compliance: how to get on the list the AI is allowed to pick from",
        "capa_frase1": "A CRM built with AI at a company of 2,500 people, and the e-mail service",
        "capa_frase2": "decided six months before the first prompt, by someone who will never compare vendors.",
        "capa_creditof": "Three cutters, two lists, a standard read by machine, and the age of the rule",
        "capa_rodape": "Matheus Ramos · arc 2, part 3",

        "v1_nome": "a2p3-three-cutters-en",
        "v1_kicker": "ADMISSIBILITY — BEFORE PREFERENCE",
        "v1_titulo": "Three things cut the set before the machine chooses",
        "v1_sub": "A product that fails here is not a weak competitor: it is absent, and the agent never knew it existed",
        "v1_c0_rot": "CUTTER 1",
        "v1_c0_nome": "A person",
        "v1_c0_com": "with a list",
        "v1_c0_txt": "Writes where the agent may pull\nvendors from, out of what the company\nalready has under contract, what the\nplatform already catalogues and what\nsecurity already reviewed. Never\ncompares e-mail products. Writes it\nsix months before the first prompt",
        "v1_c1_rot": "CUTTER 2",
        "v1_c1_nome": "A standard",
        "v1_c1_com": "with a process",
        "v1_c1_txt": "ISO/IEC 42001 applies to whoever uses\nAI, not only to whoever builds it.\nAnnex A requires a process about\nsuppliers, not a requirement. The gate\nis as concrete as the buyer makes it —\nand one named buyer has made it",
        "v1_c2_rot": "CUTTER 3",
        "v1_c2_nome": "Your own past",
        "v1_c2_com": "in the corpus",
        "v1_c2_txt": "The issue, the forum reply and the\narticle with the workaround, published\nthe day of a 2024 defect. The code was\nfixed in hours; the material survives\nfor years, and it is what the 2025\nmodel reads. The only cutter the\nvendor controls",
        "v1_barra1": "Ahead of Porter's five forces a question is missing: who decides the set, and by what criterion?",
        "v1_barra2": "On the agent-building side the stage is called tool eligibility (Zhu, May 2026); on the buying side, vendor approval (Wright and Barbour, 1977)",
        "v1_faixa": "Losing a sale leaves a trace. Being cut from the set leaves none.",
        "v1_rodape": "Builder-Led Growth, arc 2 · Porter (HBR, 1979) · Zhu (May 2026) · Wright and Barbour (1977) · ISO/IEC 42001:2023, Annex A",

        "v2_nome": "a2p3-two-lists-en",
        "v2_kicker": "WHO CUTS: THE PERSON, AND THE TWO LISTS",
        "v2_titulo": "The procurement list feeds the agent's list, and nobody compares products in either",
        "v2_sub": "The second barely exists yet; most companies sit in the middle, where the list exists and does not close everything",
        "v2_l0_rot": "LIST 1",
        "v2_l0_nome": "The procurement list",
        "v2_l0_quem": "written by procurement, security and legal — nobody who will use the service",
        "v2_l0_r0_rot": "WHAT IT ASKS",
        "v2_l0_r0_txt": "Is there an audit report? Where is the data kept? What is done with it?",
        "v2_l0_r1_rot": "WHAT IT DOES NOT ASK",
        "v2_l0_r1_txt": "Whether the e-mail service delivers better than the competitor's",
        "v2_l0_r2_rot": "HOW FAR IT REACHES",
        "v2_l0_r2_txt": "%d%% of SaaS spend is business units'; IT, %d%%; the card, %d%%" % (SAAS_NEGOCIO, SAAS_TI, SAAS_CARTAO),
        "v2_l1_rot": "LIST 2",
        "v2_l1_nome": "The agent's list",
        "v2_l1_quem": "written by whoever administers the platform or the editor",
        "v2_l1_r0_rot": "WHERE IT LIVES",
        "v2_l1_r0_txt": "Copilot, Claude Code, Cursor (Enterprise), Codex: MCP server by identity",
        "v2_l1_r1_rot": "WHAT THE DOCS WARN",
        "v2_l1_r1_txt": "\"Not a security boundary\" (Cursor); the open API goes around it",
        "v2_l1_r2_rot": "HOW MANY COMPANIES HAVE ONE",
        "v2_l1_r2_txt": "%d%% have governance for non-human identities; %d%%: concern no. 1" % (NHI_GOVERNANCA, NHI_PREOCUPACAO),
        "v2_seta": "THE FIRST\nFEEDS THE SECOND",
        "v2_barra1": "Full governance at %d%% of engineering teams; %d%% of large enterprises without full visibility" % (GOVERNADO, SEM_VISIBILIDADE),
        "v2_barra2": "Black Duck and UserEvidence (Jun 2026, n=831, security vendor) · Protiviti (May 2026, consultancy) · Zylo (Jan 2026, own base) · Okta (2026)",
        "v2_faixa": "The e-mail vendor already in the cloud contract enters the agent's list without anyone comparing anything.",
        "v2_rodape": "Builder-Led Growth, arc 2 · Cursor and OpenAI (official docs, Sep 2026) · Zylo · Okta · Black Duck · Protiviti",

        "v3_nome": "a2p3-gate-rises-en",
        "v3_kicker": "WHY THE GATE RISES",
        "v3_titulo": "The absence of governance produces the risk that will justify it",
        "v3_sub": "Direction without a measure: no survey repeats the same question two years running. The mechanism does have numbers",
        "v3_t0_rot": "WHERE THE MAJORITY IS",
        "v3_t0_num": "%d%%" % NAO_GOVERNADO,
        "v3_t0_sub": "partial or informal governance",
        "v3_t0_txt": "%d%% fully governed, %d%%\nstructured with limited\nmonitoring, the rest informal\nor individual. Companies with\nmore than 500 people, n=831" % (GOVERNADO, MONITORAMENTO_LIMITADO),
        "v3_t1_rot": "THE PACKAGE THAT DOES NOT EXIST",
        "v3_t1_num": PAC_COMERCIAL_EN,
        "v3_t1_sub": "to %s depending on the model, 2025" % PAC_ABERTO_EN,
        "v3_t1_txt": "%s unique invented names\nin 576,000 samples. In 2026,\n%s on frontier\nmodels; 127 names five models\ninvent identically" % (NOMES_INVENTADOS_EN, PAC_2026_EN),
        "v3_t2_rot": "WHAT THE COMPANY DOES NOT SEE",
        "v3_t2_num": "%d%%" % SUSPEITAM,
        "v3_t2_sub": "suspect prohibited AI use",
        "v3_t2_txt": "Security leaders, n=302\n(Gartner, 2025). Among\ndevelopers, %d%% access AI\nthrough a personal account\n(Sonar, Jan 2026)" % CONTA_PESSOAL,
        "v3_t3_rot": "WHO REGISTERED THE AGENT",
        "v3_t3_num": "%d%%" % NHI_GOVERNANCA,
        "v3_t3_sub": "with identity governance for agents",
        "v3_t3_txt": "The company knows it has agents\nrunning, does not know how\nmany, and does not know what\nthey can connect to (Okta, 2026)",
        "v3_barra1": "The incident lands on someone's desk, and the answer is to write the list",
        "v3_barra2": "Whoever writes it has a name and a title, and is almost never a committee: a president, an executive board, whoever administers the platform",
        "v3_faixa": "Whoever sells to that company today is selling to a list that has not been written yet.",
        "v3_rodape": "Builder-Led Growth, arc 2 · Black Duck (Jun 2026) · Spracklen et al. (USENIX Security 2025) · Churilov (May 2026) · Gartner via Infosecurity (Nov 2025) · Sonar · Okta",

        "v4_nome": "a2p3-read-by-machine-en",
        "v4_kicker": "THE GATE READ BY MACHINE",
        "v4_titulo": "The questionnaire the vendor answers with AI is read by the buyer's AI",
        "v4_sub": "A product sold since October 2024, not a forecast. The person comes in afterwards, to decide on what the two machines agreed",
        "v4_s0_rot": "VENDOR SIDE",
        "v4_s0_nome": "AI answers the questionnaire",
        "v4_s0_num": "%d%%" % RESPOSTAS_ACEITAS,
        "v4_s0_num_sub": "of suggestions accepted (UpGuard); %d%% acceptance (Vanta)" % VANTA_ACEITACAO,
        "v4_s0_txt": "Reads its own audit report (SOC 2,\nISO 27001) and answers each buyer's\nquestionnaire, dozens of times a\nyear. The percentages are the\ntool vendors' own",
        "v4_s1_rot": "BUYER SIDE",
        "v4_s1_nome": "AI reads the report",
        "v4_s1_num": "%d%%" % QUESTIONARIO_IA,
        "v4_s1_num_sub": "of a 100+ question questionnaire filled in from the SOC 2",
        "v4_s1_txt": "Agents that \"read vendor evidence,\nanswer controls with citations\" and\nsurface what to approve or escalate\n(Whistic). A buyer's first AI\nquestion: do you train on my data?",
        "v4_m_rot": "THE DECISION",
        "v4_m_num": "%d%%" % VALIDAM_VENDEDOR,
        "v4_m_txt": "of buyers validate what\nthe AI said with a sales\nrep (Gartner, n=645).\nThe person decides;\nthe machine prepares",
        "v4_barra1": "In the human buyer's shortlist: %d%% start with a chatbot, and comparing vendors is use no. 1 (%d%%)" % (CHATBOT_INICIO, CHATBOT_COMPARA),
        "v4_barra2": "G2 (Mar 2026, n=1,076, a review site) · procurement is a decision-maker in %d%% of cycles, from the start (Forrester, Jan 2026)" % COMPRAS_DECIDE,
        "v4_faixa": "Certification replaces the questionnaire, not the process. What the machine reads is partly what you publish, partly what you hand over under NDA.",
        "v4_rodape": "Builder-Led Growth, arc 2 · UpGuard (Oct 2024) · Whistic · Vanta · GitLab (public handbook) · G2 (Apr 2026) · Gartner (May 2026, read in a copy) · Forrester (Jan 2026)",

        "v5_nome": "a2p3-age-of-the-rule-en",
        "v5_kicker": "WHAT TO PROVE, TO WHOM",
        "v5_titulo": "The age of the rule says which argument works",
        "v5_sub": "Compliance is not the anxiety: it is the institutional answer to it. And it ages into habit",
        "v5_r0_rot": "NEW RULE",
        "v5_r0_nome": "The list written six months ago",
        "v5_r0_forca": "still anxiety — someone remembers which scare created it",
        "v5_r0_resp": "RESPONDS TO",
        "v5_r0_txt": "Evidence, proof and reversibility.\nThis is where checkable compliance\nmakes the difference: the link to the\nactual attestation, the audit report,\nthe status page, the public register\nof the questionnaire",
        "v5_r1_rot": "OLD RULE",
        "v5_r1_nome": "The vendor in the contract for five years",
        "v5_r1_forca": "already habit — nobody on the team remembers the fear, only the step",
        "v5_r1_resp": "YIELDS ONLY TO",
        "v5_r1_txt": "Coexistence, the small switch and the\npath that requires undoing nothing.\nWhoever arrives with an audit report\nagainst a five-year-old rule speaks\nto the anxiety of someone who has left",
        "v5_barra1": "Declaring compliance is a tactic that decays. Making compliance checkable is a tactic that lasts.",
        "v5_barra2": "A claim in a file is an unverified claim: if every vendor writes that it meets the standard, the machine reader starts ignoring it",
        "v5_faixa": "An untested criterion, said as such: reasoning over Moesta and Spiek's four forces, without measurement.",
        "v5_rodape": "Builder-Led Growth, arc 2 · Moesta and Spiek (The Four Forces) · Cloud Security Alliance, AI-CAIQ (Jun 2026, %d controls) · Microsoft SSPA (Apr 2025)" % CONTROLES_AICM,
    },
}


def gerar(lang):
    t = T[lang]
    salvar("a2p3-capa-pt" if lang == "pt" else "a2p3-cover-en", capa(t, lang), scale=1.5)
    for i, fn in enumerate((v1, v2, v3, v4, v5), start=1):
        salvar(t["v%d_nome" % i], fn(t, lang))


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    for lang in (["pt", "en"] if alvo is None else [alvo]):
        gerar(lang)
