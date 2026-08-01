#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais da parte 6 — Builder-Led Growth: Relações Públicas.

PT e EN no mesmo arquivo, pelo mesmo motivo de sempre: conteúdo escrito duas
vezes é conteúdo que diverge. Helpers de desenho importados do gen_p4.

Uso:  python3 scripts/gen_p6.py          # gera PT e EN
      python3 scripts/gen_p6.py pt       # só português
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

# ---------------------------------------------------------------- números
# Existem uma vez só, nas duas línguas.
CIT_TERCEIRO = "32,5%"
CIT_TERCEIRO_EN = "32.5%"
CIT_PROPRIO = "5%"
NOTAS_PERDEM = "30,2%"
NOTAS_PERDEM_EN = "30.2%"


def n(pt, en, lang):
    return pt if lang == "pt" else en


# ---------------------------------------------------------------- textos
T = {
    "pt": {
        "suf": "pt",
        "capa_kicker": "BUILDER-LED GROWTH — PARTE 6",
        "capa_t1": "A máquina é imprensa",
        "capa_t2": "e leitor ao mesmo tempo",
        "capa_sub": "O que Relações Públicas já sabia, e o que ganha significado novo",
        "capa_frase1": "Publicidade é você falar de si para os outros.",
        "capa_frase2": "Relações Públicas é fazer os outros falarem de você.",
        "capa_creditof": "definição ouvida em 1997, no primeiro ano da faculdade",
        "capa_rodape": "Matheus Ramos · com PRSA, Grunig e Hunt (1984), Schramm (1954), Saussure e Peirce",

        "v1_nome": "p6-cliente-imprensa-modelo-pt",
        "v1_kicker": "O ACÚMULO DE PAPÉIS",
        "v1_titulo": "A máquina acumula o que cliente e imprensa dividiam",
        "v1_sub": "Cada linha é uma propriedade da relação. A coluna da direita soma as duas anteriores.",
        "v1_cols": ["Cliente", "Imprensa", "Modelo"],
        "v1_linhas": [
            ("Consome e usa o que você entrega", 1, 0, 1),
            ("Tem necessidades próprias a atender", 1, 0, 1),
            ("Transforma o que recebe antes de redistribuir", 0, 1, 1),
            ("Alcança terceiros em seu nome", 0, 1, 1),
            ("Negocia condições com você", 1, 0, 0),
            ("Você controla a saída", -1, 0, 0),
            ("Você controla o insumo", -1, 1, 1),
        ],
        "v1_faixa": "O primeiro leitor da história que também é a gráfica.",
        "v1_rodape": "Correspondência de papéis, não identidade: um veículo tem intenção editorial e responsabilidade; um modelo tem pesos.",

        "v2_nome": "p6-feedback-quebrado-pt",
        "v2_kicker": "O QUINTO ELEMENTO",
        "v2_titulo": "O laço não sumiu. Fechou em outro lugar.",
        "v2_sub": "O esquema circular de Schramm (1954) pressupõe que quem recebe é distinto de quem carrega",
        "v2_antes": "ANTES",
        "v2_agora": "AGORA",
        "v2_no_produto": "Produto",
        "v2_no_usuario": "Usuário",
        "v2_no_agente": "Agente",
        "v2_no_operador": "Quem opera\no modelo",
        "v2_lbl_entrega": "entrega",
        "v2_lbl_retorno": "retorno",
        "v2_lbl_reclama": "reclama",
        "v2_lbl_registro": "registro da sessão",
        "v2_lbl_sessao": "A SESSÃO",
        "v2_corte": "o retorno não\nvolta até aqui",
        "v2_faixa": "Meio e receptor viraram a mesma entidade — e a resposta do receptor é absorvida pelo próprio canal.",
        "v2_rodape": "Raciocínio, não medição. Não conheço estudo que tenha quantificado o atraso entre a piora e a descoberta dela.",

        "v3_nome": "p6-polissemia-sinonimia-pt",
        "v3_kicker": "AS DUAS RELAÇÕES ENTRE SIGNO E SENTIDO",
        "v3_titulo": "Dois problemas desta série, um mapa só",
        "v3_sub": "Uma disciplina do século XIX já tinha os dois catalogados",
        "v3_p_tit": "POLISSEMIA",
        "v3_p_def": "um significante,\nsignificados concorrentes",
        "v3_p_serie": "a ambiguidade de identidade:\no nome que aponta para\nmais de uma coisa",
        "v3_s_tit": "SINONÍMIA",
        "v3_s_def": "significantes diversos,\num significado",
        "v3_s_serie": "a dispersão: muitas formas\nincompatíveis de dizer\na mesma operação",
        "v3_signif": "nome",
        "v3_sent": "sentido",
        "v3_faixa": "Nome ambíguo e corpus disperso não são dois assuntos. São a mesma relação, uma em cada direção.",
        "v3_rodape": "Saussure (significante e significado) e Peirce (signo, objeto, interpretante). A aplicação a nome de produto é proposta do autor.",

        "v4_nome": "p6-quatro-modelos-pt",
        "v4_kicker": "GRUNIG E HUNT, 1984",
        "v4_titulo": "O modelo mais ético virou também o mais eficaz",
        "v4_sub": "Quatro décadas depois, o arcabouço mais ensinado da área — lido pelo que a máquina recebe de cada um",
        "v4_h": ["Modelo", "O equivalente hoje", "O que a máquina recebe"],
        "v4_linhas": [
            ("Agência de imprensa", "Conteúdo para chamar atenção", "Ruído, e ruído custa contexto", 0),
            ("Informação pública", "Documentação, llms.txt, dado estruturado", "É o pilar de legibilidade", 0),
            ("Assimétrico de mão dupla", "Growth clássico", "Só o seu próprio texto", 0),
            ("Simétrico de mão dupla", "Comunidade de verdade", "Texto de terceiro sobre você", 1),
        ],
        "v4_faixa": "O argumento que faltava ao modelo simétrico não era ético. Era econômico — e ele apareceu.",
        "v4_rodape": "Ponte entre uma teoria de 1984 e um dado de recuperação de 2026. As duas coisas nunca se encontraram na literatura.",
    },
    "en": {
        "suf": "en",
        "capa_kicker": "BUILDER-LED GROWTH — PART 6",
        "capa_t1": "The machine is press",
        "capa_t2": "and reader at once",
        "capa_sub": "What public relations already knew, and what now means something new",
        "capa_frase1": "Advertising is you talking about yourself to others.",
        "capa_frase2": "Public relations is getting others to talk about you.",
        "capa_creditof": "a definition heard in 1997, in the first year of university",
        "capa_rodape": "Matheus Ramos · with PRSA, Grunig and Hunt (1984), Schramm (1954), Saussure and Peirce",

        "v1_nome": "p6-customer-press-model-en",
        "v1_kicker": "ROLES STACKED",
        "v1_titulo": "The machine stacks what customer and press kept apart",
        "v1_sub": "Each row is a property of the relationship. The right-hand column adds up the two before it.",
        "v1_cols": ["Customer", "Press", "Model"],
        "v1_linhas": [
            ("Consumes and uses what you ship", 1, 0, 1),
            ("Has its own needs to be met", 1, 0, 1),
            ("Reworks what it gets before passing it on", 0, 1, 1),
            ("Reaches third parties on your behalf", 0, 1, 1),
            ("Negotiates terms with you", 1, 0, 0),
            ("You control the output", -1, 0, 0),
            ("You control the input", -1, 1, 1),
        ],
        "v1_faixa": "The first reader in history that is also the printing press.",
        "v1_rodape": "A match of roles, not an identity: a news outlet has editorial intent and accountability; a model has weights.",

        "v2_nome": "p6-broken-feedback-en",
        "v2_kicker": "THE FIFTH ELEMENT",
        "v2_titulo": "The loop did not vanish. It closed somewhere else.",
        "v2_sub": "Schramm's circular model (1954) assumes the receiver is distinct from the carrier",
        "v2_antes": "BEFORE",
        "v2_agora": "NOW",
        "v2_no_produto": "Product",
        "v2_no_usuario": "User",
        "v2_no_agente": "Agent",
        "v2_no_operador": "Whoever runs\nthe model",
        "v2_lbl_entrega": "delivers",
        "v2_lbl_retorno": "feedback",
        "v2_lbl_reclama": "complains",
        "v2_lbl_registro": "session record",
        "v2_lbl_sessao": "THE SESSION",
        "v2_corte": "feedback never\nreaches here",
        "v2_faixa": "Medium and receiver became one entity — and the receiver's reply is absorbed by the channel itself.",
        "v2_rodape": "Reasoning, not measurement. I know of no study quantifying the lag between quality dropping and you finding out.",

        "v3_nome": "p6-polysemy-synonymy-en",
        "v3_kicker": "THE TWO RELATIONS BETWEEN SIGN AND MEANING",
        "v3_titulo": "Two problems in this series, one single map",
        "v3_sub": "A nineteenth-century discipline had both already catalogued",
        "v3_p_tit": "POLYSEMY",
        "v3_p_def": "one signifier,\ncompeting meanings",
        "v3_p_serie": "ambiguity of identity:\nthe name that points to\nmore than one thing",
        "v3_s_tit": "SYNONYMY",
        "v3_s_def": "many signifiers,\none meaning",
        "v3_s_serie": "dispersion: many\nincompatible ways to state\nthe same operation",
        "v3_signif": "name",
        "v3_sent": "meaning",
        "v3_faixa": "An ambiguous name and a scattered corpus are not two subjects. They are one relation, running each way.",
        "v3_rodape": "Saussure (signifier and signified) and Peirce (sign, object, interpretant). Applying it to product names is the author's proposal.",

        "v4_nome": "p6-four-models-en",
        "v4_kicker": "GRUNIG AND HUNT, 1984",
        "v4_titulo": "The most ethical model became the most effective one",
        "v4_sub": "Four decades on, the field's most-taught framework — read by what the machine gets from each",
        "v4_h": ["Model", "Today's equivalent", "What the machine receives"],
        "v4_linhas": [
            ("Press agentry", "Content built to grab attention", "Noise, and noise costs context", 0),
            ("Public information", "Docs, llms.txt, structured data", "This is the legibility pillar", 0),
            ("Two-way asymmetrical", "Classic growth", "Only your own copy", 0),
            ("Two-way symmetrical", "An actual community", "Third-party text about you", 1),
        ],
        "v4_faixa": "The argument the symmetrical model lacked was not ethical. It was economic — and it showed up.",
        "v4_rodape": "A bridge between a 1984 theory and a 2026 retrieval finding. The two never met in the literature.",
    },
}


