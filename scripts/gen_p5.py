#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais da parte 5 — Builder-Led Growth, pilar 3: comunidade e sinal de validação.

Gera PT e EN no mesmo arquivo, pelo mesmo motivo do gen_p4.py: número escrito
duas vezes é número que diverge. Os helpers de desenho vêm importados do gen_p4
em vez de copiados — mesma regra aplicada a código.

Uso:  python3 scripts/gen_p5.py          # gera PT e EN
      python3 scripts/gen_p5.py pt       # só português
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gen_p4 import (  # noqa: E402
    ACCENT, ACCENT_LIGHT, ACCENT_SOFT, AMBER, AMBER_SOFT, BORDER, GRAY,
    GRAY_LIGHT, GREEN, GREEN_SOFT, MUTED, NAVY, NAVY_DEEP, PANEL, WHITE,
    circle, doc, footer, header, line, lines, rect, save, txt,
)

# ---------------------------------------------------------------- números
# Existem uma vez só. Série verificada da Stack Overflow.
SERIE = [
    ("2022-11", 108_563),
    ("2023-03", 87_105),
    ("2024-03", 58_792),
    ("2024-06", 41_616),
    ("2024-12", 25_566),
]
QUEDA_TOTAL = "76,5%"
QUEDA_TOTAL_EN = "76.5%"


def num(v, lang):
    s = f"{v:,}"
    return s.replace(",", ".") if lang == "pt" else s


