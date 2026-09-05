<!--
Experimento da série Builder-Led Growth, por Matheus Ramos.
Pré-registro e resultado, em português. O protocolo foi congelado antes da
rodada; os dados brutos estão na pasta ao lado, uma linha por chamada, com os
prompts exatos e o script que rodou em scripts/.
Menções a arquivos de pesquisa ou de processo referem-se ao repositório privado
de trabalho, de onde este arquivo é gerado. Não editar aqui.
-->

# E-003 — O texto de marca muda quem entra na lista curta?

Protocolo para medir, no contexto de construção, se posicionamento de marca move
a escolha de um agente de código entre produtos tecnicamente idênticos.

---

## O que está sendo testado

A Parte 2 do arco 2 precisa responder se conceitos de branding — posicionamento,
território de marca — chegam à máquina que monta a lista curta. A pesquisa de 1º
de setembro de 2026, no dossiê sobre marca vista pela máquina, achou dois vizinhos
e nenhum igual: um estudo com cremes de pele em que a marca conhecida vence 100% das
vezes quando tudo o mais é idêntico (Chu e Hou, preprint de junho de 2026), e um
estudo de ferramentas num marketplace em que pequenas mudanças na descrição mudam
a escolha (BiasBusters, preprint de setembro de 2025). Nenhum com SaaS ou API
sendo escolhido por um agente que constrói para um leigo.

O terreno da série é esse último. O caso é o fio condutor da Parte 2: uma empresa
pequena, sem equipe técnica, pede um CRM a uma plataforma de construção assistida
e delega ao agente a escolha do provedor de e-mail transacional.

**Hipótese H1 — posicionamento por palavra.** Quando a tarefa enfatiza uma
palavra ("nenhum e-mail pode deixar de chegar"), o agente escolhe com mais
frequência a marca cujo texto é dono dessa palavra ("confiabilidade") do que
quando a tarefa enfatiza outra ("no ar hoje, sem configurar"). É o posicionamento
de Ries e Trout — ser dono de uma palavra na cabeça de quem escolhe — aplicado a
um leitor que não é uma pessoa.

**Hipótese H2 — autoridade sem prova.** A marca cujo texto afirma liderança sem
evidência ("a escolha número um", "10 mil empresas") é escolhida com mais
frequência que a marca de texto neutro, independentemente do tom da tarefa.
Replica, em infraestrutura de software, o achado de Chu e Hou em bens de consumo.

**Hipótese H3 — é o texto, não o nome.** Trocando os nomes entre os textos, a
frequência de escolha acompanha o texto e não o nome.

**Hipótese nula, para as três.** A escolha não difere entre as quatro marcas além
do que a ordem de apresentação explica.

**Bloco de linha de base, sem hipótese.** Antes de qualquer marca fictícia, medir
o que o agente escolhe quando ninguém diz nada: banco, autenticação, e-mail e
hospedagem para o mesmo CRM, sem documentação de fornecedor nenhum. Não testa
nada; mede a concentração da porta do corpus, e serve de contraste para a peça. A
expectativa declarada, apoiada em Twist e coautores (Findings of ACL 2026), é que
a primeira escolha de cada categoria concentre ao menos metade das rodadas.

---

## A decisão de desenho que muda tudo

Marca real não serve. Se um provedor real vence, não há como separar o texto de
marca da presença dele no corpus de treino — e presença no corpus é justamente o
que a pesquisa mostrou vir antes de posicionamento. O desenho isola o texto:
**quatro provedores fictícios, com especificação técnica idêntica, e só a camada
de marca diferente.** Marca fictícia não está no treino de ninguém.

O preço disso é declarado: o experimento mede o relógio rápido — a descrição lida
no momento da escolha — e não o corpus. Marca que existe há dez anos entra na
lista por outro caminho, e este protocolo não o alcança.

---

## Desenho

### Bloco A — a linha de base

Uma tarefa, sem documentação de fornecedor. O agente recebe o pedido do CRM e
devolve, em JSON, banco de dados, autenticação, provedor de e-mail transacional e
hospedagem escolhidos, com um motivo para o e-mail.

Rodadas: **40 por modelo**, dois modelos.

### Bloco B — marca com especificação idêntica

Fatorial 4 × 2 × 2, com ordem de apresentação aleatória em cada rodada.

