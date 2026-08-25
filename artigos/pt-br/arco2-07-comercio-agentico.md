<!--
Arco 2, parte 7 da série Builder-Led Growth, por Matheus Ramos.
VERSÃO NÃO CANÔNICA. A canônica é a inglesa: ../en/arc2-07-agentic-commerce.md
Em caso de divergência de fato ou de número, a inglesa prevalece.
Texto congelado. Prevista no LinkedIn para 1 de setembro de 2026.
Gerado a partir do repositório privado de trabalho. Não editar aqui.
-->

# Agentic commerce e Builder-Led Growth — o que muda para growth e engenharia

*Peça avulsa do segundo arco desta série. Não exige as anteriores. O comércio
assistido por agente é o lugar onde o funil do Builder-Led Growth é curto o
bastante para ser visto inteiro, com o que medir e o que fazer em cada etapa.*

---

## Uma assistente de loja transacionou R$ 100 milhões conversando

O Magazine Luiza tem uma assistente chamada Lu. Em 2026 ela passou a montar compra
dentro da conversa, e a empresa diz ter transacionado **R$ 100 milhões por esse
caminho**, com **conversão três vezes maior** que a dos canais tradicionais. Quem
contou foi Caio Gomes, Chief Data & AI Officer da empresa, no Fórum E-Commerce
Brasil de 2026.

O número foi divulgado pela empresa, em uma palestra. Para mim já basta, mas fica
o registro de que não é uma medição independente.

No iFood existe o Ailo. Ele monta o pedido dentro do WhatsApp, aplica cupom
sozinho, recomenda pelo que você já pediu antes, entende pedido complicado com
vários pratos e fecha a compra com um clique via Pix. Guarda preferência,
restrição alimentar e gosto de uma conversa para a outra.

Nos Estados Unidos, em **11 de janeiro de 2026**, Google e Shopify publicaram um
padrão aberto para que agentes de software consigam descobrir lojas, montar
carrinho e comprar. Vinte e poucas empresas assinaram embaixo, entre elas Visa,
Mastercard, Stripe, American Express, Walmart e Target. O objetivo declarado é
permitir que a compra aconteça dentro da conversa, sem a pessoa sair para um site.

**A infraestrutura que eles estão construindo serve para pôr o comércio dentro de
uma conversa. Aqui o comércio já está dentro de uma conversa, e o Pix já
liquida.**

