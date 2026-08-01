#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais da parte 4 — Builder-Led Growth, pilar 2: acessibilidade operacional.

DIFERENÇA EM RELAÇÃO ÀS PARTES ANTERIORES: este arquivo gera PT e EN. As partes
1, 2 e 3 têm um gerador por língua, e isso é uma fonte de deriva — corrigir um
número num arquivo e esquecer o outro é exatamente o problema que
scripts/verificar-paridade.py existe para pegar nos artigos. Aqui os números
vivem uma vez só, no dicionário de dados, e só o texto muda por língua.

Uso:  python3 scripts/gen_p4.py          # gera PT e EN
      python3 scripts/gen_p4.py pt       # só português
"""
import os
import sys

import cairosvg

OUT = os.path.dirname(os.path.abspath(__file__))
FONT = "Liberation Sans, Arial, sans-serif"

NAVY = "#16213E"
NAVY_DEEP = "#101A30"
GRAY = "#5B6472"
GRAY_LIGHT = "#8B93A1"
BG = "#FFFFFF"
PANEL = "#F7F8FA"
BORDER = "#DEE2E7"
ACCENT = "#2F5D8A"
ACCENT_LIGHT = "#6E9CC4"
ACCENT_SOFT = "#E7EEF4"
AMBER = "#B8792E"
AMBER_SOFT = "#F5EBDD"
GREEN = "#2F7D5D"
GREEN_SOFT = "#E6F0EA"
MUTED = "#C7CDD5"
WHITE = "#FFFFFF"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=16, weight="400", fill=NAVY, anchor="start", style="normal", sp=None):
    spa = f' letter-spacing="{sp}"' if sp else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" font-style="{style}" fill="{fill}" '
            f'text-anchor="{anchor}"{spa}>{esc(s)}</text>')


def lines(x, y, arr, size=14, weight="400", fill=GRAY, lh=21, anchor="start", style="normal"):
    return "\n".join(txt(x, y + i * lh, l, size, weight, fill, anchor, style)
                     for i, l in enumerate(arr))


def rect(x, y, w, h, fill, stroke=None, sw=1, rx=10, op=None):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' fill-opacity="{op}"' if op else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{o}{s}/>'


def line(x1, y1, x2, y2, stroke=BORDER, w=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{w}"{d}/>'


def circle(cx, cy, r, fill, stroke=None, sw=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}/>'


def arrow(x1, y1, x2, y2, stroke=MUTED, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{w}"{d} marker-end="url(#a)"/>')


def defs():
    return ('<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{MUTED}"/></marker></defs>')


def doc(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'{defs()}<rect x="0" y="0" width="{w}" height="{h}" fill="{BG}"/>{body}</svg>')


def header(b, kicker, title, sub, h):
    b.append(rect(0, 0, 10, h, ACCENT, rx=0))
    b.append(txt(60, 66, kicker, 14, "700", ACCENT, sp="2"))
    b.append(txt(60, 106, title, 30, "700", NAVY))
    b.append(txt(60, 138, sub, 17, "400", GRAY, style="italic"))


def footer(b, w, h, note):
    b.append(line(60, h - 66, w - 60, h - 66, BORDER, 1))
    b.append(txt(60, h - 40, note, 12.5, "400", GRAY_LIGHT))


def save(name, svg, scale=2):
    p = os.path.join(OUT, f"{name}.svg")
    open(p, "w", encoding="utf-8").write(svg)
    cairosvg.svg2png(url=p, write_to=os.path.join(OUT, f"{name}.png"), scale=scale)
    print("ok:", name)


# ---------------------------------------------------------------- textos
# Os NÚMEROS ficam fora deste dicionário, nas funções, para existirem uma vez só.
T = {
    "pt": {
        "suf": "pt",
        "capa_kicker": "BUILDER-LED GROWTH — PARTE 4",
        "capa_t1": "Quantas vezes o agente",
        "capa_t2": "precisa chamar um humano",
        "capa_sub": "Pilar 2 — acessibilidade operacional",
        "capa_saidas": ["RESPONDE NA HORA", "RESPONDE DEPOIS", "SEGUE SEM VOCÊ"],
        "capa_saidas_sub": ["adotado", "contexto perdido", "sem registro"],
        "capa_faixa": "A terceira saída não gera log, nem erro, nem ticket — e o tamanho dela é desconhecido.",
        "capa_rodape": "Matheus Ramos · com dados de Vercel, KPMG, GitGuardian, Cloudflare e a especificação MCP de 28/07/2026",

        "v1_nome": "p4-tres-saidas-parada-pt",
        "v1_kicker": "CADA PARADA HUMANA",
        "v1_titulo": "As três saídas, e só uma é boa",
        "v1_sub": "O que acontece quando o fluxo exige uma pessoa no meio do caminho",
        "v1_parada": "PARADA",
        "v1_parada_sub": ["criar conta", "confirmar e-mail", "gerar chave", "colar cartão"],
        "v1_boxes": [
            ("O humano responde na hora", ["O agente continua.", "Você foi adotado."], "bom"),
            ("O humano responde depois", ["A sessão terminou.", "O contexto se perdeu."], "meio"),
            ("O agente segue com outra coisa", ["Sem log. Sem erro. Sem ticket.", "Abandonado sem registro."], "invisivel"),
        ],
        "v1_selo": "INVISÍVEL NA SUA INSTRUMENTAÇÃO",
        "v1_rodape": "Frequência de cada saída: desconhecida. Por construção, a terceira não aparece nos dados de quem a sofre.",

        "v2_nome": "p4-atrito-muda-de-lugar-pt",
        "v2_kicker": "O ATRITO NÃO DESAPARECE",
        "v2_titulo": "Ele reaparece na forma mais barata disponível",
        "v2_sub": "Sem caminho de autenticação que a máquina percorra sozinha",
        "v2_esq_t": "O que falta",
        "v2_esq": ["Credencial que a máquina", "não consegue obter sozinha.", "",
                   "Emissão sem processo:", "78% das organizações sem", "política documentada."],
        "v2_dir_t": "Onde reaparece",
        "v2_dir_leg": ["novos segredos colados dentro de", "código no GitHub público, em 2025"],
        "v2_dir_d1": "sobre o ano anterior",
        "v2_dir_d2": "em credenciais de serviços de IA",
        "v2_seta": "o atrito migra",
        "v2_faixa": "E a chave que vaza é a sua.",
        "v2_rodape": "Fontes: GitGuardian (2025) · Cloud Security Alliance · KPMG. A ligação causal entre atrito e vazamento é raciocínio nosso, não estudo.",

        "v3_nome": "p4-custo-de-estar-disponivel-pt",
        "v3_kicker": "O CUSTO PERMANENTE DE ESTAR DISPONÍVEL",
        "v3_titulo": "Três formatos, três ordens de grandeza",
        "v3_sub": "Tokens gastos antes de qualquer chamada — pagos pelo cliente, toda sessão",
        "v3_barras": [
            ("Três servidores MCP", "~40 ferramentas expostas"),
            ("50 Agent Skills instaladas", "revelação progressiva em três estágios"),
            ("Code Mode (Cloudflare)", "~2.500 endpoints via SDK tipado"),
        ],
        "v3_escala": "tokens, em escala logarítmica — as barras comparam ordem de grandeza, não proporção direta",
        "v3_faixa": "A escolha do formato é decisão de distribuição, não de engenharia.",
        "v3_rodape": "Números de blog técnico e de material de quem tem produto no assunto. A ordem de grandeza se repete entre fontes; o valor exato, não.",

        "v4_nome": "p4-quem-ja-esta-em-producao-pt",
        "v4_kicker": "JÁ ESTÁ EM PRODUÇÃO",
        "v4_titulo": "Stripe Projects e as três exigências",
        "v4_sub": "Lançado em 30 de abril de 2026 — as exigências são as três paradas deste artigo",
        "v4_centro": "STRIPE PROJECTS",
        "v4_centro_sub": "agentes agindo em nome de donos humanos",
        "v4_exig": [
            ("Conta", ["Onboarding programático", "de agente autenticado"]),
            ("Catálogo", ["Planos em estrutura que", "o agente lê, não página"]),
            ("Cobrança", ["Upgrade e cancelamento", "iniciados por agente"]),
        ],
        "v4_parc_t": "PARCEIROS DE LANÇAMENTO E INTEGRADOS",
        "v4_trilhos_t": "TRILHOS DE PAGAMENTO PARA NÃO-HUMANOS",
        "v4_trilhos": ["Stripe Link Wallet for Agents — 29/04/2026",
                       "Stripe Issuing for Agents — 30/04/2026",
                       "AWS Bedrock AgentCore Payments — 07/05/2026"],
        "v4_rodape": "O catálogo legível por máquina era, na parte 2, um detalhe simpático da Firecrawl. Virou requisito de protocolo.",

        "v5_nome": "p4-graduacao-do-laco-pt",
        "v5_kicker": "O LAÇO HUMANO-MÁQUINA",
        "v5_titulo": "Quando o humano deve entrar",
        "v5_sub": "Human-in-the-loop — humano no circuito, em tradução livre",
        "v5_bandas": [
            ("EXECUÇÃO AUTOMÁTICA", "leitura e verificação", "sem parada", GREEN, GREEN_SOFT),
            ("ESCALAÇÃO ASSÍNCRONA", "dado conflitante ou informação faltando", "registra, enfileira e segue", ACCENT, ACCENT_SOFT),
            ("APROVAÇÃO OBRIGATÓRIA", "ação irreversível, custo alto, exceção regulatória", "portão síncrono: para e espera", AMBER, AMBER_SOFT),
        ],
        "v5_crit_t": "CRITÉRIO",
        "v5_crit": "Pause exatamente onde o custo do erro passa a exceder o custo da interrupção.",
        "v5_prop_t": "O QUE ACRESCENTAMOS",
        "v5_prop": ["A variável a otimizar não é o número de paradas.",
                    "É quanto de contexto se perde em cada uma."],
        "v5_rodape": "Proposta nossa, não prática validada. O custo humano de aprovar tudo pode exceder o custo de fazer a tarefa à mão.",
    },
    "en": {
        "suf": "en",
        "capa_kicker": "BUILDER-LED GROWTH — PART 4",
        "capa_t1": "How many times the agent",
        "capa_t2": "has to call a human",
        "capa_sub": "Pillar 2 — operational accessibility",
        "capa_saidas": ["ANSWERS RIGHT AWAY", "ANSWERS LATER", "MOVES ON WITHOUT YOU"],
        "capa_saidas_sub": ["adopted", "context lost", "no record"],
        "capa_faixa": "The third ending leaves no log, no error and no ticket — and its size is unknown.",
        "capa_rodape": "Matheus Ramos · with data from Vercel, KPMG, GitGuardian, Cloudflare and the MCP specification of 28 July 2026",

        "v1_nome": "p4-three-endings-en",
        "v1_kicker": "EVERY HUMAN STOP",
        "v1_titulo": "Three endings, and only one is good",
        "v1_sub": "What happens when the flow requires a person halfway through",
        "v1_parada": "STOP",
        "v1_parada_sub": ["create account", "confirm email", "generate key", "paste card"],
        "v1_boxes": [
            ("The human answers right away", ["The agent continues.", "You were adopted."], "bom"),
            ("The human answers later", ["The session ended.", "The context is gone."], "meio"),
            ("The agent moves on to something else", ["No log. No error. No ticket.", "Abandoned with no record."], "invisivel"),
        ],
        "v1_selo": "INVISIBLE TO YOUR INSTRUMENTATION",
        "v1_rodape": "Frequency of each ending: unknown. By construction, the third one never appears in the data of whoever it happens to.",

        "v2_nome": "p4-friction-moves-en",
        "v2_kicker": "FRICTION DOESN'T DISAPPEAR",
        "v2_titulo": "It reappears in the cheapest form available",
        "v2_sub": "With no authentication path a machine can walk on its own",
        "v2_esq_t": "What's missing",
        "v2_esq": ["A credential the machine", "cannot obtain on its own.", "",
                   "Issuing with no process:", "78% of organisations have no", "documented policy."],
        "v2_dir_t": "Where it reappears",
        "v2_dir_leg": ["new secrets pasted directly into", "code on public GitHub, in 2025"],
        "v2_dir_d1": "year over year",
        "v2_dir_d2": "in AI service credentials",
        "v2_seta": "friction migrates",
        "v2_faixa": "And the key that leaks is yours.",
        "v2_rodape": "Sources: GitGuardian (2025) · Cloud Security Alliance · KPMG. The causal link between friction and leakage is our reasoning, not a study.",

        "v3_nome": "p4-cost-of-being-available-en",
        "v3_kicker": "THE PERMANENT COST OF BEING AVAILABLE",
        "v3_titulo": "Three formats, three orders of magnitude",
        "v3_sub": "Tokens spent before any call — paid by the customer, every session",
        "v3_barras": [
            ("Three MCP servers", "~40 tools exposed"),
            ("50 Agent Skills installed", "progressive disclosure in three stages"),
            ("Code Mode (Cloudflare)", "~2,500 endpoints via typed SDK"),
        ],
        "v3_escala": "tokens, on a logarithmic scale — bars compare order of magnitude, not direct proportion",
        "v3_faixa": "The format you choose is a distribution decision, not an engineering one.",
        "v3_rodape": "Numbers from technical blogs and from vendors with a product in the space. The order of magnitude repeats across sources; the exact value doesn't.",

        "v4_nome": "p4-already-in-production-en",
        "v4_kicker": "ALREADY IN PRODUCTION",
        "v4_titulo": "Stripe Projects and its three requirements",
        "v4_sub": "Launched 30 April 2026 — the requirements are this article's three stops",
        "v4_centro": "STRIPE PROJECTS",
        "v4_centro_sub": "agents acting on behalf of human owners",
        "v4_exig": [
            ("Account", ["Programmatic onboarding", "from an authenticated agent"]),
            ("Catalogue", ["Plans in a structure the", "agent reads, not a page"]),
            ("Billing", ["Upgrades and cancellations", "initiated by an agent"]),
        ],
        "v4_parc_t": "LAUNCH PARTNERS AND INTEGRATIONS",
        "v4_trilhos_t": "PAYMENT RAILS FOR NON-HUMANS",
        "v4_trilhos": ["Stripe Link Wallet for Agents — 29 April 2026",
                       "Stripe Issuing for Agents — 30 April 2026",
                       "AWS Bedrock AgentCore Payments — 7 May 2026"],
        "v4_rodape": "In part 2 the machine-readable catalogue was a charming detail from Firecrawl. It became a protocol requirement.",

        "v5_nome": "p4-loop-graduation-en",
        "v5_kicker": "THE HUMAN-MACHINE LOOP",
        "v5_titulo": "When the human should step in",
        "v5_sub": "Human-in-the-loop: execution pauses for a human decision at defined points",
        "v5_bandas": [
            ("AUTOMATIC EXECUTION", "reading and checking", "no stop", GREEN, GREEN_SOFT),
            ("ASYNCHRONOUS ESCALATION", "conflicting data or missing information", "records, queues and carries on", ACCENT, ACCENT_SOFT),
            ("MANDATORY APPROVAL", "irreversible action, high cost, regulatory exception", "synchronous gate: stops and waits", AMBER, AMBER_SOFT),
        ],
        "v5_crit_t": "CRITERION",
        "v5_crit": "Pause exactly where the cost of the error starts to exceed the cost of the interruption.",
        "v5_prop_t": "WHAT WE ADD",
        "v5_prop": ["The variable to optimise isn't the number of stops.",
                    "It's how much context is lost at each one."],
        "v5_rodape": "Our proposal, not validated practice. The human cost of approving everything can exceed the cost of doing the task by hand.",
    },
}

# Números — existem uma vez só, compartilhados pelas duas línguas.
N_SEGREDOS = "28,65"        # milhões (PT) / 28.65 million (EN)
N_ALTA = "34%"
N_IA = "81,5%"
BARRAS_TOKENS = [144_000, 5_000, 1_000]


def num(v, lang):
    """Formata milhar conforme a língua."""
    s = f"{v:,}"
    return s.replace(",", ".") if lang == "pt" else s


# --------------------------------------------------------------- 1. três saídas
def v1(t, lang):
    W, H = 1600, 860
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    px, py, pw, ph = 60, 314, 300, 300
    b.append(rect(px, py, pw, ph, PANEL, BORDER, 1.5, rx=14))
    b.append(txt(px + pw / 2, py + 62, t["v1_parada"], 22, "700", NAVY, anchor="middle", sp="3"))
    b.append(line(px + 60, py + 86, px + pw - 60, py + 86, BORDER))
    b.append(lines(px + pw / 2, py + 128, t["v1_parada_sub"], 14.5, "400", GRAY, 30, anchor="middle"))

    bx, bw, bh = 560, 960, 82
    tops = [250, 380, 510]
    estilos = {"bom": (GREEN, GREEN_SOFT, 1.5), "meio": (AMBER, AMBER_SOFT, 1.5),
               "invisivel": (NAVY_DEEP, NAVY_DEEP, 2.5)}
    for i, (titulo, corpo, tipo) in enumerate(t["v1_boxes"]):
        cor, fundo, sw = estilos[tipo]
        y = tops[i]
        alt = bh + (86 if tipo == "invisivel" else 26)
        b.append(rect(bx, y, bw, alt, fundo, cor, sw, rx=12))
        tcor = WHITE if tipo == "invisivel" else NAVY
        ccor = "#AEB6C2" if tipo == "invisivel" else GRAY
        b.append(txt(bx + 34, y + 40, titulo, 21, "700", tcor))
        b.append(lines(bx + 34, y + 70, corpo, 15, "400", ccor, 24))
        if tipo == "invisivel":
            b.append(rect(bx + 34, y + alt - 44, 470, 30, AMBER, rx=6, op="0.9"))
            b.append(txt(bx + 50, y + alt - 23, t["v1_selo"], 13, "700", WHITE, sp="1.5"))
        b.append(arrow(px + pw + 16, py + ph / 2, bx - 14, y + alt / 2,
                       cor if tipo != "invisivel" else NAVY_DEEP, 2,
                       None if tipo == "bom" else "6 5"))

    footer(b, W, H, t["v1_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------------ 2. atrito muda de lugar
def v2(t, lang):
    W, H = 1600, 860
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    y, h = 235, 400
    lw = 560
    b.append(rect(60, y, lw, h, PANEL, BORDER, 1.5, rx=14))
    b.append(txt(96, y + 52, t["v2_esq_t"], 20, "700", NAVY))
    b.append(line(96, y + 72, 60 + lw - 36, y + 72, BORDER))
    b.append(lines(96, y + 108, t["v2_esq"], 15.5, "400", GRAY, 27))

    rx0, rw = 780, 760
    b.append(rect(rx0, y, rw, h, NAVY_DEEP, None, rx=14))
    b.append(txt(rx0 + 36, y + 52, t["v2_dir_t"], 20, "700", WHITE))
    b.append(line(rx0 + 36, y + 72, rx0 + rw - 36, y + 72, "#2C3A55"))
    b.append(txt(rx0 + 36, y + 168, N_SEGREDOS if lang == "pt" else "28.65", 92, "700", WHITE))
    b.append(txt(rx0 + 300, y + 168, "milhões" if lang == "pt" else "million", 30, "400", ACCENT_LIGHT))
    b.append(lines(rx0 + 36, y + 208, t["v2_dir_leg"], 15.5, "400", "#AEB6C2", 24))

    b.append(rect(rx0 + 36, y + 262, 330, 96, AMBER, rx=10, op="0.16"))
    b.append(rect(rx0 + 36, y + 262, 330, 96, "none", AMBER, 1.5, rx=10))
    b.append(txt(rx0 + 60, y + 314, "+" + N_ALTA, 40, "700", AMBER))
    b.append(txt(rx0 + 60, y + 342, t["v2_dir_d1"], 13.5, "400", "#AEB6C2"))
    b.append(rect(rx0 + 394, y + 262, 330, 96, AMBER, rx=10, op="0.16"))
    b.append(rect(rx0 + 394, y + 262, 330, 96, "none", AMBER, 1.5, rx=10))
    b.append(txt(rx0 + 418, y + 314, "+" + (N_IA if lang == "pt" else "81.5%"), 40, "700", AMBER))
    b.append(txt(rx0 + 418, y + 342, t["v2_dir_d2"], 13.5, "400", "#AEB6C2"))

    b.append(arrow(636, y + h / 2, 764, y + h / 2, ACCENT, 3))
    b.append(txt(700, y + h / 2 - 22, t["v2_seta"], 14, "700", ACCENT, anchor="middle"))

    b.append(rect(60, y + h + 34, W - 120, 62, AMBER, rx=10, op="0.14"))
    b.append(rect(60, y + h + 34, W - 120, 62, "none", AMBER, 1.5, rx=10))
    b.append(txt(96, y + h + 73, t["v2_faixa"], 22, "700", NAVY))

    footer(b, W, H, t["v2_rodape"])
    return doc(W, H, "".join(b))


# -------------------------------------------- 3. custo de estar disponível
def v3(t, lang):
    import math
    W, H = 1600, 820
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    x0, maxw = 540, 900
    topo = 250
    lo, hi = math.log10(min(BARRAS_TOKENS)), math.log10(max(BARRAS_TOKENS))
    cores = [AMBER, ACCENT, GREEN]
    for i, ((rot, sub), val) in enumerate(zip(t["v3_barras"], BARRAS_TOKENS)):
        y = topo + i * 130
        frac = (math.log10(val) - lo) / (hi - lo)
        w = 120 + frac * (maxw - 120)
        b.append(txt(60, y + 34, rot, 19, "700", NAVY))
        b.append(txt(60, y + 60, sub, 14, "400", GRAY_LIGHT))
        b.append(rect(x0, y + 6, maxw, 62, PANEL, BORDER, 1, rx=8))
        b.append(rect(x0, y + 6, w, 62, cores[i], rx=8, op="0.85"))
        rot = num(val, lang)
        # barra longa nao deixa espaco a direita: o rotulo entra dentro dela
        if w > maxw - 200:
            b.append(txt(x0 + w - 24, y + 46, rot, 22, "700", WHITE, anchor="end"))
        else:
            b.append(txt(x0 + w + 20, y + 46, rot, 22, "700", NAVY))
    b.append(txt(x0, topo + 3 * 130 + 6, t["v3_escala"], 13, "400", GRAY_LIGHT, style="italic"))

    fy = topo + 3 * 130 + 44
    b.append(rect(60, fy, W - 120, 66, ACCENT, rx=10, op="0.10"))
    b.append(rect(60, fy, W - 120, 66, "none", ACCENT, 1.5, rx=10))
    b.append(txt(96, fy + 42, t["v3_faixa"], 21, "700", NAVY))

    footer(b, W, H, t["v3_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------------- 4. já está em produção
def v4(t, lang):
    W, H = 1600, 750
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    cx, cy, cw, ch = 60, 240, 420, 150
    b.append(rect(cx, cy, cw, ch, NAVY_DEEP, None, rx=14))
    b.append(txt(cx + cw / 2, cy + 68, t["v4_centro"], 26, "700", WHITE, anchor="middle", sp="2"))
    b.append(txt(cx + cw / 2, cy + 100, t["v4_centro_sub"], 14, "400", "#AEB6C2", anchor="middle"))

    ex, ew, eh = 560, 980, 132
    for i, (nome, corpo) in enumerate(t["v4_exig"]):
        y = 210 + i * 152
        b.append(rect(ex, y, ew, eh, PANEL, ACCENT, 1.5, rx=12))
        b.append(circle(ex + 44, y + 44, 20, ACCENT_SOFT, ACCENT, 1.5))
        b.append(txt(ex + 44, y + 51, str(i + 1), 18, "700", ACCENT, anchor="middle"))
        b.append(txt(ex + 82, y + 51, nome, 21, "700", NAVY))
        b.append(lines(ex + 82, y + 82, corpo, 14.5, "400", GRAY, 23))
        b.append(arrow(cx + cw + 14, cy + ch / 2, ex - 14, y + eh / 2, ACCENT, 2, "6 5"))

    py = cy + ch + 40
    b.append(txt(cx, py + 26, t["v4_parc_t"], 12.5, "700", ACCENT, sp="1.5"))
    chips = ["Cloudflare", "Vercel", "Netlify", "Supabase", "PostHog", "Clerk",
             "Neon", "PlanetScale", "Twilio", "Hugging Face"]
    px_, py_ = cx, py + 46
    for c in chips:
        w = 15 + len(c) * 8.2
        if px_ + w > cx + cw:
            px_, py_ = cx, py_ + 40
        b.append(rect(px_, py_, w, 30, ACCENT_SOFT, BORDER, 1, rx=15))
        b.append(txt(px_ + w / 2, py_ + 20, c, 13, "400", ACCENT, anchor="middle"))
        px_ += w + 8

    ty = py_ + 62
    b.append(txt(cx, ty, t["v4_trilhos_t"], 12.5, "700", AMBER, sp="1.5"))
    b.append(lines(cx, ty + 30, t["v4_trilhos"], 13.5, "400", GRAY, 26))

    footer(b, W, H, t["v4_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------------- 5. graduação do laço
def v5(t, lang):
    W, H = 1600, 880
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    y0, bh = 240, 122
    for i, (nome, quando, como, cor, fundo) in enumerate(t["v5_bandas"]):
        y = y0 + i * (bh + 22)
        b.append(rect(60, y, W - 120, bh, fundo, cor, 1.5, rx=12))
        b.append(rect(60, y, 8, bh, cor, rx=0))
        b.append(txt(100, y + 44, nome, 19, "700", cor, sp="1.5"))
        b.append(txt(100, y + 76, quando, 16, "400", NAVY))
        b.append(txt(100, y + 100, como, 13.5, "400", GRAY_LIGHT, style="italic"))
        b.append(txt(W - 96, y + 70, ["1", "2", "3"][i], 46, "700", cor, anchor="end", sp="0"))

    cy = y0 + 3 * (bh + 22) + 12
    b.append(rect(60, cy, 760, 96, PANEL, BORDER, 1.5, rx=12))
    b.append(txt(96, cy + 32, t["v5_crit_t"], 12.5, "700", ACCENT, sp="1.5"))
    b.append(txt(96, cy + 66, t["v5_crit"], 16, "400", NAVY))

    b.append(rect(852, cy, W - 912, 96, AMBER, rx=12, op="0.12"))
    b.append(rect(852, cy, W - 912, 96, "none", AMBER, 1.5, rx=12))
    b.append(txt(888, cy + 32, t["v5_prop_t"], 12.5, "700", AMBER, sp="1.5"))
    b.append(lines(888, cy + 58, t["v5_prop"], 15, "400", NAVY, 22))

    footer(b, W, H, t["v5_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------------------------- capa
def capa(t, lang):
    W, H = 1920, 1080
    b = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="{NAVY_DEEP}"/>']
    for i in range(9):
        x = 1180 + i * 92
        b.append(f'<line x1="{x}" y1="0" x2="{x - 240}" y2="{H}" stroke="{ACCENT}" '
                 f'stroke-opacity="0.10" stroke-width="2"/>')

    b.append(txt(120, 196, t["capa_kicker"], 26, "700", ACCENT_LIGHT, sp="4"))
    b.append(line(120, 224, 470, 224, ACCENT, 3))
    b.append(txt(120, 330, t["capa_t1"], 76, "700", WHITE))
    b.append(txt(120, 420, t["capa_t2"], 76, "700", WHITE))
    b.append(txt(120, 486, t["capa_sub"], 32, "400", "#AEB6C2"))

    bw, gap, by = 520, 40, 600
    cores = [(GREEN, "0.20"), (AMBER, "0.20"), (WHITE, "0.05")]
    for i, nome in enumerate(t["capa_saidas"]):
        x = 120 + i * (bw + gap)
        cor, op = cores[i]
        destaque = i == 2
        b.append(rect(x, by, bw, 176, cor, rx=14, op=op))
        b.append(rect(x, by, bw, 176, "none", cor if not destaque else AMBER,
                      3 if destaque else 1.5, rx=14))
        b.append(txt(x + bw / 2, by + 78, nome, 24, "700",
                     WHITE if destaque else cor, anchor="middle", sp="1.5"))
        b.append(txt(x + bw / 2, by + 120, t["capa_saidas_sub"][i], 19, "400",
                     "#AEB6C2", anchor="middle", style="italic"))

    fy = by + 220
    b.append(rect(120, fy, W - 240, 84, AMBER, rx=12, op="0.16"))
    b.append(rect(120, fy, W - 240, 84, "none", AMBER, 2, rx=12))
    b.append(txt(152, fy + 54, t["capa_faixa"], 27, "400", WHITE))

    b.append(line(120, H - 90, W - 120, H - 90, ACCENT, 1.5))
    b.append(txt(120, H - 48, t["capa_rodape"], 22, "400", "#AEB6C2"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">{"".join(b)}</svg>')


def gerar(lang):
    t = T[lang]
    suf = t["suf"]
    save(f"p4-capa-{suf}" if lang == "pt" else f"p4-cover-{suf}", capa(t, lang), scale=1.5)
    save(t["v1_nome"], v1(t, lang))
    save(t["v2_nome"], v2(t, lang))
    save(t["v3_nome"], v3(t, lang))
    save(t["v4_nome"], v4(t, lang))
    save(t["v5_nome"], v5(t, lang))


if __name__ == "__main__":
    alvos = sys.argv[1:] or ["pt", "en"]
    for lg in alvos:
        gerar(lg)
    print("done")
