#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mede a dispersao do corpus da propria serie.

Por que existe
--------------
A parte 5 argumenta que dispersao — quantas formulacoes incompativeis existem
publicamente para a mesma coisa — e a metrica central do terceiro pilar, e diz
que ela e "a mais trabalhosa, porque hoje so da para levantar a mao". Este
script e a tentativa de nao deixar isso como lacuna.

E ele aponta primeiro para dentro. Uma serie de sete artigos em duas linguas
repete a definicao dos quatro pilares catorze vezes. Se as catorze divergirem,
a obra produz exatamente o defeito que descreve.

O que ele mede
--------------
Para cada conceito ancora, extrai todas as formulacoes que aparecem no corpus e
separa em duas coisas que nao sao a mesma:

  ANCORA      a sentenca canonica, que deveria ser identica em toda ocorrencia
  COMPLEMENTO o que vem depois dela, que pode variar com o contexto

Divergencia na ancora e defeito. Variacao no complemento e adequacao ao
contexto, e nao conta como dispersao — a mesma distincao que a parte 7 faz
entre ambiguidade na superficie, que se elimina, e no pedido, que se acomoda.

Uso:
    python scripts/medir-dispersao.py
    python scripts/medir-dispersao.py --detalhe
"""
import glob
import hashlib
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Conceito ancora: (rotulo, regex que captura a formulacao, lingua)
# A regex captura do marcador ate o fim da frase — a ancora e a primeira
# sentenca, o resto e complemento.
ANCORAS = [
    ("pilar 1 · legibilidade", "pt", r"\*\*Legibilidade por máquina\.\*\*\s*(.+?)(?:\n\n|\Z)"),
    ("pilar 2 · acessibilidade", "pt", r"\*\*Acessibilidade operacional\.\*\*\s*(.+?)(?:\n\n|\Z)"),
    ("pilar 3 · comunidade", "pt", r"\*\*Comunidade e sinal de validação\.\*\*\s*(.+?)(?:\n\n|\Z)"),
    ("pilar 4 · confiança", "pt", r"\*\*Confiança e segurança do modelo\.\*\*\s*(.+?)(?:\n\n|\Z)"),
    ("limite da tese", "pt", r"(o Builder-Led Growth decide quem entra[^.]*\.)"),
    ("pillar 1 · legibility", "en", r"\*\*Machine legibility\.\*\*\s*(.+?)(?:\n\n|\Z)"),
    ("pillar 2 · accessibility", "en", r"\*\*Operational accessibility\.\*\*\s*(.+?)(?:\n\n|\Z)"),
    ("pillar 3 · community", "en", r"\*\*Community and validation signal\.\*\*\s*(.+?)(?:\n\n|\Z)"),
    ("pillar 4 · trust", "en", r"\*\*Model trust and safety\.\*\*\s*(.+?)(?:\n\n|\Z)"),
    ("thesis limit", "en", r"(Builder-Led Growth decides who gets in[^.]*\.)"),
    ("builder é o par", "pt", r"(Builder é o par: a pessoa e o agente juntos)"),
    ("builder is the pair", "en", r"(A builder is the pair: the person and the agent together)"),
    # O par cunhado no arco 2, parte 1. Entra aqui porque cunhar cobra uma coisa:
    # redacao identica em toda peca que use os termos. Sem ancora, a segunda
    # ocorrencia deriva sozinha e o proprio texto produz a polissemia que a serie
    # descreve como defeito.
    # A ancora NAO pode depender de onde a quebra de linha caiu: o bloco de
    # citacao ocupa tres ou quatro linhas conforme a lingua. Reescrever o texto
    # deslocou a quebra do ingles em 11 de agosto de 2026 e a ancora "sumiu",
    # com o portao acusando dispersao onde a frase estava intacta.
    #
    # A cura de entao foi casar [\s>]+ entre as palavras, e ela criou um defeito
    # pior, achado em 21 de agosto de 2026: o ">" entrava na CAPTURA, e a captura
    # e o que o publicar.py grava como definicao canonica. O publico leia
    # "the machine has > already" no arquivo que manda o modelo citar dali. As
    # duas ancoras do par tambem paravam antes do verbo — "que a maquina ja",
    # sem "construiu".
    #
    # Agora quem resolve a quebra e sem_citacao(), que tira o "> " ANTES de casar.
    # A regex volta a \s+ e a captura sai limpa.
    ("decisão assistida", "pt",
     r"(Decisão\s+assistida\s+por\s+IA:\s+a\s+pessoa\s+escolhe\s+entre\s+opções\s+que\s+a\s+máquina\s+reuniu)"),
    ("decisão delegada", "pt",
     r"(Decisão\s+delegada:\s+a\s+pessoa\s+aceita\s+ou\s+recusa\s+um\s+resultado\s+que\s+a\s+máquina\s+já\s+construiu)"),
    ("assisted decision", "en",
     r"(AI-assisted\s+decision:\s+the\s+person\s+chooses\s+among\s+options\s+the\s+machine\s+assembled)"),
    ("delegated decision", "en",
     r"(Delegated\s+decision:\s+the\s+person\s+accepts\s+or\s+rejects\s+a\s+result\s+the\s+machine\s+has\s+already\s+built)"),
]

DIRS = {"pt": "artigos/pt-br/*.md", "en": "artigos/en/*.md"}


def sem_citacao(t):
    """Tira o "> " que abre cada linha de bloco de citacao, preservando a linha.

    A definicao cunhada no arco 2 vive dentro de um blockquote de markdown, e o
    marcador de continuacao nao e parte da frase. Quem casa a ancora precisa ver
    a frase; quem grava a definicao canonica precisa gravar a frase.
    """
    return re.sub(r"(?m)^[ 	]*>[ 	]?", "", t)


def sem_comentarios(t):
    return sem_citacao(re.sub(r"<!--.*?-->", "", t, flags=re.S))


def primeira_sentenca(t):
    """A ancora termina no ponto, no travessao ou nos dois-pontos.

    Cortar so no ponto final foi o primeiro erro deste script: ele lia
    "…vai se alimentar — comparativos, codigo publico" como ancora diferente de
    "…vai se alimentar.", quando a ancora e a mesma e o travessao so introduz
    exemplo. Verificador que confunde complemento com divergencia acusa defeito
    onde nao ha, e treina quem le a ignora-lo.
    """
    m = re.match(r"(.+?)(?:[.!?](?:\s|$)|\s+[—–:])", t)
    return (m.group(1) if m else t).strip().rstrip(".")


def h(s):
    return hashlib.md5(" ".join(s.split()).lower().encode()).hexdigest()[:6]


def medir(detalhe=False):
    total_ancoras = 0
    total_divergentes = 0
    print("dispersão do corpus da série — âncora e complemento\n")

    for rotulo, lang, padrao in ANCORAS:
        ocorr = []
        for f in sorted(glob.glob(os.path.join(RAIZ, DIRS[lang]))):
            texto = sem_comentarios(io.open(f, encoding="utf-8").read())
            for m in re.finditer(padrao, texto, re.S):
                bruto = " ".join(m.group(1).split())
                ocorr.append((os.path.basename(f)[:2], primeira_sentenca(bruto), bruto))
        # Ancora com ZERO ocorrencia nao e "nada a medir": e a formulacao
        # canonica tendo sumido do corpus, ou a lista tendo ficado velha. Pular
        # em silencio deixa passar o caso pior — alguem reescreve a definicao
        # central e o medidor aprova. Descoberto em 2026-08-06, quebrando a
        # ancora do arco 2 de proposito para testar o script de conferencia.
        if not ocorr:
            total_ancoras += 1
            total_divergentes += 1
            print("  [SUMIU  ] %-28s nenhuma ocorrencia no corpus" % rotulo)
            print("        a formulacao canonica foi reescrita, ou esta lista")
            print("        precisa ser atualizada. As duas exigem decisao humana.\n")
            continue

        ancoras = {}
        for parte, anc, bruto in ocorr:
            ancoras.setdefault(h(anc), (anc, []))[1].append(parte)
        complementos = {h(b) for _, _, b in ocorr}

        total_ancoras += 1
        divergente = len(ancoras) > 1
        total_divergentes += 1 if divergente else 0

        marca = "DIVERGE" if divergente else "estável"
        print("  [%s] %-28s %d ocorrência(s), %d âncora(s), %d formulação(ões)"
              % (marca, rotulo, len(ocorr), len(ancoras), len(complementos)))

        if divergente or detalhe:
            for hh, (anc, partes) in ancoras.items():
                print("        partes %s: %s" % (",".join(sorted(set(partes))), anc[:110]))
        print()

    print("-" * 72)
    print("%d conceitos âncora medidos. %d com âncora divergente." %
          (total_ancoras, total_divergentes))
    if total_divergentes == 0:
        print("\nA âncora canônica está estável em todo o corpus.")
        print("A variação que existe é de complemento, e ela é adequação ao contexto:")
        print("a mesma distinção que a parte 7 faz entre ambiguidade na superfície,")
        print("que se elimina, e no pedido, que se acomoda.")
    else:
        print("\nÂncora divergente é defeito. Duas formulações incompatíveis da mesma")
        print("definição no corpus público é a dispersão que a parte 5 descreve.")
    return 1 if total_divergentes else 0


if __name__ == "__main__":
    sys.exit(medir("--detalhe" in sys.argv))