# ------------------------------------------------------------ v1: a tabela
def v1(t, lang):
    H = 850
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    x0, xl = 60, 700          # fim da coluna de rótulo
    cw = (W - 60 - xl) / 3    # largura de cada coluna de valor
    y0 = 200
    rh = 62
    nlin = len(t["v1_linhas"])

    # faixa de destaque atrás da coluna do modelo, desenhada antes do conteúdo
    xm = xl + 2 * cw
    b.append(rect(xm, y0 - 46, cw, rh * nlin + 46 + 14, AMBER_SOFT, rx=12))
    b.append(rect(xm, y0 - 46, cw, rh * nlin + 46 + 14, "none", AMBER, 2, rx=12))

    for i, c in enumerate(t["v1_cols"]):
        cx = xl + i * cw + cw / 2
        destaque = i == 2
        b.append(txt(cx, y0 - 16, c, 17, "700", AMBER if destaque else GRAY,
                     anchor="middle", sp="1"))
    b.append(line(x0, y0 - 2, W - 60, y0 - 2, BORDER, 1.5))

    for j, (rot, *vals) in enumerate(t["v1_linhas"]):
        y = y0 + j * rh
        if j % 2 == 0:
            b.append(rect(x0, y, xl - x0, rh, PANEL, rx=8))
        b.append(txt(x0 + 16, y + rh / 2 + 6, rot, 16.5, "400", NAVY))
        for i, v in enumerate(vals):
            cx = xl + i * cw + cw / 2
            cy = y + rh / 2
            destaque = i == 2 and v == 1
            if v == -1:
                b.append(txt(cx, cy + 6, "—", 20, "400", MUTED, anchor="middle"))
            elif v == 1:
                b.append(circle(cx, cy, 15, AMBER if destaque else ACCENT))
                b.append(txt(cx, cy + 6, "sim" if lang == "pt" else "yes",
                             12.5, "700", WHITE, anchor="middle"))
            else:
                b.append(circle(cx, cy, 15, "none", MUTED, 1.5))
                b.append(txt(cx, cy + 6, "não" if lang == "pt" else "no",
                             12.5, "400", GRAY_LIGHT, anchor="middle"))
        if j < nlin - 1:
            b.append(line(x0, y + rh, xm - 4, y + rh, BORDER, 0.8))

    fy = y0 + nlin * rh + 34
    b.append(rect(x0, fy, W - 120, 62, ACCENT_SOFT, rx=12))
    b.append(rect(x0, fy, W - 120, 62, "none", ACCENT, 1.5, rx=12))
    b.append(txt(W / 2, fy + 39, t["v1_faixa"], 21, "700", ACCENT, anchor="middle"))

    footer(b, W, H, t["v1_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------- v2: o laço que fechou fora
def v2(t, lang):
    """Dois laços empilhados.

    A primeira versão punha o operador do modelo na MESMA linha dos outros nós
    e a seta cortada logo abaixo. Deu duas colisões: o rótulo "registro da
    sessão" invadiu a caixa do operador, e a faixa de fecho encostou no rodapé.
    Agora o operador desce um nível e as alturas são somadas explicitamente.
    """
    H = 950
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    def no(cx, cy, rot, cor, w=210, h=76, fill=None):
        b.append(rect(cx - w / 2, cy - h / 2, w, h, fill or WHITE, cor, 2, rx=12))
        ls = rot.split("\n")
        y = cy + 6 - (len(ls) - 1) * 11
        for i, l in enumerate(ls):
            b.append(txt(cx, y + i * 22, l, 17.5, "700", cor, anchor="middle"))

    # ---------- ANTES: laço fechado
    ya = 300
    b.append(txt(60, 222, t["v2_antes"], 14, "700", GREEN, sp="2"))
    b.append(rect(60, 238, W - 120, 132, GREEN_SOFT, rx=14, op="0.55"))
    ax1, ax2 = 460, 1140
    no(ax1, ya, t["v2_no_produto"], GREEN)
    no(ax2, ya, t["v2_no_usuario"], GREEN)
    b.append(arrow(ax1 + 108, ya - 15, ax2 - 108, ya - 15, GREEN, 2.5))
    b.append(txt((ax1 + ax2) / 2, ya - 25, t["v2_lbl_entrega"], 14.5, "400",
                 GREEN, anchor="middle", style="italic"))
    b.append(arrow(ax2 - 108, ya + 17, ax1 + 108, ya + 17, GREEN, 2.5))
    b.append(txt((ax1 + ax2) / 2, ya + 42, t["v2_lbl_retorno"], 14.5, "700",
                 GREEN, anchor="middle", style="italic"))

    # ---------- AGORA: a linha, a sessão, e o laço que fecha fora
    b.append(txt(60, 434, t["v2_agora"], 14, "700", AMBER, sp="2"))
    b.append(rect(60, 450, W - 120, 336, AMBER_SOFT, rx=14, op="0.5"))

    yl = 528                       # linha dos três nós
    bx = [300, 740, 1180]
    # moldura da sessão, envolvendo agente e usuário
    b.append(rect(bx[1] - 158, yl - 68, (bx[2] + 120) - (bx[1] - 158), 136,
                  "none", AMBER, 1.5, rx=14))
    b.append(txt(bx[1] - 142, yl - 46, t["v2_lbl_sessao"], 13, "700", AMBER, sp="1"))

    no(bx[0], yl, t["v2_no_produto"], ACCENT)
    no(bx[1], yl, t["v2_no_agente"], ACCENT)
    no(bx[2], yl, t["v2_no_usuario"], ACCENT)
    b.append(arrow(bx[0] + 108, yl, bx[1] - 108, yl, ACCENT, 2.5))
    b.append(txt((bx[0] + bx[1]) / 2, yl - 14, t["v2_lbl_entrega"], 14.5, "400",
                 GRAY, anchor="middle", style="italic"))
    b.append(arrow(bx[1] + 108, yl - 15, bx[2] - 108, yl - 15, ACCENT, 2.5))
    b.append(arrow(bx[2] - 108, yl + 17, bx[1] + 108, yl + 17, AMBER, 2.5))
    b.append(txt((bx[1] + bx[2]) / 2, yl + 42, t["v2_lbl_reclama"], 14.5, "700",
                 AMBER, anchor="middle", style="italic"))

    # o registro da sessão desce para quem opera o modelo
    yo = 706
    ox = bx[2]
    b.append(arrow(ox, yl + 70, ox, yo - 48, AMBER, 2.5))
    b.append(txt(ox + 18, yl + 106, t["v2_lbl_registro"], 14.5, "700", AMBER,
                 style="italic"))
    no(ox, yo, t["v2_no_operador"], AMBER, w=252, h=90)

    # a seta de volta ao produto, cortada no caminho
    b.append(arrow(ox - 134, yo, bx[0] + 40, yo, MUTED, 2.5, dash="8 7"))
    xc = (bx[0] + ox) / 2
    b.append(line(xc - 17, yo - 21, xc + 17, yo + 21, "#9C4A3C", 4))
    b.append(line(xc + 17, yo - 21, xc - 17, yo + 21, "#9C4A3C", 4))
    for i, l in enumerate(t["v2_corte"].split("\n")):
        b.append(txt(xc, yo + 50 + i * 20, l, 15, "700", "#9C4A3C", anchor="middle"))

    fy = 812
    b.append(rect(60, fy, W - 120, 62, NAVY, rx=12, op="0.06"))
    b.append(rect(60, fy, W - 120, 62, "none", NAVY, 1.5, rx=12))
    b.append(txt(W / 2, fy + 39, t["v2_faixa"], 19.5, "700", NAVY, anchor="middle"))

    assert fy + 62 < H - 66, "faixa encostando no rodapé"
    footer(b, W, H, t["v2_rodape"])
    return doc(W, H, "".join(b))


# --------------------------------------------- v3: polissemia e sinonímia
def v3(t, lang):
    H = 820
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    pw = (W - 120 - 40) / 2
    for k in (0, 1):
        px = 60 + k * (pw + 40)
        cor = AMBER if k == 0 else ACCENT
        soft = AMBER_SOFT if k == 0 else ACCENT_SOFT
        b.append(rect(px, 196, pw, 452, soft, rx=14))
        b.append(rect(px, 196, pw, 452, "none", cor, 2, rx=14))
        b.append(txt(px + pw / 2, 240, t["v3_p_tit"] if k == 0 else t["v3_s_tit"],
                     20, "700", cor, anchor="middle", sp="2"))
        deff = (t["v3_p_def"] if k == 0 else t["v3_s_def"]).split("\n")
        for i, l in enumerate(deff):
            b.append(txt(px + pw / 2, 272 + i * 22, l, 15.5, "400", GRAY,
                         anchor="middle", style="italic"))

        cx = px + pw / 2
        ytop, ybot = 352, 478
        tri = [cx - 168, cx, cx + 168]

        if k == 0:   # um nome -> tres sentidos
            b.append(rect(cx - 74, ytop - 24, 148, 48, WHITE, cor, 2, rx=10))
            b.append(txt(cx, ytop + 7, t["v3_signif"], 16.5, "700", cor, anchor="middle"))
            for xx in tri:
                b.append(arrow(cx, ytop + 28, xx, ybot - 26, cor, 2))
                b.append(circle(xx, ybot, 24, WHITE, cor, 2))
                b.append(txt(xx, ybot + 6, "?", 20, "700", cor, anchor="middle"))
            b.append(txt(cx, ybot + 52, t["v3_sent"], 14.5, "400", GRAY_LIGHT,
                         anchor="middle", style="italic"))
        else:        # tres nomes -> um sentido
            for xx in tri:
                b.append(rect(xx - 60, ytop - 22, 120, 44, WHITE, cor, 2, rx=10))
                b.append(txt(xx, ytop + 7, t["v3_signif"], 15, "700", cor, anchor="middle"))
                b.append(arrow(xx, ytop + 26, cx, ybot - 28, cor, 2))
            b.append(circle(cx, ybot, 26, WHITE, cor, 2))
            b.append(txt(cx, ybot + 7, "=", 22, "700", cor, anchor="middle"))
            b.append(txt(cx, ybot + 52, t["v3_sent"], 14.5, "400", GRAY_LIGHT,
                         anchor="middle", style="italic"))

        serie = (t["v3_p_serie"] if k == 0 else t["v3_s_serie"]).split("\n")
        sy = 578
        b.append(line(px + 40, sy - 22, px + pw - 40, sy - 22, cor, 1, dash="4 4"))
        assert sy - 22 > ybot + 58, "rótulo de sentido colidindo com a divisória" 
        for i, l in enumerate(serie):
            b.append(txt(cx, sy + 4 + i * 21, l, 15.5, "700", NAVY, anchor="middle"))

    fy = 672
    b.append(rect(60, fy, W - 120, 62, NAVY, rx=12, op="0.06"))
    b.append(rect(60, fy, W - 120, 62, "none", NAVY, 1.5, rx=12))
    b.append(txt(W / 2, fy + 39, t["v3_faixa"], 19.5, "700", NAVY, anchor="middle"))
    assert fy + 62 < H - 66, "faixa encostando no rodapé"

    footer(b, W, H, t["v3_rodape"])
    return doc(W, H, "".join(b))


# ------------------------------------------------- v4: os quatro modelos
def v4(t, lang):
    H = 800
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    x0 = 60
    c1, c2 = 430, 520          # larguras das duas primeiras colunas
    y0, rh = 232, 92

    for i, h in enumerate(t["v4_h"]):
        cx = x0 + (0 if i == 0 else c1 if i == 1 else c1 + c2) + 18
        b.append(txt(cx, y0 - 16, h, 14.5, "700", GRAY, sp="1.5"))
    b.append(line(x0, y0 - 2, W - 60, y0 - 2, BORDER, 1.5))

    for j, (m, eq, rec, dest) in enumerate(t["v4_linhas"]):
        y = y0 + j * rh
        cor = AMBER if dest else ACCENT
        if dest:
            b.append(rect(x0, y + 6, W - 120, rh - 12, AMBER_SOFT, rx=12))
            b.append(rect(x0, y + 6, W - 120, rh - 12, "none", AMBER, 2.5, rx=12))
        b.append(rect(x0 + 6, y + 20, 5, rh - 40, cor, rx=3))
        b.append(txt(x0 + 26, y + rh / 2 + 6, m, 18.5, "700",
                     AMBER if dest else NAVY))
        b.append(txt(x0 + c1 + 18, y + rh / 2 + 6, eq, 16, "400", GRAY))
        b.append(txt(x0 + c1 + c2 + 18, y + rh / 2 + 6, rec, 16,
                     "700" if dest else "400", AMBER if dest else NAVY))
        if not dest and j < len(t["v4_linhas"]) - 1:
            b.append(line(x0, y + rh, W - 60, y + rh, BORDER, 0.8))

    fy = y0 + len(t["v4_linhas"]) * rh + 30
    b.append(rect(x0, fy, W - 120, 62, ACCENT_SOFT, rx=12))
    b.append(rect(x0, fy, W - 120, 62, "none", ACCENT, 1.5, rx=12))
    b.append(txt(W / 2, fy + 39, t["v4_faixa"], 19.5, "700", ACCENT, anchor="middle"))

    footer(b, W, H, t["v4_rodape"])
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
    b.append(txt(120, 322, t["capa_t1"], 74, "700", WHITE))
    b.append(txt(120, 412, t["capa_t2"], 74, "700", WHITE))
    b.append(txt(120, 476, t["capa_sub"], 30, "400", "#AEB6C2"))

    qy = 574
    b.append(rect(120, qy, CW - 240, 250, AMBER, rx=16, op="0.13"))
    b.append(rect(120, qy, CW - 240, 250, "none", AMBER, 2, rx=16))
    b.append(rect(120, qy, 7, 250, AMBER, rx=0))
    b.append(txt(172, qy + 84, t["capa_frase1"], 36, "400", "#E8DCC8"))
    b.append(txt(172, qy + 146, t["capa_frase2"], 36, "700", WHITE))
    b.append(txt(172, qy + 206, t["capa_creditof"], 22, "400", "#AEB6C2",
                 style="italic"))

    b.append(line(120, CH - 90, CW - 120, CH - 90, ACCENT, 1.5))
    b.append(txt(120, CH - 48, t["capa_rodape"], 22, "400", "#AEB6C2"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{CW}" height="{CH}" '
            f'viewBox="0 0 {CW} {CH}">{"".join(b)}</svg>')


def gerar(lang):
    t = T[lang]
    save(f"p6-capa-pt" if lang == "pt" else "p6-cover-en", capa(t, lang), scale=1.5)
    save(t["v1_nome"], v1(t, lang))
    save(t["v2_nome"], v2(t, lang))
    save(t["v3_nome"], v3(t, lang))
    save(t["v4_nome"], v4(t, lang))


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    for lang in (["pt", "en"] if alvo is None else [alvo]):
        gerar(lang)
