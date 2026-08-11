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
    H = 840
    b = []
    header(b, t["v2_kicker"], t["v2_titulo"], t["v2_sub"], H)

    # Esquerda: as tres que existiam. Direita: uma no codigo, duas fora --
    # e o ponto do visual e que as duas NAO foram recusadas.
    bx, by, bw, bh = 120, 236, 560, 300
    b.append(rect(bx, by, bw, bh, PANEL, rx=14))
    b.append(txt(bx + 30, by + 46, t["v2_esq_tit"], 19, "700", NAVY))
    for i in range(3):
        yy = by + 78 + i * 68
        b.append(rect(bx + 30, yy, bw - 60, 54, WHITE, BORDER, 1.5, rx=10))
        b.append(circle(bx + 62, yy + 27, 9, MUTED))
        b.append(txt(bx + 88, yy + 33, t["v2_opc%d" % i], 17, "400", NAVY))

    b.append(arrow(bx + bw + 34, by + bh / 2, bx + bw + 128, by + bh / 2, MUTED, 3))

    dx = bx + bw + 162
    dw = W - 120 - dx
    b.append(rect(dx, by, dw, bh, WHITE, BORDER, 1.5, rx=14))
    b.append(txt(dx + 30, by + 46, t["v2_dir_tit"], 19, "700", NAVY))

    b.append(rect(dx + 30, by + 78, dw - 60, 54, GREEN_SOFT, GREEN, 2, rx=10))
    b.append(circle(dx + 62, by + 105, 9, GREEN))
    b.append(txt(dx + 88, by + 111, t["v2_entrou"], 17, "700", GREEN))

    for i in range(2):
        yy = by + 146 + i * 68
        b.append(rect(dx + 30, yy, dw - 60, 54, WHITE, BORDER, 1.5, rx=10, op="0.5"))
        b.append(circle(dx + 62, yy + 27, 9, MUTED))
        b.append(txt(dx + 88, yy + 33, t["v2_fora%d" % i], 17, "400", GRAY_LIGHT))
    b.append(txt(dx + 30, by + bh - 22, t["v2_dir_nota"], 15, "700", RED))

    yb = 570
    b.append(rect(120, yb, W - 240, 78, NAVY, rx=14))
    b.append(txt(W / 2, yb + 34, t["v2_barra1"], 25, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 62, t["v2_barra2"], 16.5, "400", "#AEB6C2", anchor="middle"))

    fecho(b, H, t["v2_faixa"])
    footer(b, W, H, t["v2_rodape"])
    assert yb + 78 < H - 152, "v2 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v3: funil, roda e camadas
def v3(t, lang):
    H = 860
    b = []
    header(b, t["v3_kicker"], t["v3_titulo"], t["v3_sub"], H)

    # Plano de baixo, a esquerda: o funil dentro da sessao.
    fx, fy = 120, 250
    fw = 560
    b.append(rect(fx, fy, fw, 300, ACCENT_SOFT, rx=14))
    b.append(rect(fx, fy, fw, 300, "none", ACCENT, 2, rx=14))
    b.append(txt(fx + 28, fy + 42, t["v3_funil_tit"], 19, "700", ACCENT))

    larguras = [420, 300, 180]
    for i, lw in enumerate(larguras):
        yy = fy + 74 + i * 66
        cx = fx + fw / 2
        b.append(rect(cx - lw / 2, yy, lw, 50, WHITE, ACCENT, 1.5, rx=8))
        b.append(txt(cx, yy + 32, t["v3_etapa%d" % i], 16.5, "700", NAVY,
                     anchor="middle"))
    b.append(txt(fx + 28, fy + 284, t["v3_funil_nota"], 15, "400", GRAY,
                 style="italic"))

    # Plano de cima, a direita: as tres camadas, com a coluna de dono.
    cx0 = fx + fw + 60
    cw = W - 120 - cx0
    b.append(rect(cx0, fy, cw, 300, PANEL, rx=14))
    b.append(txt(cx0 + 28, fy + 42, t["v3_camadas_tit"], 19, "700", NAVY))

    camadas = [
        (t["v3_c0"], t["v3_c0_dono"], MUTED, WHITE),
        (t["v3_c1"], t["v3_c1_dono"], AMBER, AMBER_SOFT),
        (t["v3_c2"], t["v3_c2_dono"], GRAY_LIGHT, WHITE),
    ]
    for i, (nome, dono, cor, soft) in enumerate(camadas):
        yy = fy + 74 + i * 66
        b.append(rect(cx0 + 28, yy, cw - 56, 50, soft, cor, 2, rx=8))
        b.append(rect(cx0 + 28, yy, 6, 50, cor, rx=0))
        b.append(txt(cx0 + 56, yy + 31, nome, 16.5, "700", NAVY))
        b.append(txt(cx0 + cw - 56, yy + 31, dono, 14.5, "400",
                     NAVY if i == 1 else GRAY_LIGHT, anchor="end"))
    b.append(txt(cx0 + 28, fy + 284, t["v3_camadas_nota"], 15, "400", GRAY,
                 style="italic"))

    yb = 596
    b.append(rect(120, yb, W - 240, 84, NAVY, rx=14))
    b.append(txt(W / 2, yb + 38, t["v3_barra1"], 26, "700", WHITE, anchor="middle"))
    b.append(txt(W / 2, yb + 68, t["v3_barra2"], 16.5, "400", "#AEB6C2",
                 anchor="middle"))

    fecho(b, H, t["v3_faixa"])
    footer(b, W, H, t["v3_rodape"])
    assert yb + 84 < H - 152, "v3 encosta no fecho"
    return doc(W, H, "".join(b))


