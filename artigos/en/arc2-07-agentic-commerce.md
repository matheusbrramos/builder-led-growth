<!--
Arc 2, part 7 of the Builder-Led Growth series, by Matheus Ramos.
CANONICAL VERSION (English).
Portuguese counterpart: ../pt-br/arco2-07-comercio-agentico.md
Text frozen. No LinkedIn date set yet.
Generated from the private working repository. Do not edit here.
-->

# Agentic commerce and Builder-Led Growth — what changes for growth and engineering

*A standalone piece from the second arc of this series. It doesn't require the
earlier ones. Agent-assisted commerce is where the Builder-Led Growth funnel is
short enough to be seen whole, with what to measure and what to do at each stage.*

---

## A shop assistant transacted R$ 100 million by chatting

Magazine Luiza, one of the largest retailers in Brazil, has an assistant called
Lu. In 2026 she started assembling purchases inside the conversation, and the
company says it has transacted **R$ 100 million** down that route, at **three
times the conversion** of its traditional channels. The figure comes from Caio
Gomes, the company's Chief Data & AI Officer, speaking at the Fórum E-Commerce
Brasil.

A company disclosed its own number, in a talk. That is enough for me, with the
record standing that it is not an independent measurement.

The food delivery platform iFood has Ailo. It assembles the order inside
WhatsApp, applies coupons on its own, recommends from what you ordered before,
handles a complicated order with several dishes, and closes the purchase in one
click over Pix, the Brazilian instant payment system. It keeps preferences,
dietary restrictions and taste from one conversation to the next.

In the United States, on **11 January 2026**, Google and Shopify published an
open standard so that software agents can discover shops, assemble a cart and
buy. Twenty-odd companies signed on, Visa, Mastercard, Stripe, American Express,
Walmart and Target among them. The declared goal is to let the purchase happen
inside the conversation, without the person leaving for a website.

**The infrastructure they are building exists to put commerce inside a
conversation. Here commerce is already inside a conversation, and Pix already
settles it.**

