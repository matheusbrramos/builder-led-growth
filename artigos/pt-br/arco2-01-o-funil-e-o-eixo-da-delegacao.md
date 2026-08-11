<!--
Arco 2, parte 1 da série Builder-Led Growth, por Matheus Ramos.
VERSÃO NÃO CANÔNICA. A canônica é a inglesa: ../en/arc2-01-the-funnel-and-the-delegation-axis.md
Em caso de divergência de fato ou de número, a inglesa prevalece.
Texto congelado. Data no LinkedIn ainda não definida.
Gerado a partir do repositório privado de trabalho. Não editar aqui.
-->

# Não é quem decide. É quanto foi delegado

*Segunda peça do segundo arco desta série, e ela não exige as anteriores — o que
importa é retomado aqui. A peça de abertura estabeleceu que quem escolhe é um par
de pessoa e máquina. Esta pergunta o que muda conforme quanto desse par foi
delegado, e onde isso cai dentro do funil.*

---

## Três opções existiam. Uma entrou no código

Peço ao par que suba a aplicação. Digo o que ela faz, digo que precisa estar no ar,
e volto para o que eu estava fazendo.

Quando olho de novo, está no ar. O código chama um provedor de hospedagem que eu
não escolhi. A configuração dele está escrita, as variáveis de ambiente estão
declaradas, e há um arquivo de implantação que eu não pedi e que funciona.

Três provedores dariam conta daquilo. Eu conheço os três. Um deles é usado por um
time vizinho ao meu, e eu teria escolhido esse se alguém tivesse perguntado.
Ninguém perguntou, e o que me incomoda não é ter ficado com o provedor errado — o
que apareceu funciona bem. O que me incomoda é outra coisa.

Eu aceitei. Olhei o resultado, vi que estava no ar, e segui. O veto era meu e eu
não o exerci, porque exercer veto exige saber que havia algo a vetar.

Então: **em que momento os outros dois saíram?**

Guarde essa pergunta, porque ela é uma armadilha e eu a montei de propósito. Ela
pressupõe que houve um momento de saída — um instante em que três viraram um. É
disso que este texto trata, e a resposta é menos confortável que a pergunta.

## O eixo, e os dois nomes que faltavam

Vou promover a estrutura uma ideia que já vinha operando de lado.

A peça de abertura deste arco estabeleceu que builder é o par — a pessoa e o
agente juntos, o agente selecionando, a pessoa validando, nenhum dos dois decidindo
sozinho. E registrou, com dado de pesquisa por trás, que o peso não fica parado no
meio: pende conforme a experiência de quem observa e conforme quanta regra escrita
existe em volta.

Aquilo entrou como observação. Aqui vira o eixo em que tudo o mais se organiza, e
declaro a promoção em vez de fazê-la calada.

**Dizer que a máquina escolhe é falso. O humano escolhe tanto quanto.** Fora desta
teoria isso é óbvio — alguém escolhendo pão na padaria não delegou nada a ninguém.
E dentro dela também: escolher qual trabalho fazer, qual avanço perseguir, qual
problema atacar, e então pedir que a máquina ajude, é decisão humana do começo ao
fim. O que muda de um caso para o outro não é quem decide. É **quanto foi
delegado** — e delegação é grau, nunca estado.

As duas pontas desse grau precisam de nome, e é a primeira coisa que este texto
cunha:

> **Decisão assistida por IA: a pessoa escolhe entre opções que a máquina reuniu.
> Decisão delegada: a pessoa aceita ou recusa um resultado que a máquina já
> construiu.**

