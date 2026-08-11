<!--
Arc 2, part 1 of the Builder-Led Growth series, by Matheus Ramos.
CANONICAL VERSION (English).
Portuguese counterpart: ../pt-br/arco2-01-o-funil-e-o-eixo-da-delegacao.md
Text frozen. No LinkedIn date set yet.
Generated from the private working repository. Do not edit here.
-->

# It isn't who decides. It's how much was delegated

*Second piece of the second arc of this series. It doesn't require the earlier
ones. The opening piece established that the one choosing is a pair, a
person and a machine. This one is about the funnel — what it is, why it survives
when the machine is the selector, and what happens at each stage as more gets
delegated.*

---

## The database I didn't choose

I ask an AI build platform to put an application together. I describe what it has
to do: store people's details, let those people sign in with a password, and
accept file uploads.

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

So the practical question, and it organises the whole piece: **where along the way
was that choice actually made?**

## What I thought, and where it didn't hold

I started this arc with a position, and it came from a correction I made to an
earlier draft. Saying the machine chooses is false, because the human chooses just
as much. Outside this theory that is plain — someone picking bread at a bakery has
delegated nothing. And inside it too: deciding which problem to attack, which
progress to chase, and then asking the machine for help, is a human decision from
end to end.

I kept investigating, and the position held about halfway.

**Where it holds:** wherever a choice is in view, the human still chooses. Every
survey I found confirms that, and some of them appear further down.

**Where it doesn't:** when the choice never comes into existence for the person.
In the database case there was no delegation — there was absence. I didn't hand a
decision to the machine; the decision simply never passed through me. Saying I
chose as much as it did would be false.

Which is why the right framing isn't about who decides, but about **how much was
delegated**. Delegation is a degree, and the degree has two ends that need names:

> **AI-assisted decision: the person chooses among options the machine assembled.
> Delegated decision: the person accepts or rejects a result the machine has
> already built.**