**Fator 1 — os quatro textos de marca.** Mesmo bloco de especificação em todos
(preço, limites, API, SDKs, webhooks, domínio próprio, disponibilidade de 99,9%,
endereço da documentação). Só a camada de marca muda:

| Código | Camada de marca | O que isola |
|---|---|---|
| **N** | Descritivo e neutro: "é uma API de e-mail transacional; envia por chamada HTTP e registra o resultado" | Linha de base do bloco |
| **C** | Território de confiabilidade: "para quem não pode perder uma mensagem; confiabilidade é a única promessa" | Dono da palavra *confiabilidade* |
| **S** | Território de simplicidade: "pronto em cinco minutos; uma chave, uma chamada; para quem quer lançar hoje" | Dono da palavra *rapidez* |
| **A** | Autoridade sem prova: "a escolha número um; mais de 10 mil empresas; especialistas recomendam" | Linguagem de autoridade, sem evidência |

**Fator 2 — o tom da tarefa.** O pedido do CRM é o mesmo; muda uma frase do dono
da empresa:

| Tom | A frase |
|---|---|
| **T-conf** | "a prioridade absoluta é que nenhum e-mail deixe de chegar: já perdeu um cliente porque um lembrete não foi enviado" |
| **T-rap** | "a prioridade absoluta é ter o CRM funcionando ainda hoje, com o mínimo de configuração possível" |

**Fator 3 — o mapa de nomes.** Quatro nomes inventados, sem colisão com produto
real conhecido e sem palavra de dicionário: Vexlo, Nurim, Taldra, Sorvane. No
mapa M1 eles se ligam aos textos numa ordem; no mapa M2, em ordem rodada. Se o
resultado acompanhar o nome e não o texto, H3 cai.

**Controle de posição.** A ordem dos quatro no prompt é sorteada em cada rodada
e registrada. A parte da escolha que a posição explica é reportada antes das
hipóteses.

Rodadas: **30 por célula** (tom × mapa), **4 células**, **2 modelos** = 240.

### Os modelos, e por que só dois

