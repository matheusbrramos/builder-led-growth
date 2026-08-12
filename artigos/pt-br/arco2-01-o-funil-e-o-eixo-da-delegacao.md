<!--
Arco 2, parte 1 da série Builder-Led Growth, por Matheus Ramos.
VERSÃO NÃO CANÔNICA. A canônica é a inglesa: ../en/arc2-01-the-funnel-and-the-delegation-axis.md
Em caso de divergência de fato ou de número, a inglesa prevalece.
Texto congelado. Data no LinkedIn ainda não definida.
Gerado a partir do repositório privado de trabalho. Não editar aqui.
-->

# Não é quem decide. É quanto foi delegado

*Segunda peça do segundo arco desta série. Não exige as anteriores. A peça de
abertura estabeleceu que quem escolhe é um par de pessoa e máquina. Esta trata do
funil: o que ele é, o que sobra dele quando o decisor é um par, e o que acontece
em cada etapa conforme mais coisa vai sendo delegada.*

---

## O banco de dados que eu não escolhi

Peço a uma plataforma de construção assistida que monte uma aplicação. Descrevo o
que ela precisa fazer: guardar cadastro de gente, deixar essa gente entrar com
senha, e subir arquivo.

Ela monta. Funciona.

Em algum lugar daquilo há um banco de dados, um serviço de autenticação e um
serviço de armazenamento. Nenhum dos três foi escolhido por mim. Eu não vi lista,
não comparei preço, não li documentação. Três nomes de banco de dados me
ocorreriam se alguém tivesse perguntado — e ninguém perguntou.

O que me interessa aqui não é ter ficado com o banco errado. O que apareceu
funciona. O que me interessa é que **eu tinha poder de veto e não o exerci**, e
não por distração: exercer veto exige saber que existe algo a vetar.

