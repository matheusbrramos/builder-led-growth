#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visuais do arco 2, parte 1 — o funil e o eixo da delegação.

PT e EN no mesmo arquivo. Helpers de desenho importados do gen_p4.
Como nas peças anteriores, cada função termina com assert de folga contra o
rodapé: peça torta falha alto em vez de sair publicada.

UMA DIFERENÇA EM RELAÇÃO AOS GERADORES ANTERIORES, E ELA É DE PROPÓSITO
-----------------------------------------------------------------------
Os outros escrevem ao lado de si mesmos, em `scripts/`, e alguém precisa mover
os arquivos para `visuais/` depois. Nenhum portão cobre esse passo — o plano do
arco 2 chegou a registrá-lo como "cuidado que os verificadores não pegam". Passo
que só existe na cabeça de quem executa é passo que um dia não acontece, então
aqui o destino é explícito e o gerador escreve direto no lugar certo.

Uso:  python scripts/gen_a2p1.py          # gera PT e EN
      python scripts/gen_a2p1.py pt       # só português
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# O gen_p4 importa cairosvg no topo, e e dele que vem TODO o desenho: paleta,
# `txt`, `rect`, `header`, `footer`. Nesta maquina esse import estoura antes de
# qualquer funcao existir — o que derruba um gerador que nem ia usar o cairosvg,
# porque rasteriza pelo Chrome (ver `_png_pelo_chrome`). Entao, quando a
# biblioteca nativa nao esta la, um substituto vazio entra no lugar so para o
# import passar. A unica funcao do gen_p4 que tocaria o cairosvg e a `save`, e
# ela nao e importada aqui de proposito.
try:
    import cairosvg  # noqa: F401
except Exception:
    import types
    sys.modules["cairosvg"] = types.ModuleType("cairosvg")

from gen_p4 import (  # noqa: E402
    ACCENT, ACCENT_LIGHT, ACCENT_SOFT, AMBER, AMBER_SOFT, BORDER, GRAY,
    GRAY_LIGHT, GREEN, GREEN_SOFT, MUTED, NAVY, NAVY_DEEP, PANEL, WHITE,
    arrow, circle, doc, footer, header, line, rect, txt,
)

W = 1600
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, "visuais", "arco2-parte-01")

RED = "#9C4A3C"
RED_SOFT = "#F5E6E2"

# ---------------------------------------------------------------- números
# Existem uma vez só, e batem com o texto das duas línguas.
TETO_DECIDIR = 11
ESTREITAR = 31
CONFEREM = 86
VALIDAM_B2B = 69
VERIFICA_ANTES = 98
SEM_BUSCA = 57.8
CONVERGE_LIB = 48
CONVERGE_PY = 58


CHROME = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium",
]


def _cairo():
    # `hasattr` e nao so o import: quando a biblioteca nativa falta, quem esta em
    # sys.modules e o substituto vazio instalado la em cima, e ele importa limpo.
    try:
        import cairosvg
        return cairosvg if hasattr(cairosvg, "svg2png") else None
    except Exception:
        return None


def _chrome():
    for c in CHROME:
        if os.path.isfile(c):
            return c
    return shutil.which("chrome") or shutil.which("google-chrome")


def _png_pelo_chrome(svg_path, png_path, w, h, scale, svg=None):
    """Rasteriza com o Chrome que ja esta instalado.

    Por que existe: nesta maquina o `cairosvg` importa e nao roda — a biblioteca
    nativa Cairo nao esta instalada no Windows, e o erro e
    `no library called "libcairo-2" was found`. Isso ja travou regeracao de
    visual antes, e o diario de publicacao registrou um comando manual de Chrome
    headless como saida. Passo manual anotado num diario e passo que um dia nao
    acontece; aqui ele vira caminho do proprio gerador.

    O `--user-data-dir` separado NAO e opcional: sem ele o Chrome termina em
    silencio, sem escrever arquivo nenhum, porque o perfil padrao esta travado
    pela janela que a pessoa tem aberta.
    """
    exe = _chrome()
    if not exe:
        return False
    perfil = os.path.join(tempfile.gettempdir(), "blg-svg-profile")

    # O SVG e embrulhado num HTML com margem zero, e nao aberto direto.
    # Aberto direto, o Chrome aplica a margem de corpo padrao — 8 pixels — e o
    # recorte come a faixa de acento que corre no x=0 da lateral esquerda. Some
    # exatamente um elemento de identidade visual da serie, e some em silencio:
    # o PNG sai com o tamanho certo e sem erro nenhum. Foi visto a olho na
    # primeira geracao desta peca.
    envoltorio = os.path.join(tempfile.gettempdir(),
                              "blg-%s.html" % os.path.basename(svg_path))
    corpo = svg if svg is not None else open(svg_path, encoding="utf-8").read()
    open(envoltorio, "w", encoding="utf-8").write(
        '<!doctype html><meta charset="utf-8">'
        '<style>html,body{margin:0;padding:0;overflow:hidden}'
        'svg{display:block}</style>' + corpo)

    url = "file:///" + os.path.abspath(envoltorio).replace("\\", "/")
    cmd = [
        exe, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        "--user-data-dir=%s" % perfil,
        "--force-device-scale-factor=%s" % scale,
        "--window-size=%d,%d" % (w, h),
        "--screenshot=%s" % os.path.abspath(png_path),
        url,
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                   timeout=120)
    return os.path.isfile(png_path)


