<!--
Arc 2, part 1 of the Builder-Led Growth series, by Matheus Ramos.
CANONICAL VERSION (English).
Portuguese counterpart: ../pt-br/arco2-01-o-funil-e-o-eixo-da-delegacao.md
Text frozen. No LinkedIn date set yet.
Generated from the private working repository. Do not edit here.
-->

# It isn't who decides. It's how much was delegated

*Second piece of the second arc of this series. It doesn't require the earlier
ones. The opening piece established that the one choosing is a pair, a person and
a machine. This one is about the funnel: what it is, what survives of it when the
decider is a pair, and what happens at each stage as more gets delegated.*

---

## The database I didn't choose

I ask an AI build platform to put an application together. I describe what it has
to do: store people's details, let those people sign in with a password, and accept
file uploads.

It builds it. It works.

Somewhere inside that there is a database, an authentication service and a storage
service. I chose none of the three. I saw no list, compared no prices, read no
documentation. Three database names would have come to mind if anyone had asked —
and nobody asked.

What interests me here isn't that I ended up with the wrong database. What turned
up works. What interests me is that **I held a veto and did not exercise it**, and
not out of inattention: exercising a veto requires knowing there is something to
veto.

And this isn't an impression of mine. The infrastructure vendor published the
mechanism in as many words, on 29 September 2025: *"every AI builder using Lovable
is already using Supabase, whether or not they realize it"*
([Supabase](https://supabase.com/blog/lovable-cloud-launch)). That is a statement
from a company with a commercial interest in emphasising its own penetration, and
it is worth reading with that in mind. But whoever wrote it sits on the side that
can see: it is the vendor, not the user, who can count decisions the decider never
saw.

## Three situations that are not the same thing

Before talking about funnels I need to separate three things — and separating them
is half the work of this piece, because treating them as one produces confusion
immediately.

**The first: governed development.** The company keeps a registry of approved
tools. When the team needs a messaging service, the set it chooses from arrives
already narrowed, by a rule written earlier and by somebody who isn't in that room.
The choice within that set is human, documented, and there is someone to ask why.

**The second: the shortlist.** Nothing was narrowed in advance. The person asks,
the machine gathers three or four names with a reason for each, and the person
picks. They compare, apply their own criteria, and decide.

**The third: the removed decision.** There was no list, no comparison and no
choice — there was a result. That is my database.

All three happen in the same market, sometimes in the same company, sometimes in
the same week. And the size of each isn't guesswork: **only 27% of organisations
enforce strict governance over AI tool adoption, and 68% have no visibility into
which AI tools their developers use**
([Northflank](https://northflank.com/blog/enterprise-ai-coding-agent-deployment)).
That is vendor material, not an independent survey, and it is worth knowing. What
it says is that the first situation is real and in the minority, and that in two
thirds of cases nobody even knows which of the other two is happening.

### What varies across the three

Not the problem. Not the type of product. Not the size of the company.

**It is how much of the decision was delegated** — and delegation is a degree, with
two ends that need names:

> **AI-assisted decision: the person chooses among options the machine assembled.
> Delegated decision: the person accepts or rejects a result the machine has
> already built.**

Governed development sits at the low-delegation end, with a wrinkle: whoever
removed the delegation wasn't the person in that room, it was a rule written
earlier. The shortlist sits in the middle. The removed decision sits at the other
end.

I looked for an existing name before coining one. **Conversational commerce** was
coined by [Chris Messina](https://www.linkedin.com/in/factoryjoe/) in 2015 and
describes buying through a messaging app. **Zero-click search** was quantified at
scale by [Rand Fishkin](https://www.linkedin.com/in/randfishkin/) from 13 August
2019 onward and describes the absence of the click. **Generative engine
optimisation** was coined on 16 November 2023
([arXiv 2311.09735](https://arxiv.org/abs/2311.09735)) and names what publishers
do. And the **Agentic Commerce Protocol**, from Stripe and OpenAI in September 2025
([openai.com](https://openai.com/index/buy-it-in-chatgpt/)), names the far end where
the agent buys on its own. None names the middle case, which is the machine
mediating with the human decision intact. If someone coined an equivalent before
me, the credit is theirs and I will swap mine for it.

### Where I was wrong

I started this arc with a position: saying the machine chooses is false, because
the human chooses just as much. I kept investigating, and it held about halfway.

In the first two situations it holds entirely. There is a choice in view, and a
person makes it.

In the third it does not. There was no delegation — there was absence. I didn't
hand a decision to the machine; the decision simply never passed through me. Saying
I chose as much as it did would be false.

## One funnel, and it belongs to the pair

Now the main subject. And it starts with a question it took me two attempts to
answer: if the decision belongs to a pair, are there two funnels — one for the
machine, one for the human — or just one?

**Two funnels don't close**, and the reason is easy to check. Two funnels require a
join point: you have to say where the output of one becomes the input of the other.
Under governance, the human comes after. In the shortlist, the two interleave. In
the removed decision, the human funnel never runs. Three different topologies for
the same phenomenon, and a model that needs one drawing per case isn't describing
anything.

**One funnel for the pair does close**, and it is what this piece uses. It has
three stages, always the same, and what changes across the three situations is
**who satisfies each one**.

### What a funnel is, and what survives of it here

A funnel is a simple shape: a lot goes in at the top, a little comes out at the
bottom, and the set shrinks at every stage. It doesn't explain why anyone dropped
out. It tells you **where** to look.

An example outside software makes that clear. A shop gets a thousand visitors a
month, a hundred try something on, and twenty buy. The funnel doesn't say whether
the problem is the price, the fitting room or the staff. It says the bigger drop
sits between walking in and trying on, and that is where you investigate first. An
instrument of location, not of diagnosis.

The shape comes from early twentieth-century advertising, and its parentage is
disputed: the stages are usually credited to Elias St. Elmo Lewis in 1898, part of
the literature attributes the full formulation to Arthur Frederick Sheldon, and the
AIDA acronym only appears in 1921, with C. P. Russell ([E. St. Elmo
Lewis](https://en.wikipedia.org/wiki/E._St._Elmo_Lewis)).

Here I need to be honest about a limit, because it is mine and I carried it for
weeks without resolving it. When I wrote about the decision, the price and what to
measure, I proposed three stages and used the word funnel. **The decomposition into
three still stands. The funnel metaphor doesn't survive whole**, and four of its
presuppositions break on this ground:

A funnel presupposes **a cohort that advances once**. Here the decision repeats
every working session, millions of times a day, independently.

A funnel presupposes **permanent loss**. Losing one decision removes nobody from
anything: you are a candidate again a minute later.

A funnel presupposes **exclusive stages**. The same product is in candidacy for one
agent and in adoption for another, at the same time.

A funnel presupposes **order**. Being inside a scaffold — a ready-made project
skeleton that already ships with a chosen set of tools — puts the product in with
no recommendation happening at all. The stage is skipped.

What survives is more precise and more useful:

> **The three stages are not stages of a journey. They are necessary conditions of
> a decision.** You need all three in every decision, and failing any one zeroes
> that decision — and only that one.

Within a decision, the funnel shape works: the set only shrinks, every stage is a
sieve, and elimination is irreversible. The moment the database went in, the code
started calling it — there is a connection string, there are tables shaped for it,
there is a library installed. The competitor is not "revisited later". It is out,
and it went out in the same session it went in.

Between decisions the shape is different: what exists is a loop. The choice becomes
public code, a forum answer, a tutorial, training data, and that feeds the next
decision, made by another pair, at another company, months later.

> **Funnel within the decision, loop between decisions.**

Worth recording why I don't use the word *flywheel* here, which would be the
expected one. A wheel that loses energy stops turning, it does not turn backwards —
and what accumulates between decisions also evaporates, which is what I described
when treating community as a water table, rising with what is deposited and falling
with what is drawn.

![The three funnel conditions against the three delegation regimes: governed development, shortlist and removed decision, and who satisfies each condition in each one](../../visuais/arco2-parte-01/a2p1-stages-en.png)

## Condition 1 — Candidacy: being in the set that gets chosen from

The first condition decides nothing. It defines who is entitled to be considered.

Picture a team that needs to send transactional email — the "confirm your account"
message that goes out automatically. Dozens of services do that. In practice the
team will consider three or four. The others didn't lose the comparison: they never
entered it.

**It is the most decisive condition and the only one where the loss is invisible.**
If your product doesn't make the set, there is no abandoned cart, no half-finished
signup, no complaint. The project went ahead with something else and nobody
recorded a thing.

**Under governed development**, what satisfies this condition is a rule written
earlier. The approved-tools registry narrows the set before the machine even looks,
and failing compliance isn't being a weak competitor — it is being absent. I treat
that gate in detail in one of the pieces that follow.

**In the shortlist**, what satisfies it is the machine, and it shows its work. A
list that is read is auditable: anyone who knows the market notices when an expected
name is missing, and asks.

**In the removed decision**, what satisfies it is the machine with nothing on
display. Nobody notices any absence, because there is nothing to notice.

One mechanism helps explain why the set closes so early in the third case. In one
measured configuration, **57.8% of repetitions did not trigger a web search**
(Schulte, Bleeker and Kaufmann, [arXiv
2604.07585](https://arxiv.org/pdf/2604.07585), 10 April 2026 — the figure comes via
a citation in a critical review, not from the primary table). Without a search, the
candidate set comes entirely from what the model already carries. There is no
curation moment to observe, because the curation happened before the session began.

### How much gets delegated here, and which of the three we are measuring

There are four useful public measurements, and it matters to say precisely what
they measure: **the second situation, the shortlist.** They do not measure the
first, which is internal to the company, and they cannot measure the third, for the
reason this piece has already set out — nobody answers about a choice never put in
front of them.

Consumer willingness to let AI **make** the purchase decision **tops out at 11%** —
the wording is the survey's own, *"topped out at 11%"*, and the ceiling occurs in
the lowest-stakes categories, such as personal care. Willingness to let AI
**narrow** the options reaches **31%** in cleaning and household products
([Gartner, 27 May
2026](https://www.gartner.com/en/newsroom/press-releases/2026-05-27-gartner-survey-finds-consumers-want-ai-shopping-help-but-not-ai-purchase-decisions)).
That is 322 US consumers, fielded in January 2026, and the release publishes no
sampling frame or margin of error — I use the pattern, not the decimals.

In corporate software buying, **69% say they prefer to validate** AI-generated
conclusions with a human sales rep ([Gartner, 20 May
2026](https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights),
645 buyers). The release's word is *prefer*: stated preference, not measured
behaviour.

And **86%** of those who researched a product with AI checked the recommendation
against another source before buying. Add the fourth population the opening piece of
this arc already brought in: 98% of consumers verify before buying.

Four measurements, four cuts, the same shape: **inside the shortlist, what gets
delegated is the assembling of the set, not the choice.** The machine assembles and
leaves before the decision. One analyst house described it as narrowing the field
before human evaluation begins ([IDC, 28 January
2026](https://www.idc.com/resource-center/blog/ai-mediated-buying-journeys-how-buyers-decide-whos-worth-their-time/)).

![The shortlist regime in four measurements: an 11% ceiling for letting AI decide the purchase, 31% for letting it narrow, 86% who check against another source, and 69% of B2B buyers who prefer to validate with a person](../../visuais/arco2-parte-01/a2p1-axis-en.png)

One caveat applies to all four: they are self-reported, and self-reporting about
work with AI has a documented problem. In a randomised experiment with 16
experienced developers and 246 real tasks from their own repositories, people were
**19% slower** with the tool. Beforehand they expected to be 24% faster. After being
measured as slower, they still estimated they had been 20% faster ([METR, 10 July
2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)).
That is **twenty points between the measured and the believed**, and from the inside
the gap is invisible. The authors are explicit that the result does not extend
beyond that group, and in the 24 February 2026 update, with 57 participants, the
confidence intervals cross zero
([METR](https://metr.org/blog/2026-02-24-uplift-update/)).

I use the four for the shape they share, not for any one of their values.

## Condition 2 — Recommendation: being the one chosen within the set

The second condition is what everyone pictures when they think about a decision.
Options on the table, criteria, one winner.

**Under governed development**, what satisfies it is a human with stated criteria,
and the choice is recorded somewhere. There is someone to ask why, months later.

**In the shortlist**, what satisfies it is also a human. They see the alternatives
side by side, weigh price, maturity and who else uses it, and pick. They may pick
for the wrong reason, but they picked.

**In the removed decision**, what satisfies it is the machine. There is no
comparison: there is a result.

And when there is no comparison, the choice doesn't spread across the available
options — it **converges**. In a study across eight models, popular libraries appear
unnecessarily in up to **48%** of cases, Python is chosen in **58%** including where
it is suboptimal, and Rust is not used once in high-performance scenarios. The
authors' conclusion, in their words: *"LLMs may prioritise familiarity and popularity
over suitability"* ([Twist, Zhang, Harman, Syme, Noppen, Yannakoudakis and Nauck,
Findings of ACL 2026, arXiv 2503.17181](https://arxiv.org/abs/2503.17181)).

Translated for anyone selling: **whoever is already the category default gains from
delegation. Whoever is fighting for second place loses twice** — not chosen, and not
compared either, which is how you improve in a contest. That last reading is mine
and untested.

### Why the third situation shows up in no survey

I suspected delegation was growing among people who build with AI. Before searching,
I wrote down what would knock the suspicion over, because research that only returns
what you already believed has a problem in the question. Three criteria: a proportion
flat over time, growth in execution only, or the heavily-delegating population
shrinking.

Two of the three happened. The suspicion fell.

The one public series that comes close to measuring whole-task handoff does not
climb: 27.8% in the December 2024 to January 2025 field, 27% in the next, 39% in
August 2025, 32% in November, and then unpublished in the two editions after that
([Anthropic Economic
Index](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)).
I don't treat that as a series: the 15 January 2026 edition declares a classifier
change midway, and the measurement is a vendor's own, about its own product.

Scrutiny, meanwhile, **rises** with experience. The interruption rate climbs from 5%
to 9% of turns among high-tenure users ([Anthropic, 24 March
2026](https://www.anthropic.com/research/economic-index-march-2026-report)). And
agents are conservative exactly where the vendor decision lives: across 26,760
agent-authored pull requests, **only 1.3% introduce a new dependency**, and those
that import a library are merged at rates 6% to 11% lower ([Twist and Zhang, King's
College London, arXiv 2512.11589](https://arxiv.org/html/2512.11589)). When a library
is at stake, the human looks harder, not less.

There is even counter-evidence from the person who named the phenomenon. [Andrej
Karpathy](https://www.linkedin.com/in/andrej-karpathy-9a650716/) coined *vibe coding*
— programming by describing what you want and accepting what the machine writes,
without reading the diffs — on 2 February 2025. On 4 February 2026 he retired the
term and proposed *agentic engineering* instead, writing that programming through
agents is becoming the professional's default flow *"except with more oversight and
scrutiny"* ([dated record by Simon
Willison](https://simonwillison.net/2026/Feb/26/andrej-karpathy/)).

All of that describes the first and second situations. None of it captures the third.

On 4 June 2026, [Paul Copplestone](https://www.linkedin.com/in/paulcopplestone/),
co-founder and chief executive of Supabase, stated: *"agents are now deploying the
majority of databases on our platform"*, over a declared base of more than 250,000
customers ([official
release](https://www.prnewswire.com/news-releases/supabase-raises-500m-at-10-5b-to-accelerate-lead-in-agentic-infrastructure-302791787.html)).
Neon shows a neighbouring figure in a Databricks report of 27 January 2026: agents
create **80% of all databases and 97% of branches**
([Databricks](https://www.databricks.com/blog/enterprise-ai-agent-trends-top-use-cases-governance-evaluations-and-more)).

Choosing a database is an architecture and a vendor decision. It is not execution.

And the reason it shows up in no opinion survey is structural, not a matter of
sampling:

> **The decision was not delegated. It was removed from view.**

Nobody answers "who chose the database?" about a choice never put in front of them.
The other databases that would have come to mind never dropped out at any point.
They never entered. Which is why the only party positioned to count those decisions
is whoever hosts the decision — and that is where both figures came from.

![Removal from view: of the three options that existed, two were not rejected but never presented to anyone](../../visuais/arco2-parte-01/a2p1-removal-en.png)

## Condition 3 — Adoption: surviving integration and use

The third condition is where most analyses stop looking, and it is where the money
goes.

Being chosen is not staying. The integration can fail, the cost can surprise, the
behaviour can differ from what the documentation promised.

**Under governed development**, the integration is watched by whoever approved it.
Somebody's name is on the decision, and that changes what happens when something
goes wrong.

**In the shortlist**, whoever integrates knows what they chose and why, so they have
patience for what goes wrong. The choice was theirs.

**In the removed decision**, you integrate what turned up. And the first time anyone
looks at it closely is usually when it breaks. A routine example: the transactional
email service went in without discussion, worked for weeks, and one day the messages
start landing in spam folders. Somebody opens the code to find out why, discovers a
service they never chose, and the first question isn't technical — it's "why are we
using this?". The switch that follows passes through no criterion the machine ever
evaluated.

### The veto changes in kind

Here is the change with the most practical consequence in the whole piece.

In the first two situations, the veto is a choice among visible alternatives. The
person sees three, prefers one, and the other two go on existing should the first
disappoint.

In the third, there are no alternatives on screen. There is a finished result.

> **The veto stops being a choice among alternatives and becomes acceptance or
> rejection of an already-built result** — cheaper to exercise, and more expensive to
> reverse.

Cheaper because accepting requires evaluating nothing: it requires that nothing look
wrong. That is what I did with the database. More expensive to reverse because, the
moment the person accepts, the thing is already written into the code, with
configuration, environment variables and tables around it.

For anyone building a product the consequence is direct: **you don't control the
comparison. You control what the person finds already done when they finally look.**

![The veto in two states: with the decision in view it is a choice among visible alternatives, and with the decision removed it is accepting or rejecting an already-built result, cheaper to exercise and more expensive to reverse](../../visuais/arco2-parte-01/a2p1-veto-en.png)

### And one asymmetry running through all three conditions

The deeper into the cascade, the more visible the loss — and the less can be done
about it.

If the product is discarded at adoption there is a trace: someone switched, someone
complained, someone opened an issue. If it never enters candidacy there is no trace
at all. And candidacy is precisely where something could still have been done.

I know of no measurement of that asymmetry, and the reading is mine. It is the reason
the first condition deserves more investment than it usually gets.

## What crosses from one decision to the next

I need to correct a sentence of mine before closing.

Writing about operational accessibility, I said the machine decides afresh every
session and accumulates nothing between one and the next — that every session starts
from zero. **The part about the machine is true. The part about the pair is not**, and
it is the pair that decides. I kept investigating and saw it holds for one layer only,
and that is the wrong layer for anyone trying to understand this subject.

There are three layers, and I had been working with two.

The **session** is where elimination happens. Ephemeral, ownerless, and nobody
strengthens their position in it.

The **public corpus** — the material that trains the next model — accumulates slowly,
has no owner, and erodes.

The middle one is what was missing, and it is the only one with an owner: the
**project's memory**. Specifications, decision records, instruction files for the
agent. Whoever builds controls that layer entirely, and it is read at the start of
every session.

Out of it comes a habit mechanism I did not have. Write "we use this database, and
here is why" into the project's memory file, and **that decision gets re-read every
session afterwards. It stops being a decision and becomes a premise.** It is the
cheapest habit to install and the hardest to dislodge: it needs neither model training
nor code written, it needs one line in a file.

Look at what that does to the distinction between the three situations: **the
project's memory is the instrument that moves a decision from the third to the
first.** Writing the choice down reintroduces the rule written earlier, only inside
the project instead of inside the company.

For anyone selling, it opens a position this series had not yet named: **being written
into the customer's memory artefact is a more durable position than being in the
training data, which refreshes, and a cheaper one than switching cost, which needs the
code to already exist.** The ethical line is clear: you write the documentation, the
customer decides whether to reference it.

![Funnel within the decision and loop between decisions, with the three layers of what crosses over: the ownerless session, the project memory controlled by whoever builds, and the public corpus that accumulates slowly and erodes](../../visuais/arco2-parte-01/a2p1-funnel-and-layers-en.png)

## What holds

There is a funnel, it belongs to the pair, and it describes a decision rather than a
journey. The three stages are necessary conditions in cascade: be in the set, be
chosen within it, survive use. Failing any one zeroes that decision, and only that
one — because the next decision starts over.

The three conditions don't change. Who satisfies them does. Under governed
development a rule written earlier narrows the set and a human chooses within it. In
the shortlist the machine assembles and the human chooses. In the removed decision the
machine does both, and the person meets the result.

The first condition is the most decisive and the only one with no trace of loss. And
the veto, still human in all three, changes in kind in the third: it becomes
acceptance of something finished, cheaper to give and more expensive to undo.

The pieces that follow walk down condition by condition: two on candidacy, one on how
you get into the set and another on how you get cut from it before any preference
forms; one on what decides the choice and which of those tactics decay; one on
adoption and the veto; and a closing one on where your product fits and who inside the
company looks after it.

I'll close with what I don't know.

Nobody publishes how many vendor decisions the agent made on its own. I looked through
developer surveys, platform reports and open-ended phrasings. None asks builders who
chose the library, the service or the database last time — the person or the agent.

And it is not a failure of searching. One of the platforms built the taxonomy that
would answer it, separating work initiated by code, by one agent and by multiple
agents, in its own metrics interface, since 29 May 2026. The aggregate is not
published.

**Someone can measure this, and does not publish it.** If you work somewhere like that,
that number is the most important thing this arc could cite — and the conversation I
would most like to have after this piece.

---

**Builder-Led Growth series**, by Matheus Ramos. Second arc:

- [Arc 2, part 0 — From PLG to BLG: what still holds when the one choosing is a pair](arc2-00-from-plg-to-blg.md)
- Arc 2, part 1 — It isn't who decides. It's how much was delegated (this text)

The first arc, for anyone who wants the full route:

- [Part 1 — When the machine is also your customer](01-when-the-machine-is-the-customer.md)
- [Part 2 — The decision, the price and what to measure](02-decision-price-and-measurement.md)
- [Part 3 — The tax the machine charges and the human never sees](03-machine-legibility.md)
- [Part 4 — How many times the agent has to call a human](04-operational-accessibility.md)
- [Part 5 — The well everyone drinks from](05-community-and-validation-signal.md)
- [Part 6 — The machine is press and reader at once](06-public-relations.md)
- [Part 7 — What makes an agent trust you, and why its competence is the problem](07-trust-and-safety.md)
