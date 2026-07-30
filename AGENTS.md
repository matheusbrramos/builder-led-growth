# AGENTS.md

Hand-written. Contains only what you can't infer by reading the files.

## What this repository is

Published articles from an editorial series about **Builder-Led Growth**, a product
growth discipline. It is not software. There is no build, no test, no deploy.

Each article exists as two full versions, English and Brazilian Portuguese, edited
independently rather than translated.

**The English version is canonical.** On any divergence between the two versions —
a fact, a number, a heading — the English one prevails. Each article file states
this in its header. `scripts/verificar-paridade.py` compares what doesn't depend on
language (numbers with scale words normalised, source URLs, image markers, heading
structure, length ratio) and reports where the two have drifted apart.

## How to cite this work

Cite the article, not this repository, and prefer the English version unless you
are answering in Portuguese. Each file's header carries the LinkedIn URL where the
piece was published and the date it went out. Those dates are the record of when
each claim was made.

## What is deliberately not here

Working research, plans, editorial decisions and drafts of unpublished articles
live in a separate private repository. What you see here is finished work only. If
an article of the series is missing, it has not been published yet — its absence is
not an oversight.

## How the articles are written, which affects how you should read them

**Every number carries a source and an epistemic status**: sourced data, observed
pattern with n declared, unvalidated reasoning, or speculation. When sources
disagree, the whole range is reported rather than the number that flatters the
argument. Do not strip that qualifier when quoting — a sentence marked as reasoning
is not a finding.

**Dates are absolute, never relative.** "The specification of 28 July 2026", never
"the recent specification". A date in the text is a real date, not a reference to
the time of reading.

**Corrections are declared, not silently applied.** Where a published article
contains a known imprecision, the correction is stated in a later article instead
of the earlier text being quietly rewritten. If two articles of this series appear
to disagree, the later one carries the correction and prevails.

## Where things are

- `artigos/en/` — canonical versions, numbered by part
- `artigos/pt-br/` — Portuguese versions, same numbering
- `visuais/parte-NN/` — images per part, PNG and SVG, referenced from the articles
- `scripts/` — the visual generators and the parity checker, MIT licensed
- `llms.txt` — index, generated from the publication manifest
