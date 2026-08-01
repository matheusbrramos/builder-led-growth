#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Visuais da parte 3 — Builder-Led Growth, pilar 1. English."""
import cairosvg, os

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
GREEN = "#2F7D5D"
MUTED = "#C7CDD5"
RED_SOFT = "#F4E6E4"
RED = "#9C4A3C"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=16, weight="400", fill=NAVY, anchor="start", style="normal", family=FONT, sp=None):
    spa = f' letter-spacing="{sp}"' if sp else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" fill="{fill}" '
            f'text-anchor="{anchor}"{spa}>{esc(s)}</text>')


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


# ------------------------------------------------- 1. três fontes de incerteza
def v1():
    W, H = 1600, 900
    b = []
    header(b, "WHERE A MODEL'S UNCERTAINTY ABOUT YOUR PRODUCT COMES FROM",
           "The three sources — and who controls each",
           "Of the three reasons a model might get you wrong, one is entirely in your hands", H)

    cols = [
        {"t": ["Knowledge", "gaps"],
         "d": ["Insufficient training coverage,", "or outdated information."],
         "quem": "You, indirectly", "prazo": "months to years",
         "acao": "Depends on accumulated adoption.", "acao2": "Effort does not speed it up.",
         "cor": MUTED, "hl": False},
        {"t": ["Decoding", "randomness"],
         "d": ["Noise from the model's own", "sampling process."],
         "quem": "The harness, not you", "prazo": "—",
         "acao": "Outside your reach.", "acao2": "It belongs to whoever runs the agent.",
         "cor": MUTED, "hl": False},
        {"t": ["Input", "ambiguity"],
         "d": ["What you hand over admits", "more than one valid reading:", "docs, schema, name, API."],
         "quem": "YOU, directly", "prazo": "now",
         "acao": "The only lever that", "acao2": "responds this week.",
         "cor": ACCENT, "hl": True},
    ]

    cw, gap, x0 = 468, 26, 60
    by, bh = 190, 500
    for i, c in enumerate(cols):
        x = x0 + i * (cw + gap)
        b.append(rect(x, by, cw, bh, ACCENT_SOFT if c["hl"] else PANEL,
                      ACCENT if c["hl"] else BORDER, 2.5 if c["hl"] else 1))
        b.append(rect(x, by, cw, 6, c["cor"], rx=0))
        b.append(lines(x + 26, by + 56, c["t"], 23, "700", NAVY if c["hl"] else GRAY, 29))
        b.append(lines(x + 26, by + 140, c["d"], 14, "400", GRAY, 21))

        b.append(line(x + 26, by + 222, x + cw - 26, by + 222, BORDER, 1))
        b.append(txt(x + 26, by + 252, "WHO CONTROLS IT", 11.5, "700", GRAY_LIGHT))
        b.append(txt(x + 26, by + 280, c["quem"], 17, "700", ACCENT if c["hl"] else GRAY))

        b.append(txt(x + 26, by + 328, "ON WHAT TIMELINE", 11.5, "700", GRAY_LIGHT))
        b.append(txt(x + 26, by + 364, c["prazo"], 28, "700", ACCENT if c["hl"] else GRAY_LIGHT))

        b.append(line(x + 26, by + bh - 82, x + cw - 26, by + bh - 82, BORDER, 1))
        b.append(txt(x + 26, by + bh - 52, c["acao"], 13.5, "400", GRAY_LIGHT, style="italic"))
        b.append(txt(x + 26, by + bh - 32, c["acao2"], 13.5, "400", GRAY_LIGHT, style="italic"))

    fy = by + bh + 30
    b.append(rect(60, fy, W - 120, 62, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, fy + 39, "And it is exactly where almost nobody works: the public conversation is about showing up, not about being unambiguous.", 17, "400", NAVY))

    footer(b, W, H, "Decomposition from The Anatomy of Uncertainty in LLMs (arXiv 2603.24967). The mapping to distribution is the author's.")
    return doc(W, H, "\n".join(b))


