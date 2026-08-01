#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais da parte 7 — Builder-Led Growth, pilar 4: confiança e segurança.

PT e EN no mesmo arquivo. Helpers de desenho importados do gen_p4.
Todas as funções terminam com assert de folga contra o rodapé — foi o defeito
recorrente das partes 4, 5 e 6, e agora falha alto em vez de gerar peça torta.

Uso:  python3 scripts/gen_p7.py          # gera PT e EN
      python3 scripts/gen_p7.py pt       # só português
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gen_p4 import (  # noqa: E402
    ACCENT, ACCENT_LIGHT, ACCENT_SOFT, AMBER, AMBER_SOFT, BORDER, GRAY,
    GRAY_LIGHT, GREEN, GREEN_SOFT, MUTED, NAVY, NAVY_DEEP, PANEL, WHITE,
    arrow, circle, doc, footer, header, line, lines, rect, save, txt,
)

W = 1600
RED = "#9C4A3C"
RED_SOFT = "#F5E6E2"

# ---------------------------------------------------------------- números
# Existem uma vez só, nas duas línguas.
CONFIA = [   # rótulo pt, rótulo en, confia muito, desconfia muito
    ("Todos", "All", 3.1, 19.6),
    ("Aprendendo", "Learning", 6.1, 19.7),
    ("Início", "Early", 3.0, 17.5),
    ("Meio", "Mid", 2.8, 19.7),
    ("Experientes", "Experienced", 2.5, 20.7),
]
ATAQUE = 72.8
RECUSA = 3
PEDE_AJUDA = 75.3


def n(pt, en, lang):
    return pt if lang == "pt" else en