# ------------------------------------------------ v4: etapas contra o eixo
def v4(t, lang):
    H = 940
    b = []
    header(b, t["v4_kicker"], t["v4_titulo"], t["v4_sub"], H)

    colx = [120, 520, 1060]
    colw = [380, 520, 420]
    ytop = 236

    b.append(txt(colx[1] + colw[1] / 2, ytop, t["v4_col1"], 16, "700", GREEN,
                 anchor="middle", sp="2"))
    b.append(txt(colx[2] + colw[2] / 2, ytop, t["v4_col2"], 16, "700", ACCENT,
                 anchor="middle", sp="2"))

    linhas = [
        (t["v4_e0"], t["v4_e0_a"], t["v4_e0_d"]),
        (t["v4_e1"], t["v4_e1_a"], t["v4_e1_d"]),
        (t["v4_e2"], t["v4_e2_a"], t["v4_e2_d"]),
    ]
    ry, rh = ytop + 26, 140
    for i, (etapa, assistida, delegada) in enumerate(linhas):
        yy = ry + i * (rh + 18)
        b.append(rect(colx[0], yy, colw[0], rh, NAVY, rx=12))
        b.append(txt(colx[0] + 28, yy + 56, etapa, 26, "700", WHITE))
        b.append(txt(colx[0] + 28, yy + 92, t["v4_e%d_def" % i], 14.5, "400",
                     "#AEB6C2"))

        for k, (texto, cor, soft, cx, cwd) in enumerate((
                (assistida, GREEN, GREEN_SOFT, colx[1], colw[1]),
                (delegada, ACCENT, ACCENT_SOFT, colx[2], colw[2]))):
            b.append(rect(cx, yy, cwd, rh, soft, rx=12))
            b.append(rect(cx, yy, cwd, rh, "none", cor, 2, rx=12))
            for j, l in enumerate(texto.split("\n")):
                b.append(txt(cx + 26, yy + 44 + j * 26, l, 16.5, "400", NAVY))

    yfim = ry + 3 * (rh + 18)
    fecho(b, H, t["v4_faixa"])
    footer(b, W, H, t["v4_rodape"])
    assert yfim < H - 152, "v4 encosta no fecho"
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
        "v1_faixa": "A máquina entra na composição do conjunto e sai antes da decisão.",
        "v1_rodape": "Builder-Led Growth, arco 2 · Gartner (mai/2026) · Idea Grove (2026) · IDC (jan/2026)",

        "v2_nome": "a2p1-remocao-pt",
        "v2_kicker": "A DECISÃO QUE NINGUÉM TOMOU",
        "v2_titulo": "Elas não foram recusadas. Não foram apresentadas",
        "v2_sub": "Por que a pergunta “em que momento as outras saíram?” não tem resposta",
        "v2_esq_tit": "TRÊS OPÇÕES EXISTIAM",
        "v2_opc0": "Provedor A",
        "v2_opc1": "Provedor B",
        "v2_opc2": "Provedor C",
        "v2_dir_tit": "O QUE CHEGOU À PESSOA",
        "v2_entrou": "Virou dependência no código",
        "v2_fora0": "nunca mencionado",
        "v2_fora1": "nunca mencionado",
        "v2_dir_nota": "Sem recusa, sem comparação, sem rastro",
        "v2_barra1": "A decisão não foi delegada. Foi removida do campo de visão",
        "v2_barra2": "Ninguém responde “quem escolheu?” sobre uma escolha que nunca lhe foi apresentada",
        "v2_faixa": "E quando é delegada, ela converge: bibliotecas populares em até %d%% dos casos, Python em %d%%." % (CONVERGE_LIB, CONVERGE_PY),
        "v2_rodape": "Builder-Led Growth, arco 2 · Supabase (jun/2026) · Neon via Databricks (jan/2026) · arXiv 2503.17181 (ACL 2026)",

        "v3_nome": "a2p1-funil-e-camadas-pt",
        "v3_kicker": "DOIS PLANOS DO MESMO FENÔMENO",
        "v3_titulo": "Funil dentro da sessão, flywheel entre sessões",
        "v3_sub": "E o que atravessa de uma sessão para a outra vive em três camadas",
        "v3_funil_tit": "DENTRO DA SESSÃO",
        "v3_etapa0": "Candidatura",
        "v3_etapa1": "Recomendação",
        "v3_etapa2": "Adoção",
        "v3_funil_nota": "A eliminação é irreversível e monotônica: perde-se opção e não se recupera",
        "v3_camadas_tit": "ENTRE SESSÕES",
        "v3_c0": "A sessão",
        "v3_c0_dono": "sem dono · efêmera",
        "v3_c1": "A memória do projeto",
        "v3_c1_dono": "quem constrói controla",
        "v3_c2": "O corpus público",
        "v3_c2_dono": "sem dono · sofre erosão",
        "v3_camadas_nota": "Só a do meio tem dono — e é a que era lida no começo de toda sessão",
        "v3_barra1": "O funil opera no nível da decisão, não no da sessão",
        "v3_barra2": "As decisões que importam são as registradas, porque essas pararam de ser decididas",
        "v3_faixa": "Roda que perde energia para de girar. O que se acumula entre sessões também evapora.",
        "v3_rodape": "Builder-Led Growth, arco 2 · a figura do funil: atribuição disputada, Lewis (1898), Sheldon, e a sigla AIDA em 1921",

        "v4_nome": "a2p1-etapas-pt",
        "v4_kicker": "AS TRÊS ETAPAS AO LONGO DO EIXO",
        "v4_titulo": "A mesma etapa muda de forma conforme a delegação sobe",
        "v4_sub": "Candidatura, recomendação e adoção nas duas pontas do eixo",
        "v4_col1": "DECISÃO ASSISTIDA",
        "v4_col2": "DECISÃO DELEGADA",
        "v4_e0": "Candidatura",
        "v4_e0_def": "estar no conjunto de onde se escolhe",
        "v4_e0_a": "Uma lista que a pessoa lê —\ne lista lida é auditável:\nquem lê percebe uma ausência",
        "v4_e0_d": "O conjunto se forma dentro\ndo processo e nunca é exibido.\nNinguém percebe ausência",
        "v4_e1": "Recomendação",
        "v4_e1_def": "ser o escolhido dentro do conjunto",
        "v4_e1_a": "A pessoa vê alternativas lado\na lado e aplica critério próprio",
        "v4_e1_d": "Não há comparação: há um\nresultado — e ele converge\npara o que é familiar",
        "v4_e2": "Adoção",
        "v4_e2_def": "sobreviver à integração e ao uso",
        "v4_e2_a": "Integra-se o que se escolheu,\nsabendo o que se escolheu",
        "v4_e2_d": "Integra-se o que apareceu, e a\nprimeira olhada com atenção\ncostuma ser quando quebra",
        "v4_faixa": "A visibilidade da perda cresce descendo o funil, e a capacidade de agir cai junto.",
        "v4_rodape": "Builder-Led Growth, arco 2 · numa configuração medida, %.1f%% das repetições não acionaram busca na web (arXiv 2604.07585)" % SEM_BUSCA,

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
        "v1_faixa": "The machine enters the composition of the set and exits before the decision.",
        "v1_rodape": "Builder-Led Growth, arc 2 · Gartner (May 2026) · Idea Grove (2026) · IDC (Jan 2026)",

        "v2_nome": "a2p1-removal-en",
        "v2_kicker": "THE DECISION NOBODY MADE",
        "v2_titulo": "They weren't rejected. They weren't presented",
        "v2_sub": "Why “at what moment did the others drop out?” has no answer",
        "v2_esq_tit": "THREE OPTIONS EXISTED",
        "v2_opc0": "Provider A",
        "v2_opc1": "Provider B",
        "v2_opc2": "Provider C",
        "v2_dir_tit": "WHAT REACHED THE PERSON",
        "v2_entrou": "Became a dependency in the code",
        "v2_fora0": "never mentioned",
        "v2_fora1": "never mentioned",
        "v2_dir_nota": "No rejection, no comparison, no trace",
        "v2_barra1": "The decision was not delegated. It was removed from view",
        "v2_barra2": "Nobody answers “who chose?” about a choice never put in front of them",
        "v2_faixa": "And when it is delegated, it converges: popular libraries in up to %d%% of cases, Python in %d%%." % (CONVERGE_LIB, CONVERGE_PY),
        "v2_rodape": "Builder-Led Growth, arc 2 · Supabase (Jun 2026) · Neon via Databricks (Jan 2026) · arXiv 2503.17181 (ACL 2026)",

        "v3_nome": "a2p1-funnel-and-layers-en",
        "v3_kicker": "TWO PLANES OF THE SAME PHENOMENON",
        "v3_titulo": "Funnel within the session, flywheel between sessions",
        "v3_sub": "And what crosses from one session to the next lives in three layers",
        "v3_funil_tit": "WITHIN THE SESSION",
        "v3_etapa0": "Candidacy",
        "v3_etapa1": "Recommendation",
        "v3_etapa2": "Adoption",
        "v3_funil_nota": "Elimination is irreversible and monotonic: options are lost and not recovered",
        "v3_camadas_tit": "BETWEEN SESSIONS",
        "v3_c0": "The session",
        "v3_c0_dono": "no owner · ephemeral",
        "v3_c1": "The project's memory",
        "v3_c1_dono": "whoever builds controls it",
        "v3_c2": "The public corpus",
        "v3_c2_dono": "no owner · erodes",
        "v3_camadas_nota": "Only the middle one has an owner — and it is read at the start of every session",
        "v3_barra1": "The funnel operates at the level of the decision, not the session",
        "v3_barra2": "The decisions that matter are the recorded ones, because those stopped being decided",
        "v3_faixa": "A wheel that loses energy stops turning. What accumulates between sessions also evaporates.",
        "v3_rodape": "Builder-Led Growth, arc 2 · the funnel figure: disputed attribution, Lewis (1898), Sheldon, and the AIDA acronym in 1921",

        "v4_nome": "a2p1-stages-en",
        "v4_kicker": "THE THREE STAGES ALONG THE AXIS",
        "v4_titulo": "The same stage changes shape as delegation rises",
        "v4_sub": "Candidacy, recommendation and adoption at both ends of the axis",
        "v4_col1": "ASSISTED DECISION",
        "v4_col2": "DELEGATED DECISION",
        "v4_e0": "Candidacy",
        "v4_e0_def": "being in the set that gets chosen from",
        "v4_e0_a": "A list a person reads — and a\nlist that is read is auditable:\nthe reader notices an absence",
        "v4_e0_d": "The set forms inside the process\nand is never displayed.\nNobody notices any absence",
        "v4_e1": "Recommendation",
        "v4_e1_def": "being the one chosen within the set",
        "v4_e1_a": "The person sees alternatives side\nby side and applies own criteria",
        "v4_e1_d": "There is no comparison: there is\na result — and it converges\ntoward the familiar",
        "v4_e2": "Adoption",
        "v4_e2_def": "surviving integration and use",
        "v4_e2_a": "You integrate what you chose,\nknowing what you chose",
        "v4_e2_d": "You integrate what turned up, and\nthe first close look usually\nhappens when it breaks",
        "v4_faixa": "Visibility of loss grows down the funnel, and the ability to act on it falls in step.",
        "v4_rodape": "Builder-Led Growth, arc 2 · in one measured configuration, %.1f%% of repetitions did not trigger a web search (arXiv 2604.07585)" % SEM_BUSCA,

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