# ------------------------------------------------- 2. quatro camadas
def v2():
    W, H = 1600, 980
    b = []
    header(b, "WHERE AMBIGUITY ACTS", "Four layers, four literatures",
           "Measured by fields that do not cite each other — which suggests a common mechanism underneath", H)

    rows = [
        {"n": "1", "t": "Can the machine use you without erring?",
         "campo": "code generation",
         "dado": "+40 points", "dadol": "constrained language over Python, on multi-step tasks",
         "nota": "The variable is not familiarity. It is how many valid paths you leave open."},
        {"n": "2", "t": "Can the machine tell you from your competitor?",
         "campo": "tool selection",
         "dado": "73%", "dadol": "of the servers analyzed have repeated tool names",
         "nota": "Your distinctness depends on what others named. There is no equivalent to this in PLG."},
        {"n": "3", "t": "Does the machine know who you are?",
         "campo": "entity linking",
         "dado": "attribution suppressed", "dadol": "when name disambiguation fails",
         "nota": "The result is not being cited wrongly. It is not being cited — a silent failure."},
        {"n": "4", "t": "What does the machine learn about you?",
         "campo": "corpus quality",
         "dado": "intra-memory conflict", "dadol": "incongruity in training becomes inconsistency in the weights",
         "nota": "Two versions of your API in the corpus teach competing versions of yourself."},
    ]

    y = 186
    rh = 148
    for i, r in enumerate(rows):
        b.append(rect(60, y, W - 120, rh - 14, PANEL if i % 2 == 0 else BG, BORDER, 1))
        b.append(rect(60, y, 6, rh - 14, ACCENT, rx=0))
        b.append(circle(112, y + 42, 20, ACCENT))
        b.append(txt(112, y + 49, r["n"], 18, "700", "#FFFFFF", "middle"))
        b.append(txt(150, y + 36, r["t"], 21, "700", NAVY))
        b.append(txt(150, y + 62, r["campo"], 13, "400", GRAY_LIGHT, style="italic"))
        b.append(txt(150, y + 104, r["nota"], 14.5, "400", GRAY))

        b.append(line(1010, y + 22, 1010, y + rh - 36, BORDER, 1))
        b.append(txt(1046, y + 52, r["dado"], 25, "700", ACCENT))
        b.append(txt(1046, y + 82, r["dadol"], 13, "400", GRAY_LIGHT, style="italic"))
        y += rh

    fy = y + 12
    b.append(rect(60, fy, W - 120, 72, ACCENT_SOFT, ACCENT, 1.5))
    b.append(txt(88, fy + 30, "WHAT AMBIGUITY DOES NOT EXPLAIN", 12.5, "700", ACCENT))
    b.append(txt(88, fy + 56, "Community, economics and accumulated presence in training data. A variable that explains everything explains nothing.", 16, "400", NAVY))

    footer(b, W, H, "Sources: arXiv 2512.23214 (Anka) · arXiv 2602.18914 (MCP descriptions, preprint) · entity disambiguation literature · arXiv 2403.08319.")
    return doc(W, H, "\n".join(b))