def salvar(nome, svg, scale=2):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "%s.svg" % nome)
    open(p, "w", encoding="utf-8").write(svg)
    png = os.path.join(OUT, "%s.png" % nome)

    cs = _cairo()
    if cs is not None:
        cs.svg2png(url=p, write_to=png, scale=scale)
    else:
        m = re.search(r'width="(\d+)" height="(\d+)"', svg)
        w, h = int(m.group(1)), int(m.group(2))
        if not _png_pelo_chrome(p, png, w, h, scale, svg=svg):
            raise SystemExit(
                "Nao consegui gerar o PNG de %s. O cairosvg nao roda aqui (falta a\n"
                "biblioteca nativa Cairo) e nao achei o Chrome para rasterizar.\n"
                "O SVG foi escrito e esta correto — falta so o PNG." % nome)
    print("ok:", os.path.relpath(png, RAIZ))


def fecho(b, H, texto, cor=NAVY, soft=None):
    y = H - 152
    b.append(rect(60, y, W - 120, 62, soft or PANEL, rx=12))
    b.append(rect(60, y, 6, 62, cor, rx=0))
    b.append(txt(92, y + 39, texto, 19, "700", cor))


def eixo_polos(b, y, esq, dir_, largura=W - 240, x0=120):
    """A barra do eixo, com os dois polos nomeados. Reaparece em tres visuais."""
    b.append(rect(x0, y, largura, 10, BORDER, rx=5))
    b.append(rect(x0, y, largura * 0.5, 10, GREEN, rx=5))
    b.append(rect(x0 + largura * 0.5, y, largura * 0.5, 10, ACCENT, rx=5))
    b.append(txt(x0, y - 18, esq, 16, "700", GREEN))
    b.append(txt(x0 + largura, y - 18, dir_, 16, "700", ACCENT, anchor="end"))


# ------------------------------------------------ v1: onde as pessoas estao
def v1(t, lang):
    H = 820
    b = []
    header(b, t["v1_kicker"], t["v1_titulo"], t["v1_sub"], H)

    eixo_polos(b, 236, t["v1_polo_esq"], t["v1_polo_dir"])
    b.append(txt(W / 2, 286, t["v1_eixo_nota"], 15.5, "400", GRAY_LIGHT,
                 anchor="middle", style="italic"))

    # Quatro cartoes, um por levantamento. O numero grande, o que ele mede, e
    # a ressalva colada nele -- nunca em rodape, que e regra da casa.
    cw, gap = 340, 24
    x0 = (W - (cw * 4 + gap * 3)) / 2
    dados = [
        (TETO_DECIDIR, "%", t["v1_0_tit"], t["v1_0_txt"], RED, RED_SOFT),
        (ESTREITAR, "%", t["v1_1_tit"], t["v1_1_txt"], AMBER, AMBER_SOFT),
        (CONFEREM, "%", t["v1_2_tit"], t["v1_2_txt"], ACCENT, ACCENT_SOFT),
        (VALIDAM_B2B, "%", t["v1_3_tit"], t["v1_3_txt"], GREEN, GREEN_SOFT),
    ]
    cy = 336
    for i, (v, un, tit, sub, cor, soft) in enumerate(dados):
        x = x0 + i * (cw + gap)
        b.append(rect(x, cy, cw, 244, soft, rx=14))
        b.append(rect(x, cy, cw, 244, "none", cor, 2, rx=14))
        b.append(rect(x, cy, cw, 6, cor, rx=0))
        b.append(txt(x + 26, cy + 88, "%s%s" % (v, un), 52, "700", cor))
        b.append(txt(x + 26, cy + 126, tit, 16.5, "700", NAVY))
        for j, l in enumerate(sub.split("\n")):
            b.append(txt(x + 26, cy + 158 + j * 22, l, 14, "400", GRAY))

    yb = 612
    b.append(rect(120, yb, W - 240, 46, PANEL, rx=10))
    b.append(txt(W / 2, yb + 30, t["v1_quarta"], 16, "400", GRAY, anchor="middle"))

    fecho(b, H, t["v1_faixa"])
    footer(b, W, H, t["v1_rodape"])
    assert yb + 46 < H - 152, "v1 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v2: a remocao