E não é impressão minha. O fornecedor de infraestrutura publicou o mecanismo com
todas as letras, em 29 de setembro de 2025: *"todo builder de IA usando a Lovable
já está usando a Supabase, saiba ele disso ou não"*
([Supabase](https://supabase.com/blog/lovable-cloud-launch)). É declaração de
empresa com interesse comercial em enfatizar a própria penetração, e vale ler com
isso em mente. Mas quem escreveu está do lado que enxerga: é o fornecedor, não o
usuário, quem consegue contar decisões que o decisor nunca viu.

## Três situações que não são a mesma coisa

Antes de falar de funil, preciso separar três coisas — e separá-las é metade do
trabalho deste texto, porque tratá-las como uma só produz confusão imediata.

**A primeira: desenvolvimento governado.** A empresa mantém um registro de
ferramentas aprovadas. Quando o time precisa de um serviço de mensageria, o
conjunto de onde ele escolhe já chegou restrito, por uma regra escrita antes e por
alguém que não está naquela sala. A escolha dentro desse conjunto é humana,
documentada, e há a quem perguntar por quê.

**A segunda: a lista curta.** Ninguém restringiu nada de antemão. A pessoa
pergunta, a máquina reúne três ou quatro nomes com uma razão para cada um, e a
pessoa escolhe. Ela compara, aplica critério próprio, e decide.

**A terceira: a decisão removida.** Não houve lista, não houve comparação, e não
houve escolha — houve um resultado. É o meu banco de dados.

As três acontecem no mesmo mercado, às vezes na mesma empresa, às vezes na mesma
semana. E o tamanho de cada uma não é palpite: **apenas 27% das organizações
aplicam governança estrita sobre adoção de ferramenta de IA, e 68% não têm
visibilidade de quais ferramentas de IA seus desenvolvedores usam**
([Northflank](https://northflank.com/blog/enterprise-ai-coding-agent-deployment)).
É material de fornecedor, não levantamento independente, e vale saber disso. O que
ele diz é que a primeira situação é real e minoritária, e que em dois terços dos
casos ninguém sequer sabe qual das outras duas está acontecendo.

### O que varia entre as três

Não é o problema. Não é o tipo de produto. Não é o tamanho da empresa.

**É quanto da decisão foi delegado** — e delegação é grau, com duas pontas que
precisam de nome:

> **Decisão assistida por IA: a pessoa escolhe entre opções que a máquina reuniu.
> Decisão delegada: a pessoa aceita ou recusa um resultado que a máquina já
> construiu.**

O desenvolvimento governado fica na ponta de baixa delegação, com uma
particularidade: quem tirou a delegação não foi a pessoa daquela sala, foi uma
regra escrita antes. A lista curta fica no meio. A decisão removida fica na outra
ponta.

Procurei nome de mercado antes de cunhar. **Comércio conversacional** foi cunhado
por [Chris Messina](https://www.linkedin.com/in/factoryjoe/) em 2015 e descreve
compra por aplicativo de mensagem. **Busca sem clique** foi quantificada em escala
por [Rand Fishkin](https://www.linkedin.com/in/randfishkin/) a partir de 13 de
agosto de 2019 e descreve a ausência do clique. **Otimização para motor
generativo** foi cunhada em 16 de novembro de 2023
([arXiv 2311.09735](https://arxiv.org/abs/2311.09735)) e nomeia o que faz quem
publica. E o **Agentic Commerce Protocol**, da Stripe e da OpenAI, de setembro de
2025 ([openai.com](https://openai.com/index/buy-it-in-chatgpt/)), nomeia o extremo
em que o agente compra sozinho. Nenhum nomeia o caso do meio, que é a máquina
mediando com a decisão humana preservada. Se alguém cunhou equivalente antes de
mim, o crédito é dessa pessoa e eu troco o meu pelo dela.

### Onde eu estava errado

Comecei este arco com uma posição: dizer que a máquina escolhe é falso, porque o
humano escolhe tanto quanto. Continuei investigando, e ela se sustentou pela
metade.

Nas duas primeiras situações, ela se sustenta inteira. Há uma escolha à vista, e
quem escolhe é gente.

Na terceira, não se sustenta. Não houve delegação — houve ausência. Eu não
transferi uma decisão para a máquina; a decisão simplesmente não passou por mim.
Dizer que eu escolhi tanto quanto ela seria falso.

## Um funil, e ele é do par

Agora o assunto principal. E ele começa por uma pergunta que eu levei duas
tentativas para responder: se a decisão é de um par, existem dois funis — um da
máquina e um do humano — ou um só?

**Dois funis não fecham**, e o motivo é simples de verificar. Dois funis exigem um
ponto de junção: você tem que dizer onde a saída de um vira entrada do outro. No
desenvolvimento governado, o humano vem depois. Na lista curta, os dois se
intercalam. Na decisão removida, o funil humano nunca roda. São três topologias
diferentes para o mesmo fenômeno, e um modelo que precisa de um desenho por caso
não está descrevendo nada.

**Um funil do par fecha**, e é o que este texto usa. Ele tem três etapas, sempre as
mesmas, e o que muda entre as três situações é **quem satisfaz cada uma**.

### O que é um funil, e o que sobra dele aqui

Um funil é uma figura simples: muita coisa entra em cima, pouca sai embaixo, e a
cada etapa o conjunto encolhe. Ele não explica por que alguém desistiu. Ele diz
**onde** procurar.

Um exemplo fora de software deixa isso claro. Uma loja recebe mil visitantes por
mês, cem experimentam alguma peça, e vinte compram. O funil não diz se o problema
é o preço, o provador ou o atendimento. Diz que a queda maior está entre entrar e
experimentar, e que é ali que se investiga primeiro. É instrumento de localização,
não de diagnóstico.

A figura vem da publicidade do começo do século XX, e a paternidade é disputada:
as etapas costumam ser creditadas a Elias St. Elmo Lewis, em 1898, parte da
literatura atribui a formulação completa a Arthur Frederick Sheldon, e a sigla AIDA
só aparece em 1921, com C. P. Russell ([E. St. Elmo
Lewis](https://en.wikipedia.org/wiki/E._St._Elmo_Lewis)).

Aqui preciso ser honesto sobre um limite, porque ele é meu e eu o carreguei por
semanas sem resolver. Quando escrevi sobre a decisão, o preço e o que medir,
propus três estágios e usei a palavra funil. **A decomposição em três continua de
pé. A metáfora do funil não aguenta inteira**, e quatro pressupostos dela quebram
neste terreno:

Funil pressupõe **coorte que avança uma vez**. Aqui a decisão se repete a cada
sessão de trabalho, milhões de vezes por dia, independentemente.

Funil pressupõe **perda permanente**. Perder uma decisão não remove ninguém de
nada: você é candidato de novo no minuto seguinte.

Funil pressupõe **estágios exclusivos**. O mesmo produto está em candidatura para
um agente e em adoção para outro, ao mesmo tempo.

Funil pressupõe **ordem**. Estar dentro de um scaffold — um esqueleto de projeto
pronto, que já vem com um conjunto de ferramentas escolhido — faz o produto entrar
sem que nenhuma recomendação aconteça. A etapa é pulada.

O que sobra é mais preciso e mais útil:

> **As três etapas não são estágios de uma jornada. São condições necessárias de
> uma decisão.** Você precisa das três em cada decisão, e falhar em qualquer uma
> zera aquela decisão — e só aquela.

Dentro de uma decisão, a figura do funil funciona: o conjunto só encolhe, cada
etapa é uma peneira, e a eliminação é irreversível. No instante em que o banco de
dados entrou, o código passou a chamá-lo — existe uma string de conexão, existem
tabelas com o formato dele, existe uma biblioteca instalada. O concorrente não é
"revisitado mais tarde". Ele sai, e sai na mesma sessão em que entrou.

Entre decisões, a figura é outra: o que existe é um laço. A escolha vira código
público, resposta em fórum, tutorial, dado de treino, e isso alimenta a próxima
decisão, tomada por outro par, em outra empresa, meses depois.

> **Funil dentro da decisão, laço entre decisões.**

Vale registrar por que eu não uso a palavra *flywheel* aqui, que seria a
esperada. Roda que perde energia para de girar, não gira ao contrário — e o que se
acumula entre decisões também evapora, que foi o que descrevi ao tratar de
comunidade como lençol freático, subindo com o que se deposita e descendo com o
que se extrai.

![As três condições do funil contra os três regimes de delegação: desenvolvimento governado, lista curta e decisão removida, e quem satisfaz cada condição em cada um](../../visuais/arco2-parte-01/a2p1-etapas-pt.png)

## Condição 1 — Candidatura: estar no conjunto de onde se escolhe

A primeira condição não decide nada. Ela define quem tem direito de ser
considerado.

Pense num time que precisa enviar e-mail transacional — aquela mensagem de
"confirme seu cadastro" que sai automaticamente. Existem dezenas de serviços que
fazem isso. Na prática, o time vai considerar três ou quatro. Os outros não
perderam a comparação: eles nunca entraram nela.

**É a condição mais decisiva e a única em que a perda é invisível.** Se o seu
produto não entra no conjunto, não existe carrinho abandonado, não existe cadastro
incompleto, não existe reclamação. O projeto seguiu com outra coisa e ninguém
registrou nada.

**No desenvolvimento governado**, quem satisfaz esta condição é uma regra escrita
antes. O registro de ferramentas aprovadas restringe o conjunto antes de a máquina
olhar, e reprovar no compliance não é ser concorrente fraco — é ser ausente. Trato
esse portão em detalhe numa das peças seguintes.

**Na lista curta**, quem satisfaz é a máquina, e ela mostra o resultado. Lista lida
é auditável: quem conhece o mercado percebe quando um nome esperado não está ali,
e pergunta.

**Na decisão removida**, quem satisfaz é a máquina sem exibir nada. Ninguém percebe
ausência nenhuma, porque não há o que perceber.

Um mecanismo ajuda a explicar por que o conjunto se fecha tão cedo no terceiro
caso. Numa configuração medida, **57,8% das repetições não acionaram busca na web**
(Schulte, Bleeker e Kaufmann, [arXiv
2604.07585](https://arxiv.org/pdf/2604.07585), 10 de abril de 2026 — número obtido
via citação em revisão crítica, não da tabela primária). Sem busca, o conjunto de
candidatos vem inteiro do que o modelo já traz de fábrica. Não há momento de
curadoria a observar, porque a curadoria aconteceu antes de a sessão começar.

### Quanto se delega aqui, e de qual das três situações estamos falando

Existem quatro medições públicas úteis, e é importante dizer com precisão o que
elas medem: **a segunda situação, a da lista curta.** Elas não medem a primeira,
que é interna à empresa, e não conseguem medir a terceira, pelo motivo que este
texto já expôs — ninguém responde sobre uma escolha que nunca lhe foi apresentada.

A disposição do consumidor de deixar a IA **tomar** a decisão de compra tem **teto
em 11%** — a palavra é do próprio levantamento, *"topped out at 11%"*, e o teto
ocorre nas categorias de menor risco, como higiene pessoal. Já a disposição de
deixar a IA **estreitar** as opções chega a **31%** em produto de limpeza e casa
([Gartner, 27 de maio de
2026](https://www.gartner.com/en/newsroom/press-releases/2026-05-27-gartner-survey-finds-consumers-want-ai-shopping-help-but-not-ai-purchase-decisions)).
São 322 consumidores nos Estados Unidos, campo em janeiro de 2026, e o comunicado
não publica amostragem nem margem de erro — uso o padrão, não os decimais.

Na compra corporativa de software, **69% dizem preferir validar com um vendedor
humano** as conclusões que a IA gerou ([Gartner, 20 de maio de
2026](https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights),
645 compradores). A palavra do comunicado é *prefer*: preferência declarada, não
comportamento medido.

E **86%** de quem pesquisou um produto com IA conferiu a recomendação em outra
fonte antes de comprar. Some-se a quarta população, que a peça de abertura deste
arco já trouxe: 98% dos consumidores verificam antes de comprar.

Quatro medições, quatro recortes, o mesmo desenho: **dentro da lista curta, o que
se delega é a montagem do conjunto, não a escolha.** A máquina monta e sai antes da
decisão. Uma casa de análise descreveu isso como estreitar o campo antes que a
avaliação humana comece ([IDC, 28 de janeiro de
2026](https://www.idc.com/resource-center/blog/ai-mediated-buying-journeys-how-buyers-decide-whos-worth-their-time/)).

![O regime da lista curta em quatro medições: 11% de teto para deixar a IA decidir a compra, 31% para deixar estreitar, 86% conferem em outra fonte e 69% dos compradores B2B preferem validar com uma pessoa](../../visuais/arco2-parte-01/a2p1-eixo-pt.png)

Uma ressalva vale para os quatro: são autodeclaração, e autodeclaração sobre
trabalho com IA tem um problema documentado. Num experimento aleatorizado com 16
desenvolvedores experientes e 246 tarefas reais dos próprios repositórios, as
pessoas ficaram **19% mais lentas** com a ferramenta. Antes esperavam acelerar 24%.
Depois de medidas como mais lentas, ainda estimavam ter acelerado 20% ([METR, 10 de
julho de 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)).
São **vinte pontos entre o medido e o acreditado**, e do lado de dentro a distância
não aparece. Os autores são explícitos ao dizer que o resultado não se estende além
daquele grupo, e na atualização de 24 de fevereiro de 2026, com 57 participantes, os
intervalos de confiança cruzam o zero
([METR](https://metr.org/blog/2026-02-24-uplift-update/)).

Uso os quatro pelo formato que eles compartilham, e não pelo valor de nenhum.

## Condição 2 — Recomendação: ser o escolhido dentro do conjunto

A segunda condição é a que todo mundo imagina quando pensa em decisão. Opções na
mesa, critérios, uma vencedora.

**No desenvolvimento governado**, quem satisfaz é um humano com critério
declarado, e a escolha fica registrada em algum lugar. Existe a quem perguntar por
quê, meses depois.

**Na lista curta**, quem satisfaz também é um humano. Ele vê as alternativas lado a
lado, pesa preço, maturidade e quem já usa, e escolhe. Pode escolher pelo motivo
errado, mas escolheu.

**Na decisão removida**, quem satisfaz é a máquina. Não há comparação: há um
resultado.

E quando não há comparação, a escolha não se espalha pelas opções disponíveis — ela
**converge**. Num trabalho com oito modelos, bibliotecas populares aparecem
desnecessariamente em até **48%** dos casos, Python é escolhido em **58%** inclusive
onde é subótimo, e Rust não é usado uma única vez em cenário de alto desempenho. A
conclusão dos autores, com as palavras deles: *"LLMs may prioritise familiarity and
popularity over suitability"* ([Twist, Zhang, Harman, Syme, Noppen, Yannakoudakis e
Nauck, Findings of ACL 2026, arXiv 2503.17181](https://arxiv.org/abs/2503.17181)).

Traduzindo para quem vende: **quem já é padrão de categoria ganha com a delegação.
Quem disputa o segundo lugar perde duas vezes** — não é escolhido, e também não é
comparado, que é como se melhora numa disputa. Aviso que essa última leitura é
minha e não foi testada.

### Por que a terceira situação não aparece em pesquisa nenhuma

Eu suspeitava que a delegação estivesse crescendo entre quem constrói com IA. Antes
de procurar, escrevi o que derrubaria a suspeita, porque pesquisa que só volta com
o que a gente já achava tem problema na pergunta. Três critérios: proporção estável
no tempo, aumento só em execução, ou população que delega muito encolhendo.

Dois dos três aconteceram. A suspeita caiu.

A única série pública que chega perto de medir entrega de tarefa inteira não sobe:
27,8% no campo de dezembro de 2024 a janeiro de 2025, 27% no seguinte, 39% em
agosto de 2025, 32% em novembro, e deixou de ser publicada nas duas edições
seguintes ([Anthropic Economic
Index](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)).
Não trato como série: a edição de 15 de janeiro de 2026 declara troca de
classificador no meio, e a medição é do próprio fornecedor sobre o próprio produto.

O escrutínio, esse, **aumenta** com experiência. A taxa de interrupção sobe de 5%
para 9% dos turnos entre usuários de alta permanência ([Anthropic, 24 de março de
2026](https://www.anthropic.com/research/economic-index-march-2026-report)). E os
agentes são conservadores justamente onde a decisão de fornecedor mora: em 26.760
pedidos de alteração autorados por agente, **apenas 1,3% introduzem dependência
nova**, e os que importam alguma biblioteca são incorporados a taxas de 6% a 11%
menores ([Twist e Zhang, King's College London, arXiv
2512.11589](https://arxiv.org/html/2512.11589)). Quando há biblioteca em jogo, o
humano olha mais, não menos.

Há até contra-evidência de quem nomeou o fenômeno. [Andrej
Karpathy](https://www.linkedin.com/in/andrej-karpathy-9a650716/) cunhou *vibe
coding* — programar descrevendo o que se quer e aceitando o que a máquina escreve,
sem ler as alterações — em 2 de fevereiro de 2025. Em 4 de fevereiro de 2026
aposentou o termo e propôs *agentic engineering* no lugar, escrevendo que programar
por meio de agentes vira fluxo padrão do profissional *"except with more oversight
and scrutiny"* ([registro datado por Simon
Willison](https://simonwillison.net/2026/Feb/26/andrej-karpathy/)).

Tudo isso descreve a primeira e a segunda situação. Nada disso captura a terceira.

Em 4 de junho de 2026, [Paul
Copplestone](https://www.linkedin.com/in/paulcopplestone/), cofundador e
presidente-executivo da Supabase, declarou: *"agents are now deploying the majority
of databases on our platform"*, sobre uma base declarada de mais de 250 mil
clientes ([release
oficial](https://www.prnewswire.com/news-releases/supabase-raises-500m-at-10-5b-to-accelerate-lead-in-agentic-infrastructure-302791787.html)).
A Neon aparece com número vizinho em relatório da Databricks de 27 de janeiro de
2026: agentes criam **80% de todos os bancos e 97% das ramificações**
([Databricks](https://www.databricks.com/blog/enterprise-ai-agent-trends-top-use-cases-governance-evaluations-and-more)).

Escolher banco de dados é decisão de arquitetura e de fornecedor. Não é execução.

E a razão de isso não aparecer em pesquisa de opinião é estrutural, não amostral:

> **A decisão não foi delegada. Foi removida do campo de visão.**

Ninguém responde "quem escolheu o banco?" sobre uma escolha que nunca lhe foi
apresentada. Os outros bancos que me ocorreriam não saíram em nenhum momento. Eles
nunca entraram. Por isso o único ator posicionado para contar essas decisões é
quem hospeda a decisão — e foi de lá que os dois números vieram.

![A remoção do campo de visão: das três opções que existiam, duas não foram recusadas, e sim nunca apresentadas a ninguém](../../visuais/arco2-parte-01/a2p1-remocao-pt.png)

## Condição 3 — Adoção: sobreviver à integração e ao uso

A terceira condição é onde a maioria das análises para de olhar, e é onde o
dinheiro some.

Ser escolhido não é ficar. A integração pode falhar, o custo pode surpreender, o
comportamento pode não ser o que a documentação prometia.

**No desenvolvimento governado**, a integração é acompanhada por quem aprovou.
Existe alguém com o nome na decisão, e isso muda o que acontece quando algo dá
errado.

**Na lista curta**, quem integra sabe o que escolheu e por quê, então tem paciência
com o que dá errado. A escolha é dele.

**Na decisão removida**, integra-se o que apareceu. E a primeira vez que alguém
olha aquilo com atenção costuma ser quando quebra. Um exemplo de rotina: o serviço
de e-mail transacional entrou sem discussão, funcionou por semanas, e um dia as
mensagens começam a cair em caixa de spam. Alguém abre o código para entender,
descobre um serviço que não escolheu, e a primeira pergunta não é técnica — é "por
que estamos usando isto?". A troca que vem depois não passa por nenhum critério que
a máquina tenha avaliado.

### O veto muda de natureza

Aqui está a mudança com mais consequência prática do texto inteiro.

Nas duas primeiras situações, o veto é uma escolha entre alternativas visíveis. A
pessoa vê três, prefere uma, e as outras duas continuam existindo caso a primeira
decepcione.

Na terceira, não há alternativas na tela. Há um resultado pronto.

> **O veto deixa de ser escolha entre alternativas e vira aceitação ou recusa de um
> resultado já construído** — mais barato de tomar, e mais caro de reverter.

Mais barato porque aceitar não exige avaliar nada: exige que nada pareça errado.
Foi o que eu fiz com o banco de dados. Mais caro de reverter porque, no instante em
que a pessoa aceita, aquilo já está escrito no código, com configuração, variáveis
de ambiente e tabelas em volta.

Para quem constrói produto, a consequência é direta: **você não controla a
comparação. Você controla o que a pessoa encontra pronto quando finalmente olha.**

![O veto em dois estados: com a decisão à vista é escolha entre alternativas visíveis, e com a decisão removida é aceitar ou recusar um resultado já construído, mais barato de tomar e mais caro de reverter](../../visuais/arco2-parte-01/a2p1-veto-pt.png)

### E uma assimetria que atravessa as três condições

Quanto mais fundo na cascata, mais visível fica a perda — e menos se pode fazer a
respeito.

Se o produto é descartado na adoção, existe rastro: alguém trocou, alguém
reclamou, alguém abriu uma issue. Se ele nem entra na candidatura, não existe
rastro nenhum. E é justamente na candidatura que ainda daria para agir.

Não conheço medição dessa assimetria, e aviso que a leitura é minha. Ela é a razão
pela qual a primeira condição merece mais investimento do que costuma receber.

## O que atravessa de uma decisão para a outra

Preciso corrigir uma frase minha antes de fechar.

Ao tratar de acessibilidade operacional, escrevi que a máquina decide de novo a
cada sessão e não acumula nada entre uma e outra — que cada sessão começa do zero.
**A parte sobre a máquina é verdadeira. A parte sobre o par não é**, e é o par que
decide. Continuei investigando e vi que aquilo vale para uma camada só, e é a
camada errada para quem quer entender este assunto.

São três camadas, e eu vinha operando com duas.

A **sessão** é onde a eliminação acontece. Efêmera, sem dono, e ninguém se reforça
nela.

O **corpus público** — o material que treina o modelo seguinte — acumula devagar,
não tem dono, e sofre erosão.

A do meio é a que faltava, e é a única com dono: a **memória do projeto**.
Especificação, registro de decisão, arquivo de instrução para o agente. Quem
constrói controla essa camada inteira, e ela é lida no começo de toda sessão.

Daí sai um mecanismo de hábito que eu não tinha. Escreva "usamos este banco de
dados, e por este motivo" no arquivo de memória do projeto, e **essa decisão passa
a ser relida em toda sessão seguinte. Ela deixa de ser decisão e vira premissa.** É
o hábito mais barato de instalar e o mais difícil de deslocar: não exige treino de
modelo nem código escrito, exige uma linha num arquivo.

Repare no que isso faz com a distinção das três situações: **a memória do projeto é
o instrumento que move uma decisão da terceira para a primeira.** Escrever a
escolha é reintroduzir a regra escrita antes, só que dentro do projeto em vez de
dentro da empresa.

Para quem vende, abre uma posição que a série ainda não tinha nomeado: **estar
inscrito no artefato de memória do cliente é posição mais durável que estar no dado
de treino, que se atualiza, e mais barata que o custo de troca, que exige o código
já existir.** A linha ética é clara: você escreve a documentação, quem decide
referenciá-la é o cliente.

![Funil dentro da decisão e laço entre decisões, com as três camadas do que atravessa: a sessão sem dono, a memória do projeto controlada por quem constrói, e o corpus público que acumula devagar e sofre erosão](../../visuais/arco2-parte-01/a2p1-funil-e-camadas-pt.png)

## O que fica

Existe um funil, ele é do par, e ele descreve uma decisão em vez de uma jornada. As
três etapas são condições necessárias em cascata: estar no conjunto, ser escolhido
dentro dele, sobreviver ao uso. Falhar em qualquer uma zera aquela decisão, e só
aquela — porque a decisão seguinte recomeça.

As três condições não mudam. Quem as satisfaz, sim. No desenvolvimento governado
uma regra escrita antes restringe o conjunto e um humano escolhe dentro dele. Na
lista curta a máquina monta e o humano escolhe. Na decisão removida a máquina faz
as duas coisas, e a pessoa encontra o resultado.

A primeira condição é a mais decisiva e a única sem rastro de perda. E o veto, que
continua sendo humano nas três, muda de natureza na terceira: vira aceitação de
algo pronto, mais barata de dar e mais cara de desfazer.

As peças seguintes descem condição por condição: duas sobre candidatura, uma sobre
como se entra no conjunto e outra sobre como se é cortado dele antes de qualquer
preferência; uma sobre o que decide a escolha e o que dessas táticas decai; uma
sobre adoção e o veto; e uma de fechamento, sobre onde o seu produto se encaixa e
quem cuida disso dentro da empresa.

Fecho com o que não sei.

Ninguém publica quantas decisões de fornecedor o agente tomou sozinho. Procurei em
levantamento de desenvolvedor, em relatório de plataforma e por formulação livre.
Nenhum pergunta a quem constrói quem escolheu a biblioteca, o serviço ou o banco na
última vez — a pessoa ou o agente.

E não é falha de busca. Uma das plataformas construiu a taxonomia que responderia
isso, separando o trabalho iniciado por código, por um agente e por vários agentes,
na própria interface de métricas, desde 29 de maio de 2026. O agregado não é
publicado.

**Existe quem consiga medir, e não publica.** Se você trabalha num lugar assim,
esse número é o dado mais importante que este arco poderia citar — e a conversa que
eu mais gostaria de ter depois deste texto.

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