# ------------------------------------------------- 3. a inversão
def v3():
    W, H = 1600, 810
    b = []
    header(b, "THE POINT WHERE THE TWO OPTIMIZATIONS DIVERGE",
           "What attracts the human confuses the machine",
           "Until now the two interests had been converging. In content strategy, they do not", H)

    bw, bh, by = 620, 340, 200
    xl, xr = 60, W - 60 - bw

    b.append(rect(xl, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xl, by, bw, 6, GREEN, rx=0))
    b.append(txt(xl + 30, by + 50, "THE HUMAN NEEDS", 12.5, "700", GREEN))
    b.append(lines(xl + 30, by + 92, ["Repetition across", "varied formats"], 23, "700", NAVY, 30))
    b.append(lines(xl + 30, by + 176, [
        "They forget and get distracted. The same idea has to",
        "meet them in the feed, in email and in short video,",
        "and each encounter reinforces the last.",
        "",
        "Atomization is reach."], 14.5, "400", GRAY, 22))

    b.append(rect(xr, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xr, by, bw, 6, RED, rx=0))
    b.append(txt(xr + 30, by + 50, "THE MACHINE NEEDS", 12.5, "700", RED))
    b.append(lines(xr + 30, by + 92, ["A single, consistent", "claim"], 23, "700", NAVY, 30))
    b.append(lines(xr + 30, by + 176, [
        "Twelve pieces saying the same thing occupy capacity.",
        "Each adaptation simplifies differently, and incompatible",
        "simplifications become conflict in the weights.",
        "",
        "Atomization is noise with a cost."], 14.5, "400", GRAY, 22))

    cy = by + bh / 2
    mx = W / 2
    b.append(f'<path d="M{mx-40},{cy-14} l-28,0 m5,-5 l-5,5 l5,5" stroke="{GRAY_LIGHT}" stroke-width="2.5" fill="none"/>')
    b.append(f'<path d="M{mx+40},{cy-14} l28,0 m-5,-5 l5,5 l-5,5" stroke="{GRAY_LIGHT}" stroke-width="2.5" fill="none"/>')

    ly = by + bh + 36
    b.append(rect(60, ly, W - 120, 108, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, ly + 32, "THE SHARP VERSION — AND THE COUNTERPOINT THAT PRODUCED IT", 12.5, "700", AMBER))
    b.append(txt(88, ly + 62, "It is not that less content is better. Content that says different things beats content that says the same thing twelve ways.", 16.5, "400", NAVY))
    b.append(txt(88, ly + 88, "Research shows removing near-duplicates worsens training — they differ in semantics. What counts is content variation, not format variation.", 14, "400", GRAY))

    footer(b, W, H, "Proposed direction: separate the circuits. Human content in human channels; a single canonical source on the machine surface.")
    return doc(W, H, "\n".join(b))


# ------------------------------------------------- 4. AGENTS.md x llms.txt
def v4():
    W, H = 1600, 780
    b = []
    header(b, "SAME FORMAT, SAME EFFORT, OPPOSITE FATES",
           "AGENTS.md and llms.txt",
           "The difference is not in the quality of the file. It is in where it sits", H)

    bw, bh, by = 700, 330, 195
    xl, xr = 60, W - 60 - bw

    b.append(rect(xl, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xl, by, bw, 6, MUTED, rx=0))
    b.append(txt(xl + 30, by + 52, "llms.txt", 26, "700", NAVY, family="Liberation Mono, monospace"))
    b.append(txt(xl + 30, by + 84, "Markdown at the domain root", 14, "400", GRAY_LIGHT, style="italic"))
    b.append(txt(xl + 30, by + 150, "97%", 46, "700", GRAY_LIGHT))
    b.append(txt(xl + 30, by + 180, "of the files got zero requests in May 2026", 14.5, "400", GRAY))
    b.append(txt(xl + 30, by + 232, "No formal standard. Google stated it does not", 14, "400", GRAY))
    b.append(txt(xl + 30, by + 254, "affect search rankings — then placed it in the", 14, "400", GRAY))
    b.append(txt(xl + 30, by + 276, "Lighthouse agentic browsing audit.", 14, "400", GRAY))

    b.append(rect(xr, by, bw, bh, ACCENT_SOFT, ACCENT, 2))
    b.append(rect(xr, by, bw, 6, ACCENT, rx=0))
    b.append(txt(xr + 30, by + 52, "AGENTS.md", 26, "700", NAVY, family="Liberation Mono, monospace"))
    b.append(txt(xr + 30, by + 84, "Markdown at the repository root", 14, "400", GRAY_LIGHT, style="italic"))
    b.append(txt(xr + 30, by + 150, "60,000+", 46, "700", ACCENT))
    b.append(txt(xr + 30, by + 180, "repositories, against 20,000 in August 2025", 14.5, "400", GRAY))
    b.append(txt(xr + 30, by + 232, "Standard formalized by OpenAI, Google, Cursor,", 14, "400", GRAY))
    b.append(txt(xr + 30, by + 254, "Factory and Sourcegraph. Under the Agentic AI Foundation.", 14, "400", GRAY))
    b.append(txt(xr + 30, by + 276, "Read natively by more than 30 tools.", 14, "400", GRAY))

    ly = by + bh + 38
    b.append(rect(60, ly, W - 120, 130, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, ly + 34, "THE EXPLANATION", 12.5, "700", AMBER))
    b.append(txt(88, ly + 66, "AGENTS.md sits where the agent already is — inside the repository it was asked to edit.", 17, "400", NAVY))
    b.append(txt(88, ly + 92, "llms.txt sits where someone has to send the agent.", 17, "400", NAVY))
    b.append(txt(88, ly + 118, "Machine legibility is not publishing a legible artifact. It is placing it on the path the agent already travels.", 15, "700", ACCENT))

    footer(b, W, H, "Sources: Ahrefs (137,000 domains) · Codersera · Search Engine Land and Chrome for Developers (Lighthouse, May 2026).")
    return doc(W, H, "\n".join(b))