T = {
    "pt": {
        "capa_kicker": "BUILDER-LED GROWTH — PARTE 7",
        "capa_t1": "O que faz o agente",
        "capa_t2": "confiar em você",
        "capa_sub": "Pilar 4 — confiança e segurança do modelo",
        "capa_frase1": "A competência que faz o modelo usar bem a sua ferramenta",
        "capa_frase2": "é a mesma que faz ele obedecer à instrução envenenada.",
        "capa_creditof": "MCPTox, 45 servidores reais, 353 ferramentas",
        "capa_rodape": "Matheus Ramos · último artigo do arco 1: os quatro pilares",

        "v1_nome": "p7-variacao-dois-pontos-pt",
        "v1_kicker": "O MESMO FENÔMENO, DUAS VEZES",
        "v1_titulo": "Variação onde se esperava reprodução",
        "v1_sub": "O que espalha o corpus e o que afasta o desenvolvedor experiente são a mesma coisa",
        "v1_e_tit": "NA ENTRADA",
        "v1_e_sub": "dispersão do corpus",
        "v1_e_txt": "muitas formulações\nincompatíveis para\na mesma tarefa",
        "v1_e_quem": "sentida pela máquina",
        "v1_s_tit": "NA SAÍDA",
        "v1_s_sub": "resposta não reproduzível",
        "v1_s_txt": "a mesma pergunta\nduas vezes produz\nrespostas diferentes",
        "v1_s_quem": "sentida pelo humano",
        "v1_meio": "MODELO",
        "v1_faixa": "Engenharia é construída sobre reprodução. O modelo opera por distribuição.",
        "v1_rodape": "Explicação de determinismo conforme a Stack Overflow; a conexão com dispersão é proposta do autor.",

        "v2_nome": "p7-quatro-dimensoes-pt",
        "v2_kicker": "AS QUATRO DIMENSÕES DA CONFIANÇA",
        "v2_titulo": "Três já têm dono. A quarta não.",
        "v2_sub": "E a quarta é a que este artigo trata",
        "v2_h": ["Dimensão", "A pergunta", "Quem responde hoje"],
        "v2_linhas": [
            ("Segurança da informação", "dá para invadir através disto?", "segurança", 0),
            ("Confiabilidade do produto", "o código faz o que a descrição promete?", "engenharia", 0),
            ("Conformidade", "consigo responder por isto a um terceiro?", "jurídico", 0),
            ("Segurança de marca", "alguém consegue falar por mim sem eu saber?", "ninguém", 1),
        ],
        "v2_faixa": "Enquanto não se decide de quem é, ninguém está olhando.",
        "v2_rodape": "Divisão proposta pelo autor. Não corresponde a nenhum arcabouço estabelecido de governança.",

        "v3_nome": "p7-descasamento-pt",
        "v3_kicker": "A RAIZ DA DESCONFIANÇA",
        "v3_titulo": "Regra determinística, executor probabilístico",
        "v3_sub": "O que entra como contrato sai como uma variação entre muitas possíveis",
        "v3_regra": "A REGRA QUE O HUMANO ESCREVE",
        "v3_regra_txt": "sempre faça assim\nnunca faça assado\no resultado tem que ser este",
        "v3_regra_tag": "determinística",
        "v3_sist": "O SISTEMA QUE EXECUTA",
        "v3_sist_tag": "probabilístico",
        "v3_saida": "O QUE SAI",
        "v3_esperado": "esperado",
        "v3_obtido": "uma variação entre muitas",
        "v3_faixa": "Um sistema probabilístico não honra instrução. Honra restrição verificável.",
        "v3_rodape": "Formulação de Mat, 31 de julho de 2026. Raciocínio, não medição.",

        "v4_nome": "p7-tres-versoes-pt",
        "v4_kicker": "A DEFINIÇÃO DO PILAR",
        "v4_titulo": "Três versões, e o que faltava em cada uma",
        "v4_sub": "A correção veio no meio da escrita, e mudou o que o pilar pede",
        "v4_linhas": [
            ("Parte 1", "confiável o bastante para agir sem supervisão",
             "supõe que a supervisão some — e ela não some", 0),
            ("Correção", "verificável o bastante para que a supervisão seja automatizável",
             "supõe que a verificação automática pega o que importa", 0),
            ("Terceira", "…e reversível o bastante para que o erro que passa não seja caro",
             "o revisor bebe da mesma água que o revisado", 1),
        ],
        "v4_faixa": "A confiança não vem de evitar o erro. Vem de limitar o raio e encurtar a reversão.",
        "v4_rodape": "Proposta do autor. Não conheço levantamento que tenha testado as propriedades contra adoção por agente.",

        "v5_nome": "p7-duas-portas-pt",
        "v5_kicker": "OS DOIS JULGADORES",
        "v5_titulo": "Um produto pode passar numa porta e falhar na outra",
        "v5_sub": "Critérios diferentes, evidências diferentes, prazos diferentes",
        "v5_a": "A MÁQUINA",
        "v5_b": "O COMPRADOR CORPORATIVO",
        "v5_rot": ["A pergunta", "A evidência que aceita", "O prazo da decisão"],
        "v5_av": ["funciona sem que eu precise conferir?", "comportamento na execução", "segundos"],
        "v5_bv": ["posso responder por isto?", "documento e certificação", "trimestres"],
        "v5_faixa": "Certificação vira critério de elegibilidade antes de o agente escolher.",
        "v5_rodape": "ISO/IEC 42001 publicada em dezembro de 2023. A magnitude da exigência de mercado não foi verificada na fonte.",

        "v6_nome": "p7-dois-tipos-ambiguidade-pt",
        "v6_kicker": "A PERGUNTA QUE FECHA O ARCO",
        "v6_titulo": "Duas ambiguidades, e elas pedem coisas opostas",
        "v6_sub": "Eliminar onde é ruído; projetar para conviver onde é a matéria-prima",
        "v6_a_tit": "NA SUA SUPERFÍCIE",
        "v6_a_sub": "nome, descrição, documentação",
        "v6_a_ex": "um nome que aponta\npara mais de uma coisa",
        "v6_a_acao": "ELIMINAR",
        "v6_a_pq": "ali ela é ruído",
        "v6_b_tit": "NO PEDIDO QUE CHEGA",
        "v6_b_sub": "e no caminho que a máquina escolhe",
        "v6_b_ex": '"faz isso ficar\nmais rápido"',
        "v6_b_acao": "PROJETAR PARA CONVIVER",
        "v6_b_pq": "ali ela é a matéria-prima",
        "v6_faixa": "Se toda ambiguidade sumisse do pedido, o resultado seria uma linguagem de programação.",
        "v6_rodape": "Raciocínio construído durante a escrita da parte 7. Não é prática validada.",
    },
    "en": {
        "capa_kicker": "BUILDER-LED GROWTH — PART 7",
        "capa_t1": "What makes an agent",
        "capa_t2": "trust you",
        "capa_sub": "Pillar 4 — model trust and safety",
        "capa_frase1": "The competence that makes a model use your tool well",
        "capa_frase2": "is the same one that makes it obey the poisoned instruction.",
        "capa_creditof": "MCPTox, 45 live servers, 353 tools",
        "capa_rodape": "Matheus Ramos · final piece of arc 1: the four pillars",

        "v1_nome": "p7-variation-two-points-en",
        "v1_kicker": "THE SAME PHENOMENON, TWICE",
        "v1_titulo": "Variation where reproduction was expected",
        "v1_sub": "What scatters the corpus and what pushes away the experienced developer are one thing",
        "v1_e_tit": "ON THE WAY IN",
        "v1_e_sub": "corpus dispersion",
        "v1_e_txt": "many incompatible\nformulations for\nthe same task",
        "v1_e_quem": "felt by the machine",
        "v1_s_tit": "ON THE WAY OUT",
        "v1_s_sub": "non-reproducible answer",
        "v1_s_txt": "the same question\ntwice produces\ndifferent answers",
        "v1_s_quem": "felt by the human",
        "v1_meio": "MODEL",
        "v1_faixa": "Engineering is built on reproduction. The model operates on distribution.",
        "v1_rodape": "Determinism explanation per Stack Overflow; the link to dispersion is the author's proposal.",

        "v2_nome": "p7-four-dimensions-en",
        "v2_kicker": "THE FOUR DIMENSIONS OF TRUST",
        "v2_titulo": "Three already have an owner. The fourth does not.",
        "v2_sub": "And the fourth is what this piece is about",
        "v2_h": ["Dimension", "The question", "Who answers today"],
        "v2_linhas": [
            ("Information security", "can someone break in through this?", "security", 0),
            ("Product reliability", "does the code do what the description promises?", "engineering", 0),
            ("Compliance", "can I answer for this to a third party?", "legal", 0),
            ("Brand safety", "can someone speak for me without my knowing?", "nobody", 1),
        ],
        "v2_faixa": "Until it is decided whose it is, nobody is watching.",
        "v2_rodape": "Division proposed by the author. It matches no established governance framework.",

        "v3_nome": "p7-mismatch-en",
        "v3_kicker": "THE ROOT OF THE DISTRUST",
        "v3_titulo": "Deterministic rule, probabilistic executor",
        "v3_sub": "What goes in as a contract comes out as one variation among many",
        "v3_regra": "THE RULE THE HUMAN WRITES",
        "v3_regra_txt": "always do it this way\nnever do it that way\nthe result has to be this",
        "v3_regra_tag": "deterministic",
        "v3_sist": "THE SYSTEM THAT EXECUTES",
        "v3_sist_tag": "probabilistic",
        "v3_saida": "WHAT COMES OUT",
        "v3_esperado": "expected",
        "v3_obtido": "one variation among many",
        "v3_faixa": "A probabilistic system does not honour instructions. It honours verifiable constraints.",
        "v3_rodape": "Formulation by Mat, 31 July 2026. Reasoning, not measurement.",

        "v4_nome": "p7-three-versions-en",
        "v4_kicker": "THE PILLAR DEFINITION",
        "v4_titulo": "Three versions, and what each was missing",
        "v4_sub": "The correction came mid-writing, and changed what the pillar asks for",
        "v4_linhas": [
            ("Part 1", "trustworthy enough to act without supervision",
             "assumes supervision goes away — it does not", 0),
            ("Correction", "verifiable enough that supervision can be automated",
             "assumes automatic checking catches what matters", 0),
            ("Third", "…and reversible enough that the error which slips is not expensive",
             "the reviewer drinks the same water as the reviewed", 1),
        ],
        "v4_faixa": "Trust does not come from avoiding the error. It comes from bounding it and reversing fast.",
        "v4_rodape": "Author's proposal. I know of no study testing these properties against agent adoption.",

        "v5_nome": "p7-two-doors-en",
        "v5_kicker": "THE TWO JUDGES",
        "v5_titulo": "A product can pass one door and fail the other",
        "v5_sub": "Different criteria, different evidence, different horizons",
        "v5_a": "THE MACHINE",
        "v5_b": "THE CORPORATE BUYER",
        "v5_rot": ["The question", "The evidence it accepts", "The decision horizon"],
        "v5_av": ["does it work without my checking?", "behaviour at execution", "seconds"],
        "v5_bv": ["can I answer for this?", "documents and certification", "quarters"],
        "v5_faixa": "Certification becomes an eligibility filter before the agent chooses.",
        "v5_rodape": "ISO/IEC 42001 published December 2023. The magnitude of market demand was not verified at source.",

        "v6_nome": "p7-two-kinds-ambiguity-en",
        "v6_kicker": "THE QUESTION THAT CLOSES THE ARC",
        "v6_titulo": "Two ambiguities, asking for opposite things",
        "v6_sub": "Eliminate where it is noise; design to live with it where it is raw material",
        "v6_a_tit": "IN YOUR SURFACE",
        "v6_a_sub": "name, description, documentation",
        "v6_a_ex": "a name that points\nto more than one thing",
        "v6_a_acao": "ELIMINATE",
        "v6_a_pq": "there it is noise",
        "v6_b_tit": "IN THE REQUEST THAT ARRIVES",
        "v6_b_sub": "and the path the machine takes",
        "v6_b_ex": '"make this\nfaster"',
        "v6_b_acao": "DESIGN TO LIVE WITH IT",
        "v6_b_pq": "there it is the raw material",
        "v6_faixa": "If all ambiguity vanished from the request, the result would be a programming language.",
        "v6_rodape": "Reasoning built while writing part 7. Not validated practice.",
    },
}


