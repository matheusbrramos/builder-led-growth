#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera os 5 recursos visuais da parte 1 do artigo Builder-Led Growth (BLG),
em PT-BR e EN, como SVG + PNG (alta resolucao, prontos pra upload no
editor de artigo do LinkedIn).
"""
import cairosvg
import os

OUT = os.path.dirname(os.path.abspath(__file__))

FONT = "Liberation Sans, Arial, sans-serif"
FONT_MONO = "Liberation Mono, Consolas, monospace"

# Paleta soubria, estilo relatorio de consultoria
NAVY = "#16213E"        # texto primario / titulos
GRAY = "#5B6472"        # texto secundario
GRAY_LIGHT = "#8B93A1"  # texto terciario / legendas
BG = "#FFFFFF"
PANEL = "#F7F8FA"       # fundo de card neutro
BORDER = "#DEE2E7"
ACCENT = "#2F5D8A"      # azul acinzentado -- identidade BLG
ACCENT_SOFT = "#E7EEF4" # fundo suave do accent
AMBER = "#B8792E"       # destaque secundario (usado com moderacao)
AMBER_SOFT = "#F5EBDD"
GOOD_BAR = "#2F5D8A"
MUTED_BAR = "#C7CDD5"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def txt(x, y, s, size=16, weight="400", fill=NAVY, anchor="start", family=FONT, style="normal"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" fill="{fill}" '
            f'text-anchor="{anchor}">{esc(s)}</text>')


def multiline(x, y, lines, size=16, weight="400", fill=GRAY, line_height=None, anchor="start", family=FONT, style="normal"):
    lh = line_height or size * 1.55
    out = []
    for i, l in enumerate(lines):
        out.append(txt(x, y + i * lh, l, size, weight, fill, anchor, family, style))
    return "\n".join(out)


def rect(x, y, w, h, fill, stroke=None, stroke_width=1, rx=10):
    s = f' stroke="{stroke}" stroke-width="{stroke_width}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}/>'

def line(x1, y1, x2, y2, stroke=BORDER, width=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"{d}/>'

def circle(cx, cy, r, fill, stroke=None, stroke_width=1):
    s = f' stroke="{stroke}" stroke-width="{stroke_width}"' if stroke else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}/>'


def svg_doc(w, h, body, bg=BG):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<rect x="0" y="0" width="{w}" height="{h}" fill="{bg}"/>
{body}
</svg>'''


def save(name, svg_str, scale=2):
    svg_path = os.path.join(OUT, f"{name}.svg")
    png_path = os.path.join(OUT, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_str)
    cairosvg.svg2png(url=svg_path, write_to=png_path, scale=scale)
    print("ok:", name)


def kicker_title(t, subtitle_y_gap=34):
    parts = []
    parts.append(rect(0, 0, 8, 700, ACCENT, rx=0))  # overridden per-canvas below if needed
    return parts


# ---------------------------------------------------------------------------
# V1 -- Mapa de posicionamento: ALG / BLG / PLG 3.0
# ---------------------------------------------------------------------------
def build_v1(lang):
    W, H = 1600, 760
    t = TEXTS[lang]["v1"]
    body = []
    body.append(rect(0, 0, 10, H, ACCENT, rx=0))
    body.append(txt(60, 66, t["kicker"], 14, "700", ACCENT, family=FONT))
    body.append(txt(60, 104, t["title"], 30, "700", NAVY))
    body.append(txt(60, 136, t["subtitle"], 17, "400", GRAY, style="italic"))

    box_y, box_h = 200, 330
    box_w, gap = 460, 30
    x1 = 60
    x2 = x1 + box_w + gap
    x3 = x2 + box_w + gap

    # Box 1 -- ALG
    body.append(rect(x1, box_y, box_w, box_h, PANEL, BORDER, 1))
    body.append(rect(x1, box_y, box_w, 6, GRAY_LIGHT, rx=0))
    body.append(txt(x1 + 26, box_y + 46, t["b1_tag"], 12, "700", GRAY, family=FONT))
    body.append(txt(x1 + 26, box_y + 78, t["b1_title"], 20, "700", NAVY))
    body.append(multiline(x1 + 26, box_y + 116, t["b1_lines"], 15, "400", GRAY, 27))
    body.append(txt(x1 + 26, box_y + box_h - 24, t["b1_who"], 13, "700", GRAY_LIGHT, style="italic"))

    # Box 2 -- BLG (destacado)
    body.append(rect(x2, box_y - 14, box_w, box_h + 28, ACCENT_SOFT, ACCENT, 2))
    body.append(rect(x2, box_y - 14, box_w, 8, ACCENT, rx=0))
    body.append(txt(x2 + 26, box_y - 14 + 48, t["b2_tag"], 12, "700", ACCENT, family=FONT))
    body.append(txt(x2 + 26, box_y - 14 + 82, t["b2_title"], 22, "700", NAVY))
    body.append(multiline(x2 + 26, box_y - 14 + 122, t["b2_lines"], 15.5, "400", NAVY, 28))
    body.append(txt(x2 + 26, box_y - 14 + box_h + 28 - 24, t["b2_who"], 13, "700", ACCENT, style="italic"))

    # Box 3 -- PLG 3.0
    body.append(rect(x3, box_y, box_w, box_h, PANEL, BORDER, 1))
    body.append(rect(x3, box_y, box_w, 6, GRAY_LIGHT, rx=0))
    body.append(txt(x3 + 26, box_y + 46, t["b3_tag"], 12, "700", GRAY, family=FONT))
    body.append(txt(x3 + 26, box_y + 78, t["b3_title"], 20, "700", NAVY))
    body.append(multiline(x3 + 26, box_y + 116, t["b3_lines"], 15, "400", GRAY, 27))
    body.append(txt(x3 + 26, box_y + box_h - 24, t["b3_who"], 13, "700", GRAY_LIGHT, style="italic"))

    # conectores com nota de sobreposicao honesta
    mid_y = box_y + box_h + 55
    body.append(line(x1 + box_w, box_y + box_h / 2, x2, box_y + box_h / 2, GRAY_LIGHT, 1.5, "4,4"))
    body.append(line(x2 + box_w, box_y + box_h / 2, x3, box_y + box_h / 2, GRAY_LIGHT, 1.5, "4,4"))

    note_y = box_y + box_h + 40
    for i, l in enumerate(t["overlap1"]):
        body.append(txt(x1 + box_w + gap / 2, note_y + i * 18, l, 12.5, "400", GRAY_LIGHT, "middle", style="italic"))
    for i, l in enumerate(t["overlap2"]):
        body.append(txt(x2 + box_w + gap / 2, note_y + i * 18, l, 12.5, "400", GRAY_LIGHT, "middle", style="italic"))

    body.append(line(60, H - 70, W - 60, H - 70, BORDER, 1))
    body.append(txt(60, H - 44, t["footer"], 12.5, "400", GRAY_LIGHT))

    return svg_doc(W, H, "\n".join(body))


# ---------------------------------------------------------------------------
# V2 -- Os quatro pilares
# ---------------------------------------------------------------------------
def build_v2(lang):
    W, H = 1600, 820
    t = TEXTS[lang]["v2"]
    body = []
    body.append(rect(0, 0, 10, H, ACCENT, rx=0))
    body.append(txt(60, 66, t["kicker"], 14, "700", ACCENT))
    body.append(txt(60, 104, t["title"], 30, "700", NAVY))
    body.append(txt(60, 136, t["subtitle"], 17, "400", GRAY, style="italic"))

    cols = t["pillars"]
    col_w, gap = 358, 26
    x0 = 60
    box_y, box_h = 200, 540
    for i, p in enumerate(cols):
        x = x0 + i * (col_w + gap)
        body.append(rect(x, box_y, col_w, box_h, PANEL, BORDER, 1))
        body.append(circle(x + 40, box_y + 46, 20, ACCENT))
        body.append(txt(x + 40, box_y + 53, str(i + 1), 18, "700", "#FFFFFF", "middle"))
        body.append(multiline(x + 26, box_y + 100, p["title_lines"], 18.5, "700", NAVY, 25))
        ty = box_y + 100 + len(p["title_lines"]) * 25 + 22
        body.append(multiline(x + 26, ty, p["desc_lines"], 14, "400", GRAY, 22, family=FONT))
        # stat callout
        sy = box_y + box_h - 118
        body.append(line(x + 26, sy, x + col_w - 26, sy, BORDER, 1))
        body.append(multiline(x + 26, sy + 34, p["stat_lines"], 15.5, "700", ACCENT, 22))
        body.append(txt(x + 26, box_y + box_h - 18, p["stat_src"], 11.5, "400", GRAY_LIGHT, style="italic"))

    body.append(line(60, H - 66, W - 60, H - 66, BORDER, 1))
    body.append(txt(60, H - 40, t["footer"], 12.5, "400", GRAY_LIGHT))
    return svg_doc(W, H, "\n".join(body))


# ---------------------------------------------------------------------------
# V3 -- GEO: como a IA decide o que citar (dois paineis de barras)
# ---------------------------------------------------------------------------
def hbar_panel(x, y, w, h, title, items, max_val, unit, accent=ACCENT, base=MUTED_BAR):
    """items: list of (label, value, is_accent_bool, value_label)"""
    out = []
    out.append(txt(x, y, title, 19, "700", NAVY))
    bar_x = x
    bar_w_max = w
    row_h = 74
    top = y + 40
    for i, (label, val, is_accent, vlabel) in enumerate(items):
        ry = top + i * row_h
        out.append(txt(bar_x, ry, label, 15, "400", GRAY))
        track_y = ry + 12
        track_h = 30
        out.append(rect(bar_x, track_y, bar_w_max, track_h, "#EEF0F3", rx=6))
        bw = max(6, bar_w_max * (val / max_val))
        out.append(rect(bar_x, track_y, bw, track_h, accent if is_accent else base, rx=6))
        out.append(txt(bar_x + bw + 14, track_y + 21, vlabel, 16, "700", NAVY if is_accent else GRAY))
    return "\n".join(out)


def build_v3(lang):
    W, H = 1600, 760
    t = TEXTS[lang]["v3"]
    body = []
    body.append(rect(0, 0, 10, H, ACCENT, rx=0))
    body.append(txt(60, 66, t["kicker"], 14, "700", ACCENT))
    body.append(txt(60, 104, t["title"], 30, "700", NAVY))
    body.append(txt(60, 136, t["subtitle"], 17, "400", GRAY, style="italic"))

    panel_y, panel_h = 190, 420
    panel_w, gap = 700, 60
    x1 = 60
    x2 = x1 + panel_w + gap

    body.append(rect(x1, panel_y, panel_w, panel_h, PANEL, BORDER, 1))
    body.append(hbar_panel(x1 + 34, panel_y + 60, panel_w - 68, panel_h - 100,
                            t["p1_title"], t["p1_items"], t["p1_max"], "%"))
    body.append(multiline(x1 + 34, panel_y + panel_h - 22, [t["p1_src"]], 11.5, "400", GRAY_LIGHT, style="italic"))

    body.append(rect(x2, panel_y, panel_w, panel_h, PANEL, BORDER, 1))
    body.append(hbar_panel(x2 + 34, panel_y + 60, panel_w - 68, panel_h - 100,
                            t["p2_title"], t["p2_items"], t["p2_max"], "%"))
    body.append(multiline(x2 + 34, panel_y + panel_h - 22, [t["p2_src"]], 11.5, "400", GRAY_LIGHT, style="italic"))

    body.append(txt(60, panel_y + panel_h + 56, t["callout"], 16, "700", ACCENT))
    body.append(line(60, H - 66, W - 60, H - 66, BORDER, 1))
    body.append(txt(60, H - 40, t["footer"], 12.5, "400", GRAY_LIGHT))
    return svg_doc(W, H, "\n".join(body))


# ---------------------------------------------------------------------------
# V4 -- Economia de token: CLI vs MCP
# ---------------------------------------------------------------------------
def build_v4(lang):
    W, H = 1600, 760
    t = TEXTS[lang]["v4"]
    body = []
    body.append(rect(0, 0, 10, H, ACCENT, rx=0))
    body.append(txt(60, 66, t["kicker"], 14, "700", ACCENT))
    body.append(txt(60, 104, t["title"], 30, "700", NAVY))
    body.append(txt(60, 136, t["subtitle"], 17, "400", GRAY, style="italic"))

    # painel esquerdo: barras em escala log (representacao proporcional simplificada)
    panel_y, panel_h = 190, 420
    left_w = 780
    body.append(rect(60, panel_y, left_w, panel_h, PANEL, BORDER, 1))
    body.append(txt(60 + 34, panel_y + 52, t["chart_title"], 19, "700", NAVY))

    # duas barras: CLI curta, MCP longa (proporcao ~1:6 visual, nao literal, com valores reais no rotulo)
    bx = 60 + 34
    bw_max = left_w - 68 - 220
    bar_y1 = panel_y + 110
    bar_y2 = panel_y + 200
    cli_frac = 0.10   # representacao visual comprimida, valor real no rotulo
    mcp_frac = 1.0
    body.append(txt(bx, bar_y1 - 12, t["cli_label"], 15, "400", GRAY))
    body.append(rect(bx, bar_y1, bw_max, 34, "#EEF0F3", rx=6))
    body.append(rect(bx, bar_y1, max(10, bw_max * cli_frac), 34, GOOD_BAR, rx=6))
    body.append(txt(bx + max(10, bw_max * cli_frac) + 16, bar_y1 + 24, t["cli_value"], 17, "700", NAVY))

    body.append(txt(bx, bar_y2 - 12, t["mcp_label"], 15, "400", GRAY))
    body.append(rect(bx, bar_y2, bw_max, 34, "#EEF0F3", rx=6))
    body.append(rect(bx, bar_y2, bw_max * mcp_frac, 34, AMBER, rx=6))
    body.append(txt(bx + bw_max * mcp_frac + 16, bar_y2 + 24, t["mcp_value"], 17, "700", NAVY))

    body.append(txt(bx, bar_y2 + 80, t["multiplier"], 20, "700", AMBER))
    body.append(multiline(bx, bar_y2 + 112, t["example_lines"], 13.5, "400", GRAY_LIGHT, 20, style="italic"))

    # painel direito: divisao recomendada 80/20
    right_x = 60 + left_w + 40
    right_w = W - 60 - right_x
    body.append(rect(right_x, panel_y, right_w, panel_h, PANEL, BORDER, 1))
    body.append(txt(right_x + 30, panel_y + 52, t["split_title"], 19, "700", NAVY))

    cy = panel_y + panel_h / 2 + 20
    cx = right_x + right_w / 2
    r = 95
    # donut simplificado: dois arcos 80/20 via path
    import math
    def arc_path(cx, cy, r, start_deg, end_deg):
        s = math.radians(start_deg - 90)
        e = math.radians(end_deg - 90)
        x1 = cx + r * math.cos(s)
        y1 = cy + r * math.sin(s)
        x2 = cx + r * math.cos(e)
        y2 = cy + r * math.sin(e)
        large = 1 if (end_deg - start_deg) > 180 else 0
        return f"M{cx},{cy} L{x1:.2f},{y1:.2f} A{r},{r} 0 {large} 1 {x2:.2f},{y2:.2f} Z"

    body.append(f'<path d="{arc_path(cx, cy, r, 0, 288)}" fill="{GOOD_BAR}"/>')
    body.append(f'<path d="{arc_path(cx, cy, r, 288, 360)}" fill="{AMBER}"/>')
    body.append(circle(cx, cy, r * 0.55, "#FFFFFF"))
    body.append(txt(cx, cy - 6, "80% / 20%", 20, "700", NAVY, "middle"))
    body.append(txt(cx, cy + 20, t["split_center"], 12.5, "400", GRAY, "middle"))

    legend_y = panel_y + panel_h - 78
    body.append(rect(right_x + 30, legend_y, 16, 16, GOOD_BAR, rx=3))
    body.append(txt(right_x + 54, legend_y + 13, t["split_cli"], 13.5, "400", GRAY))
    body.append(rect(right_x + 30, legend_y + 30, 16, 16, AMBER, rx=3))
    body.append(txt(right_x + 54, legend_y + 43, t["split_mcp"], 13.5, "400", GRAY))

    body.append(line(60, H - 66, W - 60, H - 66, BORDER, 1))
    body.append(txt(60, H - 40, t["footer"], 12.5, "400", GRAY_LIGHT))
    return svg_doc(W, H, "\n".join(body))


# ---------------------------------------------------------------------------
# V5 -- Provas no mundo real: Supabase & shadcn/ui
# ---------------------------------------------------------------------------
def build_v5(lang):
    W, H = 1600, 800
    t = TEXTS[lang]["v5"]
    body = []
    body.append(rect(0, 0, 10, H, ACCENT, rx=0))
    body.append(txt(60, 66, t["kicker"], 14, "700", ACCENT))
    body.append(txt(60, 104, t["title"], 30, "700", NAVY))
    body.append(txt(60, 136, t["subtitle"], 17, "400", GRAY, style="italic"))

    card_y, card_h = 190, 520
    card_w, gap = 700, 60
    x1 = 60
    x2 = x1 + card_w + gap

    for x, c in [(x1, t["c1"]), (x2, t["c2"])]:
        body.append(rect(x, card_y, card_w, card_h, PANEL, BORDER, 1))
        body.append(rect(x, card_y, card_w, 6, ACCENT, rx=0))
        body.append(txt(x + 30, card_y + 56, c["name"], 24, "700", NAVY))
        body.append(txt(x + 30, card_y + 84, c["tag"], 14, "400", GRAY_LIGHT, style="italic"))

        sy = card_y + 130
        stat_h = 92
        for j, (val, lab) in enumerate(c["stats"]):
            yy = sy + j * stat_h
            body.append(txt(x + 30, yy, val, 30, "700", ACCENT))
            body.append(multiline(x + 30, yy + 26, lab, 13.5, "400", GRAY, 19))
            if j < len(c["stats"]) - 1:
                body.append(line(x + 30, yy + stat_h - 16, x + card_w - 30, yy + stat_h - 16, BORDER, 1))
        body.append(txt(x + 30, card_y + card_h - 20, c["src"], 11.5, "400", GRAY_LIGHT, style="italic"))

    body.append(line(60, H - 66, W - 60, H - 66, BORDER, 1))
    body.append(txt(60, H - 40, t["footer"], 12.5, "400", GRAY_LIGHT))
    return svg_doc(W, H, "\n".join(body))


# ===========================================================================
# TEXTOS (PT-BR / EN)
# ===========================================================================
TEXTS = {
"pt": {
    "v1": {
        "kicker": "POSICIONAMENTO DA TESE",
        "title": "Onde o Builder-Led Growth se encaixa",
        "subtitle": "Duas fronteiras já mapeadas por outros — e o vão real entre elas",
        "b1_tag": "JÁ EXISTE — COMPRA FORMAL",
        "b1_title": "ALG — Agent-Led Growth",
        "b1_lines": [
            "Agente contratado avalia e",
            "compra em nome de um comprador",
            "Funil: pesquisa -> comparação ->",
            "teste -> decisão -> compra",
            "Pago por resultado verificado",
        ],
        "b1_who": "quem decide: um comprador",
        "b2_tag": "O VÃO — ESTA TESE",
        "b2_title": "Builder-Led Growth (BLG)",
        "b2_lines": [
            "Agente está construindo",
            "algo diferente",
            "Recomenda ferramenta de terceiro",
            "como efeito colateral instrumental",
            "Sem comprador formal, sem funil",
        ],
        "b2_who": "quem decide: um agente construtor",
        "b3_tag": "JÁ EXISTE — PRODUTO PRÓPRIO",
        "b3_title": "PLG 3.0 / Headless (Wes Bush)",
        "b3_lines": [
            "Seu próprio produto operado",
            "por um agente sem interface",
            "Questão de design do produto",
            "que está sendo usado",
            "Ex.: Netlify, 80% signups via agente",
        ],
        "b3_who": "quem decide: o seu produto",
        "overlap1": ["sobreposição parcial reconhecida", "(estágio de avaliação do ALG)"],
        "overlap2": ["infraestrutura compartilhada", "(AGENTS.md, MCP, Agent Skills)"],
        "footer": "Fontes: Agent-Led Strategy (agentledstrategy.com/thesis) · Wes Bush via Userpilot (userpilot.com/blog/product-led-growth) · análise completa e ressalvas no artigo.",
    },
    "v2": {
        "kicker": "OS QUATRO PILARES",
        "title": "O que um produto precisa fazer bem",
        "subtitle": "Quatro alavancas independentes que se reforçam — não um canal a mais",
        "footer": "Fontes citadas individualmente no artigo completo (Digidop, Connor Kimball, earezki.com, Firecrawl, Towards AI).",
        "pillars": [
            {
                "title_lines": ["Legibilidade", "por máquina"],
                "desc_lines": ["Documentação, APIs e conteúdo", "estruturados pra serem lidos", "por um agente antes de", "serem lidos por um humano."],
                "stat_lines": ["16% -> 54%", "citação correta (GPT-4)"],
                "stat_src": "com dados estruturados · Digidop",
            },
            {
                "title_lines": ["Acessibilidade", "operacional"],
                "desc_lines": ["MCP, CLI e SDK não são", "intercambiáveis — a escolha", "certa é por ferramenta,", "não por sistema."],
                "stat_lines": ["até 32x", "mais tokens via MCP"],
                "stat_src": "vs. CLI equivalente · earezki.com",
            },
            {
                "title_lines": ["Comunidade e", "sinal de validação"],
                "desc_lines": ["Alimenta dois caminhos: entrar", "no dado de treino (lento) e", "virar conteúdo comparativo", "de terceiros (rápido)."],
                "stat_lines": ["32,5%", "das citações de IA"],
                "stat_src": "vem de conteúdo de terceiros · Connor Kimball",
            },
            {
                "title_lines": ["Confiança e", "segurança do modelo"],
                "desc_lines": ["Não é segurança da informação —", "é o quanto o agente confia em", "agir sem checagem humana", "constante."],
                "stat_lines": ["fronteira", "mais delicada dos 4"],
                "stat_src": "sem métrica pública consolidada ainda",
            },
        ],
    },
    "v3": {
        "kicker": "GEO — GENERATIVE ENGINE OPTIMIZATION",
        "title": "Como a IA decide o que citar",
        "subtitle": "Dois achados que mudam onde vale investir conteúdo",
        "p1_title": "Taxa de citação correta (GPT-4)",
        "p1_max": 54,
        "p1_items": [
            ("Sem dados estruturados", 16, False, "16%"),
            ("Com dados estruturados (schema.org/JSON-LD)", 54, True, "54%"),
        ],
        "p1_src": "Fonte: Digidop (digidop.com)",
        "p2_title": "Origem das citações de IA",
        "p2_max": 32.5,
        "p2_items": [
            ("Páginas comerciais próprias", 5, False, "< 5%"),
            ("Conteúdo comparativo de terceiros", 32.5, True, "32,5%"),
        ],
        "p2_src": "Fonte: Connor Kimball (connorkimball.com)",
        "callout": "Aparecer bem numa comparação de terceiros pesa mais de 6x do que caprichar na própria landing page.",
        "footer": "Dados citados com fonte individual no artigo completo — não são medição própria.",
    },
    "v4": {
        "kicker": "PILAR 2 — ACESSIBILIDADE OPERACIONAL",
        "title": "Economia de token: CLI vs. MCP",
        "subtitle": "A escolha certa é por ferramenta, não por sistema inteiro",
        "chart_title": "Exemplo citado: checar a linguagem de um repositório",
        "cli_label": "Via CLI",
        "cli_value": "1.365 tokens",
        "mcp_label": "Via MCP",
        "mcp_value": "44.026 tokens",
        "multiplier": "~32x mais caro via MCP",
        "example_lines": ["Overhead de schema JSON injetado", "a cada turno de conversa.", "Fonte: earezki.com"],
        "split_title": "Padrão observado (ex.: Claude Code)",
        "split_center": "CLI / MCP",
        "split_cli": "CLI — piso padrão (~80% das tarefas)",
        "split_mcp": "MCP — auth, estado, sem CLI (~20%)",
        "footer": "\"Code execution with MCP\" (Anthropic) reduz consumo de token em até 98% quando aplicável. Fonte: Towards AI.",
    },
    "v5": {
        "kicker": "CASOS REAIS",
        "title": "Duas provas, duas camadas de stack",
        "subtitle": "SaaS financiado vs. open source sem funding direto — o mesmo padrão se repetindo",
        "footer": "Fontes individuais no artigo completo (Let's Data Science, SiliconANGLE, Supabase Blog, ShadcnDeck, Vibe Coder Blog).",
        "c1": {
            "name": "Supabase",
            "tag": "backend / banco de dados — SaaS financiado",
            "stats": [
                ("US$500M", ["Rodada levantada em junho de 2026,", "avaliação de US$10,5 bilhões"]),
                ("60%+", ["dos novos bancos de dados criados", "na plataforma via ferramentas de IA"]),
                ("600%", ["alta ano-contra-ano em bancos", "de dados criados via Claude Code"]),
            ],
            "src": "Let's Data Science · SiliconANGLE · Supabase Blog",
        },
        "c2": {
            "name": "shadcn/ui",
            "tag": "componentes de interface — open source",
            "stats": [
                ("109 mil+", ["estrelas no GitHub em menos", "de 3 anos, sem funding direto"]),
                ("5", ["ferramentas de fornecedores", "independentes geram por padrão"]),
                ("US$0", ["gastos em vendas — tração vem", "de estar no dado de treino"]),
            ],
            "src": "ShadcnDeck · Vibe Coder Blog",
        },
    },
},
"en": {
    "v1": {
        "kicker": "THESIS POSITIONING",
        "title": "Where Builder-Led Growth fits",
        "subtitle": "Two boundaries already mapped by others — and the real gap between them",
        "b1_tag": "ALREADY EXISTS — FORMAL PURCHASE",
        "b1_title": "ALG — Agent-Led Growth",
        "b1_lines": [
            "A hired agent evaluates and",
            "buys on a buyer's behalf",
            "Funnel: research -> compare ->",
            "test -> decide -> purchase",
            "Paid on verified outcomes",
        ],
        "b1_who": "who decides: a buyer",
        "b2_tag": "THE GAP — THIS THESIS",
        "b2_title": "Builder-Led Growth (BLG)",
        "b2_lines": [
            "Agent is busy building",
            "something else",
            "Recommends a third-party tool",
            "as an instrumental side effect",
            "No formal buyer, no funnel",
        ],
        "b2_who": "who decides: a building agent",
        "b3_tag": "ALREADY EXISTS — YOUR OWN PRODUCT",
        "b3_title": "PLG 3.0 / Headless (Wes Bush)",
        "b3_lines": [
            "Your own product operated",
            "by an agent without an interface",
            "Design question about the",
            "product being used",
            "Ex.: Netlify, 80% signups via agent",
        ],
        "b3_who": "who decides: your product",
        "overlap1": ["partial overlap acknowledged", "(ALG's evaluation stage)"],
        "overlap2": ["shared infrastructure", "(AGENTS.md, MCP, Agent Skills)"],
        "footer": "Sources: Agent-Led Strategy (agentledstrategy.com/thesis) · Wes Bush via Userpilot (userpilot.com/blog/product-led-growth) · full analysis and caveats in the piece.",
    },
    "v2": {
        "kicker": "THE FOUR PILLARS",
        "title": "What a product needs to do well",
        "subtitle": "Four independent, mutually reinforcing levers — not one more channel",
        "footer": "Sources cited individually in the full piece (Digidop, Connor Kimball, earezki.com, Firecrawl, Towards AI).",
        "pillars": [
            {
                "title_lines": ["Machine", "legibility"],
                "desc_lines": ["Documentation, APIs, and content", "structured to be read by an", "agent before being read", "by a human."],
                "stat_lines": ["16% -> 54%", "correct citation (GPT-4)"],
                "stat_src": "with structured data · Digidop",
            },
            {
                "title_lines": ["Operational", "accessibility"],
                "desc_lines": ["MCP, CLI, and SDK aren't", "interchangeable — the right", "choice is per tool,", "not per system."],
                "stat_lines": ["up to 32x", "more tokens via MCP"],
                "stat_src": "vs. equivalent CLI · earezki.com",
            },
            {
                "title_lines": ["Community and", "validation signal"],
                "desc_lines": ["Feeds two paths: entering", "training data (slow) and", "becoming third-party", "comparative content (fast)."],
                "stat_lines": ["32.5%", "of AI citations"],
                "stat_src": "come from third-party content · Connor Kimball",
            },
            {
                "title_lines": ["Model trust", "and safety"],
                "desc_lines": ["Not information security —", "it's how much the agent trusts", "acting without constant", "human checking."],
                "stat_lines": ["most delicate", "frontier of the four"],
                "stat_src": "no consolidated public metric yet",
            },
        ],
    },
    "v3": {
        "kicker": "GEO — GENERATIVE ENGINE OPTIMIZATION",
        "title": "How AI decides what to cite",
        "subtitle": "Two findings that change where content investment pays off",
        "p1_title": "Correct citation rate (GPT-4)",
        "p1_max": 54,
        "p1_items": [
            ("Without structured data", 16, False, "16%"),
            ("With structured data (schema.org/JSON-LD)", 54, True, "54%"),
        ],
        "p1_src": "Source: Digidop (digidop.com)",
        "p2_title": "Where AI citations come from",
        "p2_max": 32.5,
        "p2_items": [
            ("Own commercial pages", 5, False, "< 5%"),
            ("Third-party comparative content", 32.5, True, "32.5%"),
        ],
        "p2_src": "Source: Connor Kimball (connorkimball.com)",
        "callout": "Showing up well in a third-party comparison outweighs polishing your own landing page by more than 6x.",
        "footer": "Data cited with individual sources in the full piece — not our own measurement.",
    },
    "v4": {
        "kicker": "PILLAR 2 — OPERATIONAL ACCESSIBILITY",
        "title": "Token economics: CLI vs. MCP",
        "subtitle": "The right choice is per tool, not per whole system",
        "chart_title": "Cited example: checking a repository's language",
        "cli_label": "Via CLI",
        "cli_value": "1,365 tokens",
        "mcp_label": "Via MCP",
        "mcp_value": "44,026 tokens",
        "multiplier": "~32x more expensive via MCP",
        "example_lines": ["JSON schema overhead injected", "on every conversation turn.", "Source: earezki.com"],
        "split_title": "Observed pattern (e.g., Claude Code)",
        "split_center": "CLI / MCP",
        "split_cli": "CLI — default floor (~80% of tasks)",
        "split_mcp": "MCP — auth, state, no CLI (~20%)",
        "footer": "\"Code execution with MCP\" (Anthropic) cuts token use by up to 98% where applicable. Source: Towards AI.",
    },
    "v5": {
        "kicker": "REAL CASES",
        "title": "Two proofs, two layers of the stack",
        "subtitle": "Funded SaaS vs. unfunded open source — the same pattern repeating",
        "footer": "Individual sources in the full piece (Let's Data Science, SiliconANGLE, Supabase Blog, ShadcnDeck, Vibe Coder Blog).",
        "c1": {
            "name": "Supabase",
            "tag": "backend / database — funded SaaS",
            "stats": [
                ("$500M", ["Raised June 2026,", "$10.5B valuation"]),
                ("60%+", ["of new databases created on", "the platform via AI coding tools"]),
                ("600%", ["year-over-year increase in databases", "created via Claude Code"]),
            ],
            "src": "Let's Data Science · SiliconANGLE · Supabase Blog",
        },
        "c2": {
            "name": "shadcn/ui",
            "tag": "UI components — open source",
            "stats": [
                ("109k+", ["GitHub stars in under 3 years,", "with no direct funding"]),
                ("5", ["independent vendors' tools", "generate it by default"]),
                ("$0", ["spent on sales — traction comes", "from being in the training data"]),
            ],
            "src": "ShadcnDeck · Vibe Coder Blog",
        },
    },
},
}


if __name__ == "__main__":
    for lang in ["pt", "en"]:
        save(f"v1-posicionamento-{lang}" if lang == "pt" else f"v1-positioning-{lang}", build_v1(lang))
        save(f"v2-pilares-{lang}" if lang == "pt" else f"v2-pillars-{lang}", build_v2(lang))
        save(f"v3-geo-citacao-{lang}" if lang == "pt" else f"v3-geo-citation-{lang}", build_v3(lang))
        save(f"v4-token-economia-{lang}" if lang == "pt" else f"v4-token-economics-{lang}", build_v4(lang))
        save(f"v5-casos-{lang}" if lang == "pt" else f"v5-cases-{lang}", build_v5(lang))
    print("done")