Isso é o Brasil seguindo por um caminho próprio, com outra infraestrutura por
baixo, com um mecanismo que explica por que esse caminho funciona. Jason Goldberg,
escrevendo sobre quem vai controlar a superfície onde a compra acontece, formulou
assim: *"quanto mais perto o agente chega do contexto padrão do consumidor, mais
influência ele tem sobre a decisão de compra"* ([Forbes, 19 de fevereiro de
2026](https://www.forbes.com/sites/jasongoldberg/2026/02/19/the-agentic-commerce-wars-part-2-the-race-for-the-glass/)).
O contexto padrão do consumidor brasileiro é um aplicativo de mensagem que ele já
abre o dia inteiro. Ninguém precisou ser convencido a adotar um agente novo. O
agente apareceu onde a pessoa já estava.

## Comércio agêntico, Builder-Led Growth e o que um tem a ver com o outro

Comércio agêntico é a compra em que um agente de software executa uma ou mais
etapas do processo — descobrir, comparar, montar o carrinho, pagar — em nome de
uma pessoa, com grau variável de delegação.

Procurei quem cunhou o termo e não achei. A expressão circula sem autoria
atribuível, o que é raro o bastante para valer o registro: ninguém reivindica,
então não atribuirei a ninguém.

### Do PLG ao BLG

**Product-Led Growth — crescimento liderado pelo produto.** O próprio produto faz
o trabalho que antes cabia a vendas e marketing: a pessoa experimenta, percebe o
valor sozinha e decide. Teste gratuito, plano de entrada, produto que se explica
sem apresentação comercial. Foi popularizado em meados da década de 2010 pela
OpenView — com [Blake Bartlett](https://www.linkedin.com/in/blakebartlett) — e
codificado em livro por [Wes Bush](https://www.linkedin.com/in/wesbush) em 2019.

**Builder-Led Growth — crescimento liderado pelo uso do seu produto na construção
de uma solução em que a IA participa da escolha.** É o nome que dei, em julho de
2026, a um arranjo diferente: a escolha do seu produto acontece dentro de um
trabalho de construção, sem processo de compra, sem cotação, sem comitê.

O ponto que mais confunde quem chega a essa ideia é imaginar que a máquina
substituiu a pessoa. Ela não substituiu.

> **No PLG quem experimenta e decide é uma pessoa. No BLG quem experimenta e
> decide é um par — a pessoa e a máquina —, e o que muda de um caso para o outro
> é quanto dessa decisão foi delegado à máquina.**

O grau de delegação não é fixo. Ele varia com a tarefa, com o contexto, com o
ambiente e com as normas que valem ali. Uma equipe com política de fornecedor
homologado delega pouco. Alguém montando um protótipo no fim de semana delega
quase tudo.

### O que decide quando a pessoa não decide

Alguém pede a uma plataforma de construção assistida uma loja online: catálogo,
carrinho, pagamento, e-mail de confirmação de pedido.

Em alguns casos essa pessoa nomeia as peças — *"usa a Stripe para pagamento"* —, e
aí a decisão foi dela. Em outros ela não nomeia nada, e o serviço de pagamento, o
de catálogo e o de e-mail aparecem prontos no que foi montado. Quando isso
acontece, o fornecedor ganhou um cliente que nunca soube que estava contratando
alguém.

Entre os dois extremos existe um gradiente, e ele determina **o que** influencia a
escolha:

- **Quanto mais autônoma a máquina for para concluir a tarefa, mais o corpus
  decide.** Corpus é o material público que treinou o modelo — documentação,
  repositório de código, artigo, fórum, avaliação de produto. Sem instrução
  específica, a máquina vai no que ela já conhecia, que é o que apareceu mais
  vezes ali.
- **Quanto mais direcionada ela for, mais o harness decide.** Harness é o andaime
  que executa o agente e delimita o que ele pode chamar e enxergar — as
  instruções que recebeu, as ferramentas que estão ligadas, os limites do
  ambiente. Aqui o que decide não é a fama do fornecedor, é estar dentro do
  alcance daquele arranjo.

Quatro coisas determinam se o seu produto é o escolhido nesse jogo. Esta série
chama de pilares: **ser legível por máquina** — dizer sem contexto o que você faz;
**ser operacionalmente acessível** — dar para integrar sem interpretação; **ter
comunidade** que escreva sobre você em lugares que a máquina lê; **ser confiável o
bastante** para o agente agir sem parar para perguntar.

### O que isso tem a ver com uma loja

A definição fala de agente montando software, porque foi ali que o fenômeno
apareceu primeiro. Este texto pergunta o que sobra dela quando o que está sendo
montado é uma compra.

## O protocolo publicado é um pilar escrito como norma

Um agente que queira transacionar com uma loja precisa primeiro descobrir do que
aquela loja é capaz. A solução do padrão de janeiro é um arquivo num caminho fixo
e previsível: **`/.well-known/ucp`**. O que vive lá se chama perfil de capacidade —
a declaração estruturada do que aquela loja sabe fazer, em que versão, com que
extensões. Nas palavras do documento de engenharia da Shopify, escrito por Ilya
Grigorik: *"Discovery is the process of fetching these profiles; negotiation
computes their intersection."* Descobrir é buscar esses perfis; negociar é
calcular a interseção entre eles.

No mesmo dia, o Google passou a pedir do varejista dezenas de atributos novos no
cadastro de produto, incluindo **respostas a perguntas comuns, acessórios
compatíveis e substitutos**.

Um arquivo canônico, em endereço previsível, que diz sem contexto o que uma coisa
faz e o que ela aceita. Se você acompanha esta série, reconheceu: é o primeiro
pilar — o de ser legível por máquina — e o segundo — o de ser operacionalmente
acessível — escritos como especificação técnica por duas empresas grandes.

A teoria não previu o protocolo. **O método deste trabalho é o inverso disso: o
Builder-Led Growth já está sendo praticado; o que fazemos aqui é observar e
nomear.** Aconteceu o mesmo com o Product-Led Growth, que empresas praticavam anos
antes de alguém escrever o nome disso num livro. O padrão de janeiro de 2026 é
Builder-Led Growth em exercício, publicado como norma por quem o pratica.

## Dois funis lado a lado: o de marketing e o do Builder-Led Growth

Um funil descreve **onde alguém está** no caminho até a compra, desenhado assim
porque entra muita gente na boca e sai pouca no bico. Ele serve para duas coisas:
dizer o que se mede em cada altura e dizer que ação move alguém para a altura
seguinte.

### O funil de marketing

O mais conhecido de todos. A formulação inicial é de Elias St. Elmo Lewis, em
1898 — atrair atenção, manter interesse, criar desejo —, ao que depois se somou
obter ação. A sigla AIDA apareceu em 1921 — com C. P. Russell — e o desenho de funil
foi associado ao modelo em 1924. Em linguagem de hoje, três alturas:

- **Topo, descoberta.** A pessoa não conhece você. Mede-se alcance, impressão,
  visita.
- **Meio, consideração.** Ela conhece e está comparando. Mede-se lead, clique,
  tempo no site, carrinho montado.
- **Fundo, decisão.** Ela compra. Mede-se conversão, ticket médio, custo de
  aquisição.

Tudo nesse desenho descreve **uma pessoa se movendo**, com você tentando ser
notado no caminho dela.

### O funil do Builder-Led Growth

Descreve outra coisa: **onde o seu produto está** dentro de um trabalho que um par
de pessoa e máquina está executando. Quem anda pelo funil não é o cliente.

- **Candidatura.** Você está no conjunto de onde se escolhe.
- **Construção.** A decisão fechou sobre você, e tirar ainda é barato.
- **Adoção.** Você virou premissa, e tirar custa um projeto.

> **No funil de marketing quem se move é o cliente. No funil do BLG o que se
> move é o produto e quem o move é o par.**

![Os dois funis lado a lado: no de marketing as etapas são descoberta, consideração e decisão, com o cliente se movendo; no do Builder-Led Growth são candidatura, construção e adoção, com o produto se movendo, empurrado pelo par de pessoa e máquina](../../visuais/arco2-comercio-agentico/ca-comparacao-pt.png)

### Primeira etapa: descoberta no marketing, candidatura no BLG

**No marketing, a comparação mais direta é uma busca no Google.** Você pode
aparecer ou não na primeira página, e o seu link pode ou não ser clicado.
Trabalhar o posicionamento — o que o mercado chama de **SEO**, otimização para
motor de busca — aumenta as duas chances. Nenhuma das duas vira garantia.

**No BLG a lista é mais curta, e clicar deixa de ser uma escolha de quem
procura.** A máquina não devolve dez links azuis para alguém percorrer; ela monta
uma resposta com dois ou três nomes dentro. Estar nessa lista curta é o mesmo
jogo do SEO com outro nome: **GEO**, otimização para motor generativo, e **AEO**,
otimização para motor de resposta. Melhorar ali aumenta a probabilidade de o seu
produto aparecer, tanto para a pessoa que lê a resposta quanto para a máquina que
a monta.

A diferença prática entre os dois: no Google a pessoa vê a lista inteira e decide
onde clicar. Na resposta do agente ela vê o que sobrou da curadoria, sem saber o
que foi descartado.

Em comércio, estar no conjunto quer dizer estar no catálogo, no feed ou na base de
onde o agente tira as opções.

**O que se mede.** Não é tráfego nem sessão, que é o que o topo de funil mediria.
É **presença na resposta**. Escolha as trinta perguntas que um cliente faria na
sua categoria, pergunte ao agente com repetição, registre em quantas delas você
aparece. Essa taxa é sua e ninguém a publica.

**As ferramentas.** AEO e GEO, a documentação canônica, o conteúdo que terceiros
escrevem sobre você e, em comércio, o feed de produto mais o perfil de
capacidade.

**A perda aqui não aparece nos seus relatórios**, o que é diferente de não
acontecer. Antes de qualquer carrinho existir, houve uma curadoria: alguma peça do
sistema montou uma lista curta e você não entrou nela. Essa eliminação é real e
está registrada em algum lugar — no log de quem operou o agente. Do seu lado não
há carrinho abandonado para investigar, porque não houve carrinho.

### Segunda etapa: consideração no marketing, construção no BLG

**No marketing, o meio de funil é onde a pessoa compara.** Ela abriu três abas,
montou carrinho em duas, leu avaliação. O que você mede é quanto disso vira
compra.

**No BLG a comparação já aconteceu, e você venceu.** A etapa começa quando o
processo de escolha fecha sobre você: o agente parou de considerar alternativas e
passou a montar a resposta com você dentro. Antes disso houve pergunta de
esclarecimento, comparação, verificação de preço e prazo — tudo isso é
candidatura ainda.

O carrinho é onde esse estado fica visível. O padrão de janeiro nomeia o objeto,
chamando de *Cart Mandate* o contrato do que vai ser comprado antes de ser
comprado. Você foi escolhido. Tirar você ainda custa um clique.

**O que se mede.** A **taxa de substituição** entre a decisão e o pagamento:
quantas vezes o agente montou a resposta com você e trocou antes de fechar. É o
primo do carrinho abandonado, com uma diferença que importa — quem abandona não
é a pessoa, é a máquina, ao encontrar algo que fez você deixar de servir.

**As ferramentas.** Completude do dado de produto, que é literalmente o que o
cadastro passou a pedir — substituto, acessório compatível, resposta a pergunta
comum. Preço e estoque corretos no feed, porque agente que encontra divergência
troca. Tempo de resposta do endereço de capacidade, porque agente que espera
demais segue adiante.

### Terceira etapa: decisão no marketing, adoção no BLG

**O funil de marketing clássico termina na compra.** Foi essa lacuna que o funil
pirata veio preencher décadas depois — aquisição, ativação, retenção, receita e
indicação, apresentado por [Dave McClure](https://www.linkedin.com/in/davemcclure)
em 2007 —, ao acrescentar o que acontece depois que o dinheiro troca de mãos.

**No BLG a terceira etapa é justamente essa.** Adoção não é a compra: é a compra
ter virado premissa. Existem dados no seu formato, existe pagamento guardado,
existe gente comprando sem reabrir a comparação.

**O que se mede.** A fatia de recompra que **não** volta a passar pelo conjunto de
consideração. Na prática: dos pedidos dos últimos noventa dias, quantos vieram de
alguém que não comparou nada.

**As ferramentas.** A camada de memória. Assinatura, pagamento guardado, recompra
de um clique. É a mesma força que a teoria do trabalho a ser feito chama de
hábito — Bob Moesta a descreve como a mais forte das contrárias a qualquer
troca.

### A etapa do meio encolhe até sumir

> **Em comércio a etapa do meio é curta e encolhe até desaparecer conforme a
> delegação sobe.**

Uma recompra de um clique vai de candidatura direto a adoção. Não existe intervalo
em que você esteja escolhido e ainda dê para tirar sem custo. A janela em que um
concorrente poderia entrar não abre.

**A candidatura é ainda mais decisiva aqui do que no software**, porque quase nada
morre na construção. O verbo que descreve a etapa também muda. Em software você
trabalha para **ser encontrado**. Em comércio você trabalha para **ser admitido**.
Ninguém opera um portão na instalação de bibliotecas; em comércio o portão
existe, tem dono e tem processo de entrada.

![As três etapas do funil em comércio com o que se mede em cada uma: candidatura pela presença na resposta, construção pela taxa de substituição depois que a decisão fecha, adoção pela recompra que não reabre comparação — e a etapa do meio encolhendo conforme a delegação sobe](../../visuais/arco2-comercio-agentico/ca-funil-pt.png)

## A loja deixa de ser destino e vira fonte de dados

O tráfego já mudou de origem, com medição instrumentada. A Adobe acompanha
o que chega às lojas americanas a partir de ferramentas de inteligência artificial,
sobre uma base de **mais de um trilhão de visitas**. Em maio de 2026 esse tráfego
cresceu **138% em um ano**, acumulando **1.324% desde outubro de 2024**, quando
eles começaram a medir. Quem chega por ali converte **54% melhor** que o restante,
passa **53% mais tempo** no site e vê **23% mais páginas**
([Adobe Analytics, via Digital Commerce 360, 17 de junho de
2026](https://www.digitalcommerce360.com/2026/06/17/adobe-ai-referred-traffic-to-retail-sites-doubles-in-a-year/)).

A mesma medição mostra o outro lado. A Adobe avalia quanto do conteúdo de uma
página é legível para um modelo de linguagem, e o resultado por categoria fica entre **47% em móveis e decoração e 63% em
cosméticos**, com eletrônicos em 56% e vestuário em 51%. Mesmo nos setores que vão
melhor, **de 30% a 40% do conteúdo das páginas de maior valor não é capturado**.

Perto de metade do que uma loja escreve sobre os próprios produtos não chega à
máquina que hoje decide se aquela loja aparece na resposta.

### O que fica público e o que não fica

Uma parte do que acontece numa compra **é** pública e treina o modelo. Avaliação de
produto, nota, seção de comentários, comparativo de terceiro, vídeo de quem usou —
tudo isso está escrito, indexado e disponível.

O que não fica público é outra coisa: **o registro da escolha.** Qual produto o
agente colocou na resposta, o que ele descartou antes de montar a lista, se houve
devolução, se houve disputa, se a pessoa comprou de novo. Esse registro fica com
quem operou o agente.

A diferença com o software muda a estratégia inteira. Lá o artefato construído
**é** o registro da escolha: o código que usa a sua biblioteca
está publicado, e quem lê aquele repositório aprende que você foi escolhido. Em
comércio o público é opinião sobre o produto; a escolha em si não deixa rastro
fora de quem a operou.

[Alexandre Sato](https://www.linkedin.com/in/alexandresato/) me apontou o
movimento mais amplo por trás disso. Conforme se espalham o ajuste fino de modelo
e a recuperação sobre acervo próprio, o que a máquina sabe passa a se concentrar
dentro de quem opera a plataforma. A mesma inteligência artificial que o seu
concorrente usa, ou um modelo que aprendeu como a sua operação funciona e a que só
você tem acesso — a segunda é a que tem valor comercial defensável.

Para o varejista, a consequência prática cabe numa frase: **a sua loja deixou de
ser um destino e virou uma fonte de dados.** Antes a pessoa entrava, e você
observava — o que ela procurou, onde parou, o que abandonou. Agora o agente
observa, e você recebe uma requisição. A venda pode continuar acontecendo. A
observação, não.

![Quanto do conteúdo de uma loja é legível para a máquina, por categoria: 63% em cosméticos, 56% em eletrônicos, 51% em esportivos e vestuário, 48% em mercearia e 47% em móveis e decoração — com 30% a 40% do conteúdo das páginas de maior valor não capturado mesmo nos melhores setores](../../visuais/arco2-comercio-agentico/ca-legibilidade-pt.png)

## Quem está onde nessa história

### O consumidor não participa do funil, recebe o resultado dele

Quem passa pelo funil é quem **constrói**: a empresa de meio de pagamento, a
plataforma, o varejista que precisa ser escolhido. Essas escolhem fornecedor, e é
sobre elas que a teoria fala. O consumidor não escolhe fornecedor de nada. Ele
recebe uma resposta pronta.

O que ele recebe, porém, depende inteiramente da qualidade daquele funil. Se
metade do que existe escrito sobre uma categoria não é legível para a máquina, a
recomendação que chega até ele foi montada com informação parcial — e nada na tela
diz isso. Ele não escolheu as fontes, não sabe quais foram, e não tem como
conferir. Recebe o resultado de um processo que não vê.

Ele determina uma restrição dura para quem constrói. A disposição declarada de
deixar a inteligência artificial **tomar** a decisão de compra **tem teto em 11%**,
nas categorias de menor risco. A disposição de deixar a máquina apenas
**estreitar** as opções chega a **31%** em produto de limpeza e casa e **28%** em
eletrônico pessoal. São 322 consumidores nos Estados Unidos, com campo em janeiro
de 2026, num levantamento da Gartner que não publica amostragem nem margem de erro
— uso a ordem de grandeza, não os decimais. É autodeclaração, que em assunto de
inteligência artificial costuma divergir do comportamento medido.

> **Quem está construindo autonomia total está construindo para 11% do mercado.**

A força que trava tem nome. Bob Moesta, ao descrever o que faz alguém trocar de
solução, separa a atração do novo da **ansiedade** que ele provoca. Na velha
comparação entre a furadeira e a fita dupla-face disputando o mesmo trabalho de
pendurar um quadro, dá para testar a fita e desistir. Numa compra delegada não:
**a transação é o compromisso.** Você descobre se foi bom depois de já ter pago.

![O teto da delegação do consumidor: 11% aceitam que a IA decida a compra, contra 31% que aceitam que ela apenas estreite as opções em produto de limpeza e casa e 28% em eletrônico pessoal](../../visuais/arco2-comercio-agentico/ca-teto-pt.png)

### O comerciante está dentro, mesmo sem escrever uma linha de código

O varejista não constrói software. Ainda assim ele é, literalmente, um produto
sendo selecionado por uma máquina. Ou ele se adequa ao modo como o agente
descobre, entende e transaciona, ou fica de fora.

Cresci ouvindo do Senna que o segundo nada mais é do que o primeiro dos
perdedores. Em comércio agêntico isso é máxima, com a lógica do *winner takes
all*.

Com uma ressalva que importa. A conversa com um agente não é uma linha reta.
Alguém pergunta por hambúrguer para a família, o agente traz opções, a pessoa reformula, e o
pedido termina numa pizza que agrada todo mundo e sai mais barata. A cada
reformulação o conjunto é remontado. Ficar de fora da primeira resposta não é
sentença — ficar de fora de todas elas é.

Isso muda o que você mede. Não basta aparecer para *"melhor hambúrguer perto de
mim"*. É preciso continuar alcançável quando a pergunta vira *"o que agrada quatro
pessoas com gostos diferentes por até cento e vinte reais"*, que é uma pergunta
sobre adequação e preço, não sobre categoria.

Há uma razão organizacional para a adequação demorar mais do que a urgência
sugere. Num relatório de agosto de 2026 sobre por que a adoção de agentes trava
dentro das empresas, a McKinsey descreve o medo que mais congela comportamento nas
palavras de quem o sente: se o agente me dá a resposta errada e eu ajo com base
nela, o erro ainda é meu. Responsabilidade sem controle.

Esse estudo olha para o uso de agentes dentro de organizações, não para comércio.
Levar a conclusão dele para a mesa de um varejista é conjectura minha. Palpite
embasado, mas conjectura: a decisão de expor catálogo e checkout a um
agente externo tem exatamente o mesmo formato — alguém assina embaixo de uma
resposta que a máquina vai dar sozinha.

### A porta: você talvez não possa recusar o agente

A maior varejista do mundo tentou. A Amazon processou a Perplexity por causa de um
agente de navegador que comprava em nome de quem o usava e obteve uma liminar
bloqueando o acesso em 10 de março de 2026.

**Em 4 de agosto de 2026 o Nono Circuito reverteu.** O raciocínio: sob a lei
americana que trata de acesso não autorizado a sistemas, quem acessou os
computadores da Amazon foi **o usuário**, com a ajuda do agente. A ferramenta não
acessa; a pessoa acessa usando a ferramenta.

O critério que a corte usou não é o que se imagina. **Não é o quanto o agente é
autônomo, é por onde os pacotes passam.** O tribunal apontou que as comunicações
eram roteadas pelo computador do próprio usuário e que a empresa do agente não
falava diretamente com os servidores da Amazon, distinguindo de um caso anterior
em que os sistemas do réu conversavam direto com a plataforma.

O agente que roda no navegador da pessoa, o que parece mais invasivo, é o que fica
protegido. **O agente hospedado num servidor, que é o desenho de quase toda
plataforma de comércio agêntico, cai do outro lado da linha.** Onde o seu agente
roda deixou de ser só uma decisão de arquitetura.

Para o varejista a leitura é direta: se recusar o agente na porta não é um direito
garantido, **preparar-se para ele deixa de ser opção estratégica e vira condição a
que você está sujeito.**

![O critério do Nono Circuito não é autonomia, é arquitetura: agente que roda no navegador do usuário é instrumento dele; agente hospedado que fala direto com o servidor da loja pode ser tratado como ator próprio](../../visuais/arco2-comercio-agentico/ca-porta-pt.png)

## O que fazer — e por que nenhum time resolve isso sozinho

### A fronteira entre marketing e engenharia dissolveu

> **Quando quem lê é a máquina, o artefato de engenharia e a peça de marketing são
> o mesmo objeto.**

A descrição de produto é material de venda, porque é ela que o comprador lê. O
comprador é uma máquina. O arquivo de capacidade em `/.well-known/ucp` é a vitrine.
O atributo de catálogo, aquele campo chato que alguém preenche sem entusiasmo, é o
argumento comercial. Não são coisas parecidas: são a mesma coisa, vista de dois
departamentos que não se falam.

Os 47% a 63% de legibilidade por categoria são a conta desse desencontro. Ninguém
escreveu uma página ruim de propósito. As páginas foram escritas para uma pessoa
olhar, por um time que não sabia que o próximo leitor seria um programa.

Um número mostra onde o dinheiro está indo. A pesquisa da McKinsey de agosto de
2026 descreve o padrão das transformações que dão certo como **1:3:5** — para cada
dólar investido em tecnologia de agentes, três em redesenho de processo e cinco em
capacitação e adoção. A maioria das empresas **inverte essa fórmula por completo**,
colocando quase tudo na tecnologia e tratando o resto como detalhe de
implementação. Se o seu investimento está invertido, o atraso na adoção é seu.

![O padrão 1:3:5 das transformações que funcionam — um em tecnologia, três em redesenho de processo, cinco em capacitação — contra a distribuição invertida que a maioria das empresas pratica](../../visuais/arco2-comercio-agentico/ca-135-pt.png)

### Para engenharia

**Publique um perfil canônico em caminho previsível.** Se você é comerciante, isso
hoje tem endereço literal. O princípio vale para qualquer fornecedor: um lugar só,
legível sem contexto, que diga o que você faz e o que você aceita.

**Escreva o dado que a máquina pede, não o que a página precisa.** Substituto,
acessório compatível, resposta a pergunta comum.

**Meça a sua própria legibilidade.** A conta é simples e ninguém faz: pegue as
vinte páginas que mais vendem, liste os fatos que um comprador precisa saber para
decidir — medida, compatibilidade, prazo, política de devolução, o que vem na
caixa — e então peça a um modelo que responda cada um desses fatos usando só
aquela página. O que ele não conseguir responder está na página de um jeito que a
máquina não alcança: dentro de imagem, escondido atrás de aba que só abre com
clique, ou implicado num texto de venda em vez de dito. A referência pública de
mercado está entre 47% e 63% por categoria. Saber onde você cai nessa faixa é
trabalho de uma tarde; consertar o que aparecer é trabalho de um trimestre.

**Decida conscientemente onde o agente roda.** Navegador ou servidor mudou de
natureza depois de agosto de 2026, e a resposta muda quem responde pelo acesso.

**Instrumente o invisível.** Registre quais decisões vieram de um agente e quais
vieram de uma pessoa. Ninguém publica esse número hoje. Quem o tiver internamente
enxerga o próprio funil enquanto o mercado discute por impressão.

**Preserve o caminho de reversão.** Toda a tolerância a pagamento delegado se
apoia em poder desfazer. Onde desfazer é difícil, a delegação encontra um teto
mais baixo.

### Para growth

**Meça presença na resposta, não só tráfego.** Trinta perguntas da sua categoria,
repetição, registro. É a única forma que conheço de enxergar a etapa em que a
perda não aparece em relatório nenhum.

**Teste a pergunta reformulada, não só a pergunta óbvia.** Se o cliente pode
chegar por *"o que agrada quatro pessoas por até cento e vinte reais"*, é essa a
consulta que precisa te encontrar.

**Trate catálogo e feed como topo de funil**, porque em comércio candidatura é
admissão, não descoberta. AEO e GEO continuam valendo; o feed é o que você
controla.

**Recupere a observação que você perdeu.** Se a pessoa não entra mais na loja, os
sinais que você lia na navegação secaram. O que sobra vem da conversa que o agente
teve, e negociar acesso a isso é assunto comercial, não técnico.

**Projete para o teto de 11%.** Ganha o produto que faz a delegação parecer
reversível, não o que automatiza mais.

### Para os dois, juntos

**A descrição de produto tem prazo e dono de crescimento**, porque é material de
venda. Tratá-la como tarefa de cadastro que alguém faz quando sobrar tempo é
deixar a vitrine fechada.

**O alvo é estar escrito na diretriz do cliente.** As empresas mais organizadas já
não deixam o agente escolher sozinho: escrevem documentos de especificação que
conduzem a máquina dentro das linhas gerais da casa. Estar nomeado nesse documento
é posição mais durável do que estar no dado de treino, que se atualiza, e mais
barata do que o custo de troca, que exige o código já existir. Ela se conquista
com credibilidade técnica e se fecha comercialmente, o que significa que nenhum
dos dois times chega lá sozinho.

**Alguém precisa ser dono da resposta a "quem responde quando o agente erra".** Não
é pergunta de conformidade. É a pergunta que está travando a adoção nas empresas
que já compraram a tecnologia.

## O que eu não sei

**Decompor amplia ou fragmenta o conjunto?** Ferramentas novas quebram um problema
em pedaços e mandam cada pedaço para um modelo especializado. Isso pode criar mais
vagas — mais subproblemas, mais oportunidades de ser considerado — ou o contrário,
vagas com menos candidatos plausíveis, em que o especialista ganha por ausência de
concorrente. As duas leituras se sustentam.

**Não achei medição brasileira do teto da delegação.** O número de 11% é
americano, e há razão para desconfiar que aqui seja diferente, não porque o
brasileiro confie mais, mas porque a delegação chega por um canal que ele já usa
todo dia. Se alguém tiver esse dado, é o número mais valioso que este texto
poderia ter citado.

**Ninguém publica quantos produtos foram descartados antes da lista curta.** A
etapa em que a maior parte da concorrência morre é a única sem instrumento
público. Quem opera o agente tem esse log.

**Esta série ainda não provou a própria afirmação central.** Sustento que a máquina
está participando da escolha de fornecedor numa escala que ninguém está medindo.
Existe quem consiga medir isso e não publica. Até esse número existir, quem afirma
carrega o ônus, e quem afirma sou eu.

Se você trabalha num lugar que consegue medir, essa é a conversa que eu mais quero
ter depois deste texto.

---

**Série Builder-Led Growth**, por Matheus Ramos. Segundo arco:

- [Arco 2, parte 0: Do PLG ao BLG — o que continua valendo quando quem escolhe é um par](arco2-00-do-plg-ao-blg.md)
- [Arco 2, parte 1: O funil do Builder-Led Growth — as três etapas e o que acelera a passagem](arco2-01-o-funil-e-o-eixo-da-delegacao.md)
- Agentic commerce e Builder-Led Growth — o que muda para growth e engenharia (este texto)

O primeiro arco, para quem quiser o percurso completo:

- [Parte 1 — Quando a máquina também é seu cliente](01-quando-a-maquina-e-cliente.md)
- [Parte 2 — A decisão, o preço e o que medir](02-decisao-preco-e-medicao.md)
- [Parte 3 — O imposto que a máquina cobra e o humano não vê](03-legibilidade-por-maquina.md)
- [Parte 4 — Quantas vezes o agente precisa chamar um humano](04-acessibilidade-operacional.md)
- [Parte 5 — O poço de onde todos bebem](05-comunidade-e-sinal-de-validacao.md)
- [Parte 6 — A máquina é imprensa e leitor ao mesmo tempo](06-relacoes-publicas.md)
- [Parte 7 — O que faz o agente confiar, e por que a competência dele é o problema](07-confianca-e-seguranca.md)