def v2(t, lang):
    """Os quatro mecanismos que encolhem o conjunto conforme a delegacao sobe.

    Este visual mostrava "tres opcoes existiam, uma entrou no codigo". A cena
    continua no texto, mas o achado que a explica ficou mais forte que ela: nao e
    so que a pessoa deixa de escolher, e que o CONJUNTO de onde se escolheria
    encolhe — e ha quatro mecanismos medidos empurrando nessa direcao.
    """
    H = 880
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    cw, gap = 355, 20
    x0 = (W - (cw * 4 + gap * 3)) / 2
    cy, ch = 246, 330
    cores = [ACCENT, AMBER, GREEN, RED]
    softs = [ACCENT_SOFT, AMBER_SOFT, GREEN_SOFT, RED_SOFT]

    for i in range(4):
        cx = x0 + i * (cw + gap)
        b.append(rect(cx, cy, cw, ch, softs[i], rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cores[i], 2, rx=14))
        b.append(rect(cx, cy, cw, 6, cores[i], rx=0))
        b.append(txt(cx + 24, cy + 52, t["v2_m%d_rot" % i], 13, "700", cores[i],
                     sp="1.5"))
        b.append(txt(cx + 24, cy + 100, t["v2_m%d_num" % i], 34, "700", cores[i]))
        for j, l in enumerate(t["v2_m%d_txt" % i].split("\n")):
            b.append(txt(cx + 24, cy + 142 + j * 23, l, 14.5, "400", NAVY))
        b.append(txt(cx + 24, cy + ch - 26, t["v2_m%d_fonte" % i], 12.5, "400",
                     GRAY_LIGHT))

    yb = cy + ch + 34
    b.append(rect(60, yb, W - 120, 78, NAVY, rx=14))
    b.append(txt(W / 2, yb + 34, t["v2_barra1"], 24, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 62, t["v2_barra2"], 16, "400", "#AEB6C2",
                 anchor="middle"))

    fecho(b, H, t["v2_faixa"])
    footer(b, W, H, t["v2_rodape"])
    assert yb + 78 < H - 152, "v2 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v3: funil, roda e camadas
def v3(t, lang):
    """As tres camadas do que atravessa de uma decisao para a outra.

    Tinha o funil e a roda em dois planos, a esquerda. O debate funil-contra-roda
    saiu do texto por decisao de Mat — o funil ja esta resolvido como figura e
    relitiga-lo so confundia. Sobra o que interessa: a camada do meio e a unica
    com dono, e e o freio que a pessoa controla.
    """
    H = 900
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    camadas = [
        (t["v3_c0"], t["v3_c0_dono"], t["v3_c0_txt"], MUTED, WHITE),
        (t["v3_c1"], t["v3_c1_dono"], t["v3_c1_txt"], AMBER, AMBER_SOFT),
        (t["v3_c2"], t["v3_c2_dono"], t["v3_c2_txt"], GRAY_LIGHT, WHITE),
    ]
    cy, ch = 246, 116
    for i, (nome, dono, txt_, cor, soft) in enumerate(camadas):
        yy = cy + i * (ch + 18)
        b.append(rect(120, yy, W - 240, ch, soft, cor, 2, rx=12))
        b.append(rect(120, yy, 7, ch, cor, rx=0))
        b.append(txt(156, yy + 46, nome, 26, "700", NAVY))
        b.append(txt(156, yy + 82, txt_, 15.5, "400", GRAY))
        b.append(txt(W - 156, yy + 46, dono, 17, "700",
                     NAVY if i == 1 else GRAY_LIGHT, anchor="end"))
        if i == 1:
            b.append(txt(W - 156, yy + 78, t["v3_c1_marca"], 14, "400", AMBER,
                         anchor="end", style="italic"))

    yb = cy + 3 * (ch + 18) + 12
    b.append(rect(120, yb, W - 240, 76, NAVY, rx=14))
    b.append(txt(W / 2, yb + 34, t["v3_barra1"], 24, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 62, t["v3_barra2"], 15.5, "400", "#AEB6C2",
                 anchor="middle"))

    fecho(b, H, t["v3_faixa"])
    footer(b, W, H, t["v3_rodape"])
    assert yb + 76 < H - 152, "v3 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v4: etapas contra o eixo