I looked for an existing name before coining one. **Conversational commerce** was
coined by [Chris Messina](https://www.linkedin.com/in/factoryjoe/) in 2015 and
describes buying through a messaging app. **Zero-click search** was quantified at
scale by [Rand Fishkin](https://www.linkedin.com/in/randfishkin/) from 13 August
2019 onward and describes the absence of the click. **Generative engine
optimisation** was coined on 16 November 2023
([arXiv 2311.09735](https://arxiv.org/abs/2311.09735)) and names what publishers
do. And the **Agentic Commerce Protocol**, from Stripe and OpenAI in September 2025
([openai.com](https://openai.com/index/buy-it-in-chatgpt/)), names the far end
where the agent buys on its own. None names the common case, which is the machine
in the middle with the human decision intact. If someone coined an equivalent
before me, the credit is theirs and I will swap mine for it.

One fence before moving on. An organisation deciding to start building with AI is
a big switch, with a committee and a budget. The already-formed pair choosing which
tool to use mid-build is another. This piece is about the second.

## The funnel, properly

Now the main subject.

A funnel is a simple shape: a lot goes in at the top, a little comes out at the
bottom, and the set shrinks at every stage. It doesn't explain why anyone dropped
out. It tells you **where** to look.

An example outside software makes that clear. A shop gets a thousand visitors a
month, a hundred try something on, and twenty buy. The funnel doesn't say whether
the problem is the price, the fitting room or the staff. It says the bigger drop
sits between walking in and trying on, and that is where you investigate first. It
is an instrument of location, not of diagnosis.

The shape comes from early twentieth-century advertising, and its parentage is
disputed: the stages are usually credited to Elias St. Elmo Lewis in 1898, part of
the literature attributes the full formulation to Arthur Frederick Sheldon, and the
AIDA acronym only appears in 1921, with C. P. Russell ([E. St. Elmo
Lewis](https://en.wikipedia.org/wiki/E._St._Elmo_Lewis)).

### Why still a funnel, and not the wheel

There is a running argument about replacing the funnel with the *flywheel*, the
wheel that turns and gains momentum with each revolution. The case against the
funnel is reasonable: human buyers don't walk in a straight line. They double back,
revisit, ask a colleague, disappear for three weeks and come back. A corporate
purchase involves ten or more people arriving at different moments. A funnel drawn
as a staircase doesn't describe that. The dominant reading today is
complementarity — funnel for acquisition and forecasting, wheel for retention. The
numbers circulating in that argument come from agency material with no published
methodology, and I treat them as the weather of the discussion.

**When the machine is the selector, the main objection to the funnel loses its
force**, and the reason is concrete: within a working session, elimination is
irreversible.

Go back to the database. The moment it was picked, the code started calling it.
There is a connection string, there are tables shaped for it, there is a client
library installed. The competitor isn't "revisited later" — it is out, and it went
out in the same session it went in. No committee reopens it. There is no second
meeting. Options are lost, and not recovered for free.

That is exactly the behaviour a funnel describes: a set that only shrinks, never
grows, with every stage acting as a sieve.

**And the wheel comes back over the top, on a different plane.** That choice becomes
public code, a forum answer, a tutorial, training data. That feeds the next
selection, made by another agent, at another company, months later.

> **Funnel within the session, flywheel between sessions.**

The two shapes describe different planes of the same phenomenon, and the fight
between them dissolves once you say which plane you mean. With one correction to
the wheel: a wheel that loses energy stops turning, it does not turn backwards.
What accumulates between sessions also evaporates — which is what I described when
treating community as a water table that rises with what is deposited and falls
with what is drawn. When decay is what matters, that is the shape I use.

### The three stages, and what each one means

This funnel has three stages. They were named when I wrote about the decision, the
price and what to measure, and here they get the explanation that was missing, with
an example in each.

![The three funnel stages crossed with the delegation axis: candidacy, recommendation and adoption, and what each looks like under an assisted decision and under a delegated one](../../visuais/arco2-parte-01/a2p1-stages-en.png)

## Candidacy: being in the set that gets chosen from

The first stage decides nothing. It defines who is entitled to be considered.

Picture a team that needs to send transactional email — the "confirm your account"
message that goes out automatically. Dozens of services do that. In practice the
team will consider three or four. The others didn't lose the comparison. They never
entered it.

Being in the set depends on things that have nothing to do with being good: the
model having seen your name attached to that problem, documentation that makes
sense without context, a product name that doesn't collide with something else,
and — where there is governance — being on the company's approved-tools list.

**It is the most decisive stage and the only one where the loss is invisible.** If
your product doesn't make the set, there is no abandoned cart, no half-finished
signup, no complaint. The project went ahead with something else and nobody
recorded a thing.

### What gets delegated here, measured

This is the stage people hand to the machine most, and three independent surveys,
across three populations, point at the same shape.

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
against another source before buying. Add the fourth population the opening piece
of this arc already brought in: 98% of consumers verify before buying.

Four measurements, four cuts, the same shape: **what gets delegated today is the
shortlisting, not the choice.** The machine assembles the set and leaves before the
decision. One analyst house described it as narrowing the field before human
evaluation begins ([IDC, 28 January
2026](https://www.idc.com/resource-center/blog/ai-mediated-buying-journeys-how-buyers-decide-whos-worth-their-time/)).

![The delegation axis with four measurements: an 11% ceiling for letting AI decide the purchase, 31% for letting it narrow, 86% who check against another source, and 69% of B2B buyers who prefer to validate with a person](../../visuais/arco2-parte-01/a2p1-axis-en.png)

Before using any of those numbers, one caveat that applies to all of them: they are
self-reported, and self-reporting about work with AI has a documented problem. In a
randomised experiment with 16 experienced developers and 246 real tasks from their
own repositories, people were **19% slower** with the tool. Beforehand they expected
to be 24% faster. After being measured as slower, they still estimated they had been
20% faster ([METR, 10 July
2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)).
That is **twenty points between the measured and the believed**, and from the inside
the gap is invisible. The authors are explicit that the result does not extend
beyond that group, and in the 24 February 2026 update, with 57 participants, the
confidence intervals cross zero
([METR](https://metr.org/blog/2026-02-24-uplift-update/)).

I use the four surveys for the shape they share, not for any one of their values.

### Candidacy changes shape as delegation rises

At the assisted end, the set is a **list somebody reads**. A list that is read is
auditable: anyone who knows the market notices when an expected name is missing, and
asks.

At the delegated end, the set forms inside the process and is never displayed. Nobody
notices any absence, because there is nothing there to notice. That is what happened
with my database.

One mechanism helps explain why the set closes so early. In one measured
configuration, **57.8% of repetitions did not trigger a web search** (Schulte,
Bleeker and Kaufmann, [arXiv 2604.07585](https://arxiv.org/pdf/2604.07585), 10 April
2026 — the figure comes via a citation in a critical review, not from the primary
table). Without a search, the candidate set comes entirely from what the model
already carries. The curation happened before the session began, which is why there
is no curation moment to observe.

## Recommendation: being the one chosen within the set

The second stage is what everyone pictures when they think about a decision. Three
options on the table, criteria, one winner.

At the assisted end that is exactly what happens. The person sees the alternatives
side by side, weighs price, maturity and who else uses it, and picks. They may pick
for the wrong reason, but they picked.

At the delegated end there is no comparison. There is a result.

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

### The decision nobody made

Here I come back to the database, because this is the stage that explains it.

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
College London, arXiv 2512.11589](https://arxiv.org/html/2512.11589)). Meaning: when
a library is at stake, the human looks harder, not less.

There is even counter-evidence from the person who named the phenomenon. [Andrej
Karpathy](https://www.linkedin.com/in/andrej-karpathy-9a650716/) coined *vibe coding*
— programming by describing what you want and accepting what the machine writes,
without reading the diffs — on 2 February 2025. On 4 February 2026 he retired the
term and proposed *agentic engineering* instead, writing that programming through
agents is becoming the professional's default flow *"except with more oversight and
scrutiny"* ([dated record by Simon
Willison](https://simonwillison.net/2026/Feb/26/andrej-karpathy/)).

None of that captures my database.

On 4 June 2026, [Paul Copplestone](https://www.linkedin.com/in/paulcopplestone/),
co-founder and chief executive of Supabase, stated: *"agents are now deploying the
majority of databases on our platform"*, over a declared base of more than 250,000
customers ([official
release](https://www.prnewswire.com/news-releases/supabase-raises-500m-at-10-5b-to-accelerate-lead-in-agentic-infrastructure-302791787.html)).
Neon shows a neighbouring figure in a Databricks report of 27 January 2026: agents
create **80% of all databases and 97% of branches**
([Databricks](https://www.databricks.com/blog/enterprise-ai-agent-trends-top-use-cases-governance-evaluations-and-more)).

Choosing a database is an architecture and a vendor decision. It is not execution.

Why do those decisions show up in no opinion survey? Because the question makes no
sense to the person answering:

> **The decision was not delegated. It was removed from view.**

Nobody answers "who chose the database?" about a choice never put in front of them.
The other databases that would have come to mind never dropped out at any point.
They never entered.

![Removal from view: of the three options that existed, two were not rejected but never presented to anyone](../../visuais/arco2-parte-01/a2p1-removal-en.png)

## Adoption: surviving integration and use

The third stage is where most analyses stop looking, and it is where the money goes.

Being chosen is not staying. The integration can fail, the cost can surprise, the
behaviour can differ from what the documentation promised. At the assisted end,
whoever integrates knows what they chose and why, so they have patience for what goes
wrong — the choice was theirs.

At the delegated end, you integrate what turned up. And the first time anyone looks
at it closely is usually when it breaks.

A routine example: the transactional email service went in without discussion, worked
for weeks, and one day the messages start landing in spam folders. Somebody opens the
code to find out why, discovers a service they never chose, and the first question
isn't technical — it's "why are we using this?". The switch that follows passes
through no criterion the machine ever evaluated.

### The veto changes in kind

Here is the change with the most practical consequence in the whole piece.

At the assisted end, the veto is a choice among visible alternatives. The person sees
three, prefers one, and the other two go on existing should the first disappoint.

At the delegated end there are no alternatives on screen. There is a finished result.

> **The veto stops being a choice among alternatives and becomes acceptance or
> rejection of an already-built result** — cheaper to exercise, and more expensive to
> reverse.

Cheaper because accepting requires evaluating nothing: it requires that nothing look
wrong. That is what I did with the database. More expensive to reverse because, the
moment the person accepts, the thing is already written into the code, with
configuration, environment variables and tables around it.

For anyone building a product the consequence is direct: **you don't control the
comparison. You control what the person finds already done when they finally look.**

![The veto in two states: under an assisted decision it is a choice among visible alternatives, and under a delegated one it is accepting or rejecting an already-built result, cheaper to exercise and more expensive to reverse](../../visuais/arco2-parte-01/a2p1-veto-en.png)

### And one asymmetry running through all three

The deeper into the funnel, the more visible the loss — and the less can be done
about it.

If the product is discarded at adoption there is a trace: someone switched, someone
complained, someone opened an issue. If it never enters candidacy there is no trace
at all. And candidacy is precisely where something could still have been done.

I know of no measurement of that asymmetry, and the reading is mine. It is the reason
the first stage deserves more investment than it usually gets.

## What crosses from one session to the next

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

For anyone selling, that opens a position this series had not yet named: **being
written into the customer's memory artefact is a more durable position than being in
the training data, which refreshes, and a cheaper one than switching cost, which needs
the code to already exist.** The ethical line is clear: you write the documentation,
the customer decides whether to reference it.

And it forces an adjustment to the funnel formulation: **it operates at the level of
the decision, not the session.** Not every decision is the same size. Some are local
to the task and will be re-decided tomorrow; others are recorded and become premises.
The ones that matter are the recorded ones, because those stopped being decided.

![Funnel within the session and wheel between sessions, with the three layers of what crosses over: the ownerless session, the project memory controlled by whoever builds, and the public corpus that accumulates slowly and erodes](../../visuais/arco2-parte-01/a2p1-funnel-and-layers-en.png)

## What holds

The funnel still serves, at the level of the decision. Candidacy defines who is
considered, recommendation defines who wins, adoption defines who stays — and candidacy
is the most decisive stage and the only one with no trace of loss.

As delegation rises, all three change shape. The set stops being displayed, the
comparison disappears, and the veto becomes acceptance of a finished result.

And there is a whole class of decision that no opinion measurement captures, because it
was not delegated — it was removed from view. The database I didn't choose is one case
of it, and the vendor published the mechanism.

The pieces that follow walk down stage by stage: two on candidacy, one on how you get
into the set and another on how you get cut from it before any preference forms; one on
what decides the choice and which of those tactics decay; one on adoption and the veto;
and a closing one on where your product fits and who inside the company looks after it.

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