def fecho(b, H, texto, cor=NAVY, soft=None):
    """Faixa de fecho, sempre com folga verificada contra o rodapé."""
    fy = H - 66 - 24 - 62
    b.append(rect(60, fy, W - 120, 62, soft or cor, rx=12, op=None if soft else "0.06"))
    b.append(rect(60, fy, W - 120, 62, "none", cor, 1.8, rx=12))
    b.append(txt(W / 2, fy + 39, texto, 19.5, "700", cor, anchor="middle"))
    assert fy + 62 < H - 66, "faixa encostando no rodapé"
    return fy


# ------------------------------------------------ v1: variação em dois pontos
def v1(t, lang):
    H = 760
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    cx = W / 2
    b.append(rect(cx - 110, 300, 220, 130, NAVY, rx=16))
    b.append(txt(cx, 372, t["v1_meio"], 24, "700", WHITE, anchor="middle", sp="2"))

    pw = 470
    for k in (0, 1):
        px = 60 if k == 0 else W - 60 - pw
        cor = AMBER if k == 0 else ACCENT
        soft = AMBER_SOFT if k == 0 else ACCENT_SOFT
        pcx = px + pw / 2
        b.append(rect(px, 236, pw, 258, soft, rx=14))
        b.append(rect(px, 236, pw, 258, "none", cor, 2, rx=14))
        b.append(txt(pcx, 278, t["v1_e_tit"] if k == 0 else t["v1_s_tit"],
                     17, "700", cor, anchor="middle", sp="2"))
        b.append(txt(pcx, 308, t["v1_e_sub"] if k == 0 else t["v1_s_sub"],
                     16, "400", GRAY, anchor="middle", style="italic"))
        ls = (t["v1_e_txt"] if k == 0 else t["v1_s_txt"]).split("\n")
        for i, l in enumerate(ls):
            b.append(txt(pcx, 350 + i * 25, l, 17.5, "700", NAVY, anchor="middle"))
        b.append(txt(pcx, 462, t["v1_e_quem"] if k == 0 else t["v1_s_quem"],
                     14.5, "400", GRAY_LIGHT, anchor="middle", style="italic"))
        if k == 0:
            b.append(arrow(px + pw + 12, 365, cx - 122, 365, cor, 3))
        else:
            b.append(arrow(cx + 122, 365, px - 12, 365, cor, 3))

    b.append(txt(cx, 540, "↑", 30, "400", MUTED, anchor="middle"))
    b.append(txt(cx, 574, n("é a mesma variação", "it is the same variation", lang),
                 18, "700", NAVY, anchor="middle", style="italic"))

    fecho(b, H, t["v1_faixa"])
    footer(b, W, H, t["v1_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------ v2: as quatro dimensões
def v2(t, lang):
    H = 720
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    x0, c1, c2 = 60, 400, 620
    y0, rh = 226, 82
    for i, h in enumerate(t["v2_h"]):
        cx = x0 + (0 if i == 0 else c1 if i == 1 else c1 + c2) + 18
        b.append(txt(cx, y0 - 16, h, 14.5, "700", GRAY, sp="1.5"))
    b.append(line(x0, y0 - 2, W - 60, y0 - 2, BORDER, 1.5))

    for j, (dim, perg, quem, dest) in enumerate(t["v2_linhas"]):
        y = y0 + j * rh
        cor = AMBER if dest else ACCENT
        if dest:
            b.append(rect(x0, y + 5, W - 120, rh - 10, AMBER_SOFT, rx=12))
            b.append(rect(x0, y + 5, W - 120, rh - 10, "none", AMBER, 2.5, rx=12))
        b.append(rect(x0 + 6, y + 18, 5, rh - 36, cor, rx=3))
        b.append(txt(x0 + 26, y + rh / 2 + 6, dim, 18, "700", AMBER if dest else NAVY))
        b.append(txt(x0 + c1 + 18, y + rh / 2 + 6, perg, 15.5, "400", GRAY, style="italic"))
        if dest:
            b.append(txt(x0 + c1 + c2 + 18, y + rh / 2 + 6, quem, 18, "700", AMBER))
        else:
            b.append(txt(x0 + c1 + c2 + 18, y + rh / 2 + 6, quem, 16, "400", NAVY))
        if not dest and j < len(t["v2_linhas"]) - 1:
            b.append(line(x0, y + rh, W - 60, y + rh, BORDER, 0.8))

    fecho(b, H, t["v2_faixa"], AMBER, AMBER_SOFT)
    footer(b, W, H, t["v2_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------ v3: o descasamento
def v3(t, lang):
    H = 800
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    # a regra, à esquerda
    rx0, rw = 60, 430
    b.append(rect(rx0, 216, rw, 210, ACCENT_SOFT, rx=14))
    b.append(rect(rx0, 216, rw, 210, "none", ACCENT, 2, rx=14))
    b.append(txt(rx0 + rw / 2, 252, t["v3_regra"], 14, "700", ACCENT, anchor="middle", sp="1.5"))
    for i, l in enumerate(t["v3_regra_txt"].split("\n")):
        b.append(txt(rx0 + rw / 2, 296 + i * 26, l, 16.5, "400", NAVY,
                     anchor="middle", style="italic"))
    b.append(rect(rx0 + rw / 2 - 78, 380, 156, 30, ACCENT, rx=15))
    b.append(txt(rx0 + rw / 2, 401, t["v3_regra_tag"], 14, "700", WHITE, anchor="middle", sp="1"))

    # o sistema, no meio
    sx, sw = 560, 300
    b.append(rect(sx, 216, sw, 210, NAVY, rx=14))
    b.append(txt(sx + sw / 2, 252, t["v3_sist"], 14, "700", "#AEB6C2", anchor="middle", sp="1.5"))
    import random
    random.seed(7)
    for i in range(26):
        px = sx + 34 + random.random() * (sw - 68)
        py = 284 + random.random() * 78
        b.append(circle(px, py, 3.5, ACCENT_LIGHT))
    b.append(rect(sx + sw / 2 - 78, 380, 156, 30, AMBER, rx=15))
    b.append(txt(sx + sw / 2, 401, t["v3_sist_tag"], 14, "700", WHITE, anchor="middle", sp="1"))
    b.append(arrow(rx0 + rw + 12, 321, sx - 12, 321, ACCENT, 3))

    # a saída, à direita
    ox, ow = 930, W - 60 - 930
    b.append(rect(ox, 216, ow, 210, AMBER_SOFT, rx=14))
    b.append(rect(ox, 216, ow, 210, "none", AMBER, 2, rx=14))
    b.append(txt(ox + ow / 2, 252, t["v3_saida"], 14, "700", AMBER, anchor="middle", sp="1.5"))
    b.append(arrow(sx + sw + 12, 321, ox - 12, 321, AMBER, 3))

    base, bw = 300, 46
    for i, h in enumerate([26, 58, 40, 22, 12]):
        bx = ox + 46 + i * (bw + 14)
        b.append(rect(bx, base + (62 - h), bw, h, AMBER, rx=5, op="0.75"))
    b.append(line(ox + 40, base + 64, ox + ow - 40, base + 64, AMBER, 1.5))
    mx = ox + 46 + bw / 2 + (bw + 14)
    b.append(txt(mx, base - 14, "▼", 13, "400", GREEN, anchor="middle"))
    b.append(txt(mx, base - 28, t["v3_esperado"], 13.5, "700", GREEN, anchor="middle"))
    b.append(txt(ox + ow / 2, 396, t["v3_obtido"], 15, "400", GRAY,
                 anchor="middle", style="italic"))

    # a frustração
    fy0 = 476
    b.append(rect(60, fy0, W - 120, 96, RED_SOFT, rx=14))
    b.append(rect(60, fy0, W - 120, 96, "none", RED, 2, rx=14))
    b.append(txt(W / 2, fy0 + 40, n("A pessoa conclui que a máquina não obedece.",
                                    "The person concludes the machine does not obey.", lang),
                 20, "700", RED, anchor="middle"))
    b.append(txt(W / 2, fy0 + 72, n("A máquina fez exatamente o que ela faz.",
                                    "The machine did exactly what it does.", lang),
                 20, "400", RED, anchor="middle"))

    fecho(b, H, t["v3_faixa"])
    footer(b, W, H, t["v3_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------ v4: as três versões
def v4(t, lang):
    H = 740
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    y0, rh = 224, 118
    for j, (tag, defn, falta, dest) in enumerate(t["v4_linhas"]):
        y = y0 + j * rh
        cor = AMBER if dest else ACCENT
        soft = AMBER_SOFT if dest else PANEL
        b.append(rect(60, y, W - 120, rh - 16, soft, rx=14))
        b.append(rect(60, y, W - 120, rh - 16, "none", cor, 2.5 if dest else 1.2, rx=14))
        b.append(rect(60, y, 7, rh - 16, cor, rx=0))
        b.append(txt(92, y + 40, tag, 15, "700", cor, sp="1.5"))
        b.append(txt(92, y + 72, defn, 20, "700", AMBER if dest else NAVY))
        b.append(txt(92, y + 96, falta, 15, "400", GRAY, style="italic"))

    fecho(b, H, t["v4_faixa"], AMBER, AMBER_SOFT)
    footer(b, W, H, t["v4_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------ v5: as duas portas
def v5(t, lang):
    H = 720
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    pw = (W - 120 - 40) / 2
    for k in (0, 1):
        px = 60 + k * (pw + 40)
        cor = ACCENT if k == 0 else AMBER
        soft = ACCENT_SOFT if k == 0 else AMBER_SOFT
        pcx = px + pw / 2
        b.append(rect(px, 216, pw, 314, soft, rx=14))
        b.append(rect(px, 216, pw, 314, "none", cor, 2, rx=14))
        b.append(rect(px, 216, pw, 54, cor, rx=14))
        b.append(rect(px, 244, pw, 26, cor, rx=0))
        b.append(txt(pcx, 250, t["v5_a"] if k == 0 else t["v5_b"], 18, "700",
                     WHITE, anchor="middle", sp="2"))
        vals = t["v5_av"] if k == 0 else t["v5_bv"]
        for i in range(3):
            yy = 306 + i * 76
            b.append(txt(px + 28, yy, t["v5_rot"][i], 13.5, "700", GRAY, sp="1"))
            b.append(txt(px + 28, yy + 30, vals[i], 18.5, "700", NAVY))
            if i < 2:
                b.append(line(px + 24, yy + 50, px + pw - 24, yy + 50, cor, 0.9, dash="4 4"))

    fecho(b, H, t["v5_faixa"])
    footer(b, W, H, t["v5_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------ v6: os dois tipos de ambiguidade
def v6(t, lang):
    H = 800
    b = []
    header(b, t["v6_kicker"], t["v6_titulo"], t["v6_sub"], H)

    pw = (W - 120 - 40) / 2
    for k in (0, 1):
        px = 60 + k * (pw + 40)
        cor = RED if k == 0 else GREEN
        soft = RED_SOFT if k == 0 else GREEN_SOFT
        pcx = px + pw / 2
        b.append(rect(px, 216, pw, 386, soft, rx=14))
        b.append(rect(px, 216, pw, 386, "none", cor, 2, rx=14))

        b.append(txt(pcx, 258, t["v6_a_tit"] if k == 0 else t["v6_b_tit"],
                     18, "700", cor, anchor="middle", sp="2"))
        b.append(txt(pcx, 288, t["v6_a_sub"] if k == 0 else t["v6_b_sub"],
                     15, "400", GRAY, anchor="middle", style="italic"))

        b.append(rect(px + 46, 316, pw - 92, 92, WHITE, cor, 1.5, rx=12))
        ex = (t["v6_a_ex"] if k == 0 else t["v6_b_ex"]).split("\n")
        for i, l in enumerate(ex):
            b.append(txt(pcx, 352 + i * 24, l, 17, "400", NAVY, anchor="middle", style="italic"))

        b.append(rect(px + 46, 438, pw - 92, 58, cor, rx=12))
        b.append(txt(pcx, 475, t["v6_a_acao"] if k == 0 else t["v6_b_acao"],
                     20, "700", WHITE, anchor="middle", sp="1.5"))
        b.append(txt(pcx, 532, t["v6_a_pq"] if k == 0 else t["v6_b_pq"],
                     16.5, "700", cor, anchor="middle"))
        b.append(txt(pcx, 570, n("o que você controla", "what you control", lang) if k == 0
                     else n("o que você não controla", "what you do not control", lang),
                     14.5, "400", GRAY_LIGHT, anchor="middle", style="italic"))

    fecho(b, H, t["v6_faixa"])
    footer(b, W, H, t["v6_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------------------------- capa
def capa(t, lang):
    CW, CH = 1920, 1080
    b = [f'<rect x="0" y="0" width="{CW}" height="{CH}" fill="{NAVY_DEEP}"/>']
    for i in range(9):
        x = 1180 + i * 92
        b.append(f'<line x1="{x}" y1="0" x2="{x - 240}" y2="{CH}" stroke="{ACCENT}" '
                 f'stroke-opacity="0.10" stroke-width="2"/>')

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
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{CW}" height="{CH}" '
            f'viewBox="0 0 {CW} {CH}">{"".join(b)}</svg>')


def gerar(lang):
    t = T[lang]
    save("p7-capa-pt" if lang == "pt" else "p7-cover-en", capa(t, lang), scale=1.5)
    for i, fn in enumerate((v1, v2, v3, v4, v5, v6), start=1):
        save(t[f"v{i}_nome"], fn(t, lang))


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    for lang in (["pt", "en"] if alvo is None else [alvo]):
        gerar(lang)