# ---------------------------------------------------------------- textos
T = {
    "pt": {
        "suf": "pt",
        "capa_kicker": "BUILDER-LED GROWTH — PARTE 5",
        "capa_t1": "O poço de onde",
        "capa_t2": "todos bebem",
        "capa_sub": "Pilar 3 — comunidade e sinal de validação",
        "capa_faixa": "Comunidade não é um pilar. É o lençol freático — e ele é compartilhado com o vizinho.",
        "capa_props": ["PRODUZ A MATÉRIA-PRIMA", "É COMPARTILHADO", "É ESGOTÁVEL", "SOZINHO NÃO SUSTENTA"],
        "capa_rodape": "Matheus Ramos · com a série verificada da Stack Overflow, ArchWiki, MDN e as normas ISO 9001, 30401 e 19770-2",

        "v1_nome": "p5-o-poco-secou-pt",
        "v1_kicker": "A SÉRIE VERIFICADA",
        "v1_titulo": "O poço secou, e dá para ver a data",
        "v1_sub": "Perguntas novas por mês na Stack Overflow",
        "v1_meses": ["nov/2022", "mar/2023", "mar/2024", "jun/2024", "dez/2024"],
        "v1_marco": "lançamento do ChatGPT",
        "v1_queda": "de queda no período",
        "v1_rodape": "Fonte: Stack Overflow Data Explorer, extraído por Theodore R. Smith. Valores de 2025 e 2026 divergem entre fontes e não entram aqui.",

        "v2_nome": "p5-cobertura-x-convergencia-pt",
        "v2_kicker": "OS FORMATOS DE COMUNIDADE",
        "v2_titulo": "Cobertura e convergência pedem desenhos opostos",
        "v2_sub": "Cobertura é quanto do espaço do problema o formato alcança; convergência é o quanto as respostas apontam para o mesmo lugar",
        "v2_x": "CONVERGÊNCIA",
        "v2_y": "COBERTURA",
        "v2_pontos": [
            ("Fórum", 0.22, 0.88, AMBER),
            ("Discord", 0.08, 0.62, "#9C4A3C"),
            ("Stack Overflow", 0.80, 0.86, ACCENT),
            ("GitHub Discussions", 0.78, 0.72, GREEN),
            ("ArchWiki e MDN", 0.92, 0.58, GREEN),
            ("Changelog", 0.88, 0.20, ACCENT),
            ("Receituário", 0.95, 0.28, GREEN),
        ],
        "v2_faixa": "O problema de desenho do pilar: obter o calor do Discord com a convergência da Stack Overflow.",
        "v2_rodape": "Posições são qualitativas, a partir da análise do artigo. Não há medida publicada comparando formatos nesses dois eixos.",

        "v3_nome": "p5-ferramentas-tres-propriedades-pt",
        "v3_kicker": "A COLUNA QUE NINGUÉM USA",
        "v3_titulo": "As ferramentas pelas três propriedades",
        "v3_sub": "Registrabilidade, convergência e durabilidade — convergência é o critério que falta nas comparações usuais",
        "v3_cols": ["REGISTRABILIDADE", "CONVERGÊNCIA", "DURABILIDADE"],
        "v3_linhas": [
            ("GitHub Discussions", 3, 3, 3),
            ("Fórum próprio", 3, 2, 2),
            ("Discord e Slack", 0, 0, 0),
            ("Stack Overflow", 3, 3, 2),
            ("Changelog", 3, 3, 3),
            ("Receituário de exemplos", 3, 3, 3),
        ],
        "v3_legenda": ["nula", "média", "alta"],
        "v3_rodape": "Mitigação para canal fechado: publicar a thread resolvida num arquivo público. Não é abandonar o canal, é parar de perder o que acontece nele.",

        "v4_nome": "p5-normas-mapeadas-pt",
        "v4_kicker": "O QUE JÁ ESTAVA RESOLVIDO",
        "v4_titulo": "Três normas, três problemas deste pilar",
        "v4_sub": "Builder-Led Growth não precisa inventar um sistema de qualidade",
        "v4_normas": [
            ("ISO 9001 — requisito 7.5", "Informação documentada",
             ["Análise crítica antes da divulgação", "Disponível no local de uso",
              "Legível", "Proteção contra versão obsoleta"]),
            ("ISO 30401 — 2018", "Gestão do conhecimento",
             ["Identificação e criação", "REPRESENTAÇÃO", "Distribuição e aplicação"]),
            ("ISO/IEC 19770-2 — 2015", "Identificação de software",
             ["Nome, edição e versão", "Procedência e artefatos",
              "Descoberta e contextualização"]),
        ],
        "v4_faixa": "O limite: a norma controla o que é seu. O resto se resolve por gravidade — tornar o canônico fácil de citar.",
        "v4_rodape": "A ISO/IEC 19770-2 tem descendência viva na RFC 9393 e adoção pelo NIST. Não encontrei ninguém propondo-a como resposta ao problema de nome.",

        "v5_nome": "p5-sete-estrategias-pt",
        "v5_kicker": "COMO FOMENTAR CONTEÚDO QUE CONVERGE",
        "v5_titulo": "Sete estratégias, um princípio só",
        "v5_sub": "Baratear a citação do canônico em relação à reescrita",
        "v5_itens": [
            ("Artefato pronto para citar", "trecho canônico, URL estável, versão"),
            ("Recompensar registro, não interação", "premie o que deixa rastro"),
            ("Pedir em público antes do privado", "converte mensagem direta em discussão"),
            ("Publicar o suporte", "ticket resolvido é o material de maior sinal"),
            ("Fechar o loop de versão", "o trabalho anti-deriva que ninguém faz"),
            ("Facilitar comparação honesta", "inclusive onde você perde"),
            ("Documentação em forma de pergunta", "casa com a forma da recuperação"),
        ],
        "v5_anti_t": "O QUE NÃO FAZER",
        "v5_anti": ["Premiar volume de conteúdo", "Concurso sem gabarito canônico",
                    "Resposta atrás de login", "Documentação sem data e versão"],
        "v5_rodape": "As pessoas compartilham o que é fácil compartilhar, e descrevem com as próprias palavras o que não veio pronto.",
    },
    "en": {
        "suf": "en",
        "capa_kicker": "BUILDER-LED GROWTH — PART 5",
        "capa_t1": "The well everyone",
        "capa_t2": "drinks from",
        "capa_sub": "Pillar 3 — community and validation signal",
        "capa_faixa": "Community isn't a pillar. It's the water table — and it's shared with the neighbours.",
        "capa_props": ["PRODUCES THE RAW MATERIAL", "IS SHARED", "IS EXHAUSTIBLE", "ALONE HOLDS NOTHING UP"],
        "capa_rodape": "Matheus Ramos · with the verified Stack Overflow series, ArchWiki, MDN and the ISO 9001, 30401 and 19770-2 standards",

        "v1_nome": "p5-the-well-ran-dry-en",
        "v1_kicker": "THE VERIFIED SERIES",
        "v1_titulo": "The well ran dry, and you can see the dates",
        "v1_sub": "New questions per month on Stack Overflow",
        "v1_meses": ["Nov 2022", "Mar 2023", "Mar 2024", "Jun 2024", "Dec 2024"],
        "v1_marco": "ChatGPT launch",
        "v1_queda": "decline over the period",
        "v1_rodape": "Source: Stack Overflow Data Explorer, extracted by Theodore R. Smith. Figures for 2025 and 2026 disagree across sources and are not shown.",

        "v2_nome": "p5-coverage-vs-convergence-en",
        "v2_kicker": "COMMUNITY FORMATS",
        "v2_titulo": "Coverage and convergence call for opposite designs",
        "v2_sub": "Coverage is how much of the problem space the format reaches; convergence is how far the answers point at the same place",
        "v2_x": "CONVERGENCE",
        "v2_y": "COVERAGE",
        "v2_pontos": [
            ("Forum", 0.22, 0.88, AMBER),
            ("Discord", 0.08, 0.62, "#9C4A3C"),
            ("Stack Overflow", 0.80, 0.86, ACCENT),
            ("GitHub Discussions", 0.78, 0.72, GREEN),
            ("ArchWiki and MDN", 0.92, 0.58, GREEN),
            ("Changelog", 0.88, 0.20, ACCENT),
            ("Cookbook", 0.95, 0.28, GREEN),
        ],
        "v2_faixa": "The pillar's design problem: getting Discord's warmth with Stack Overflow's convergence.",
        "v2_rodape": "Positions are qualitative, from the article's analysis. No published measurement compares formats on these two axes.",

        "v3_nome": "p5-tools-three-properties-en",
        "v3_kicker": "THE COLUMN NOBODY USES",
        "v3_titulo": "The tools by the three properties",
        "v3_sub": "Recordability, convergence and durability — convergence is the criterion missing from the usual comparisons",
        "v3_cols": ["RECORDABILITY", "CONVERGENCE", "DURABILITY"],
        "v3_linhas": [
            ("GitHub Discussions", 3, 3, 3),
            ("Own forum", 3, 2, 2),
            ("Discord and Slack", 0, 0, 0),
            ("Stack Overflow", 3, 3, 2),
            ("Changelog", 3, 3, 3),
            ("Cookbook of examples", 3, 3, 3),
        ],
        "v3_legenda": ["zero", "medium", "high"],
        "v3_rodape": "Mitigation for closed channels: publish the resolved thread to a public archive. Not abandoning the channel — just no longer losing what happens in it.",

        "v4_nome": "p5-standards-mapped-en",
        "v4_kicker": "WHAT WAS ALREADY SOLVED",
        "v4_titulo": "Three standards, three problems of this pillar",
        "v4_sub": "Builder-Led Growth doesn't need to invent a quality system",
        "v4_normas": [
            ("ISO 9001 — requirement 7.5", "Documented information",
             ["Review before release", "Available at the point of use",
              "Legible", "Protection against obsolete versions"]),
            ("ISO 30401 — 2018", "Knowledge management",
             ["Identification and creation", "REPRESENTATION", "Distribution and application"]),
            ("ISO/IEC 19770-2 — 2015", "Software identification",
             ["Name, edition and version", "Provenance and artifacts",
              "Discovery and contextualisation"]),
        ],
        "v4_faixa": "The limit: a standard controls what is yours. The rest is gravity — make the canonical easy to cite.",
        "v4_rodape": "ISO/IEC 19770-2 has living descendants in RFC 9393 and adoption by NIST. I found nobody proposing it as an answer to the naming problem.",

        "v5_nome": "p5-seven-strategies-en",
        "v5_kicker": "HOW TO GROW CONTENT THAT CONVERGES",
        "v5_titulo": "Seven strategies, one principle",
        "v5_sub": "Make citing the canonical cheaper than rewriting it",
        "v5_itens": [
            ("Artifact ready to cite", "canonical snippet, stable URL, version"),
            ("Reward the record, not interaction", "reward what leaves a trace"),
            ("Ask in public before private", "turns a direct message into a discussion"),
            ("Publish the support", "a resolved ticket is the highest-signal material"),
            ("Close the version loop", "the anti-drift work nobody does"),
            ("Make honest comparison easy", "including where you lose"),
            ("Documentation as questions", "matches the shape retrieval takes"),
        ],
        "v5_anti_t": "WHAT NOT TO DO",
        "v5_anti": ["Reward content volume", "Contest with no canonical reference",
                    "Answers behind a login", "Docs with no date or version"],
        "v5_rodape": "People share what's easy to share, and describe in their own words whatever didn't arrive ready-made.",
    },
}


