#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Part 2 visuals — Builder-Led Growth. English."""
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
MUTED = "#C7CDD5"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=16, weight="400", fill=NAVY, anchor="start", style="normal", family=FONT):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" fill="{fill}" '
            f'text-anchor="{anchor}">{esc(s)}</text>')


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


# ---------------------------------------------------------------- 1. three inputs
def v1():
    W, H = 1600, 860
    b = []
    header(b, "WHAT COMPETES IN AN AGENT'S DECISION", "The three inputs",
           "Power, speed of influence and time to return do not coincide", H)

    cols = [
        {
            "n": "1", "t": ["Parametric", "knowledge"],
            "d": ["What the model learned in", "training and carries in its",
                  "weights. Answers even with no", "internet access."],
            "poder": 1.0, "vel": 0.12,
            "prazo": "18 to 36 months",
            "ex": "Explains shadcn/ui: volume of", "ex2": "public code became the default"
        },
        {
            "n": "2", "t": ["Real-time", "retrieval"],
            "d": ["What the agent fetches during", "the task: docs, search results,",
                  "repository files, llms.txt."],
            "poder": 0.55, "vel": 0.85,
            "prazo": "weeks",
            "ex": "Only reaches those who already", "ex2": "know to look for you"
        },
        {
            "n": "3", "t": ["Execution", "friction"],
            "d": ["What happens when the agent", "tries to use it. Custom DSL,",
                  "manual steps, schema token", "cost."],
            "poder": 0.75, "vel": 0.7,
            "prazo": "one sprint",
            "ex": "Only acts after the first two", "ex2": "battles have been won"
        },
    ]

    cw, gap, x0 = 468, 26, 60
    by, bh = 195, 545
    for i, c in enumerate(cols):
        x = x0 + i * (cw + gap)
        b.append(rect(x, by, cw, bh, PANEL, BORDER, 1))
        b.append(circle(x + 40, by + 46, 20, ACCENT))
        b.append(txt(x + 40, by + 53, c["n"], 18, "700", "#FFFFFF", "middle"))
        b.append(lines(x + 26, by + 100, c["t"], 20, "700", NAVY, 26))
        b.append(lines(x + 26, by + 168, c["d"], 14, "400", GRAY, 21))

        bx, bw = x + 26, cw - 52
        yb = by + 275
        for label, val, col in [("relative power", c["poder"], ACCENT), ("speed of influence", c["vel"], AMBER)]:
            b.append(txt(bx, yb, label, 12.5, "400", GRAY_LIGHT))
            b.append(rect(bx, yb + 10, bw, 18, "#EEF0F3", rx=5))
            b.append(rect(bx, yb + 10, max(8, bw * val), 18, col, rx=5))
            yb += 56

        b.append(line(bx, by + bh - 128, x + cw - 26, by + bh - 128, BORDER, 1))
        b.append(txt(bx, by + bh - 100, "time to return", 12.5, "400", GRAY_LIGHT))
        b.append(txt(bx, by + bh - 72, c["prazo"], 22, "700", NAVY))
        b.append(txt(bx, by + bh - 40, c["ex"], 12.5, "400", GRAY_LIGHT, style="italic"))
        b.append(txt(bx, by + bh - 22, c["ex2"], 12.5, "400", GRAY_LIGHT, style="italic"))

    footer(b, W, H, "Treating all three as one thing — \"optimize for AI\" — is what makes teams spend six months in the wrong place.")
    return doc(W, H, "\n".join(b))