def v4(t, lang):
    """As tres etapas do funil, com o custo de remocao subindo.

    Terceira forma deste visual. Foi "assistida contra delegada" em duas colunas,
    depois "tres condicoes contra tres regimes" numa grade — e nenhuma das duas
    servia, porque a lista de etapas estava errada. Mat reclassificou recomendacao
    de etapa para forca dentro da candidatura, e as etapas passaram a ser
    candidatura, construcao e adocao. O que o visual precisa mostrar agora e outra
    coisa: onde o produto esta, e quanto custa tira-lo de la.
    """
    H = 880
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    colx = [60, 570, 1080]
    cw = 460
    cores = [GREEN, AMBER, ACCENT]
    softs = [GREEN_SOFT, AMBER_SOFT, ACCENT_SOFT]
    cy, ch = 250, 300

    for i in range(3):
        cx = colx[i]
        b.append(rect(cx, cy, cw, ch, softs[i], rx=14))
        b.append(rect(cx, cy, cw, ch, "none", cores[i], 2, rx=14))
        b.append(rect(cx, cy, cw, 7, cores[i], rx=0))
        b.append(txt(cx + 30, cy + 66, t["v4_e%d" % i], 34, "700", NAVY))
        for j, l in enumerate(t["v4_e%d_def" % i].split("\n")):
            b.append(txt(cx + 30, cy + 106 + j * 24, l, 16, "400", GRAY))

        # O custo de remocao e a espinha do visual: e a unica coisa que sobe de
        # forma monotonica ao longo das tres, e e o que faz disto um funil.
        b.append(line(cx + 30, cy + 196, cx + cw - 30, cy + 196, cores[i], 1.5))
        b.append(txt(cx + 30, cy + 226, t["v4_custo_rot"], 13, "700", cores[i],
                     sp="1.5"))
        b.append(txt(cx + 30, cy + 264, t["v4_e%d_custo" % i], 24, "700", cores[i]))

        if i < 2:
            b.append(arrow(cx + cw + 14, cy + ch / 2, cx + cw + 42, cy + ch / 2,
                           MUTED, 3))

    # A barra da delegacao, embaixo: e ela que diz a velocidade da travessia.
    yb = cy + ch + 46
    b.append(rect(60, yb, W - 120, 76, NAVY, rx=14))
    b.append(txt(92, yb + 34, t["v4_barra1"], 22, "700", WHITE))
    b.append(txt(92, yb + 62, t["v4_barra2"], 15.5, "400", "#AEB6C2"))

    fecho(b, H, t["v4_faixa"])
    footer(b, W, H, t["v4_rodape"])
    assert yb + 76 < H - 152, "v4 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v5: o veto em dois estados
def v5(t, lang):
    H = 830
    b = []
    header(b, t["v5_kicker"], t["v5_titulo"], t["v5_sub"], H)

    pw = 700
    py = 246
    ph = 300
    for k in (0, 1):
        px = 120 if k == 0 else W - 120 - pw
        cor = GREEN if k == 0 else ACCENT
        soft = GREEN_SOFT if k == 0 else ACCENT_SOFT
        pcx = px + pw / 2
        b.append(rect(px, py, pw, ph, soft, rx=14))
        b.append(rect(px, py, pw, ph, "none", cor, 2, rx=14))
        b.append(txt(pcx, py + 44, t["v5_%d_tit" % k], 17, "700", cor,
                     anchor="middle", sp="2"))
        b.append(txt(pcx, py + 92, t["v5_%d_gesto" % k], 32, "700", NAVY,
                     anchor="middle"))

        # Tres caixinhas na assistida, uma so na delegada -- a diferenca e o
        # argumento inteiro, entao ela e desenhada e nao escrita.
        n = 3 if k == 0 else 1
        bw = 170 if k == 0 else 400
        total = n * bw + (n - 1) * 20
        sx = pcx - total / 2
        for i in range(n):
            b.append(rect(sx + i * (bw + 20), py + 128, bw, 56, WHITE, cor,
                          1.5 if (k == 1 or i == 0) else 1, rx=8))
            b.append(txt(sx + i * (bw + 20) + bw / 2, py + 163,
                         t["v5_%d_cx%d" % (k, i)], 16, "700" if i == 0 else "400",
                         NAVY if i == 0 else GRAY, anchor="middle"))
        for j, l in enumerate(t["v5_%d_txt" % k].split("\n")):
            b.append(txt(pcx, py + 218 + j * 24, l, 15.5, "400", GRAY,
                         anchor="middle"))

    yb = 580
    b.append(rect(120, yb, W - 240, 72, AMBER_SOFT, rx=14))
    b.append(rect(120, yb, 6, 72, AMBER, rx=0))
    b.append(txt(160, yb + 30, t["v5_custo1"], 18, "700", NAVY))
    b.append(txt(160, yb + 56, t["v5_custo2"], 15.5, "400", GRAY))

    fecho(b, H, t["v5_faixa"])
    footer(b, W, H, t["v5_rodape"])
    assert yb + 72 < H - 152, "v5 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ capa