# ------------------------------------------------- 5. quadro de evidência
def v5():
    W, H = 1600, 950
    b = []
    header(b, "WHAT IS BACKED AND WHAT IS NOT",
           "Evidence table for this article",
           "A claim with no declared epistemic status is a claim with no address", H)

    rows = [
        ["Constrained syntax beats a familiar language", "Published experiment", "arXiv 2512.23214, validated on 2 models", ACCENT],
        ["73% of MCP servers have repeated names", "Survey", "arXiv 2602.18914 — preprint, 10,000+ servers", ACCENT],
        ["Failed disambiguation suppresses attribution", "Documented mechanism", "entity linking literature; no loss figure", AMBER],
        ["Corpus incongruity becomes conflict in the weights", "Literature review", "arXiv 2403.08319", ACCENT],
        ["Facts compete for model capacity", "Experiment", "arXiv 2604.08519 — small models, pretraining from scratch", AMBER],
        ["Structured data improves citation", "IN CONFLICT", "Ahrefs finds no effect; arXiv finds +29.6%", AMBER],
        ["Markdown reduces tokens", "Range without a standard", "25% to 87% across studies — not a margin of error", AMBER],
        ["Context cost is a retention decision", "Author's reasoning", "no source treats it this way", GRAY_LIGHT],
        ["Separate the human and canonical circuits", "Author's reasoning", "no published conversion data", GRAY_LIGHT],
        ["Ambiguity affects parametric knowledge", "Open question", "found no study measuring it", GRAY_LIGHT],
    ]
    heads = ["CLAIM", "STATUS", "BASIS"]
    colx = [60, 700, 1010]
    ty = 200

    b.append(rect(60, ty - 28, W - 120, 42, ACCENT_SOFT, rx=6))
    for i, h in enumerate(heads):
        b.append(txt(colx[i] + 16, ty, h, 12.5, "700", ACCENT))

    ry = ty + 44
    for i, r in enumerate(rows):
        if i % 2 == 0:
            b.append(rect(60, ry - 24, W - 120, 52, PANEL, rx=6))
        b.append(txt(colx[0] + 16, ry, r[0], 15, "400", NAVY))
        b.append(txt(colx[1] + 16, ry, r[1], 13.5, "700", r[3]))
        b.append(txt(colx[2] + 16, ry, r[2], 13.5, "400", GRAY, style="italic"))
        ry += 52

    b.append(rect(60, ry + 6, W - 120, 66, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, ry + 34, "WHAT THAT COSTS", 12.5, "700", AMBER))
    b.append(txt(88, ry + 58, "Three of the ten claims are my own reasoning or open questions. I would rather say so than present everything with equal confidence.", 15.5, "400", NAVY))

    footer(b, W, H, "Builder-Led Growth, part 3 — pillar 1, machine legibility.")
    return doc(W, H, "\n".join(b))


