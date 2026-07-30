#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capa da parte 2 — 1920x1080."""
import cairosvg, os

OUT = os.path.dirname(os.path.abspath(__file__))
FONT = "Liberation Sans, Arial, sans-serif"
NAVY_DEEP = "#101A30"
GRAY_LIGHT = "#AEB6C2"
ACCENT = "#2F5D8A"
ACCENT_LIGHT = "#6E9CC4"
AMBER = "#C68B3E"
WHITE = "#FFFFFF"


def txt(x, y, s, size=16, weight="400", fill=NAVY_DEEP, anchor="start", style="normal", sp=None):
    spa = f' letter-spacing="{sp}"' if sp else ""
    s = str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'font-style="{style}" fill="{fill}" text-anchor="{anchor}"{spa}>{s}</text>')


W, H = 1920, 1080
b = [f'<rect width="{W}" height="{H}" fill="{NAVY_DEEP}"/>']
for i in range(14):
    x0 = W - 620 + i * 46
    b.append(f'<line x1="{x0}" y1="0" x2="{x0+340}" y2="340" stroke="{ACCENT}" stroke-opacity="0.14" stroke-width="2"/>')
b.append(f'<rect x="0" y="0" width="14" height="{H}" fill="{ACCENT}"/>')

b.append(txt(120, 196, "BUILDER-LED GROWTH — PARTE 2 DE 9", 26, "700", ACCENT_LIGHT, sp="4"))
b.append(f'<line x1="120" y1="224" x2="560" y2="224" stroke="{ACCENT}" stroke-width="3"/>')

b.append(txt(114, 336, "Como a máquina decide,", 88, "700", WHITE))
b.append(txt(114, 436, "e onde ela para de decidir", 88, "700", WHITE))
b.append(txt(118, 512, "O mecanismo, o preço e o que medir", 46, "400", GRAY_LIGHT))

# três estágios com o limite
bw, bh, gap = 400, 150, 46
y = 660
labels = [("CANDIDATURA", "conhecimento paramétrico"),
          ("RECOMENDAÇÃO", "recuperação + comunidade"),
          ("ADOÇÃO", "atrito de execução")]
for i, (t, s) in enumerate(labels):
    x = 120 + i * (bw + gap)
    hl = (i == 2)
    b.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="14" fill="{ACCENT if hl else "none"}" '
             f'fill-opacity="{0.18 if hl else 0}" stroke="{ACCENT_LIGHT if hl else GRAY_LIGHT}" '
             f'stroke-opacity="{1 if hl else 0.45}" stroke-width="{3 if hl else 2}"/>')
    b.append(txt(x + bw / 2, y + 62, t, 30, "700", WHITE if hl else GRAY_LIGHT, "middle"))
    b.append(txt(x + bw / 2, y + 102, s, 21, "400", ACCENT_LIGHT if hl else GRAY_LIGHT, "middle", style="italic"))
    if i < 2:
        cy = y + bh / 2
        b.append(f'<line x1="{x+bw+8}" y1="{cy}" x2="{x+bw+gap-8}" y2="{cy}" stroke="{ACCENT_LIGHT}" '
                 f'stroke-width="2.5" stroke-dasharray="7,7"/>')

# faixa do limite
ly = y + bh + 44
b.append(f'<rect x="120" y="{ly}" width="{3*bw+2*gap}" height="76" rx="12" fill="{AMBER}" fill-opacity="0.16" stroke="{AMBER}" stroke-width="2"/>')
b.append(txt(150, ly + 48, "O limite da tese é o boleto — o BLG decide quem entra, a economia humana decide quem fica.", 27, "400", WHITE))

b.append(f'<line x1="120" y1="{H-90}" x2="{W-120}" y2="{H-90}" stroke="{ACCENT}" stroke-opacity="0.5" stroke-width="1.5"/>')
b.append(txt(120, H - 48, "Matheus Ramos · com Supabase, shadcn/ui, Drizzle, Better Auth, Firecrawl e Tailwind", 24, "400", GRAY_LIGHT))

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(b)}</svg>'
p = os.path.join(OUT, "p2-capa-pt.svg")
open(p, "w", encoding="utf-8").write(svg)
cairosvg.svg2png(url=p, write_to=os.path.join(OUT, "p2-capa-pt.png"), scale=1.5)
print("ok: p2-capa-pt")