Procurei nome de mercado antes de inventar um, e o que existe nomeia outras coisas.
**Comércio conversacional** foi cunhado por [Chris
Messina](https://www.linkedin.com/in/factoryjoe/) em 2015, e descreve compra por
aplicativo de mensagem — é anterior aos modelos de linguagem. **Busca sem clique**
foi quantificada em escala por [Rand
Fishkin](https://www.linkedin.com/in/randfishkin/) a partir de 13 de agosto de 2019,
e descreve a ausência do clique, não a decisão. **Otimização para motor
generativo**, cunhada em 16 de novembro de 2023 pelos autores do trabalho que a
propôs ([arXiv 2311.09735](https://arxiv.org/abs/2311.09735)), nomeia a resposta de
quem publica. E o **Agentic Commerce Protocol**, anunciado pela Stripe e pela OpenAI
em setembro de 2025 ([openai.com](https://openai.com/index/buy-it-in-chatgpt/)),
nomeia o extremo em que o agente compra sozinho.

Nenhum desses nomeia a mediação com a decisão humana preservada, que é justamente
o caso comum. O espaço estava vazio, e por isso o preenchi — com a ressalva de que
o par acima é proposta minha, não achado de campo. Se alguém cunhou equivalente
antes de mim, o crédito é dessa pessoa e eu troco o meu pelo dela.

Uma cerca de escopo, porque duas trocas diferentes se confundem com facilidade.
Uma organização decidindo passar a desenvolver com IA é uma troca — grande, lenta,
com comitê. O par já formado escolhendo qual ferramenta usar no meio da construção
é outra. Este texto trata da segunda.

## Onde as pessoas estão nesse eixo hoje

A pergunta seguinte é empírica: na prática, quanto se delega?

Três levantamentos, em três populações diferentes, devolvem o mesmo formato de
resultado — e é essa coincidência de formato, mais que qualquer um dos números,
que sustenta o que vem depois.

A disposição do consumidor de deixar a IA **tomar** a decisão de compra tem **teto
em 11%**. A palavra é do próprio levantamento: *"topped out at 11%"*, e o teto
ocorre nas categorias de menor risco — higiene pessoal e produto de limpeza. Não é
média, é o valor máximo observado. Já a disposição de deixar a IA **estreitar** as
opções chega a **31%** em produto de limpeza e casa, e **28%** em eletrônico
pessoal ([Gartner, 27 de maio de
2026](https://www.gartner.com/en/newsroom/press-releases/2026-05-27-gartner-survey-finds-consumers-want-ai-shopping-help-but-not-ai-purchase-decisions)).
Vale dizer de onde vem: 322 consumidores nos Estados Unidos, campo em janeiro de
2026, e o comunicado não publica amostragem, modo de coleta nem margem de erro. Uso
o padrão, e não os decimais.

Na compra corporativa de software, **69% dizem preferir validar com um vendedor
humano** as conclusões que a IA gerou, e 45% usaram IA generativa, *"primarily to
gather information on vendors and products"* ([Gartner, 20 de maio de
2026](https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights),
645 compradores, campo entre agosto e setembro de 2025). A palavra que o comunicado
usa é *prefer* — preferência declarada, e não comportamento medido. A diferença
importa e eu não vou apagá-la.

E **86%** de quem usou IA para pesquisar um produto conferiu a recomendação em outra
fonte antes de comprar. Some-se a isso a quarta população, que a peça de abertura
deste arco já tinha trazido: 98% dos consumidores verificam a recomendação da IA
antes de comprar.

Quatro medições, quatro recortes, e o mesmo desenho em todas: **o que se delega
hoje é a formação da lista curta, não a escolha.** A máquina entra na composição do
conjunto e sai antes da decisão. É a descrição do que uma casa de análise chamou de
estreitar o campo antes que a avaliação humana comece ([IDC, 28 de janeiro de
2026](https://www.idc.com/resource-center/blog/ai-mediated-buying-journeys-how-buyers-decide-whos-worth-their-time/)).

![O eixo da delegação com quatro medições: 11% de teto para deixar a IA decidir a compra, 31% para deixar estreitar, 86% conferem em outra fonte e 69% dos compradores B2B preferem validar com uma pessoa](../../visuais/arco2-parte-01/a2p1-eixo-pt.png)

## A decisão que ninguém tomou

Se hoje se delega a lista curta, a pergunta que interessa é a tendência. E eu
suspeitava de uma resposta específica: que na comunidade de quem constrói com IA a
proporção estivesse mudando, com a máquina decidindo cada vez mais.

Antes de procurar, escrevi o que derrubaria a suspeita — porque pesquisa que só
volta com o que a gente já achava tem problema na pergunta, não no mundo. Três
critérios: proporção estável ao longo do tempo; aumento só em execução e não em
decisão; ou população que delega muito encolhendo em vez de crescer.

**Dois dos três aconteceram, e a suspeita caiu.**

A única série pública que chega perto de medir entrega de tarefa inteira sem
avaliação do caminho não sobe: foi de 27,8% no campo de dezembro de 2024 a janeiro
de 2025 para 27% no seguinte, subiu a 39% em agosto de 2025, caiu a 32% em novembro
de 2025, e deixou de ser publicada nas duas edições seguintes ([Anthropic Economic
Index](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)).
Não trato isso como série: a edição de 15 de janeiro de 2026 declara troca de
classificador no meio, e a medição é do próprio fornecedor sobre o próprio produto.

O escrutínio, esse, aumenta com experiência. Usuários de alta permanência são
descritos como *"much less likely to delegate greater responsibility"*, e a taxa de
interrupção sobe de 5% para 9% dos turnos ([Anthropic, 24 de março de
2026](https://www.anthropic.com/research/economic-index-march-2026-report)). Num
levantamento de 500 mil sessões e 998.481 chamadas de ferramenta, 73% tinham humano
no laço e 80% algum mecanismo de proteção ([Anthropic, 18 de fevereiro de
2026](https://www.anthropic.com/research/measuring-agent-autonomy)) — outra vez,
material do próprio fornecedor.

E há contra-evidência de quem nomeou o fenômeno. [Andrej
Karpathy](https://www.linkedin.com/in/andrej-karpathy-9a650716/) cunhou *vibe
coding* — programar descrevendo o que se quer e aceitando o que a máquina escreve,
sem ler as alterações — em 2 de fevereiro de 2025, e o texto fundador é sobre
delegação de decisão, não de execução: *"I 'Accept All' always, I don't read the
diffs anymore."* Em 4 de fevereiro de 2026 ele aposentou o termo, propôs *agentic
engineering* no lugar, e escreveu que programar por meio de agentes está virando
fluxo padrão do profissional *"except with more oversight and scrutiny"* ([registro
datado por Simon
Willison](https://simonwillison.net/2026/Feb/26/andrej-karpathy/)).

Os agentes, aliás, são conservadores justamente onde a decisão de fornecedor mora.
Num estudo de 26.760 pedidos de alteração autorados por agente, em 1.832
repositórios com mais de cem estrelas, **apenas 1,3% introduzem dependência nova**,
e os pedidos que importam alguma biblioteca são incorporados a taxas de 6% a 11%
menores — ou seja, o escrutínio humano sobe quando há escolha de biblioteca em jogo
([Twist e Zhang, King's College London, arXiv
2512.11589](https://arxiv.org/html/2512.11589)).

Tudo isso aponta para o mesmo lugar, e o lugar não é o que eu esperava. Só que
existe uma medição que não cabe em nenhuma dessas séries.

Em 4 de junho de 2026, [Paul
Copplestone](https://www.linkedin.com/in/paulcopplestone/), cofundador e
presidente-executivo da Supabase, declarou: *"agents are now deploying the majority
of databases on our platform"*, sobre uma base declarada de mais de 250 mil clientes
([release
oficial](https://www.prnewswire.com/news-releases/supabase-raises-500m-at-10-5b-to-accelerate-lead-in-agentic-infrastructure-302791787.html)).
A Neon, em relatório da Databricks de 27 de janeiro de 2026 sobre mais de 20 mil
clientes, aparece com número vizinho: agentes criam **80% de todos os bancos e 97%
das ramificações de banco**
([Databricks](https://www.databricks.com/blog/enterprise-ai-agent-trends-top-use-cases-governance-evaluations-and-more)).

Qual banco de dados usar é decisão de arquitetura e de fornecedor. Não é execução.

E o mecanismo está declarado pelo próprio fornecedor, em 29 de setembro de 2025:
*"every AI builder using Lovable is already using Supabase, whether or not they
realize it"* ([Supabase](https://supabase.com/blog/lovable-cloud-launch)). São
declarações de empresas com interesse comercial em enfatizar a própria penetração,
e vale saber disso ao ler os números. O mecanismo, porém, não depende do número
estar certo na terceira casa.

Repare no que isso faz com a pergunta que abriu o texto:

> **A decisão não foi delegada. Foi removida do campo de visão.**

Ninguém responde "quem escolheu o banco?" sobre uma escolha que nunca lhe foi
apresentada. E é por isso que nenhuma pesquisa de opinião capta esse caso: o único
ator posicionado para contar decisões que o decisor nunca viu é quem hospeda a
decisão. Essa leitura é minha, e é a peça central deste texto.

Os outros dois provedores da minha cena não saíram em nenhum momento. Eles nunca
entraram.

E quando a decisão é de fato delegada, ela não se espalha — **converge**. Num
trabalho com oito modelos, bibliotecas populares aparecem desnecessariamente em até
**48%** dos casos, Python é escolhido em **58%** inclusive onde é subótimo, e Rust
não é usado uma única vez em cenário de alto desempenho. A conclusão dos autores,
com as palavras deles: *"LLMs may prioritise familiarity and popularity over
suitability"* ([Twist, Zhang, Harman, Syme, Noppen, Yannakoudakis e Nauck, Findings
of ACL 2026, arXiv 2503.17181](https://arxiv.org/abs/2503.17181)).

Daqui em diante é raciocínio meu, e sem validação: se a escolha delegada concentra
no que é familiar, **quem já é padrão de categoria ganha com a delegação, e quem
disputa o segundo lugar perde duas vezes** — não é escolhido, e também não é
comparado.

![A remoção do campo de visão: das três opções que existiam, duas não foram recusadas, e sim nunca apresentadas a ninguém](../../visuais/arco2-parte-01/a2p1-remocao-pt.png)

## Vinte pontos entre o medido e o acreditado

Preciso parar aqui e dizer o que dá para fazer com os números que vieram até agora,
porque quase todos eles são autodeclaração.

Num experimento aleatorizado com 16 desenvolvedores experientes e 246 tarefas reais
dos próprios repositórios, com sorteio por tarefa entre usar e não usar IA, as
pessoas ficaram **19% mais lentas** com a ferramenta. Antes esperavam acelerar 24%.
E, depois de terem sido medidas como mais lentas, ainda estimavam ter acelerado 20%
([METR, 10 de julho de
2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
[arXiv 2507.09089](https://arxiv.org/abs/2507.09089)).

> Vinte pontos de distância entre o que foi medido e o que a pessoa acredita.

A ressalva é dos próprios autores e eu tenho obrigação de reproduzi-la: eles **não**
afirmam que a IA deixa a maioria dos desenvolvedores mais lenta, e dizem que o
resultado não se estende além daquele grupo e daqueles repositórios. Na atualização
de 24 de fevereiro de 2026, com 57 participantes e mais de 800 tarefas, o efeito foi
de −18% para os originais e −4% para os novos, com os intervalos de confiança
cruzando o zero ([METR](https://metr.org/blog/2026-02-24-uplift-update/)).

A ponte que eu construo em cima disso é minha: se quem delega não consegue avaliar
corretamente o próprio desempenho com a máquina, pesquisa de opinião sobre delegação
mede crença, não comportamento.

E a mesma atualização traz o dado que eu considero o mais forte de todo este texto,
porque não é opinião — é comportamento. **De 30% a 50% dos participantes disseram
que estavam deixando de submeter tarefas ao estudo porque não queriam fazê-las sem
IA**, num desenho que lhes pagava 50 dólares por hora para trabalhar em tarefas de
escolha própria. Recusar trabalhar sem a ferramenta ainda não é deixar a ferramenta
escolher. Mas é o degrau anterior, e ele está medido.

Daqui para o fim do texto, nada se apoia no que as pessoas dizem sobre si mesmas.

## Por que o funil, e não a roda

Com o eixo montado, dá para responder onde ele opera — e a resposta exige entrar
numa discussão que o marketing tem há anos.

O debate entre o funil e o flywheel — a roda que gira e ganha momento — é um debate
sobre comprador humano. O argumento contra o funil é que o comprador não anda em
linha reta: ele volta, revisita, consulta pares, e uma compra corporativa envolve
dez ou mais pessoas entrando em momentos diferentes. A leitura dominante hoje é de
complementaridade: funil para aquisição e previsão, roda para retenção e advocacia.
Os números que circulam nesse debate vêm de material de agência, sem metodologia
publicada, e eu os cito como o clima da discussão, não como medida.

A figura do funil vem da publicidade do começo do século XX, e a paternidade é
disputada — as etapas costumam ser creditadas a Elias St. Elmo Lewis, em 1898, parte
da literatura atribui a formulação completa a Arthur Frederick Sheldon, e a sigla
AIDA só aparece em 1921, com C. P. Russell ([E. St. Elmo
Lewis](https://en.wikipedia.org/wiki/E._St._Elmo_Lewis)).

**O que muda quando quem seleciona é a máquina é específico, e é o que salva o
funil aqui.** Dentro de uma sessão, a eliminação é irreversível e monotônica. Quando
o agente resolve hospedar num provedor, o concorrente não é "revisitado mais tarde"
— ele sai, e a escolha endurece dentro do código na mesma sessão. Não há comitê que
reabra, não há segunda reunião. Perde-se opção, e não se recupera.

E a roda volta por cima, num plano diferente: a escolha vira código público,
resposta em fórum, tutorial, dado de treino, e isso alimenta a próxima seleção,
feita por outro agente, em outra empresa.

> **Funil dentro da sessão, flywheel entre sessões.**

As duas figuras descrevem planos diferentes do mesmo fenômeno, e a briga entre elas
se dissolve quando se diz de qual plano se está falando. Com uma correção à figura
da roda, e ela vale a pena: roda que perde energia para de girar, não gira ao
contrário. O que se acumula entre sessões também **evapora** — foi o que eu descrevi
ao tratar de comunidade como lençol freático, que sobe com o que se deposita e desce
com o que se extrai. Quando o decaimento importa, é essa a figura que eu uso.

## O que atravessa de uma sessão para a outra

Aqui preciso corrigir uma frase minha antes de seguir.

Ao tratar de acessibilidade operacional, escrevi que a máquina decide de novo a cada
sessão e não acumula nada entre uma e outra — que cada sessão começa do zero. **A
parte sobre a máquina é verdadeira. A parte sobre o par não é** — e é o par que
decide. Continuei investigando e vi que aquilo está certo para uma camada só, e é a
camada errada para quem quer entender este assunto.

São três camadas, e eu vinha operando com duas.

A **sessão** é onde a eliminação acontece. É efêmera, não tem dono, e ninguém se
reforça nela.

O **corpus público** — o material que treina o modelo seguinte — acumula devagar,
não tem dono, e sofre erosão.

A do meio é a que faltava, e é a única com dono: a **memória do projeto**.
Especificação, registro de decisão, arquivo de instrução para o agente. Quem
constrói controla essa camada inteira, e ela é lida no começo de toda sessão.

Daí sai um mecanismo de hábito que eu não tinha:

Uma vez que "escolhemos este provedor, e por este motivo" está escrito no arquivo de
memória do projeto, **essa decisão é relida no começo de toda sessão seguinte. Ela
deixa de ser decisão e vira premissa.** É o hábito mais barato de instalar e o mais
difícil de deslocar, porque não exige treino de modelo nem código escrito — exige
uma linha num arquivo.

Isso já é categoria de mercado: engenharia de contexto, com camadas de memória
persistente vendidas por fornecedores que repetem que memória é o fosso. É material
de quem vende memória, com interesse evidente na tese; o que ele estabelece com
segurança é que a categoria existe e tem concorrentes nomeados.

E para quem vende, abre uma posição que a série ainda não tinha nomeado: **estar
inscrito no artefato de memória do cliente é posição mais durável que estar no dado
de treino, que se atualiza, e mais barata que o custo de troca, que exige o código
já existir.** A linha ética é clara e vale dizer: você escreve a documentação, quem
decide referenciá-la é o cliente.

O ajuste que isso obriga na formulação do funil é pequeno e muda bastante: **o funil
opera no nível da decisão, não no da sessão.** Nem toda decisão tem o mesmo tamanho
— algumas são locais à tarefa e vão ser redecididas amanhã, outras são registradas e
viram premissa. As que importam são as registradas, porque essas pararam de ser
decididas.

![Funil dentro da sessão e roda entre sessões, com as três camadas do que atravessa: a sessão sem dono, a memória do projeto controlada por quem constrói, e o corpus público que acumula devagar e sofre erosão](../../visuais/arco2-parte-01/a2p1-funil-e-camadas-pt.png)

## As três etapas, corridas ao longo do eixo

O funil que esta série usa tem três etapas, e elas não são novas — foram nomeadas e
definidas quando tratei de decisão, preço e medição. Em uma frase cada, só para
retomar o que fazem: **candidatura** é estar no conjunto de onde se escolhe;
**recomendação** é ser o escolhido dentro dele; **adoção** é sobreviver à
integração e ao uso.

O que este texto acrescenta é o cruzamento delas com o eixo. A mesma etapa parece
uma coisa quando a decisão é assistida e outra quando é delegada.

**Na candidatura**, a ponta assistida é uma lista que a pessoa lê — e uma lista lida
é auditável, porque quem lê percebe uma ausência conhecida. Na ponta delegada, o
conjunto se forma dentro do processo e nunca é exibido. Ninguém percebe ausência
nenhuma. É por isso que aquela pergunta sobre o momento de saída não tem resposta.

**Na recomendação**, a ponta assistida compara — a pessoa vê alternativas lado a
lado e aplica critério próprio. Na delegada, não há comparação: há um resultado. E o
que decide qual resultado aparece é a convergência para o familiar, que é a medição
do parágrafo sobre bibliotecas populares acima.

**Na adoção**, a ponta assistida integra o que escolheu, sabendo o que escolheu. Na
delegada, integra-se o que apareceu — e a primeira vez que alguém olha aquilo com
atenção costuma ser quando quebra.

Um fato de mecanismo ajuda a entender por que o conjunto se forma tão cedo: numa
configuração medida, **57,8% das repetições não acionaram busca na web** (Schulte,
Bleeker e Kaufmann, [arXiv 2604.07585](https://arxiv.org/pdf/2604.07585), 10 de
abril de 2026 — número obtido via citação em revisão crítica, não da tabela
primária). Quando a busca não é acionada, o conjunto de candidatos vem inteiro do
que o modelo já traz de fábrica. Não há momento de curadoria a observar, porque a
curadoria aconteceu antes de a sessão começar.

E há uma assimetria que atravessa as três, e eu apresento como raciocínio meu:
**a visibilidade da perda cresce à medida que se desce o funil, e a capacidade de
agir sobre ela cai junto.** Quando o produto é descartado na adoção, existe um
rastro — alguém trocou, alguém reclamou, alguém abriu uma issue. Quando ele não
entra na candidatura, não existe rastro nenhum, e é justamente ali que ainda dava
para fazer alguma coisa a respeito.

![As três etapas do funil cruzadas com o eixo da delegação: candidatura, recomendação e adoção, e o que cada uma parece na decisão assistida e na decisão delegada](../../visuais/arco2-parte-01/a2p1-etapas-pt.png)

## O veto muda de natureza

Três coisas mudam conforme a delegação sobe, e as duas primeiras já apareceram aqui:
a curadoria do conjunto acontece mais cedo e mais calada, e a perda para de deixar
rastro. A terceira é a que interessa mais, porque é a que dá alavanca a quem vende.

Na ponta assistida, o veto é uma escolha entre alternativas visíveis: a pessoa vê
três, prefere uma, e as outras duas continuam existindo como opção caso a primeira
decepcione. Na ponta delegada, não há alternativas na tela. Há um resultado pronto,
e a pessoa aceita ou recusa.

> **O veto deixa de ser escolha entre alternativas e vira aceitação ou recusa de um
> resultado já construído** — mais barato de tomar, e mais caro de reverter.

Mais barato porque aceitar não exige avaliar nada: exige apenas que nada pareça
errado. Foi o que eu fiz na cena de abertura. E mais caro de reverter porque, no
instante em que a pessoa aceita, aquilo já está escrito no código, com configuração,
variável de ambiente e arquivo de implantação em volta.

Isso tem consequência direta para quem constrói produto, e é o assunto da peça sobre
adoção: se o veto é exercido olhando um resultado, então o que você controla não é a
comparação — é o que a pessoa encontra pronto quando finalmente olha.

![O veto em dois estados: na decisão assistida é escolha entre alternativas visíveis, e na decisão delegada é aceitar ou recusar um resultado já construído, mais barato de tomar e mais caro de reverter](../../visuais/arco2-parte-01/a2p1-veto-pt.png)

## O que fica, e o que vem

Quatro coisas, e as quatro sustentam o resto do arco.

Não é quem decide, é quanto foi delegado — e delegação é grau, com uma ponta em que
a pessoa escolhe entre opções reunidas pela máquina e outra em que ela aceita ou
recusa um resultado construído.

O que se delega hoje, medido em quatro populações diferentes, é a formação da lista
curta e não a escolha.

Existe uma categoria inteira de decisão que nenhuma dessas medições capta, porque
ela não foi delegada: foi removida do campo de visão.

E o funil sobrevive, no nível da decisão e não no da sessão, porque dentro de uma
sessão a eliminação é irreversível — enquanto o que se acumula entre sessões vive em
três camadas, das quais só a do meio tem dono.

As peças seguintes descem o funil. Duas sobre candidatura, uma sobre como se entra
no conjunto e outra sobre como se é cortado dele antes de qualquer preferência; uma
sobre o que decide a escolha dentro do conjunto, e o que dessas táticas decai; uma
sobre adoção, o guardrail e quem fica; e uma de fechamento, sobre onde o seu produto
se encaixa e quem cuida disso na sua empresa.

Fecho com o que eu não sei, e é uma coisa só.

Ninguém publica quantas decisões de fornecedor o agente tomou sozinho. Procurei em
levantamento de desenvolvedor, em relatório de plataforma e por formulação livre, e
a pergunta não é feita em lugar nenhum — nenhum levantamento pergunta a quem
constrói quem escolheu a biblioteca, o serviço ou o banco na última vez, a pessoa ou
o agente.

E não é falha de busca. Uma das plataformas construiu a taxonomia que responderia
isso — separa o trabalho iniciado por código, por um agente e por vários agentes, na
própria interface de métricas, desde 29 de maio de 2026 — e não publica o agregado.

**Existe quem consiga medir, e não publica.** Se você trabalha num lugar que
consegue, esse número é o dado mais importante que este arco poderia citar, e a
conversa que eu mais gostaria de ter depois deste texto.

---

**Série Builder-Led Growth**, por Matheus Ramos. Segundo arco:

- [Arco 2, parte 0 — Do PLG ao BLG: o que continua valendo quando quem escolhe é um par](arco2-00-do-plg-ao-blg.md)
- Arco 2, parte 1 — Não é quem decide. É quanto foi delegado (este texto)

O primeiro arco, para quem quiser o percurso completo:

- [Parte 1 — Quando a máquina também é seu cliente](01-quando-a-maquina-e-cliente.md)
- [Parte 2 — A decisão, o preço e o que medir](02-decisao-preco-e-medicao.md)
- [Parte 3 — O imposto que a máquina cobra e o humano não vê](03-legibilidade-por-maquina.md)
- [Parte 4 — Quantas vezes o agente precisa chamar um humano](04-acessibilidade-operacional.md)
- [Parte 5 — O poço de onde todos bebem](05-comunidade-e-sinal-de-validacao.md)
- [Parte 6 — A máquina é imprensa e leitor ao mesmo tempo](06-relacoes-publicas.md)
- [Parte 7 — O que faz o agente confiar, e por que a competência dele é o problema](07-confianca-e-seguranca.md)