# ------------------------------------------------- capa
def cover():
    NAVY_DEEP = "#101A30"
    ACCENT_LIGHT = "#6E9CC4"
    AMBER_C = "#C68B3E"
    WHITE = "#FFFFFF"
    GL = "#AEB6C2"
    W, H = 1920, 1080
    b = [f'<rect width="{W}" height="{H}" fill="{NAVY_DEEP}"/>']
    for i in range(14):
        x0 = W - 620 + i * 46
        b.append(f'<line x1="{x0}" y1="0" x2="{x0+340}" y2="340" stroke="{ACCENT}" stroke-opacity="0.14" stroke-width="2"/>')
    b.append(f'<rect x="0" y="0" width="14" height="{H}" fill="{ACCENT}"/>')

    b.append(f'<text x="120" y="196" font-family="{FONT}" font-size="26" font-weight="700" fill="{ACCENT_LIGHT}" letter-spacing="4">BUILDER-LED GROWTH — PART 3</text>')
    b.append(f'<line x1="120" y1="224" x2="620" y2="224" stroke="{ACCENT}" stroke-width="3"/>')

    b.append(txt(114, 344, "The tax the machine charges", 86, "700", WHITE))
    b.append(txt(114, 444, "and the human never sees", 86, "700", WHITE))
    b.append(txt(118, 520, "Pillar 1 — machine legibility, and the variable that decides", 44, "400", GL))

    bw, bh, gap = 400, 118, 46
    y = 618
    labels = [("EXECUTION", "use you without erring"),
              ("SELECTION", "tell you from the competitor"),
              ("IDENTITY", "know who you are")]
    for i, (t, s) in enumerate(labels):
        x = 120 + i * (bw + gap)
        b.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="14" fill="none" '
                 f'stroke="{GL}" stroke-opacity="0.45" stroke-width="2"/>')
        b.append(txt(x + bw / 2, y + 50, t, 26, "700", GL, "middle"))
        b.append(txt(x + bw / 2, y + 84, s, 19, "400", GL, "middle", style="italic"))

    y2 = y + bh + 18
    b.append(f'<rect x="120" y="{y2}" width="{3*bw+2*gap}" height="{bh}" rx="14" fill="{ACCENT}" '
             f'fill-opacity="0.18" stroke="{ACCENT_LIGHT}" stroke-width="3"/>')
    b.append(txt(120 + (3*bw+2*gap) / 2, y2 + 50, "KNOWLEDGE", 26, "700", WHITE, "middle"))
    b.append(txt(120 + (3*bw+2*gap) / 2, y2 + 84, "what it ends up learning about you", 19, "400", ACCENT_LIGHT, "middle", style="italic"))

    ly = y2 + bh + 30
    b.append(f'<rect x="120" y="{ly}" width="{3*bw+2*gap}" height="66" rx="12" fill="{AMBER_C}" fill-opacity="0.16" stroke="{AMBER_C}" stroke-width="2"/>')
    b.append(txt(150, ly + 43, "The human resolves ambiguity for free. The machine picks someone else.", 26, "400", WHITE))

    b.append(f'<line x1="120" y1="{H-70}" x2="{W-120}" y2="{H-70}" stroke="{ACCENT}" stroke-opacity="0.5" stroke-width="1.5"/>')
    b.append(txt(120, H - 34, "Matheus Ramos · with AGENTS.md, Anka, Go/Golang, WebMCP and seven studies", 23, "400", GL))

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(b)}</svg>'
    p = os.path.join(OUT, "p3-cover-en.svg")
    open(p, "w", encoding="utf-8").write(svg)
    cairosvg.svg2png(url=p, write_to=os.path.join(OUT, "p3-cover-en.png"), scale=1.5)
    print("ok: p3-cover-en")


if __name__ == "__main__":
    save("p3-three-sources-uncertainty-en", v1())
    save("p3-four-layers-ambiguity-en", v2())
    save("p3-inversion-human-machine-en", v3())
    save("p3-agents-md-vs-llms-txt-en", v4())
    save("p3-evidence-table-en", v5())
    cover()
    print("done")
