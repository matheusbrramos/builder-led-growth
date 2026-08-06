#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais do arco 2, parte 0 — do PLG ao BLG.

PT e EN no mesmo arquivo. Helpers de desenho importados do gen_p4.
Como nas partes anteriores, cada função termina com assert de folga contra o
rodapé: peça torta falha alto em vez de sair publicada.

Uso:  python3 scripts/gen_a2p0.py          # gera PT e EN
      python3 scripts/gen_a2p0.py pt       # só português
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
# Existem uma vez só, e batem com o texto das duas línguas.
CONFIA_APRENDENDO = 6.1
CONFIA_EXPERIENTE = 2.5
VERIFICA_ANTES = 98
COMPRA_SEM_CONFERIR = 2
GOVERNANCA_ESTRITA = 27
SEM_VISIBILIDADE = 68


def n(pt, en, lang):
    return pt if lang == "pt" else en


def fecho(b, H, texto, cor=NAVY, soft=None):
    y = H - 152
    b.append(rect(60, y, W - 120, 62, soft or PANEL, rx=12))
    b.append(rect(60, y, 6, 62, cor, rx=0))
    b.append(txt(92, y + 39, texto, 19, "700", cor))


# ------------------------------------------------ v1: quem é o builder
def v1(t, lang):
    H = 780
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    cx = W / 2
    pw = 470
    for k in (0, 1):
        px = 120 if k == 0 else W - 120 - pw
        cor = ACCENT if k == 0 else AMBER
        soft = ACCENT_SOFT if k == 0 else AMBER_SOFT
        pcx = px + pw / 2
        b.append(rect(px, 226, pw, 232, soft, rx=14))
        b.append(rect(px, 226, pw, 232, "none", cor, 2, rx=14))
        b.append(txt(pcx, 268, t[f"v1_{k}_tit"], 17, "700", cor, anchor="middle", sp="2"))
        b.append(txt(pcx, 320, t[f"v1_{k}_verbo"], 34, "700", NAVY, anchor="middle"))
        for i, l in enumerate(t[f"v1_{k}_txt"].split("\n")):
            b.append(txt(pcx, 366 + i * 25, l, 16.5, "400", GRAY, anchor="middle"))

    b.append(txt(cx, 330, "+", 46, "700", MUTED, anchor="middle"))

    b.append(rect(120, 496, W - 240, 92, NAVY, rx=14))
    b.append(txt(cx, 536, t["v1_barra1"], 25, "700", WHITE, anchor="middle"))
    b.append(txt(cx, 570, t["v1_barra2"], 19, "400", "#AEB6C2", anchor="middle"))

    fecho(b, H, t["v1_faixa"])
    footer(b, W, H, t["v1_rodape"])
    assert 496 + 92 < H - 152, "v1 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v2: o gradiente
def v2(t, lang):
    H = 860
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    # Centros em 1/4 e 3/4 da largura. A versao anterior punha o card da direita
    # terminando em 1550, dez pixels alem da margem de 60.
    y = 300
    b.append(line(90, y, W - 90, y, BORDER, 3))
    for k in (0, 1):
        cx = W * 0.25 if k == 0 else W * 0.75
        cor = GREEN if k == 0 else ACCENT
        soft = GREEN_SOFT if k == 0 else ACCENT_SOFT
        b.append(circle(cx, y, 15, cor))
        b.append(rect(cx - 250, y + 46, 500, 176, soft, rx=14))
        b.append(rect(cx - 250, y + 46, 500, 176, "none", cor, 2, rx=14))
        b.append(txt(cx, y + 84, t[f"v2_{k}_tit"], 20, "700", cor, anchor="middle"))
        for i, l in enumerate(t[f"v2_{k}_txt"].split("\n")):
            b.append(txt(cx, y + 122 + i * 26, l, 17, "400", NAVY, anchor="middle"))
        b.append(txt(cx, y + 202, t[f"v2_{k}_apoio"], 15, "700", cor,
                     anchor="middle", style="italic"))

    b.append(txt(W / 2, y - 26, t["v2_eixo"], 16, "400", GRAY_LIGHT,
                 anchor="middle", style="italic"))

    yb = 566
    b.append(rect(150, yb, W - 300, 92, AMBER_SOFT, rx=14))
    b.append(rect(150, yb, 6, 92, AMBER, rx=0))
    b.append(txt(190, yb + 44, f"{VERIFICA_ANTES}%", 34, "700", AMBER))
    b.append(txt(276, yb + 38, t["v2_num1"], 18, "700", NAVY))
    b.append(txt(276, yb + 66, t["v2_num2"], 15.5, "400", GRAY))

    fecho(b, H, t["v2_faixa"])
    footer(b, W, H, t["v2_rodape"])
    assert yb + 92 < H - 152, "v2 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v3: o peso pende