def capa(t, lang):
    CW, CH = 1920, 1080
    b = ['<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (CW, CH, NAVY_DEEP)]
    for i in range(9):
        x = 1180 + i * 92
        b.append('<line x1="%d" y1="0" x2="%d" y2="%d" stroke="%s" '
                 'stroke-opacity="0.10" stroke-width="2"/>' % (x, x - 240, CH, ACCENT))

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
    b.append(txt(172, qy + 206, t["capa_creditof"], 22, "400", "#AEB6C2",
                 style="italic"))

    b.append(line(120, CH - 90, CW - 120, CH - 90, ACCENT, 1.5))
    b.append(txt(120, CH - 48, t["capa_rodape"], 22, "400", "#AEB6C2"))
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 %d %d">%s</svg>' % (CW, CH, CW, CH, "".join(b)))


# ---------------------------------------------------------------- textos
T = {
    "pt": {
        "capa_kicker": "BUILDER-LED GROWTH — ARCO 2, PARTE 1",
        "capa_t1": "Não é quem decide.",
        "capa_t2": "É quanto foi delegado",
        "capa_sub": "O funil, o eixo da delegação, e a decisão que ninguém tomou",
        "capa_frase1": "Decisão assistida: a pessoa escolhe entre opções que a máquina reuniu.",
        "capa_frase2": "Decisão delegada: ela aceita ou recusa um resultado já construído.",
        "capa_creditof": "Quatro levantamentos, três camadas de memória, e um número que ninguém publica",
        "capa_rodape": "Matheus Ramos · arco 2, parte 1",

        "v1_nome": "a2p1-eixo-pt",
        "v1_kicker": "ONDE AS PESSOAS ESTÃO HOJE",
        "v1_titulo": "O que se delega é a lista curta, não a escolha",
        "v1_sub": "Quatro medições, quatro populações, e o mesmo desenho em todas",
        "v1_polo_esq": "DECISÃO ASSISTIDA",
        "v1_polo_dir": "DECISÃO DELEGADA",
        "v1_eixo_nota": "delegação é grau, nunca estado",
        "v1_0_tit": "deixar a IA decidir a compra",
        "v1_0_txt": "É TETO, não média — e ocorre\nnas categorias de menor risco\nGartner, mai/2026, n=322",
        "v1_1_tit": "deixar a IA estreitar as opções",
        "v1_1_txt": "Categoria específica: limpeza\ne casa. Eletrônico pessoal: 28%\nGartner, mai/2026, n=322",
        "v1_2_tit": "conferem em outra fonte",
        "v1_2_txt": "Quem pesquisou produto com IA\nverificou antes de comprar\npadrão observado, n não confirmado",
        "v1_3_tit": "validam com uma pessoa",
        "v1_3_txt": "Compradores B2B. É preferência\nDECLARADA, não comportamento\nGartner, mai/2026, n=645",
        "v1_quarta": "E uma quarta população na mesma direção: %d%% dos consumidores verificam a recomendação da IA antes de comprar" % VERIFICA_ANTES,
        "v1_faixa": "Este é o regime da lista curta. A máquina monta o conjunto e sai antes da decisão.",
        "v1_rodape": "Builder-Led Growth, arco 2 · Gartner (mai/2026) · Idea Grove (2026) · IDC (jan/2026)",

        "v2_nome": "a2p1-remocao-pt",
        "v2_kicker": "O QUE A DELEGAÇÃO FAZ COM O CONJUNTO",
        "v2_titulo": "Não é só que a pessoa deixa de escolher",
        "v2_sub": "Quatro mecanismos medidos encolhem o conjunto de onde a escolha sairia",
        "v2_m0_rot": "O RECUPERADOR",
        "v2_m0_num": "1,4 ou 7,4",
        "v2_m0_txt": "Quantos candidatos o modelo\nchega a ver, sobre os MESMOS\ndados. Trocar uma peça de\ninfraestrutura muda isso",
        "v2_m0_fonte": "arXiv 2605.24660 · escopo: se a certa aparece",
        "v2_m1_rot": "O TAMANHO DO CATÁLOGO",
        "v2_m1_num": "95% → 20%",
        "v2_m1_txt": "Acurácia de selecionar a certa:\n84-95% com ~50 ferramentas,\n41-83% com 200, e 0-20% na\nmaioria dos modelos com 740",
        "v2_m1_fonte": "arXiv 2510.00307 · laboratório, catálogo sintético",
        "v2_m2_rot": "A ORDEM",
        "v2_m2_num": "13% a 85%",
        "v2_m2_txt": "O quanto a ordem sozinha move\no desempenho. No meio de lista\nlonga, a ferramenta certa é\nescolhida em 22% a 52%",
        "v2_m2_fonte": "arXiv 2510.00307 · mesma ressalva",
        "v2_m3_rot": "A BUSCA QUE NÃO ACONTECE",
        "v2_m3_num": "57,8%",
        "v2_m3_txt": "Das repetições não acionaram\nbusca na web. Sem busca, o\nconjunto vem inteiro do que o\nmodelo já traz de fábrica",
        "v2_m3_fonte": "arXiv 2604.07585 · via citação em revisão",
        "v2_barra1": "A delegação encolhe o conjunto de onde a escolha sairia",
        "v2_barra2": "Quem já é padrão de categoria ganha. Quem disputa o segundo lugar não é escolhido nem comparado",
        "v2_faixa": "Medido no comportamento: bibliotecas populares em até %d%% dos casos, Python em %d%%." % (CONVERGE_LIB, CONVERGE_PY),
        "v2_rodape": "Builder-Led Growth, arco 2 · arXiv 2605.24660 · BiasBusters (ICLR 2026) · arXiv 2604.07585 · arXiv 2503.17181 (ACL 2026)",

        "v3_nome": "a2p1-funil-e-camadas-pt",
        "v3_kicker": "O QUE ATRAVESSA DE UMA DECISÃO PARA A OUTRA",
        "v3_titulo": "Três camadas, e só a do meio tem dono",
        "v3_sub": "E é ela o freio que quem constrói controla",
        "v3_c0": "A sessão",
        "v3_c0_txt": "Onde a eliminação acontece. Ninguém se reforça nela",
        "v3_c0_dono": "sem dono · efêmera",
        "v3_c1": "A memória do projeto",
        "v3_c1_txt": "Especificação, registro de decisão, arquivo de instrução para o agente",
        "v3_c1_dono": "quem constrói controla",
        "v3_c1_marca": "lida no começo de toda sessão",
        "v3_c2": "O corpus público",
        "v3_c2_txt": "O material que treina o modelo seguinte. Sobe devagar e desce devagar",
        "v3_c2_dono": "sem dono · sofre erosão",
        "v3_barra1": "A decisão escrita no arquivo deixa de ser decisão e vira premissa",
        "v3_barra2": "Não exige treino de modelo nem código escrito — exige uma linha num arquivo",
        "v3_faixa": "Estar inscrito ali é posição mais durável que o dado de treino, e mais barata que o custo de troca.",
        "v3_rodape": "Builder-Led Growth, arco 2 · corrige uma afirmação da parte 4 sobre a sessão começar do zero",

        "v4_nome": "a2p1-etapas-pt",
        "v4_kicker": "O FUNIL DO BUILDER",
        "v4_titulo": "Três etapas, e o custo de tirar você sobe em cada uma",
        "v4_sub": "As etapas dizem onde o produto está, não o que acontece com ele",
        "v4_custo_rot": "CUSTO DE REMOÇÃO",
        "v4_e0": "Candidatura",
        "v4_e0_def": "Você está no conjunto de onde\nse escolhe. É conhecido,\nencontrável, e ninguém\nprecisou de você ainda",
        "v4_e0_custo": "zero",
        "v4_e1": "Construção",
        "v4_e1_def": "Você saiu do corpus e entrou\nno código de algo que está\nsendo feito. Começa na\nprimeira linha que te chama",
        "v4_e1_custo": "algumas horas",
        "v4_e2": "Adoção",
        "v4_e2_def": "Você virou premissa do que\nfoi entregue. Há dados no seu\nformato e gente usando sem\nsaber que você existe",
        "v4_e2_custo": "um projeto",
        "v4_barra1": "Quanto mais o par delega, mais rápido um produto atravessa as três",
        "v4_barra2": "Recomendação não é etapa: é uma das forças que agem dentro da candidatura",
        "v4_faixa": "Chegar à adoção cria uma barreira competitiva que não foi conquistada em comparação.",
        "v4_rodape": "Builder-Led Growth, arco 2 · a separação entre decisão e implementação já estava em Rogers",

        "v5_nome": "a2p1-veto-pt",
        "v5_kicker": "O VETO MUDA DE NATUREZA",
        "v5_titulo": "De escolher entre alternativas a aceitar um resultado",
        "v5_sub": "O poder de veto continua com a pessoa. O que ela veta é que mudou",
        "v5_0_tit": "NA PONTA ASSISTIDA",
        "v5_0_gesto": "escolher",
        "v5_0_cx0": "Opção A",
        "v5_0_cx1": "Opção B",
        "v5_0_cx2": "Opção C",
        "v5_0_txt": "As alternativas continuam existindo\ncaso a primeira decepcione",
        "v5_1_tit": "NA PONTA DELEGADA",
        "v5_1_gesto": "aceitar ou recusar",
        "v5_1_cx0": "Um resultado já construído",
        "v5_1_txt": "Aceitar não exige avaliar nada:\nexige que nada pareça errado",
        "v5_custo1": "Mais barato de tomar, e mais caro de reverter",
        "v5_custo2": "No instante em que a pessoa aceita, aquilo já está escrito no código, com configuração e variável de ambiente em volta",
        "v5_faixa": "O que você controla não é a comparação — é o que a pessoa encontra pronto quando olha.",
        "v5_rodape": "Builder-Led Growth, arco 2 · desenvolvido na peça sobre adoção",
    },
    "en": {
        "capa_kicker": "BUILDER-LED GROWTH — ARC 2, PART 1",
        "capa_t1": "It isn't who decides.",
        "capa_t2": "It's how much was delegated",
        "capa_sub": "The funnel, the delegation axis, and the decision nobody made",
        "capa_frase1": "Assisted decision: the person chooses among options the machine assembled.",
        "capa_frase2": "Delegated decision: they accept or reject an already-built result.",
        "capa_creditof": "Four surveys, three layers of memory, and a number nobody publishes",
        "capa_rodape": "Matheus Ramos · arc 2, part 1",

        "v1_nome": "a2p1-axis-en",
        "v1_kicker": "WHERE PEOPLE SIT TODAY",
        "v1_titulo": "What gets delegated is the shortlist, not the choice",
        "v1_sub": "Four measurements, four populations, and the same shape in all of them",
        "v1_polo_esq": "ASSISTED DECISION",
        "v1_polo_dir": "DELEGATED DECISION",
        "v1_eixo_nota": "delegation is a degree, never a state",
        "v1_0_tit": "let AI make the purchase call",
        "v1_0_txt": "A CEILING, not an average —\nand it occurs in the lowest-stakes\ncategories · Gartner, May 2026, n=322",
        "v1_1_tit": "let AI narrow the options",
        "v1_1_txt": "One specific category: cleaning\nand household. Personal electronics: 28%\nGartner, May 2026, n=322",
        "v1_2_tit": "check against another source",
        "v1_2_txt": "Of those who researched a product\nwith AI, before buying\nobserved pattern, n unconfirmed",
        "v1_3_tit": "validate with a person",
        "v1_3_txt": "B2B buyers. This is STATED\npreference, not measured behaviour\nGartner, May 2026, n=645",
        "v1_quarta": "And a fourth population pointing the same way: %d%% of consumers verify the AI recommendation before buying" % VERIFICA_ANTES,
        "v1_faixa": "This is the shortlist regime. The machine assembles the set and leaves before the decision.",
        "v1_rodape": "Builder-Led Growth, arc 2 · Gartner (May 2026) · Idea Grove (2026) · IDC (Jan 2026)",

        "v2_nome": "a2p1-removal-en",
        "v2_kicker": "WHAT DELEGATION DOES TO THE SET",
        "v2_titulo": "It is not only that the person stops choosing",
        "v2_sub": "Four measured mechanisms shrink the set the choice would come from",
        "v2_m0_rot": "THE RETRIEVER",
        "v2_m0_num": "1.4 or 7.4",
        "v2_m0_txt": "How many candidates the model\ngets to see, over the SAME data.\nSwapping one piece of\ninfrastructure changes it",
        "v2_m0_fonte": "arXiv 2605.24660 · scope: whether the right one appears",
        "v2_m1_rot": "CATALOGUE SIZE",
        "v2_m1_num": "95% → 20%",
        "v2_m1_txt": "Accuracy at selecting the right\none: 84-95% with ~50 tools,\n41-83% with 200, and 0-20% for\nmost models with 740",
        "v2_m1_fonte": "arXiv 2510.00307 · lab, synthetic catalogue",
        "v2_m2_rot": "ORDER",
        "v2_m2_num": "13% to 85%",
        "v2_m2_txt": "How much ordering alone moves\nperformance. Mid-way down a long\nlist, the right tool is picked in\n22% to 52% of cases",
        "v2_m2_fonte": "arXiv 2510.00307 · same caveat",
        "v2_m3_rot": "THE SEARCH THAT NEVER HAPPENS",
        "v2_m3_num": "57.8%",
        "v2_m3_txt": "Of repetitions triggered no web\nsearch. Without one, the set comes\nentirely from what the model\nalready carries",
        "v2_m3_fonte": "arXiv 2604.07585 · via citation in a review",
        "v2_barra1": "Delegation shrinks the set the choice would have come from",
        "v2_barra2": "The category default gains. Whoever fights for second place is neither chosen nor compared",
        "v2_faixa": "Measured in behaviour: popular libraries in up to %d%% of cases, Python in %d%%." % (CONVERGE_LIB, CONVERGE_PY),
        "v2_rodape": "Builder-Led Growth, arc 2 · arXiv 2605.24660 · BiasBusters (ICLR 2026) · arXiv 2604.07585 · arXiv 2503.17181 (ACL 2026)",

        "v3_nome": "a2p1-funnel-and-layers-en",
        "v3_kicker": "WHAT CROSSES FROM ONE DECISION TO THE NEXT",
        "v3_titulo": "Three layers, and only the middle one has an owner",
        "v3_sub": "And it is the brake whoever builds controls",
        "v3_c0": "The session",
        "v3_c0_txt": "Where elimination happens. Nobody strengthens a position in it",
        "v3_c0_dono": "no owner · ephemeral",
        "v3_c1": "The project memory",
        "v3_c1_txt": "Specifications, decision records, instruction files for the agent",
        "v3_c1_dono": "whoever builds controls it",
        "v3_c1_marca": "read at the start of every session",
        "v3_c2": "The public corpus",
        "v3_c2_txt": "The material that trains the next model. Rises slowly and falls slowly",
        "v3_c2_dono": "no owner · erodes",
        "v3_barra1": "A decision written into the file stops being a decision and becomes a premise",
        "v3_barra2": "It needs neither model training nor code written — it needs one line in a file",
        "v3_faixa": "Being written there is a more durable position than the training data, and cheaper than switching cost.",
        "v3_rodape": "Builder-Led Growth, arc 2 · corrects a claim in part 4 about the session starting from zero",

        "v4_nome": "a2p1-stages-en",
        "v4_kicker": "THE BUILDER FUNNEL",
        "v4_titulo": "Three stages, and the cost of removing you rises at each",
        "v4_sub": "The stages say where the product is, not what happens to it",
        "v4_custo_rot": "COST OF REMOVAL",
        "v4_e0": "Candidacy",
        "v4_e0_def": "You are in the set that gets\nchosen from. Known, findable,\nand nobody has needed you\nyet",
        "v4_e0_custo": "zero",
        "v4_e1": "Construction",
        "v4_e1_def": "You left the corpus and entered\nthe code of something being\nmade. It starts at the first\nline that calls you",
        "v4_e1_custo": "a few hours",
        "v4_e2": "Adoption",
        "v4_e2_def": "You became a premise of what\nshipped. There is data in your\nformat and people using it\nwithout knowing you exist",
        "v4_e2_custo": "a project",
        "v4_barra1": "The more the pair delegates, the faster a product crosses all three",
        "v4_barra2": "Recommendation is not a stage: it is one of the forces acting inside candidacy",
        "v4_faixa": "Reaching adoption creates a competitive barrier that was never won in a comparison.",
        "v4_rodape": "Builder-Led Growth, arc 2 · the split between decision and implementation was already in Rogers",

        "v5_nome": "a2p1-veto-en",
        "v5_kicker": "THE VETO CHANGES IN KIND",
        "v5_titulo": "From choosing among alternatives to accepting a result",
        "v5_sub": "The veto power stays with the person. What they veto is what changed",
        "v5_0_tit": "AT THE ASSISTED END",
        "v5_0_gesto": "choose",
        "v5_0_cx0": "Option A",
        "v5_0_cx1": "Option B",
        "v5_0_cx2": "Option C",
        "v5_0_txt": "The alternatives go on existing\nshould the first one disappoint",
        "v5_1_tit": "AT THE DELEGATED END",
        "v5_1_gesto": "accept or reject",
        "v5_1_cx0": "One already-built result",
        "v5_1_txt": "Accepting requires evaluating nothing:\nit requires that nothing look wrong",
        "v5_custo1": "Cheaper to exercise, and more expensive to reverse",
        "v5_custo2": "The moment the person accepts, the thing is already written into the code, with configuration and environment variables around it",
        "v5_faixa": "What you control isn't the comparison — it's what the person finds already done when they look.",
        "v5_rodape": "Builder-Led Growth, arc 2 · developed in the piece on adoption",
    },
}


def gerar(lang):
    t = T[lang]
    salvar("a2p1-capa-pt" if lang == "pt" else "a2p1-cover-en", capa(t, lang), scale=1.5)
    for i, fn in enumerate((v1, v2, v3, v4, v5), start=1):
        salvar(t["v%d_nome" % i], fn(t, lang))


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    for lang in (["pt", "en"] if alvo is None else [alvo]):
        gerar(lang)