# ---------------------------------------------------------------- 2. funnel
def v2():
    W, H = 1600, 900
    b = []
    header(b, "THE BUILDER-LED GROWTH FUNNEL", "Three stages, three mechanisms",
           "Each stage is decided by a different input — and lost in a different way", H)

    st = [
        {"n": "01", "t": "Candidacy",
         "q": "Does the model know you exist,\nprecisely enough to cite you right?",
         "mec": "Parametric knowledge",
         "perda": "Being cited incorrectly:\nwrong package name, method that\ndoesn't exist, deprecated version",
         "dado": "16% → 54%",
         "dadol": "GPT-4 accuracy with structured data"},
        {"n": "02", "t": "Recommendation",
         "q": "Among the candidates,\ndoes the agent pick you?",
         "mec": "Retrieval + community signal",
         "perda": "Absence from the third-party\ncomparative content that carries\nthe largest share of citations",
         "dado": "32.5% vs <5%",
         "dadol": "third-party vs. your own page"},
        {"n": "03", "t": "Adoption",
         "q": "Did the recommendation become\na working integration?",
         "mec": "Execution friction",
         "perda": "Manual steps in the middle of\nthe flow. No marketing metric\nflags the loss",
         "dado": "the blind stage",
         "dadol": "\"I was recommended\" is already satisfied"},
    ]

    x0, cw, gap = 60, 468, 26
    by, bh = 200, 520
    for i, s in enumerate(st):
        x = x0 + i * (cw + gap)
        hl = (i == 2)
        b.append(rect(x, by, cw, bh, ACCENT_SOFT if hl else PANEL, ACCENT if hl else BORDER, 2 if hl else 1))
        b.append(rect(x, by, cw, 6, ACCENT if hl else MUTED, rx=0))
        b.append(txt(x + 26, by + 48, s["n"], 30, "700", ACCENT if hl else GRAY_LIGHT))
        b.append(txt(x + 100, by + 48, s["t"], 24, "700", NAVY))

        b.append(txt(x + 26, by + 96, "THE QUESTION", 11.5, "700", GRAY_LIGHT))
        b.append(lines(x + 26, by + 122, s["q"].split("\n"), 15.5, "400", NAVY, 23))

        b.append(txt(x + 26, by + 200, "DOMINANT MECHANISM", 11.5, "700", GRAY_LIGHT))
        b.append(txt(x + 26, by + 226, s["mec"], 15, "700", ACCENT))

        b.append(txt(x + 26, by + 272, "HOW YOU LOSE HERE", 11.5, "700", GRAY_LIGHT))
        b.append(lines(x + 26, by + 298, s["perda"].split("\n"), 14, "400", GRAY, 21))

        b.append(line(x + 26, by + bh - 96, x + cw - 26, by + bh - 96, BORDER, 1))
        b.append(txt(x + 26, by + bh - 58, s["dado"], 24, "700", ACCENT))
        b.append(txt(x + 26, by + bh - 30, s["dadol"], 12.5, "400", GRAY_LIGHT, style="italic"))

        if i < 2:
            cy = by + bh / 2
            ax = x + cw + 3
            b.append(f'<path d="M{ax},{cy} l14,0 m-5,-5 l5,5 l-5,5" stroke="{GRAY_LIGHT}" stroke-width="2" fill="none"/>')

    fy = by + bh + 34
    b.append(rect(60, fy, W - 120, 74, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, fy + 32, "THE LIMIT OF THE THESIS", 12.5, "700", AMBER))
    b.append(txt(88, fy + 58, "BLG decides who enters. What decides whether they stay is human economics — the limit of the thesis is the invoice.", 17, "400", NAVY))

    footer(b, W, H, "Sources: Digidop (structured data) · Connor Kimball (citation provenance) · full analysis in the article.")
    return doc(W, H, "\n".join(b))