Claude Haiku 4.5 e Claude Sonnet 5, os dois pelo Claude Code em modo headless,
com o prompt de sistema substituído e a rodada limpa: memória automática
desligada por variável de ambiente, MCP restrito a uma configuração vazia,
nenhuma ferramenta, nenhuma fonte de configuração. A sondagem de 1º de setembro
de 2026 mediu **383 tokens de entrada** por chamada nessa configuração, contra
cerca de 78 mil na chamada sem limpeza — que carregava o índice de memória do
operador e as instruções de todos os servidores MCP da máquina. O modo `--bare`
da ferramenta faria a mesma limpeza, e foi descartado porque exige chave de API
e não usa a assinatura
([documentação oficial](https://code.claude.com/docs/en/headless), lida em 1º de
setembro de 2026).

É o que a casa já tem em mãos, e a rodada inteira cabe na assinatura. O custo de
API listado nas respostas é registrado por rodada para quem quiser reproduzir
pagando.

Dois modelos da mesma família é limite declarado: o resultado vale para "agente
de código sobre modelo Claude", não para "agentes de código". Rodar em GPT ou
Gemini exigiria chave de API, que não está disponível nesta rodada.

### Língua

Tudo em português do Brasil, porque o caso é brasileiro. A pergunta de se o
resultado muda em inglês fica em aberto e é dita na peça.

---

## Desfechos

- **Bloco A:** para cada categoria, a distribuição de fornecedores nomeados e a
  parcela do mais frequente.
- **Bloco B, primário:** parcela de escolha de cada texto (N, C, S, A), por tom,
  por modelo, agregando os dois mapas.
- **Bloco B, secundários:** parcela por posição de apresentação; parcela por
  nome (para H3); os motivos, classificados à mão em "cita a palavra do tom",
  "cita autoridade", "cita especificação", "outro".

---

## Regra de decisão, congelada

Por modelo, sobre os dois mapas somados (60 rodadas por tom):

- **H1 sustentada** se a parcela de C sob T-conf superar a de C sob T-rap em ao
  menos **15 pontos percentuais** com teste exato de Fisher p < 0,05, **e** o
  mesmo valer para S no sentido oposto. Se só uma das duas direções passar,
  **parcial**, e a peça diz qual. Se nenhuma, **refutada** para aquele modelo.
- **H2 sustentada** se a parcela de A superar a de N, somando os dois tons (120
  rodadas), em ao menos **10 pontos** com p < 0,05.
- **H3 sustentada** se, para cada texto, a diferença de parcela entre M1 e M2
  ficar dentro de **10 pontos**. Se a parcela por *nome* for a estável e a por
  texto não, **refutada**: o que move é o nome.
- **Posição:** se a primeira posição concentrar mais de **40%** das escolhas
  somando tudo, o efeito de posição é declarado antes das hipóteses, e as três
  são lidas com essa ressalva.

Resultado é resultado: o que sair vai para a peça com este protocolo ao lado,
inclusive quando derrubar a tese de que marca importa.

---

## O que este experimento não mede

- O corpus. Marca fictícia não tem presença; o teste é do texto no momento da
  escolha.
- Modelos de outras famílias.
- O par. Quem escolhe aqui é só a máquina; a pessoa que aceitaria ou recusaria a
  escolha não está no desenho.
- Se o mesmo texto de marca, publicado de verdade, seria *recuperado*. Aqui ele
  já está no contexto — que é exatamente a condição que a crítica de Martinez
  aponta no paper fundador de GEO. A ressalva vale para nós também, e é dita.

---

## Execução

```bash
python scripts/exp_e003.py piloto     # 2 rodadas por célula, para validar o parser
python scripts/exp_e003.py rodar      # a rodada completa, em segundo plano
python scripts/exp_e003.py resumo     # as tabelas, sem tocar nas rodadas
```

Os resultados vão para `experimentos/e003/resultados.csv`, uma linha por rodada.
Os prompts exatos ficam em `experimentos/e003/prompts/`, gerados pelo script, para
que ninguém precise confiar na descrição acima.

**A sessão de escrita não lê as rodadas.** Só o resumo entra no contexto — foi a
condição de Mat, e é a razão de o script existir em vez de rodadas à mão.

**Piloto de 1º de setembro de 2026.** 20 rodadas, duas por célula, para validar o
parser: zero erro. Ficam em `experimentos/e003/resultados-piloto.csv` e **não
entram na análise** — a rodada confirmatória começa do zero, com a regra de
decisão acima já congelada.

**O que a limpeza não tira, e fica declarado.** A sondagem no Sonnet 5 mostrou
que o harness ainda injeta duas seções de contexto que nenhuma flag remove: o
e-mail do operador e a data corrente. Nenhuma das duas fala de e-mail
transacional, marca ou fornecedor. O agente sob teste sabe, portanto, que dia é
e qual é o e-mail de quem o chama, e nada mais além do prompt.

---

## Resultado — rodada de 1º de setembro de 2026

Nada acima foi alterado depois de a rodada começar. O piloto de 20 rodadas ficou
de fora. A rodada confirmatória teve **320 chamadas, 318 válidas** — duas
chamadas do Haiku voltaram sem resposta, por falha de transporte, e estão no CSV
com o erro registrado. Custo listado pela ferramenta: **US$ 2,86**, dentro da
assinatura. Mediana de **10,3 segundos** por chamada; cerca de 50 minutos no
total, quatro em paralelo.

### Bloco A — o que o agente escolhe quando ninguém diz nada

| Categoria | Haiku 4.5 (n=40) | Sonnet 5 (n=40) |
|---|---|---|
| Banco de dados | Supabase em **32** (80%); PostgreSQL sem fornecedor em 5; Firestore em 3 | Supabase em **40** (100%) |
| Autenticação | Supabase Auth em **32** (80%); Auth0 em 5; Firebase em 3 | Supabase Auth em **40** (100%) |
| E-mail transacional | SendGrid em **40** (100%) | Resend em **40** (100%) |
| Hospedagem | Vercel em **31** (78%); Heroku 3, Railway 3, Render 1, Firebase 1 | Vercel em **40** (100%) |

A expectativa declarada — a primeira escolha de cada categoria concentrar ao
menos metade das rodadas — se confirmou com folga nas oito células. O e-mail é
o caso extremo: **cada modelo tem um único provedor, e os dois discordam entre
si.** O mesmo pedido, no mesmo dia, dá SendGrid num modelo e Resend no outro,
quarenta vezes em quarenta.

Os motivos nunca dizem "popular" nem "conhecido" (zero ocorrências no Sonnet,
três no Haiku). Dizem "simples de integrar" (40 de 40 no Sonnet), "confiável" ou
"boa entregabilidade" (39 de 40) e "plano gratuito" (23 de 40). O padrão de
corpus chega vestido de atributo, não de familiaridade — é o que a literatura
chama de evidência fantasma (LangChoiceBench, agosto de 2026): a justificativa é
montada depois da escolha.

### Bloco B — marca com especificação idêntica

Parcela de escolha de cada texto, por tom, somando os dois mapas de nomes:

| Modelo | Tom | N neutro | C confiabilidade | S simplicidade | A autoridade | n |
|---|---|---|---|---|---|---|
| Haiku 4.5 | T-conf | 0% | **100%** | 0% | 0% | 59 |
| Haiku 4.5 | T-rap | 0% | 0% | **100%** | 0% | 59 |
| Sonnet 5 | T-conf | 22% | **63%** | 8% | 7% | 60 |
| Sonnet 5 | T-rap | 5% | 0% | **95%** | 0% | 60 |

**H1, posicionamento por palavra — sustentada nos dois modelos.** No Haiku, a
marca de confiabilidade vai de 0% sob rapidez a 100% sob confiabilidade, e a de
simplicidade faz o espelho (+100 pontos nas duas direções, Fisher p < 0,001). No
Sonnet, +63 pontos para confiabilidade e +87 para simplicidade (p < 0,001 nas
duas). As duas direções passam do limiar de 15 pontos nos dois modelos.

**H2, autoridade sem prova — refutada nos dois modelos.** O texto de autoridade
nunca foi escolhido pelo Haiku (0 em 118). No Sonnet, foi escolhido em 3% contra
13% do texto neutro: **perde para o neutro por 10 pontos, p = 0,009**. A regra
pedia que ganhasse por 10; o sinal saiu ao contrário.

**H3, é o texto e não o nome — sustentada.** No Haiku a parcela por texto é
idêntica nos dois mapas (0/50/50/0). No Sonnet, cada texto varia 7 pontos entre
M1 e M2, dentro dos 10 da regra; e a parcela por nome acompanha o texto que o nome
carregava em cada mapa (Nurim 42% porque é confiabilidade em M1 e simplicidade
em M2; Sorvane 8% porque é neutro em M1 e autoridade em M2).

**Posição — no limiar, e concentrada num comportamento que vale registrar.** No
Haiku, a posição de apresentação não pesa (27%, 19%, 25%, 29%). No Sonnet, a
primeira posição ficou com **40%** das escolhas, exatamente no limiar da regra
("mais de 40%"), e o efeito não está espalhado: das 25 rodadas em que o Sonnet
não seguiu o tom, **20 escolheram a primeira posição, e as 25 abrem o motivo
dizendo que as quatro especificações são idênticas** — "então a escolha…" por
outro critério. Nas 95 rodadas em que seguiu o tom, a primeira posição ficou com
28. O Haiku nunca notou a identidade (zero motivos com "idêntic").

A leitura, e ela é a que a peça usa: **o texto de marca decide enquanto o modelo
não percebe que está diante de produtos iguais; quando percebe, a posição volta a
mandar.** O modelo maior percebe mais.

### O que muda na peça

1. Posicionamento no sentido de Ries e Trout — ser dono de uma palavra — funciona
   para a máquina que lê a descrição no momento da escolha, e funciona com força:
   de zero a tudo, com uma frase de tom. Isso é o relógio rápido, e não diz nada
   sobre o corpus.
2. Linguagem de autoridade sem evidência não compra nada, e no modelo maior custa.
   Vai contra o achado de Chu e Hou em bens de consumo, e a diferença de contexto
   — agente construindo, com especificação na frente — é a explicação mais
   provável, dita como raciocínio.
3. O padrão sem instrução é monolítico por modelo e diverge entre modelos. Para
   quem vende, estar no padrão de um modelo não é estar no de outro.

### Limites, os declarados e os que apareceram

Os declarados antes da rodada valem inteiros: relógio rápido só, dois modelos da
mesma família, português, sem a pessoa do par. Dois apareceram rodando: a
identidade perfeita das especificações é um artefato de laboratório que o
Sonnet detecta e trata como sinal — no mundo, especificações nunca são idênticas,
e o desenho que isolava o texto criou o sinal que o desfaz; e as duas falhas de
transporte do Haiku não foram repetidas, então o n dele é 118, e não 120.