# --------------------------------------------------------------- 1. a série
def v1(t, lang):
    W, H = 1600, 860
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    x0, base, altura_max = 150, 640, 400
    larg, gap = 200, 80
    topo = max(v for _, v in SERIE)
    for i, ((_, val), rot) in enumerate(zip(SERIE, t["v1_meses"])):
        x = x0 + i * (larg + gap)
        h = altura_max * val / topo
        cor = AMBER if i == 0 else (ACCENT if i < 4 else "#9C4A3C")
        b.append(rect(x, base - h, larg, h, cor, rx=8, op="0.85"))
        b.append(txt(x + larg / 2, base - h - 18, num(val, lang), 24, "700", NAVY, anchor="middle"))
        b.append(txt(x + larg / 2, base + 30, rot, 16, "400", GRAY, anchor="middle"))
    b.append(line(x0 - 30, base, x0 + 5 * (larg + gap) - gap + 30, base, BORDER, 2))
    b.append(txt(x0 + larg / 2, base - altura_max - 54, t["v1_marco"], 14, "700", AMBER, anchor="middle"))

    fy = base + 66
    b.append(rect(150, fy, W - 300, 84, AMBER, rx=12, op="0.14"))
    b.append(rect(150, fy, W - 300, 84, "none", AMBER, 1.5, rx=12))
    q = QUEDA_TOTAL if lang == "pt" else QUEDA_TOTAL_EN
    b.append(txt(196, fy + 56, q, 44, "700", AMBER))
    b.append(txt(330, fy + 54, t["v1_queda"], 22, "400", NAVY))

    footer(b, W, H, t["v1_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------ 2. cobertura x convergência
def v2(t, lang):
    W, H = 1600, 1000
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    gx, gy, gw, gh = 260, 240, 1080, 500
    b.append(rect(gx, gy, gw, gh, PANEL, BORDER, 1.5, rx=12))
    b.append(line(gx + gw / 2, gy, gx + gw / 2, gy + gh, BORDER, 1, "6 6"))
    b.append(line(gx, gy + gh / 2, gx + gw, gy + gh / 2, BORDER, 1, "6 6"))
    b.append(txt(gx + gw / 2, gy + gh + 40, t["v2_x"], 13, "700", ACCENT, anchor="middle", sp="2"))
    b.append(f'<text x="{gx - 40}" y="{gy + gh / 2}" font-family="Liberation Sans, Arial, sans-serif" '
             f'font-size="13" font-weight="700" fill="{ACCENT}" text-anchor="middle" letter-spacing="2" '
             f'transform="rotate(-90 {gx - 40} {gy + gh / 2})">{t["v2_y"]}</text>')

    for nome, cx, cy, cor in t["v2_pontos"]:
        px = gx + 40 + cx * (gw - 80)
        py = gy + gh - 40 - cy * (gh - 80)
        b.append(circle(px, py, 13, cor, WHITE, 2))
        anchor = "end" if cx > 0.7 else "start"
        dx = -22 if cx > 0.7 else 22
        b.append(txt(px + dx, py + 6, nome, 16, "700", NAVY, anchor=anchor))

    fy = gy + gh + 86
    b.append(rect(150, fy, W - 300, 68, ACCENT, rx=12, op="0.10"))
    b.append(rect(150, fy, W - 300, 68, "none", ACCENT, 1.5, rx=12))
    b.append(txt(190, fy + 43, t["v2_faixa"], 21, "700", NAVY))

    footer(b, W, H, t["v2_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------------- 3. ferramentas
def v3(t, lang):
    W, H = 1600, 820
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    x_rot, x0, passo = 60, 700, 280
    y0, lh = 250, 66
    for j, c in enumerate(t["v3_cols"]):
        b.append(txt(x0 + j * passo, y0 - 24, c, 12.5, "700", ACCENT, anchor="middle", sp="1.2"))
    cores = {0: MUTED, 2: AMBER, 3: GREEN}
    for i, (nome, a, bb, c) in enumerate(t["v3_linhas"]):
        y = y0 + i * lh
        if i % 2 == 0:
            b.append(rect(x_rot - 10, y - 26, W - 100, lh - 8, PANEL, rx=8))
        b.append(txt(x_rot, y, nome, 18, "700" if i in (0, 4, 5) else "400", NAVY))
        for j, v in enumerate((a, bb, c)):
            cx = x0 + j * passo
            b.append(circle(cx, y - 6, 15, cores[v], WHITE, 2))
            if v == 0:
                b.append(line(cx - 7, y - 6, cx + 7, y - 6, WHITE, 2.5))

    ly = y0 + len(t["v3_linhas"]) * lh + 16
    for k, (v, rot) in enumerate(zip((0, 2, 3), t["v3_legenda"])):
        b.append(circle(x0 - 120 + k * 170, ly, 10, cores[v], WHITE, 1.5))
        b.append(txt(x0 - 100 + k * 170, ly + 5, rot, 14, "400", GRAY))

    footer(b, W, H, t["v3_rodape"])
    return doc(W, H, "".join(b))


# ----------------------------------------------------------- 4. as normas
def v4(t, lang):
    W, H = 1600, 760
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    x, w = 60, 480
    for i, (nome, tema, itens) in enumerate(t["v4_normas"]):
        px = x + i * (w + 20)
        alt = 300
        b.append(rect(px, 240, w, alt, PANEL, ACCENT, 1.5, rx=12))
        b.append(rect(px, 240, w, 8, ACCENT, rx=0))
        b.append(txt(px + 28, 292, nome, 18, "700", ACCENT))
        b.append(txt(px + 28, 322, tema, 21, "700", NAVY))
        b.append(line(px + 28, 342, px + w - 28, 342, BORDER))
        for j, it in enumerate(itens):
            destaque = it.isupper()
            b.append(circle(px + 40, 374 + j * 34, 4, AMBER if destaque else MUTED))
            b.append(txt(px + 58, 380 + j * 34, it, 15,
                         "700" if destaque else "400",
                         NAVY if destaque else GRAY))

    fy = 580
    b.append(rect(60, fy, W - 120, 74, AMBER, rx=12, op="0.14"))
    b.append(rect(60, fy, W - 120, 74, "none", AMBER, 1.5, rx=12))
    b.append(txt(96, fy + 46, t["v4_faixa"], 20, "700", NAVY))

    footer(b, W, H, t["v4_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------------- 5. as estratégias
def v5(t, lang):
    W, H = 1600, 860
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    cw, y0, lh = 740, 250, 92
    for i, (titulo, sub) in enumerate(t["v5_itens"]):
        col, row = i % 2, i // 2
        px = 60 + col * (cw + 20)
        py = y0 + row * lh
        b.append(rect(px, py, cw, lh - 14, PANEL, BORDER, 1, rx=10))
        b.append(circle(px + 36, py + 39, 18, ACCENT_SOFT, ACCENT, 1.5))
        b.append(txt(px + 36, py + 46, str(i + 1), 17, "700", ACCENT, anchor="middle"))
        b.append(txt(px + 70, py + 36, titulo, 18, "700", NAVY))
        b.append(txt(px + 70, py + 60, sub, 14, "400", GRAY_LIGHT))

    ay = y0 + 4 * lh + 14
    b.append(rect(60, ay, W - 120, 130, "#9C4A3C", rx=12, op="0.08"))
    b.append(rect(60, ay, W - 120, 130, "none", "#9C4A3C", 1.5, rx=12))
    b.append(txt(96, ay + 34, t["v5_anti_t"], 12.5, "700", "#9C4A3C", sp="1.5"))
    for k, a in enumerate(t["v5_anti"]):
        cx = 96 + (k % 2) * 740
        cy = ay + 66 + (k // 2) * 30
        b.append(txt(cx, cy, "·  " + a, 15, "400", NAVY))

    footer(b, W, H, t["v5_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------------------------- capa
def capa(t, lang):
    W, H = 1920, 1080
    b = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="{NAVY_DEEP}"/>']
    # camadas de solo e nível do lençol caindo
    for i, (yy, op) in enumerate([(760, "0.06"), (820, "0.10"), (880, "0.14")]):
        b.append(f'<rect x="0" y="{yy}" width="{W}" height="{H - yy}" fill="{ACCENT}" fill-opacity="{op}"/>')
    for i in range(7):
        x = 1300 + i * 96
        b.append(f'<line x1="{x}" y1="0" x2="{x - 200}" y2="{H}" stroke="{ACCENT}" '
                 f'stroke-opacity="0.08" stroke-width="2"/>')

    b.append(txt(120, 176, t["capa_kicker"], 26, "700", ACCENT_LIGHT, sp="4"))
    b.append(line(120, 204, 470, 204, ACCENT, 3))
    b.append(txt(120, 312, t["capa_t1"], 82, "700", WHITE))
    b.append(txt(120, 404, t["capa_t2"], 82, "700", WHITE))
    b.append(txt(120, 468, t["capa_sub"], 32, "400", "#AEB6C2"))

    bw, gap, by = 400, 26, 560
    for i, p in enumerate(t["capa_props"]):
        x = 120 + i * (bw + gap)
        cor = AMBER if i == 2 else ACCENT_LIGHT
        b.append(rect(x, by, bw, 92, cor, rx=12, op="0.14"))
        b.append(rect(x, by, bw, 92, "none", cor, 2 if i == 2 else 1.5, rx=12))
        b.append(txt(x + bw / 2, by + 56, p, 17, "700", WHITE, anchor="middle", sp="1"))

    fy = by + 136
    b.append(rect(120, fy, W - 240, 88, AMBER, rx=12, op="0.16"))
    b.append(rect(120, fy, W - 240, 88, "none", AMBER, 2, rx=12))
    b.append(txt(152, fy + 56, t["capa_faixa"], 27, "400", WHITE))

    b.append(line(120, H - 90, W - 120, H - 90, ACCENT, 1.5))
    b.append(txt(120, H - 48, t["capa_rodape"], 21, "400", "#AEB6C2"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">{"".join(b)}</svg>')


def gerar(lang):
    t = T[lang]
    save(f"p5-capa-{t['suf']}" if lang == "pt" else f"p5-cover-{t['suf']}", capa(t, lang), scale=1.5)
    for fn in (v1, v2, v3, v4, v5):
        save(t[f"v{[v1, v2, v3, v4, v5].index(fn) + 1}_nome"], fn(t, lang))


if __name__ == "__main__":
    for lg in (sys.argv[1:] or ["pt", "en"]):
        gerar(lg)
    print("done")