That is Brazil taking a route of its own, on different plumbing, with a mechanism
that explains why the route works. Jason Goldberg, writing about who will control
the surface where the purchase happens, put it this way: *"the closer the agent
gets to the consumer's default context, the more influence it has over the
purchase decision"* ([Forbes, 19 February
2026](https://www.forbes.com/sites/jasongoldberg/2026/02/19/the-agentic-commerce-wars-part-2-the-race-for-the-glass/)).
The default context of the Brazilian consumer is a messaging app they already
have open all day. Nobody had to be talked into adopting a new agent. The agent
showed up where the person already was.

## Agentic commerce, Builder-Led Growth, and what one has to do with the other

Agentic commerce is a purchase in which a software agent performs one or more
steps of the process — discovering, comparing, assembling the cart, paying — on
behalf of a person, with a variable degree of delegation.

I went looking for whoever coined the term and found nobody. The expression
circulates without attributable authorship, which is rare enough to be worth
recording: nobody claims it, so I will attribute it to nobody.

### From PLG to BLG

**Product-Led Growth.** The product itself does the work that used to belong to
sales and marketing: the person tries it, sees the value on their own, and
decides. Free trial, entry plan, a product that explains itself without a sales
deck. It was popularised in the mid-2010s by OpenView — with [Blake
Bartlett](https://www.linkedin.com/in/blakebartlett) — and written into a book by
[Wes Bush](https://www.linkedin.com/in/wesbush) in 2019.

**Builder-Led Growth — growth led by your product being used to build a solution
in which AI takes part in the choice.** It is the name I gave, in July 2026, to a
different arrangement: your product gets chosen inside a piece of construction
work, with no purchasing process, no quote, no committee.

The point that most confuses people arriving at this idea is imagining that the
machine replaced the person. It did not.

> **In PLG the one who tries and decides is a person. In BLG the one who tries
> and decides is a pair — the person and the machine — and what changes from case
> to case is how much of that decision was delegated to the machine.**

The degree of delegation is not fixed. It moves with the task, with the context,
with the environment and with the rules in force there. A team with an approved
vendor policy delegates little. Someone assembling a prototype over a weekend
delegates nearly everything.

### What decides when the person doesn't

Someone asks an AI build platform for an online shop: catalogue, cart, payment,
order confirmation e-mail.

In some cases that person names the parts — *"use Stripe for payments"* — and the
decision was theirs. In others they name nothing, and the payment service, the
catalogue service and the e-mail service turn up already wired into what was
built. When that happens, the vendor gained a customer who never knew they were
signing anyone up.

Between the two extremes there is a gradient, and it determines **what** drives
the choice:

- **The more autonomous the machine is in finishing the task, the more the corpus
  decides.** The corpus is the public material the model trained on —
  documentation, code repositories, articles, forums, product reviews. With no
  specific instruction, the machine goes with what it already knew, which is
  whatever showed up there most often.
- **The more directed it is, the more the harness decides.** The harness is the
  scaffolding that runs the agent and bounds what it can call and see — the
  instructions it received, the tools that are switched on, the limits of the
  environment. What decides here is not a vendor's fame, it is being within reach
  of that particular arrangement.

Four things determine whether your product is the one picked in this game. This
series calls them the pillars: **being machine-legible** — saying what you do
without context; **being operationally accessible** — being integrable without
interpretation; **having a community** that writes about you in places the
machine reads; **being trustworthy enough** for the agent to act without stopping
to ask.

### What this has to do with a shop

The definition talks about an agent assembling software, because that is where
the phenomenon showed up first. This text asks what survives of it when the thing
being assembled is a purchase.

## The published protocol is a pillar written as a standard

An agent that wants to transact with a shop first has to discover what that shop
is capable of. The answer in the January standard is a file at a fixed,
predictable path: **`/.well-known/ucp`**. What lives there is called a capability
profile — the structured declaration of what that shop knows how to do, in which
version, with which extensions. In the words of the Shopify engineering write-up,
by Ilya Grigorik: *"Discovery is the process of fetching these profiles;
negotiation computes their intersection."*

On the same day, Google began asking retailers for dozens of new attributes in
the product feed, including **answers to common questions, compatible accessories
and substitutes**.

A canonical file, at a predictable address, saying without context what a thing
does and what it accepts. If you have been following this series, you recognised
it: the first pillar — machine legibility — and the second — operational
accessibility — written as a technical specification by two large companies.

The theory did not predict the protocol. **The method of this work is the
reverse: Builder-Led Growth is already being practised; what we do here is
observe and name.** The same happened with Product-Led Growth, which companies
practised for years before anyone wrote the name of it in a book. The January
2026 standard is Builder-Led Growth in exercise, published as a norm by the
people practising it.

## Two funnels side by side: marketing's and Builder-Led Growth's

A funnel describes **where somebody is** on the way to a purchase, drawn that way
because many enter at the mouth and few come out at the spout. It serves two
purposes: saying what gets measured at each height, and saying which action moves
somebody to the next one.

### The marketing funnel

The best known of all of them. The original formulation belongs to Elias St. Elmo
Lewis, in 1898 — attract attention, hold interest, create desire — to which
obtaining action was added later. The AIDA acronym appeared in 1921, with C. P.
Russell, and the funnel drawing was attached to the model in 1924. In today's
language, three heights:

- **Top, discovery.** The person doesn't know you. You measure reach,
  impressions, visits.
- **Middle, consideration.** They know you and are comparing. You measure leads,
  clicks, time on site, carts assembled.
- **Bottom, decision.** They buy. You measure conversion, average order value,
  acquisition cost.

Everything in that drawing describes **a person moving**, with you trying to be
noticed along their way.

### The Builder-Led Growth funnel

It describes something else: **where your product is** inside a piece of work
that a pair of person and machine is carrying out. The one walking the funnel is
not the customer.

- **Candidacy.** You are in the set the choice is made from.
- **Construction.** The decision closed around you, and removing you is still
  cheap.
- **Adoption.** You became a premise, and removing you costs a project.

> **In the marketing funnel what moves is the customer. In the BLG funnel what
> moves is the product, and what moves it is the pair.**

![The two funnels side by side: in the marketing one the stages are discovery, consideration and decision, with the customer moving; in the Builder-Led Growth one they are candidacy, construction and adoption, with the product moving, pushed by the pair of person and machine](../../visuais/arco2-comercio-agentico/ca-comparacao-en.png)

### First stage: discovery in marketing, candidacy in BLG

**In marketing, the closest comparison is a Google search.** You may or may not
show up on the first page, and your link may or may not get clicked. Working your
position — what the market calls **SEO**, search engine optimisation — raises
both odds. Neither one turns into a guarantee.

**In BLG the list is shorter, and clicking stops being a choice made by whoever
is searching.** The machine doesn't hand back ten blue links for someone to work
through; it assembles an answer with two or three names inside it. Being on that
short list is the same game as SEO under other names: **GEO**, generative engine
optimisation, and **AEO**, answer engine optimisation. Improving there raises the
probability of your product appearing, both for the person reading the answer and
for the machine assembling it.

The practical difference between the two: on Google the person sees the whole
list and decides where to click. In the agent's answer they see what survived the
curation, without knowing what was discarded.

In commerce, being in the set means being in the catalogue, in the feed, or in
the base the agent draws its options from.

**What gets measured.** Not traffic and not sessions, which is what a top of
funnel would measure. It is **presence in the answer**. Pick the thirty questions
a customer would ask in your category, put them to the agent repeatedly, record
how many of them you show up in. That rate is yours, and nobody publishes it.

**The tools.** AEO and GEO, canonical documentation, the content third parties
write about you, and, in commerce, the product feed plus the capability profile.

**The loss here doesn't show up in your reports**, which is different from not
happening. Before any cart exists, there was a curation: some part of the system
assembled a short list and you weren't on it. That elimination is real and it is
recorded somewhere — in the logs of whoever operated the agent. On your side
there is no abandoned cart to investigate, because there was no cart.

### Second stage: consideration in marketing, construction in BLG

**In marketing, the middle of the funnel is where the person compares.** They
opened three tabs, assembled carts in two, read reviews. What you measure is how
much of that turns into a purchase.

**In BLG the comparison already happened, and you won.** The stage begins when
the process of choosing closes around you: the agent stopped considering
alternatives and started assembling the answer with you inside it. Before that
there were clarifying questions, comparison, checks on price and delivery time —
all of that is still candidacy.

The cart is where this state becomes visible. The January standard names the
object, calling *Cart Mandate* the contract of what is going to be bought before
it is bought. You were chosen. Taking you out still costs one click.

**What gets measured.** The **substitution rate** between decision and payment:
how many times the agent assembled the answer with you and swapped you out before
closing. It is the cousin of the abandoned cart, with one difference that matters
— the one abandoning is not the person, it is the machine, on finding something
that made you stop fitting.

**The tools.** Completeness of product data, which is literally what the feed
started asking for — substitutes, compatible accessories, answers to common
questions. Correct price and stock in the feed, because an agent that finds a
mismatch swaps. Response time at the capability address, because an agent that
waits too long moves on.

### Third stage: decision in marketing, adoption in BLG

**The classic marketing funnel ends at the purchase.** That gap is what the
pirate funnel came to fill decades later — acquisition, activation, retention,
revenue and referral, presented by [Dave
McClure](https://www.linkedin.com/in/davemcclure) in 2007 — by adding what
happens after the money changes hands.

**In BLG the third stage is exactly that.** Adoption is not the purchase: it is
the purchase having become a premise. There is data in your format, there is a
stored payment method, there are people buying without reopening the comparison.

**What gets measured.** The share of repurchase that does **not** go back through
the consideration set. In practice: of the orders from the last ninety days, how
many came from somebody who compared nothing.

**The tools.** The memory layer. Subscription, stored payment, one-click
repurchase. It is the same force that jobs-to-be-done theory calls habit — Bob
Moesta describes it as the strongest of the forces opposing any switch.

### The middle stage shrinks until it disappears

> **In commerce the middle stage is short, and it shrinks until it disappears as
> delegation rises.**

A one-click repurchase goes from candidacy straight to adoption. There is no
interval in which you are chosen and can still be removed at no cost. The window
a competitor could enter through never opens.

**Candidacy is even more decisive here than in software**, because almost nothing
dies during construction. The verb describing the stage changes too. In software
you work to **be found**. In commerce you work to **be admitted**. Nobody
operates a gate on the installation of libraries; in commerce the gate exists,
has an owner, and has an admissions process.

![The three funnel stages in commerce with what gets measured at each: candidacy by presence in the answer, construction by the substitution rate after the decision closes, adoption by repurchase that never reopens the comparison — and the middle stage shrinking as delegation rises](../../visuais/arco2-comercio-agentico/ca-funil-en.png)

## The shop stops being a destination and becomes a data source

Traffic has already changed origin, with instrumented measurement. Adobe tracks
what reaches American shops from artificial intelligence tools, over a base of
more than a trillion visits. In May 2026 that traffic grew **138% in a year**,
accumulating **1,324% since October 2024**, when they started measuring. Whoever
arrives that way converts **54% better** than the rest, spends **53% more time**
on the site and sees **23% more pages** ([Adobe Analytics, via Digital Commerce
360, 17 June
2026](https://www.digitalcommerce360.com/2026/06/17/adobe-ai-referred-traffic-to-retail-sites-doubles-in-a-year/)).

The same measurement shows the other side. Adobe scores how much of a page's
content is legible to a language model, and the result by category lands between
**47% in furniture and home decor and 63% in cosmetics**, with electronics at 56%
and apparel at 51%. Even in the sectors doing best, **30% to 40% of the content
on the highest-value pages is not captured**.

Close to half of what a shop writes about its own products never reaches the
machine that now decides whether that shop shows up in the answer.

### What stays public and what doesn't

Part of what happens in a purchase **is** public and does train the model.
Product reviews, ratings, comment sections, third-party comparisons, videos from
people who used it — all of that is written, indexed and available.

What does not stay public is something else: **the record of the choice.** Which
product the agent put in the answer, what it discarded before assembling the
list, whether there was a return, whether there was a dispute, whether the person
bought again. That record stays with whoever operated the agent.

The difference from software changes the whole strategy. There the artefact that
gets built **is** the record of the choice: the code that uses your library is
published, and anyone reading that repository learns that you were chosen. In
commerce what is public is opinion about the product; the choice itself leaves no
trace outside the party that operated it.

[Alexandre Sato](https://www.linkedin.com/in/alexandresato/) pointed me at the
wider movement behind this. As model fine-tuning and retrieval over proprietary
collections spread, what the machine knows starts concentrating inside whoever
operates the platform. The same artificial intelligence your competitor uses, or
a model that learned how your operation works and that only you can reach — the
second is the one with defensible commercial value.

For the retailer, the practical consequence fits in a sentence: **your shop
stopped being a destination and became a data source.** Before, the person came
in and you watched — what they searched for, where they stopped, what they
abandoned. Now the agent watches, and you receive a request. The sale can go on
happening. The watching, not.

![How much of a shop's content is legible to the machine, by category: 63% in cosmetics, 56% in electronics, 51% in sporting goods and apparel, 48% in grocery and 47% in furniture and home decor — with 30% to 40% of the content on the highest-value pages not captured even in the best sectors](../../visuais/arco2-comercio-agentico/ca-legibilidade-en.png)

## Who sits where in this story

### The consumer isn't in the funnel, they receive its output

The one walking the funnel is whoever **builds**: the payments company, the
platform, the retailer who needs to be chosen. Those pick vendors, and they are
what the theory is about. The consumer picks no vendor at all. They receive a
finished answer.

What they receive, though, depends entirely on the quality of that funnel. If
half of what is written about a category is not legible to the machine, the
recommendation reaching them was assembled from partial information — and nothing
on the screen says so. They didn't choose the sources, don't know which ones they
were, and have no way to check. They receive the output of a process they can't
see.

They do set a hard constraint for whoever is building. Declared willingness to
let artificial intelligence **make** the purchase decision **tops out at 11%**, in
the lowest-risk categories. Willingness to let the machine merely **narrow** the
options reaches **31%** for cleaning and household products and **28%** for
personal electronics. That is 322 consumers in the United States, fielded in
January 2026, in a Gartner survey that publishes neither sampling method nor
margin of error — I use the order of magnitude, not the decimals. It is
self-report, which on the subject of artificial intelligence tends to diverge
from measured behaviour.

> **Anyone building for full autonomy is building for 11% of the market.**

The force holding this back has a name. Bob Moesta, describing what makes
somebody switch solutions, separates the pull of the new from the **anxiety** it
provokes. In the old comparison between a drill and double-sided tape competing
for the same job of hanging a picture, you can try the tape and give up. In a
delegated purchase you cannot: **the transaction is the commitment.** You find out
whether it was any good after you have already paid.

![The ceiling on consumer delegation: 11% accept AI making the purchase decision, against 31% who accept it merely narrowing the options for cleaning and household products and 28% for personal electronics](../../visuais/arco2-comercio-agentico/ca-teto-en.png)

### The merchant is in it, without writing a line of code

The retailer doesn't build software. They are still, literally, a product being
selected by a machine. Either they fit the way the agent discovers, understands
and transacts, or they are left out.

I grew up hearing Ayrton Senna say that second place is nothing more than the
first of the losers. In agentic commerce that is the rule, with winner-takes-all
logic.

With one caveat that matters. A conversation with an agent is not a straight line.
Somebody asks for burgers for the family, the agent brings options, the person
reformulates, and the order ends up as a pizza that pleases everyone and costs
less. At every reformulation the set is reassembled. Being left out of the first
answer is not a sentence — being left out of all of them is.

That changes what you measure. Showing up for *"best burger near me"* is not
enough. You have to stay reachable when the question becomes *"what pleases four
people with different tastes for up to a hundred and twenty reais"*, which is a
question about fit and price, not about category.

There is an organisational reason for the fitting to take longer than the urgency
suggests. In an August 2026 report on why agent adoption stalls inside companies,
McKinsey describes the fear that freezes behaviour most, in the words of the
people who feel it: if the agent gives me the wrong answer and I act on it, the
mistake is still mine. Responsibility without control.

That study looks at agent use inside organisations, not at commerce. Carrying its
conclusion to a retailer's desk is conjecture on my part. Informed guess, but
conjecture: the decision to expose catalogue and checkout to an external agent
has exactly the same shape — somebody signs their name under an answer the
machine is going to give on its own.

### The door: you may not be able to refuse the agent

The largest retailer in the world tried. Amazon sued Perplexity over a browser
agent that bought on behalf of the people using it, and obtained an injunction
blocking access on 10 March 2026.

**On 4 August 2026 the Ninth Circuit reversed.** The reasoning: under the
American statute covering unauthorised access to computer systems, the party who
accessed Amazon's computers was **the user**, with the agent's help. The tool
doesn't access; the person accesses using the tool.

The criterion the court used is not the one you would imagine. **It is not how
autonomous the agent is, it is where the packets travel.** The court noted that
communications were routed through the user's own computer and that the agent
company was not talking directly to Amazon's servers, distinguishing an earlier
case in which the defendant's systems spoke straight to the platform.

The agent running in the person's browser, which looks more invasive, is the one
that ends up protected. **The server-hosted agent, which is the design of nearly
every agentic commerce platform, falls on the other side of the line.** Where your
agent runs stopped being only an architecture decision.

For the retailer the reading is direct: if refusing the agent at the door is not a
guaranteed right, **preparing for it stops being a strategic option and becomes a
condition you are subject to.**

![The Ninth Circuit's criterion is not autonomy, it is architecture: an agent running in the user's browser is that user's instrument; a hosted agent talking straight to the shop's server can be treated as an actor in its own right](../../visuais/arco2-comercio-agentico/ca-porta-en.png)

## What to do — and why no single team solves this alone

### The boundary between marketing and engineering dissolved

> **When the reader is a machine, the engineering artefact and the marketing
> piece are the same object.**

The product description is sales material, because it is what the buyer reads. The
buyer is a machine. The capability file at `/.well-known/ucp` is the shop window.
The catalogue attribute, that dull field somebody fills in without enthusiasm, is
the commercial argument. These are not similar things: they are the same thing,
seen from two departments that don't talk to each other.

The 47% to 63% legibility by category is the bill for that mismatch. Nobody wrote
a bad page on purpose. The pages were written for a person to look at, by a team
that didn't know the next reader would be a program.

One number shows where the money is going. The August 2026 McKinsey research
describes the pattern of transformations that work as **1:3:5** — for every dollar
invested in agent technology, three in process redesign and five in enablement and
adoption. Most companies **invert that formula completely**, putting nearly
everything into the technology and treating the rest as an implementation detail.
If your investment is inverted, the adoption lag is yours.

![The 1:3:5 pattern of transformations that work — one in technology, three in process redesign, five in enablement — against the inverted distribution most companies practise](../../visuais/arco2-comercio-agentico/ca-135-en.png)

### For engineering

**Publish a canonical profile at a predictable path.** If you are a merchant, that
now has a literal address. The principle holds for any vendor: one place, legible
without context, saying what you do and what you accept.

**Write the data the machine asks for, not the data the page needs.** Substitutes,
compatible accessories, answers to common questions.

**Measure your own legibility.** The calculation is simple and nobody does it:
take the twenty pages that sell most, list the facts a buyer needs in order to
decide — dimensions, compatibility, delivery time, returns policy, what's in the
box — and then ask a model to answer each of those facts using that page alone.
Whatever it can't answer is on the page in a way the machine can't reach: inside
an image, hidden behind a tab that only opens on click, or implied by sales copy
instead of stated. The public market reference sits between 47% and 63% by
category. Finding out where you land in that range is an afternoon's work; fixing
what turns up is a quarter's.

**Decide deliberately where the agent runs.** Browser or server changed in nature
after August 2026, and the answer changes who answers for the access.

**Instrument the invisible.** Record which decisions came from an agent and which
came from a person. Nobody publishes that number today. Whoever holds it
internally can see their own funnel while the market argues from impressions.

**Preserve the path back.** All the tolerance for delegated payment rests on being
able to undo. Where undoing is hard, delegation finds a lower ceiling.

### For growth

**Measure presence in the answer, not only traffic.** Thirty questions from your
category, repeated, recorded. It is the only way I know to see the stage where the
loss appears in no report at all.

**Test the reformulated question, not only the obvious one.** If the customer can
arrive through *"what pleases four people for up to a hundred and twenty reais"*,
that is the query that has to find you.

**Treat catalogue and feed as top of funnel**, because in commerce candidacy is
admission, not discovery. AEO and GEO still hold; the feed is the part you
control.

**Recover the watching you lost.** If the person no longer comes into the shop,
the signals you used to read in their browsing have dried up. What is left comes
from the conversation the agent had, and negotiating access to that is a
commercial matter, not a technical one.

**Design for the 11% ceiling.** The product that wins is the one that makes
delegation feel reversible, not the one that automates most.

### For both, together

**The product description has a deadline and a growth owner**, because it is sales
material. Treating it as a data-entry chore somebody does when there's time left
over is leaving the shop window shut.

**The target is being written into the customer's own guidelines.** The
best-organised companies already don't let the agent choose alone: they write
specification documents that steer the machine within the general lines of the
house. Being named in that document is a more durable position than being in the
training data, which refreshes, and a cheaper one than switching cost, which
requires the code to already exist. It is won on technical credibility and closed
commercially, which means neither team gets there alone.

**Somebody has to own the answer to "who answers when the agent gets it wrong".**
That is not a compliance question. It is the question stalling adoption in the
companies that already bought the technology.

## What I don't know

**Does decomposition widen the set or fragment it?** New tools break a problem
into pieces and send each piece to a specialised model. That could create more
openings — more subproblems, more chances to be considered — or the opposite,
openings with fewer plausible candidates, where the specialist wins for lack of a
competitor. Both readings hold up.

**I found no Brazilian measurement of the delegation ceiling.** The 11% figure is
American, and there is reason to suspect it differs here, not because Brazilians
trust more, but because delegation arrives through a channel they already use
every day. If anybody has that number, it is the most valuable one this text could
have cited.

**Nobody publishes how many products were discarded before the short list.** The
stage where most of the competition dies is the only one with no public
instrument. Whoever operates the agent holds that log.

**This series still hasn't proved its own central claim.** I hold that the machine
is taking part in vendor choice at a scale nobody is measuring. There are people
who can measure it and don't publish. Until that number exists, the burden sits
with whoever makes the claim, and the one making it is me.

If you work somewhere that can measure it, that is the conversation I most want to
have after this text.

---

**Builder-Led Growth series**, by Matheus Ramos. Second arc:

- [Arc 2, part 0: From PLG to BLG — what still holds when the one choosing is a pair](arc2-00-from-plg-to-blg.md)
- [Arc 2, part 1: The Builder-Led Growth funnel — the three stages and what makes a product move faster](arc2-01-the-funnel-and-the-delegation-axis.md)
- Agentic commerce and Builder-Led Growth — what changes for growth and engineering (this piece)

The first arc, for anyone who wants the full route:

- [Part 1 — When the machine is also your customer](01-when-the-machine-is-the-customer.md)
- [Part 2 — The decision, the price and what to measure](02-decision-price-and-measurement.md)
- [Part 3 — The tax the machine charges and the human never sees](03-machine-legibility.md)
- [Part 4 — How many times the agent has to call a human](04-operational-accessibility.md)
- [Part 5 — The well everyone drinks from](05-community-and-validation-signal.md)
- [Part 6 — The machine is press and reader at once](06-public-relations.md)
- [Part 7 — What makes an agent trust you, and why its competence is the problem](07-trust-and-safety.md)