def v3(t, lang):
    H = 760
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    bx, by, bw = 120, 250, W - 240
    b.append(rect(bx, by, bw, 210, PANEL, rx=14))
    b.append(txt(bx + 34, by + 46, t["v3_dado"], 17, "700", NAVY))

    barw, barh, bay = 560, 40, by + 84
    for k, (val, rot, cor) in enumerate((
            (CONFIA_APRENDENDO, t["v3_r1"], GREEN),
            (CONFIA_EXPERIENTE, t["v3_r2"], ACCENT))):
        yy = bay + k * 62
        b.append(txt(bx + 34, yy + 26, rot, 16.5, "400", GRAY))
        b.append(rect(bx + 300, yy, barw, barh, WHITE, BORDER, 1, rx=6))
        b.append(rect(bx + 300, yy, barw * (val / 8.0), barh, cor, rx=6))
        b.append(txt(bx + 316 + barw * (val / 8.0), yy + 27,
                     f"{val}%".replace(".", "," if lang == "pt" else "."),
                     19, "700", cor))

    ay = 500
    b.append(txt(120, ay, t["v3_eixo"], 16, "700", MUTED, sp="2"))
    b.append(line(120, ay + 18, W - 120, ay + 18, BORDER, 2))
    b.append(arrow(W - 460, ay + 18, W - 130, ay + 18, MUTED, 2))
    b.append(txt(120, ay + 52, t["v3_esq"], 17, "400", NAVY))
    b.append(txt(W - 120, ay + 52, t["v3_dir"], 17, "400", NAVY, anchor="end"))

    fecho(b, H, t["v3_faixa"])
    footer(b, W, H, t["v3_rodape"])
    assert ay + 52 < H - 152, "v3 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v4: onde o PLG deixa de servir
def v4(t, lang):
    H = 800
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    # 60 de margem de cada lado, 4 vaos de 20: (1600-120-80)/5 = 276.
    # A versao anterior usava 292 e a quinta coluna encostava na borda direita.
    gap = 20
    cw = (W - 120 - gap * 4) / 5
    x0 = 60
    for k in range(5):
        px = x0 + k * (cw + gap)
        b.append(rect(px, 232, cw, 340, WHITE, BORDER, 1.5, rx=14))
        b.append(rect(px, 232, cw, 6, ACCENT, rx=0))
        b.append(txt(px + cw / 2, 288, t[f"v4_{k}_tit"], 17, "700", ACCENT,
                     anchor="middle"))
        for i, l in enumerate(t[f"v4_{k}_plg"].split("\n")):
            b.append(txt(px + 24, 336 + i * 23, l, 15, "400", GRAY))
        b.append(line(px + 24, 424, px + cw - 24, 424, BORDER, 1))
        b.append(txt(px + 24, 456, t["v4_rot"], 13, "700", AMBER, sp="1"))
        for i, l in enumerate(t[f"v4_{k}_blg"].split("\n")):
            b.append(txt(px + 24, 484 + i * 23, l, 15.5, "700", NAVY))

    fecho(b, H, t["v4_faixa"], AMBER, AMBER_SOFT)
    footer(b, W, H, t["v4_rodape"])
    assert 232 + 340 < H - 152, "v4 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v5: o conjunto competitivo
def v5(t, lang):
    H = 740
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    cx = W / 2
    b.append(rect(cx - 300, 226, 600, 78, NAVY, rx=14))
    b.append(txt(cx, 274, t["v5_trabalho"], 24, "700", WHITE, anchor="middle"))

    itens = t["v5_itens"].split("|")
    iw, gap = 268, 18
    total = len(itens) * iw + (len(itens) - 1) * gap
    x0 = (W - total) / 2
    for k, it in enumerate(itens):
        px = x0 + k * (iw + gap)
        destaque = k == len(itens) - 1
        cor = AMBER if destaque else ACCENT
        soft = AMBER_SOFT if destaque else ACCENT_SOFT
        b.append(arrow(px + iw / 2, 322, px + iw / 2, 372, cor, 2))
        b.append(rect(px, 378, iw, 118, soft, rx=12))
        b.append(rect(px, 378, iw, 118, "none", cor, 2 if destaque else 1.5, rx=12))
        for i, l in enumerate(it.split("\n")):
            b.append(txt(px + iw / 2, 424 + i * 26, l,
                         17.5 if destaque else 17,
                         "700" if destaque else "400",
                         NAVY, anchor="middle"))

    b.append(txt(cx, 540, t["v5_nota"], 17, "400", GRAY, anchor="middle",
                 style="italic"))

    fecho(b, H, t["v5_faixa"], AMBER, AMBER_SOFT)
    footer(b, W, H, t["v5_rodape"])
    assert 540 < H - 152, "v5 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ capa
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


