#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Visuais da parte 3 — Builder-Led Growth, pilar 1. PT-BR."""
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
    header(b, "DE ONDE VEM A INCERTEZA DE UM MODELO SOBRE O SEU PRODUTO",
           "As três fontes — e quem controla cada uma",
           "Das três razões pelas quais um modelo pode errar sobre você, uma está inteiramente nas suas mãos", H)

    cols = [
        {"t": ["Lacuna de", "conhecimento"],
         "d": ["Cobertura insuficiente no", "treino, ou informação", "desatualizada."],
         "quem": "Você, indiretamente", "prazo": "meses a anos",
         "acao": "Depende de adoção acumulada.", "acao2": "Não acelera com esforço.",
         "cor": MUTED, "hl": False},
        {"t": ["Aleatoriedade", "de decodificação"],
         "d": ["O ruído do próprio processo", "de amostragem do modelo."],
         "quem": "O harness, não você", "prazo": "—",
         "acao": "Fora do seu alcance.", "acao2": "É decisão de quem roda o agente.",
         "cor": MUTED, "hl": False},
        {"t": ["Ambiguidade", "de entrada"],
         "d": ["O que você entrega admite", "mais de uma leitura válida:", "docs, schema, nome, API."],
         "quem": "VOCÊ, diretamente", "prazo": "agora",
         "acao": "É a única alavanca que", "acao2": "responde nesta semana.",
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
        b.append(txt(x + 26, by + 252, "QUEM CONTROLA", 11.5, "700", GRAY_LIGHT))
        b.append(txt(x + 26, by + 280, c["quem"], 17, "700", ACCENT if c["hl"] else GRAY))

        b.append(txt(x + 26, by + 328, "EM QUE PRAZO", 11.5, "700", GRAY_LIGHT))
        b.append(txt(x + 26, by + 364, c["prazo"], 28, "700", ACCENT if c["hl"] else GRAY_LIGHT))

        b.append(line(x + 26, by + bh - 82, x + cw - 26, by + bh - 82, BORDER, 1))
        b.append(txt(x + 26, by + bh - 52, c["acao"], 13.5, "400", GRAY_LIGHT, style="italic"))
        b.append(txt(x + 26, by + bh - 32, c["acao2"], 13.5, "400", GRAY_LIGHT, style="italic"))

    fy = by + bh + 30
    b.append(rect(60, fy, W - 120, 62, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, fy + 39, "E é justamente onde quase ninguém trabalha: a discussão pública está em aparecer, não em ser inequívoco.", 17, "400", NAVY))

    footer(b, W, H, "Decomposição a partir de The Anatomy of Uncertainty in LLMs (arXiv 2603.24967). O mapeamento para distribuição é do autor.")
    return doc(W, H, "\n".join(b))


# ------------------------------------------------- 2. quatro camadas
def v2():
    W, H = 1600, 980
    b = []
    header(b, "ONDE A AMBIGUIDADE AGE", "Quatro camadas, quatro literaturas",
           "Medidas por campos que não se citam entre si — o que sugere um mecanismo comum por baixo", H)

    rows = [
        {"n": "1", "t": "A máquina consegue usar você sem errar?",
         "campo": "geração de código",
         "dado": "+40 pontos", "dadol": "linguagem restrita sobre Python, em tarefas multi-passo",
         "nota": "A variável não é familiaridade. É quantos caminhos válidos você deixa em aberto."},
        {"n": "2", "t": "A máquina distingue você do concorrente?",
         "campo": "seleção de ferramenta",
         "dado": "73%", "dadol": "dos servidores analisados têm nome de ferramenta repetido",
         "nota": "Sua distinção depende do que os outros nomearam. Não existe equivalente disso no PLG."},
        {"n": "3", "t": "A máquina sabe quem você é?",
         "campo": "ligação de entidade",
         "dado": "atribuição suprimida", "dadol": "quando a desambiguação de nome falha",
         "nota": "O resultado não é ser citado errado. É não ser citado — falha silenciosa."},
        {"n": "4", "t": "O que a máquina aprende sobre você?",
         "campo": "qualidade de corpus",
         "dado": "conflito intra-memória", "dadol": "incongruência no treino vira inconsistência nos pesos",
         "nota": "Duas versões da sua API no corpus ensinam versões concorrentes de você mesmo."},
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
    b.append(txt(88, fy + 30, "O QUE AMBIGUIDADE NÃO EXPLICA", 12.5, "700", ACCENT))
    b.append(txt(88, fy + 56, "Comunidade, economia e presença acumulada em dado de treino. Uma variável que explica tudo não explica nada.", 16, "400", NAVY))

    footer(b, W, H, "Fontes: arXiv 2512.23214 (Anka) · arXiv 2602.18914 (descrições MCP, preprint) · literatura de entity disambiguation · arXiv 2403.08319.")
    return doc(W, H, "\n".join(b))


# ------------------------------------------------- 3. a inversão
def v3():
    W, H = 1600, 810
    b = []
    header(b, "O PONTO EM QUE AS DUAS OTIMIZAÇÕES DIVERGEM",
           "O que atrai o humano confunde a máquina",
           "Até aqui os dois interesses vinham convergindo. Na estratégia de conteúdo, não", H)

    bw, bh, by = 620, 340, 200
    xl, xr = 60, W - 60 - bw

    b.append(rect(xl, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xl, by, bw, 6, GREEN, rx=0))
    b.append(txt(xl + 30, by + 50, "O HUMANO PRECISA DE", 12.5, "700", GREEN))
    b.append(lines(xl + 30, by + 92, ["Repetição em formatos", "variados"], 23, "700", NAVY, 30))
    b.append(lines(xl + 30, by + 176, [
        "Ele esquece e se distrai. A mesma ideia precisa",
        "encontrá-lo no feed, no e-mail e no vídeo curto,",
        "e cada encontro reforça o anterior.",
        "",
        "Atomização é alcance."], 14.5, "400", GRAY, 22))

    b.append(rect(xr, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xr, by, bw, 6, RED, rx=0))
    b.append(txt(xr + 30, by + 50, "A MÁQUINA PRECISA DE", 12.5, "700", RED))
    b.append(lines(xr + 30, by + 92, ["Afirmação única", "e consistente"], 23, "700", NAVY, 30))
    b.append(lines(xr + 30, by + 176, [
        "Doze peças que dizem o mesmo ocupam capacidade.",
        "Cada adaptação simplifica diferente, e simplificações",
        "incompatíveis viram conflito nos pesos.",
        "",
        "Atomização é ruído com custo."], 14.5, "400", GRAY, 22))

    cy = by + bh / 2
    mx = W / 2
    b.append(f'<path d="M{mx-40},{cy-14} l-28,0 m5,-5 l-5,5 l5,5" stroke="{GRAY_LIGHT}" stroke-width="2.5" fill="none"/>')
    b.append(f'<path d="M{mx+40},{cy-14} l28,0 m-5,-5 l5,5 l-5,5" stroke="{GRAY_LIGHT}" stroke-width="2.5" fill="none"/>')

    ly = by + bh + 36
    b.append(rect(60, ly, W - 120, 108, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, ly + 32, "A VERSÃO PRECISA — E O CONTRAPONTO QUE A PRODUZIU", 12.5, "700", AMBER))
    b.append(txt(88, ly + 62, "Não é que menos conteúdo seja melhor. É que conteúdo que diz coisas diferentes vale mais que conteúdo que diz o mesmo de doze jeitos.", 16.5, "400", NAVY))
    b.append(txt(88, ly + 88, "Há pesquisa mostrando que remover quase-duplicatas piora o treino — elas diferem em semântica. O que pesa é variação de conteúdo, não de formato.", 14, "400", GRAY))

    footer(b, W, H, "Encaminhamento proposto: separar os circuitos. Conteúdo humano nos canais humanos; fonte canônica única na superfície de máquina.")
    return doc(W, H, "\n".join(b))


# ------------------------------------------------- 4. AGENTS.md x llms.txt
def v4():
    W, H = 1600, 780
    b = []
    header(b, "MESMO FORMATO, MESMO ESFORÇO, DESTINOS OPOSTOS",
           "AGENTS.md e llms.txt",
           "A diferença não está na qualidade do arquivo. Está em onde ele fica", H)

    bw, bh, by = 700, 330, 195
    xl, xr = 60, W - 60 - bw

    b.append(rect(xl, by, bw, bh, PANEL, BORDER, 1))
    b.append(rect(xl, by, bw, 6, MUTED, rx=0))
    b.append(txt(xl + 30, by + 52, "llms.txt", 26, "700", NAVY, family="Liberation Mono, monospace"))
    b.append(txt(xl + 30, by + 84, "Markdown na raiz do domínio", 14, "400", GRAY_LIGHT, style="italic"))
    b.append(txt(xl + 30, by + 150, "97%", 46, "700", GRAY_LIGHT))
    b.append(txt(xl + 30, by + 180, "dos arquivos com zero requisições em maio de 2026", 14.5, "400", GRAY))
    b.append(txt(xl + 30, by + 232, "Sem padrão formal. O Google declarou que não", 14, "400", GRAY))
    b.append(txt(xl + 30, by + 254, "afeta ranking de busca — e depois o colocou na", 14, "400", GRAY))
    b.append(txt(xl + 30, by + 276, "auditoria de navegação agêntica do Lighthouse.", 14, "400", GRAY))

    b.append(rect(xr, by, bw, bh, ACCENT_SOFT, ACCENT, 2))
    b.append(rect(xr, by, bw, 6, ACCENT, rx=0))
    b.append(txt(xr + 30, by + 52, "AGENTS.md", 26, "700", NAVY, family="Liberation Mono, monospace"))
    b.append(txt(xr + 30, by + 84, "Markdown na raiz do repositório", 14, "400", GRAY_LIGHT, style="italic"))
    b.append(txt(xr + 30, by + 150, "60 mil+", 46, "700", ACCENT))
    b.append(txt(xr + 30, by + 180, "repositórios, contra 20 mil em agosto de 2025", 14.5, "400", GRAY))
    b.append(txt(xr + 30, by + 232, "Padrão formalizado por OpenAI, Google, Cursor,", 14, "400", GRAY))
    b.append(txt(xr + 30, by + 254, "Factory e Sourcegraph. Sob a Agentic AI Foundation.", 14, "400", GRAY))
    b.append(txt(xr + 30, by + 276, "Lido nativamente por mais de 30 ferramentas.", 14, "400", GRAY))

    ly = by + bh + 38
    b.append(rect(60, ly, W - 120, 130, AMBER_SOFT, AMBER, 1.5))
    b.append(txt(88, ly + 34, "A EXPLICAÇÃO", 12.5, "700", AMBER))
    b.append(txt(88, ly + 66, "O AGENTS.md fica onde o agente já está — dentro do repositório que ele foi encarregado de editar.", 17, "400", NAVY))
    b.append(txt(88, ly + 92, "O llms.txt fica onde alguém precisa mandar o agente ir.", 17, "400", NAVY))
    b.append(txt(88, ly + 118, "Legibilidade por máquina não é publicar um artefato legível. É colocá-lo no trajeto que o agente já percorre.", 15, "700", ACCENT))

    footer(b, W, H, "Fontes: Ahrefs (137 mil domínios) · Codersera · Search Engine Land e Chrome for Developers (Lighthouse, maio de 2026).")
    return doc(W, H, "\n".join(b))


# ------------------------------------------------- 5. quadro de evidência
def v5():
    W, H = 1600, 950
    b = []
    header(b, "O QUE ESTÁ SUSTENTADO E O QUE NÃO ESTÁ",
           "Quadro de evidência deste artigo",
           "Uma afirmação sem status epistêmico declarado é uma afirmação sem endereço", H)

    rows = [
        ["Sintaxe restrita supera linguagem conhecida", "Experimento publicado", "arXiv 2512.23214, validado em 2 modelos", ACCENT],
        ["73% dos servidores MCP têm nome repetido", "Levantamento", "arXiv 2602.18914 — preprint, 10 mil+ servidores", ACCENT],
        ["Desambiguação falha suprime a atribuição", "Mecanismo documentado", "literatura de entity linking; sem número de perda", AMBER],
        ["Incongruência no corpus vira conflito nos pesos", "Revisão de literatura", "arXiv 2403.08319", ACCENT],
        ["Fatos competem por capacidade do modelo", "Experimento", "arXiv 2604.08519 — modelos pequenos, pré-treino do zero", AMBER],
        ["Dados estruturados melhoram citação", "EM CONFLITO", "Ahrefs não encontra efeito; arXiv encontra +29,6%", AMBER],
        ["Markdown reduz tokens", "Faixa sem padrão", "de 25% a 87% entre estudos — não é margem de erro", AMBER],
        ["Custo de contexto é decisão de retenção", "Raciocínio do autor", "nenhuma fonte trata assim", GRAY_LIGHT],
        ["Separar circuito humano e circuito canônico", "Raciocínio do autor", "sem dado de conversão publicado", GRAY_LIGHT],
        ["Ambiguidade afeta o conhecimento paramétrico", "Pergunta em aberto", "não encontrei estudo que meça", GRAY_LIGHT],
    ]
    heads = ["AFIRMAÇÃO", "STATUS", "BASE"]
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
    b.append(txt(88, ry + 34, "O QUE ISSO CUSTA", 12.5, "700", AMBER))
    b.append(txt(88, ry + 58, "Três das dez afirmações são raciocínio meu ou pergunta em aberto. Preferi dizer isso a apresentar tudo com a mesma confiança.", 15.5, "400", NAVY))

    footer(b, W, H, "Builder-Led Growth, parte 3 — pilar 1, legibilidade por máquina.")
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

    b.append(f'<text x="120" y="196" font-family="{FONT}" font-size="26" font-weight="700" fill="{ACCENT_LIGHT}" letter-spacing="4">BUILDER-LED GROWTH — PARTE 3</text>')
    b.append(f'<line x1="120" y1="224" x2="620" y2="224" stroke="{ACCENT}" stroke-width="3"/>')

    b.append(txt(114, 344, "O imposto que a máquina", 86, "700", WHITE))
    b.append(txt(114, 444, "cobra e o humano não vê", 86, "700", WHITE))
    b.append(txt(118, 520, "Pilar 1 — legibilidade por máquina, e a variável que decide", 44, "400", GL))

    bw, bh, gap = 400, 118, 46
    y = 618
    labels = [("EXECUÇÃO", "usar sem errar"),
              ("SELEÇÃO", "distinguir do concorrente"),
              ("IDENTIDADE", "saber quem você é")]
    for i, (t, s) in enumerate(labels):
        x = 120 + i * (bw + gap)
        b.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="14" fill="none" '
                 f'stroke="{GL}" stroke-opacity="0.45" stroke-width="2"/>')
        b.append(txt(x + bw / 2, y + 50, t, 26, "700", GL, "middle"))
        b.append(txt(x + bw / 2, y + 84, s, 19, "400", GL, "middle", style="italic"))

    y2 = y + bh + 18
    b.append(f'<rect x="120" y="{y2}" width="{3*bw+2*gap}" height="{bh}" rx="14" fill="{ACCENT}" '
             f'fill-opacity="0.18" stroke="{ACCENT_LIGHT}" stroke-width="3"/>')
    b.append(txt(120 + (3*bw+2*gap) / 2, y2 + 50, "CONHECIMENTO", 26, "700", WHITE, "middle"))
    b.append(txt(120 + (3*bw+2*gap) / 2, y2 + 84, "o que ela acaba aprendendo a seu respeito", 19, "400", ACCENT_LIGHT, "middle", style="italic"))

    ly = y2 + bh + 30
    b.append(f'<rect x="120" y="{ly}" width="{3*bw+2*gap}" height="66" rx="12" fill="{AMBER_C}" fill-opacity="0.16" stroke="{AMBER_C}" stroke-width="2"/>')
    b.append(txt(150, ly + 43, "O humano resolve ambiguidade de graça. A máquina escolhe outro.", 26, "400", WHITE))

    b.append(f'<line x1="120" y1="{H-70}" x2="{W-120}" y2="{H-70}" stroke="{ACCENT}" stroke-opacity="0.5" stroke-width="1.5"/>')
    b.append(txt(120, H - 34, "Matheus Ramos · com AGENTS.md, Anka, Go/Golang, WebMCP e sete estudos", 23, "400", GL))

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(b)}</svg>'
    p = os.path.join(OUT, "p3-capa-pt.svg")
    open(p, "w", encoding="utf-8").write(svg)
    cairosvg.svg2png(url=p, write_to=os.path.join(OUT, "p3-capa-pt.png"), scale=1.5)
    print("ok: p3-capa-pt")


if __name__ == "__main__":
    save("p3-tres-fontes-incerteza-pt", v1())
    save("p3-quatro-camadas-ambiguidade-pt", v2())
    save("p3-inversao-humano-maquina-pt", v3())
    save("p3-agents-md-vs-llms-txt-pt", v4())
    save("p3-quadro-evidencia-pt", v5())
    cover()
    print("done")