# ---------------------------------------------------------------- 3. two pricing forces
def v3():
    W, H = 1600, 800
    b = []
    header(b, "PRICING UNDER BLG", "The two forces to balance",
           "The free tier stops being top-of-funnel and becomes an entry ticket — while still having to produce revenue", H)

    bw, bh, by = 620, 330, 205
    xl, xr = 60, W - 60 - bw

    b.append(rect(xl, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xl, by, bw, 6, ACCENT, rx=0))
    b.append(txt(xl + 30, by + 52, "FORCE 1 — ENTRY TICKET", 12.5, "700", ACCENT))
    b.append(lines(xl + 30, by + 92, ["The machine has to be able to", "try without asking permission"], 22, "700", NAVY, 30))
    b.append(lines(xl + 30, by + 172, [
        "An agent that hits a paywall has to stop, notify the",
        "human and wait. The interruption breaks the flow",
        "and transfers the decision to someone who was",
        "doing something else — opening room for the agent",
        "to pick the tool that required no stop."], 14, "400", GRAY, 21))
    b.append(txt(xl + 30, by + bh - 26, "Without a free tier, you aren't in the game.", 14.5, "700", ACCENT))

    b.append(rect(xr, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xr, by, bw, 6, AMBER, rx=0))
    b.append(txt(xr + 30, by + 52, "FORCE 2 — SUFFICIENCY", 12.5, "700", AMBER))
    b.append(lines(xr + 30, by + 92, ["The free tier can't solve", "the whole problem"], 22, "700", NAVY, 30))
    b.append(lines(xr + 30, by + 172, [
        "PLG freemium converts because the human builds a",
        "habit, hits the limit and feels pain. The machine",
        "doesn't feel friction as discomfort, forms no",
        "attachment, and has infinite patience to wait for a",
        "reset. Pain-driven conversion doesn't transfer."], 14, "400", GRAY, 21))
    b.append(txt(xr + 30, by + bh - 26, "Published guides already teach stacking free tiers.", 14.5, "700", AMBER))

    cy = by + bh / 2
    mx = W / 2
    b.append(f'<path d="M{mx-42},{cy} l-30,0 m5,-5 l-5,5 l5,5" stroke="{GRAY_LIGHT}" stroke-width="2.5" fill="none"/>')
    b.append(f'<path d="M{mx+42},{cy} l30,0 m-5,-5 l5,5 l-5,5" stroke="{GRAY_LIGHT}" stroke-width="2.5" fill="none"/>')

    ly = by + bh + 40
    b.append(rect(60, ly, W - 120, 118, ACCENT_SOFT, ACCENT, 1.5))
    b.append(txt(88, ly + 34, "THE LEVERS THAT RESOLVE THE TENSION", 12.5, "700", ACCENT))
    items = [
        "Credit cost proportional to cost-to-serve",
        "Quota calibrated by unit of work, not by calendar",
        "Concurrency limits, on top of volume limits",
        "A revenue path the machine can traverse",
    ]
    for i, it in enumerate(items):
        cx = 88 + (i % 2) * 740
        cyy = ly + 66 + (i // 2) * 30
        b.append(circle(cx + 5, cyy - 5, 4, ACCENT))
        b.append(txt(cx + 20, cyy, it, 15, "400", NAVY))

    footer(b, W, H, "The least copied detail: limiting concurrency lets you stay generous on volume without serving as production infrastructure.")
    return doc(W, H, "\n".join(b))


# ---------------------------------------------------------------- 4. where to measure
def v4():
    W, H = 1600, 840
    b = []
    header(b, "MEASUREMENT", "Where each stage is measured",
           "Candidacy measures the model's past. Community measures its future.", H)

    zones = [
        {"t": "INSIDE THE MODEL", "e": "Candidacy", "c": ACCENT,
         "m": ["Share of Model — % of answers", "in the category that cite you",
               "", "Citation accuracy rate — when", "it cites you, does it get the",
               "package, install and method right?"],
         "n": "Measures what the model already knows:\na corpus that closed months ago."},
        {"t": "IN THE COMMUNITY", "e": "Recommendation", "c": AMBER,
         "m": ["Presence in the 15-20 most-searched", "comparisons in your category",
               "Dependent repos on GitHub (Used by)", "Downloads next to 3 competitors",
               "Inclusion in scaffolds and starters", "Annual surveys and curated lists"],
         "n": "Measures the material that future\nrecommendation will feed on."},
        {"t": "INSIDE THE PRODUCT", "e": "Adoption", "c": "#2F7D5D",
         "m": ["The event that only happens once", "the integration actually worked",
               "", "Not the download. Not the install.", "Not the signup. The first call",
               "with real data."],
         "n": "Separates \"I was recommended\" from\n\"I am being used\"."},
    ]

    x0, cw, gap = 60, 468, 26
    by, bh = 200, 520
    for i, z in enumerate(zones):
        x = x0 + i * (cw + gap)
        b.append(rect(x, by, cw, bh, PANEL, BORDER, 1))
        b.append(rect(x, by, cw, 6, z["c"], rx=0))
        b.append(txt(x + 26, by + 50, z["t"], 12.5, "700", z["c"]))
        b.append(txt(x + 26, by + 86, z["e"], 26, "700", NAVY))
        b.append(line(x + 26, by + 110, x + cw - 26, by + 110, BORDER, 1))
        b.append(lines(x + 26, by + 146, z["m"], 14, "400", GRAY, 24))
        b.append(line(x + 26, by + bh - 92, x + cw - 26, by + bh - 92, BORDER, 1))
        b.append(lines(x + 26, by + bh - 60, z["n"].split("\n"), 13.5, "400", GRAY_LIGHT, 20, style="italic"))

    footer(b, W, H, "Measuring recommendation by asking the agent is measuring candidacy again — the model only returns what it already knew.")
    return doc(W, H, "\n".join(b))


# ---------------------------------------------------------------- 5. consolidated table
def v5():
    W, H = 1600, 780
    b = []
    header(b, "CONSOLIDATED VIEW", "What each metric answers — and what it doesn't",
           "The most common error is reporting AI mentions as though they were adoption", H)

    rows = [
        ["Candidacy", "Inside the model", "Share of Model", "Doesn't say whether the citation is correct"],
        ["Candidacy", "Inside the model", "Citation accuracy rate", "Doesn't say whether you are the one picked"],
        ["Recommendation", "In the community", "Presence in comparisons", "Doesn't say whether the integration works"],
        ["Recommendation", "In the community", "Dependents, downloads, scaffolds", "Doesn't say whether usage recurs"],
        ["Adoption", "Inside the product", "First successful call", "Doesn't say whether the customer stays"],
        ["Crosses all 3", "Inside the product", "Architectural adoption rate", "Doesn't say why the agent chose you"],
    ]
    heads = ["STAGE", "WHERE TO MEASURE", "METRIC", "WHAT IT DOESN'T ANSWER"]
    colx = [60, 300, 590, 1030]
    ty = 205

    b.append(rect(60, ty - 30, W - 120, 44, ACCENT_SOFT, rx=6))
    for i, h in enumerate(heads):
        b.append(txt(colx[i] + 16, ty, h, 12.5, "700", ACCENT))

    ry = ty + 46
    for i, r in enumerate(rows):
        if i % 2 == 0:
            b.append(rect(60, ry - 26, W - 120, 62, PANEL, rx=6))
        for j, cell in enumerate(r):
            wt = "700" if j == 2 else "400"
            fl = NAVY if j == 2 else GRAY
            sz = 15.5 if j == 2 else 14.5
            st = "italic" if j == 3 else "normal"
            b.append(txt(colx[j] + 16, ry, cell, sz, wt, fl, style=st))
        ry += 62

    b.append(rect(60, ry + 6, W - 120, 70, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, ry + 38, "THE FIRST NUMBER TO MEASURE", 12.5, "700", AMBER))
    b.append(txt(88, ry + 62, "If you don't know what share of the resources in your product is created by an agent, you don't know whether BLG is already relevant to you.", 15.5, "400", NAVY))

    footer(b, W, H, "References: Supabase (60%+ of databases via AI tools) · Vercel (from <3% to more than half of deploys).")
    return doc(W, H, "\n".join(b))


# ---------------------------------------------------------------- cover
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

    b.append(f'<text x="120" y="196" font-family="{FONT}" font-size="26" font-weight="700" fill="{ACCENT_LIGHT}" letter-spacing="4">BUILDER-LED GROWTH — PART 2</text>')
    b.append(f'<line x1="120" y1="224" x2="560" y2="224" stroke="{ACCENT}" stroke-width="3"/>')

    b.append(txt(114, 336, "How the machine decides,", 88, "700", WHITE))
    b.append(txt(114, 436, "and where it stops deciding", 88, "700", WHITE))
    b.append(txt(118, 512, "The mechanism, the price and what to measure", 46, "400", GL))

    bw, bh, gap = 400, 150, 46
    y = 660
    labels = [("CANDIDACY", "parametric knowledge"),
              ("RECOMMENDATION", "retrieval + community"),
              ("ADOPTION", "execution friction")]
    for i, (t, s) in enumerate(labels):
        x = 120 + i * (bw + gap)
        hl = (i == 2)
        b.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="14" fill="{ACCENT if hl else "none"}" '
                 f'fill-opacity="{0.18 if hl else 0}" stroke="{ACCENT_LIGHT if hl else GL}" '
                 f'stroke-opacity="{1 if hl else 0.45}" stroke-width="{3 if hl else 2}"/>')
        b.append(txt(x + bw / 2, y + 62, t, 28, "700", WHITE if hl else GL, "middle"))
        b.append(txt(x + bw / 2, y + 102, s, 21, "400", ACCENT_LIGHT if hl else GL, "middle", style="italic"))
        if i < 2:
            cy = y + bh / 2
            b.append(f'<line x1="{x+bw+8}" y1="{cy}" x2="{x+bw+gap-8}" y2="{cy}" stroke="{ACCENT_LIGHT}" '
                     f'stroke-width="2.5" stroke-dasharray="7,7"/>')

    ly = y + bh + 44
    b.append(f'<rect x="120" y="{ly}" width="{3*bw+2*gap}" height="76" rx="12" fill="{AMBER_C}" fill-opacity="0.16" stroke="{AMBER_C}" stroke-width="2"/>')
    b.append(txt(150, ly + 48, "The limit of the thesis is the invoice — BLG decides who enters, human economics decides who stays.", 26, "400", WHITE))

    b.append(f'<line x1="120" y1="{H-90}" x2="{W-120}" y2="{H-90}" stroke="{ACCENT}" stroke-opacity="0.5" stroke-width="1.5"/>')
    b.append(txt(120, H - 48, "Matheus Ramos · with Supabase, shadcn/ui, Drizzle, Better Auth, Firecrawl and Tailwind", 24, "400", GL))

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(b)}</svg>'
    p = os.path.join(OUT, "p2-cover-en.svg")
    open(p, "w", encoding="utf-8").write(svg)
    cairosvg.svg2png(url=p, write_to=os.path.join(OUT, "p2-cover-en.png"), scale=1.5)
    print("ok: p2-cover-en")


if __name__ == "__main__":
    save("p2-three-inputs-en", v1())
    save("p2-three-stage-funnel-en", v2())
    save("p2-two-pricing-forces-en", v3())
    save("p2-where-to-measure-en", v4())
    save("p2-metrics-table-en", v5())
    cover()
    print("done")