# ---------------------------------------------------------------- textos
T = {
    "pt": {
        "capa_kicker": "BUILDER-LED GROWTH — ARCO 2, PARTE 0",
        "capa_t1": "Do PLG ao BLG",
        "capa_t2": "quando quem escolhe é um par",
        "capa_sub": "Abre o segundo arco — não exige ter lido o primeiro",
        "capa_frase1": "Builder é o par: a pessoa e o agente juntos.",
        "capa_frase2": "Nenhum dos dois decide sozinho.",
        "capa_creditof": "Trabalho a ser feito, quatro forças, e o limite que o próprio PLG reconhece",
        "capa_rodape": "Matheus Ramos · abertura do arco 2",

        "v1_nome": "a2p0-o-par-pt",
        "v1_kicker": "QUEM DECIDE",
        "v1_titulo": "Builder é o par, não a máquina",
        "v1_sub": "Cada um faz uma coisa, e nenhum dos dois decide sozinho",
        "v1_0_tit": "O AGENTE",
        "v1_0_verbo": "seleciona",
        "v1_0_txt": "Escolhe a peça, escreve o código,\nintegra e segue em frente",
        "v1_1_tit": "A PESSOA",
        "v1_1_verbo": "valida",
        "v1_1_txt": "Olha o resultado, aceita ou\ndesfaz — e paga a conta",
        "v1_barra1": "A decisão sai do par, e o peso não fica parado no meio",
        "v1_barra2": "Quanto menos experiência de quem observa, e menos regra em volta, mais ela pende para a máquina",
        "v1_faixa": "O agente seleciona. A pessoa valida. Ninguém decide sozinho.",
        "v1_rodape": "Builder-Led Growth, arco 2 · a definição que o arco inteiro usa",

        "v2_nome": "a2p0-gradiente-pt",
        "v2_kicker": "DOIS FENÔMENOS, UM GRADIENTE",
        "v2_titulo": "Recomendar e construir não são caixas separadas",
        "v2_sub": "O papel da máquina muda com a especificidade do que está sendo feito",
        "v2_eixo": "quanto mais específica a tarefa →",
        "v2_0_tit": "RECOMENDAÇÃO",
        "v2_0_txt": "A máquina aponta.\nA pessoa vai lá e compra.",
        "v2_0_apoio": "ela se apoia no corpus",
        "v2_1_tit": "CONSTRUÇÃO",
        "v2_1_txt": "A máquina escolhe, integra,\ncontrata em seu nome.",
        "v2_1_apoio": "ela é limitada pelo harness e pelo contexto",
        "v2_num1": "verificam a recomendação da IA antes de comprar",
        "v2_num2": f"Só {COMPRA_SEM_CONFERIR}% compram sem conferir · Idea Grove, 2026, mil consumidores nos EUA",
        "v2_faixa": "Validação humana não é peculiaridade de quem constrói software. É o padrão.",
        "v2_rodape": "Builder-Led Growth, arco 2 · Idea Grove (2026) · Semrush (dez/2025)",

        "v3_nome": "a2p0-peso-pende-pt",
        "v3_kicker": "O CENTRO DE GRAVIDADE",
        "v3_titulo": "O peso pende conforme quem está do lado humano",
        "v3_sub": "Confiança alta na saída da IA, por tempo de estrada",
        "v3_dado": "Quem diz confiar muito na saída da IA — pesquisa Stack Overflow",
        "v3_r1": "Aprendendo a programar",
        "v3_r2": "Experientes",
        "v3_eixo": "E O MESMO DESLOCA POR AMBIENTE",
        "v3_esq": "Pouca regra escrita → o agente decide mais",
        "v3_dir": "Registro, comitê, revisão → ele propõe mais e decide menos",
        "v3_faixa": "O par é o mesmo. O centro de gravidade, não.",
        "v3_rodape": "Builder-Led Growth, arco 2 · Stack Overflow Developer Survey",

        "v4_nome": "a2p0-onde-plg-para-pt",
        "v4_kicker": "ONDE O PLG DEIXA DE SERVIR",
        "v4_titulo": "Cinco técnicas desenhadas para um humano na ponta",
        "v4_sub": "Nenhuma delas está errada — todas pressupõem quem já não está ali",
        "v4_rot": "SOB O BLG",
        "v4_0_tit": "Momento do valor",
        "v4_0_plg": "A pessoa opera e\nsente o valor",
        "v4_0_blg": "Troca de destinatário:\nquem recebe o\nresultado é que sente",
        "v4_1_tit": "Revelação progressiva",
        "v4_1_plg": "Mostrar pouco de cada\nvez, para não\nsobrecarregar",
        "v4_1_blg": "Informação retida\nvira ambiguidade —\ne ambiguidade custa",
        "v4_2_tit": "Indicação",
        "v4_2_plg": "Pessoas indicam por\nrazão social",
        "v4_2_blg": "Vira sedimentação\nno corpus: mais lenta\ne não social",
        "v4_3_tit": "Freemium",
        "v4_3_plg": "O usuário converte\nquando sente o limite",
        "v4_3_blg": "O agente não sente:\nconsome até a conta\nchegar a alguém",
        "v4_4_tit": "Piso de compliance",
        "v4_4_plg": "Autosserviço puro vivia\nonde não havia\ncompliance",
        "v4_4_blg": "O portão de empresa\nexiste sem o contrato\nde empresa",
        "v4_faixa": "A melhor prática de um é o defeito do outro.",
        "v4_rodape": (f"Builder-Led Growth, arco 2 · o portão é real onde existe: "
                      f"{GOVERNANCA_ESTRITA}% aplicam governança estrita, "
                      f"{SEM_VISIBILIDADE}% não sabem quais ferramentas de IA são usadas"),

        "v5_nome": "a2p0-conjunto-competitivo-pt",
        "v5_kicker": "QUEM DISPUTA COM VOCÊ",
        "v5_titulo": "O conjunto é definido pelo trabalho, não pela categoria",
        "v5_sub": "Quando o builder precisa de um banco que suba e conecte",
        "v5_trabalho": "Subir um banco e conectar",
        "v5_itens": ("Outro banco\nde dados|O serviço já\nincluso na\nplataforma|"
                     "O arquivo local\nque resolve\npor enquanto|"
                     "A instância que\no time já tem\nrodando|"
                     "O agente\nescrevendo\npor conta própria"),
        "v5_nota": "Nada disso está no mesmo setor. Tudo disputa o mesmo avanço.",
        "v5_faixa": "A última é a que mudou de preço — e quando ela vence, ninguém consultou a sua preferência.",
        "v5_rodape": "Builder-Led Growth, arco 2 · trabalho a ser feito: Ulwick (1990), Moesta, Pedi e Palmer, Christensen (2003)",
    },
    "en": {
        "capa_kicker": "BUILDER-LED GROWTH — ARC 2, PART 0",
        "capa_t1": "From PLG to BLG",
        "capa_t2": "when the one choosing is a pair",
        "capa_sub": "Opens the second arc — no need to have read the first",
        "capa_frase1": "A builder is the pair: the person and the agent together.",
        "capa_frase2": "Neither of them decides alone.",
        "capa_creditof": "Jobs to be done, four forces, and the limit PLG itself acknowledges",
        "capa_rodape": "Matheus Ramos · opening of arc 2",

        "v1_nome": "a2p0-the-pair-en",
        "v1_kicker": "WHO DECIDES",
        "v1_titulo": "A builder is the pair, not the machine",
        "v1_sub": "Each does one thing, and neither decides alone",
        "v1_0_tit": "THE AGENT",
        "v1_0_verbo": "selects",
        "v1_0_txt": "Picks the piece, writes the code,\nintegrates and moves on",
        "v1_1_tit": "THE PERSON",
        "v1_1_verbo": "validates",
        "v1_1_txt": "Looks at the result, accepts or\nundoes it — and pays the bill",
        "v1_barra1": "The decision comes out of the pair, and the weight doesn't sit still",
        "v1_barra2": "The less experience the watcher has, and the less rule around them, the more it tips toward the machine",
        "v1_faixa": "The agent selects. The person validates. Neither decides alone.",
        "v1_rodape": "Builder-Led Growth, arc 2 · the definition the whole arc uses",

        "v2_nome": "a2p0-gradient-en",
        "v2_kicker": "TWO PHENOMENA, ONE GRADIENT",
        "v2_titulo": "Recommending and building aren't separate boxes",
        "v2_sub": "The machine's role shifts with the specificity of what is being made",
        "v2_eixo": "the more specific the task →",
        "v2_0_tit": "RECOMMENDATION",
        "v2_0_txt": "The machine points.\nThe person goes and buys.",
        "v2_0_apoio": "it leans on the corpus",
        "v2_1_tit": "CONSTRUCTION",
        "v2_1_txt": "The machine chooses, integrates,\nhires on your behalf.",
        "v2_1_apoio": "it is bounded by harness and context",
        "v2_num1": "verify the AI recommendation before buying",
        "v2_num2": f"Only {COMPRA_SEM_CONFERIR}% buy without checking · Idea Grove, 2026, a thousand US consumers",
        "v2_faixa": "Human validation isn't a quirk of people who build software. It's the norm.",
        "v2_rodape": "Builder-Led Growth, arc 2 · Idea Grove (2026) · Semrush (Dec 2025)",

        "v3_nome": "a2p0-weight-tips-en",
        "v3_kicker": "THE CENTRE OF GRAVITY",
        "v3_titulo": "The weight tips with who is on the human side",
        "v3_sub": "High trust in AI output, by time on the road",
        "v3_dado": "Share reporting high trust in AI output — Stack Overflow survey",
        "v3_r1": "Learning to code",
        "v3_r2": "Experienced",
        "v3_eixo": "AND THE SAME SHIFTS BY ENVIRONMENT",
        "v3_esq": "Little written rule → the agent decides more",
        "v3_dir": "Registry, committee, review → it proposes more and decides less",
        "v3_faixa": "The pair is the same. The centre of gravity isn't.",
        "v3_rodape": "Builder-Led Growth, arc 2 · Stack Overflow Developer Survey",

        "v4_nome": "a2p0-where-plg-stops-en",
        "v4_kicker": "WHERE PLG STOPS SERVING",
        "v4_titulo": "Five techniques designed for a human at the end",
        "v4_sub": "None of them is wrong — all of them assume someone who is no longer there",
        "v4_rot": "UNDER BLG",
        "v4_0_tit": "The value moment",
        "v4_0_plg": "The person operates\nand feels the value",
        "v4_0_blg": "Changes recipient:\nwhoever receives the\nresult is who feels it",
        "v4_1_tit": "Progressive disclosure",
        "v4_1_plg": "Show a little at a\ntime, so as not to\noverwhelm",
        "v4_1_blg": "Withheld information\nbecomes ambiguity —\nand ambiguity costs",
        "v4_2_tit": "Referral",
        "v4_2_plg": "People refer for\nsocial reasons",
        "v4_2_blg": "Becomes sedimentation\nin the corpus: slower\nand not social",
        "v4_3_tit": "Freemium",
        "v4_3_plg": "The user converts\nwhen they feel the limit",
        "v4_3_blg": "The agent doesn't feel it:\nit consumes until the\nbill reaches someone",
        "v4_4_tit": "Compliance floor",
        "v4_4_plg": "Pure self-serve lived\nwhere there was no\ncompliance",
        "v4_4_blg": "The enterprise gate\nexists without the\nenterprise contract",
        "v4_faixa": "One's best practice is the other's defect.",
        "v4_rodape": (f"Builder-Led Growth, arc 2 · the gate is real where it exists: "
                      f"{GOVERNANCA_ESTRITA}% enforce strict governance, "
                      f"{SEM_VISIBILIDADE}% don't know which AI tools are in use"),

        "v5_nome": "a2p0-competitive-set-en",
        "v5_kicker": "WHO COMPETES WITH YOU",
        "v5_titulo": "The set is defined by the job, not by the category",
        "v5_sub": "When the builder needs a database that comes up and connects",
        "v5_trabalho": "Bring up a database and connect",
        "v5_itens": ("Another\ndatabase|The service already\nbundled into the\nplatform|"
                     "The local file\nthat does\nfor now|"
                     "The instance the\nteam already\nruns|"
                     "The agent\nwriting it\nthemselves"),
        "v5_nota": "None of that sits in the same industry. All of it competes for the same progress.",
        "v5_faixa": "The last one is the one whose price changed — and when it wins, nobody consulted your preference.",
        "v5_rodape": "Builder-Led Growth, arc 2 · jobs to be done: Ulwick (1990), Moesta, Pedi and Palmer, Christensen (2003)",
    },
}


def gerar(lang):
    t = T[lang]
    save("a2p0-capa-pt" if lang == "pt" else "a2p0-cover-en", capa(t, lang), scale=1.5)
    for i, fn in enumerate((v1, v2, v3, v4, v5), start=1):
        save(t[f"v{i}_nome"], fn(t, lang))


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    for lang in (["pt", "en"] if alvo is None else [alvo]):
        gerar(lang)
