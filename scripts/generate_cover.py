#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capa de artigo LinkedIn (1920x1080) — Builder-Led Growth, PT-BR e EN."""
import cairosvg
import os

OUT = os.path.dirname(os.path.abspath(__file__))
FONT = "Liberation Sans, Arial, sans-serif"

NAVY = "#16213E"
NAVY_DEEP = "#101A30"
GRAY_LIGHT = "#AEB6C2"
ACCENT = "#2F5D8A"
ACCENT_LIGHT = "#6E9CC4"
ACCENT_SOFT = "#E7EEF4"
AMBER = "#B8792E"
WHITE = "#FFFFFF"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=16, weight="400", fill=NAVY, anchor="start", style="normal", spacing=None):
    sp = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" fill="{fill}" '
            f'text-anchor="{anchor}"{sp}>{esc(s)}</text>')


def build_cover(lang):
    W, H = 1920, 1080
    if lang == "pt":
        kicker = "UMA NOVA DISCIPLINA DE GROWTH — PARTE 1 DE 2"
        title1 = "Builder-Led Growth"
        sub1 = "Quando a máquina também"
        sub2 = "é seu cliente"
        d1 = "ALG"
        d1b = "compra formal"
        d2 = "BLG"
        d2b = "construção"
        d3 = "PLG 3.0"
        d3b = "produto headless"
        gap_label = "o vão entre as fronteiras existentes"
        footer = "Matheus Ramos · com casos Supabase e shadcn/ui, dados de GEO e economia de token"
    else:
        kicker = "A NEW GROWTH DISCIPLINE — PART 1 OF 2"
        title1 = "Builder-Led Growth"
        sub1 = "When the machine is also"
        sub2 = "your customer"
        d1 = "ALG"
        d1b = "formal purchase"
        d2 = "BLG"
        d2b = "construction"
        d3 = "PLG 3.0"
        d3b = "headless product"
        gap_label = "the gap between existing boundaries"
        footer = "Matheus Ramos · with Supabase and shadcn/ui cases, GEO data, and token economics"

    body = []
    # fundo: navy profundo com faixa diagonal sutil
    body.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{NAVY_DEEP}"/>')
    # textura geometrica sutil: linhas diagonais no canto superior direito
    for i in range(14):
        x0 = W - 620 + i * 46
        body.append(f'<line x1="{x0}" y1="0" x2="{x0 + 340}" y2="340" stroke="{ACCENT}" stroke-opacity="0.14" stroke-width="2"/>')
    # barra de identidade na esquerda
    body.append(f'<rect x="0" y="0" width="14" height="{H}" fill="{ACCENT}"/>')

    # kicker
    body.append(txt(120, 200, kicker, 26, "700", ACCENT_LIGHT, spacing="4"))
    body.append(f'<line x1="120" y1="228" x2="470" y2="228" stroke="{ACCENT}" stroke-width="3"/>')

    # titulo
    body.append(txt(114, 340, title1, 104, "700", WHITE))
    body.append(txt(118, 430, sub1, 54, "400", GRAY_LIGHT))
    body.append(txt(118, 494, sub2, 54, "400", GRAY_LIGHT))

    # motivo grafico: tres blocos, o do meio destacado (o vao)
    blocks_y = 640
    bw, bh, gap = 420, 210, 60
    total = 3 * bw + 2 * gap
    x0 = 120

    # bloco 1
    body.append(f'<rect x="{x0}" y="{blocks_y}" width="{bw}" height="{bh}" rx="14" fill="none" stroke="{GRAY_LIGHT}" stroke-opacity="0.45" stroke-width="2"/>')
    body.append(txt(x0 + bw / 2, blocks_y + 95, d1, 44, "700", GRAY_LIGHT, "middle"))
    body.append(txt(x0 + bw / 2, blocks_y + 145, d1b, 24, "400", GRAY_LIGHT, "middle", style="italic"))

    # bloco 2 (BLG, destacado)
    x2 = x0 + bw + gap
    body.append(f'<rect x="{x2 - 8}" y="{blocks_y - 26}" width="{bw + 16}" height="{bh + 52}" rx="16" fill="{ACCENT}" fill-opacity="0.18" stroke="{ACCENT_LIGHT}" stroke-width="3.5"/>')
    body.append(txt(x2 + bw / 2, blocks_y + 88, d2, 58, "700", WHITE, "middle"))
    body.append(txt(x2 + bw / 2, blocks_y + 142, d2b, 26, "400", ACCENT_LIGHT, "middle", style="italic"))

    # bloco 3
    x3 = x2 + bw + gap
    body.append(f'<rect x="{x3}" y="{blocks_y}" width="{bw}" height="{bh}" rx="14" fill="none" stroke="{GRAY_LIGHT}" stroke-opacity="0.45" stroke-width="2"/>')
    body.append(txt(x3 + bw / 2, blocks_y + 95, d3, 44, "700", GRAY_LIGHT, "middle"))
    body.append(txt(x3 + bw / 2, blocks_y + 145, d3b, 24, "400", GRAY_LIGHT, "middle", style="italic"))

    # conectores tracejados
    cy = blocks_y + bh / 2
    body.append(f'<line x1="{x0 + bw}" y1="{cy}" x2="{x2 - 8}" y2="{cy}" stroke="{ACCENT_LIGHT}" stroke-width="2.5" stroke-dasharray="7,7"/>')
    body.append(f'<line x1="{x2 + bw + 8}" y1="{cy}" x2="{x3}" y2="{cy}" stroke="{ACCENT_LIGHT}" stroke-width="2.5" stroke-dasharray="7,7"/>')

    # legenda do vao
    body.append(txt(x2 + bw / 2, blocks_y + bh + 76, gap_label, 24, "400", GRAY_LIGHT, "middle", style="italic"))

    # rodape
    body.append(f'<line x1="120" y1="{H - 90}" x2="{W - 120}" y2="{H - 90}" stroke="{ACCENT}" stroke-opacity="0.5" stroke-width="1.5"/>')
    body.append(txt(120, H - 48, footer, 24, "400", GRAY_LIGHT))

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{chr(10).join(body)}
</svg>'''
    return svg


for lang, name in [("pt", "v0-capa-pt"), ("en", "v0-cover-en")]:
    svg = build_cover(lang)
    p = os.path.join(OUT, f"{name}.svg")
    with open(p, "w", encoding="utf-8") as f:
        f.write(svg)
    cairosvg.svg2png(url=p, write_to=os.path.join(OUT, f"{name}.png"), scale=1.5)
    print("ok:", name)
