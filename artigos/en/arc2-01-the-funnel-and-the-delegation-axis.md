<!--
Arc 2, part 1 of the Builder-Led Growth series, by Matheus Ramos.
CANONICAL VERSION (English).
Portuguese counterpart: ../pt-br/arco2-01-o-funil-e-o-eixo-da-delegacao.md
Text frozen. No LinkedIn date set yet.
Generated from the private working repository. Do not edit here.
-->

# The more you delegate, the faster the funnel moves

*Second piece of the second arc of this series. It doesn't require the earlier
ones. Here the builder's funnel gets the three stages it needed — candidacy,
construction and adoption — and the explanation of why the speed at which a product
crosses all three depends on how much the pair of person and machine delegated.*

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

What interests me isn't that I ended up with the wrong database. What turned up
works. What interests me is the speed. That product crossed the entire route, from
unknown name to dependency written into the code, in minutes. No meeting, no
comparison, no objection.

And this isn't an impression of mine. The infrastructure vendor published the
mechanism in as many words, on 29 September 2025: *"every AI builder using Lovable
is already using Supabase, whether or not they realize it"*
([Supabase](https://supabase.com/blog/lovable-cloud-launch)). That is a statement
from a company with a commercial interest in emphasising its own penetration, and
it is worth reading with that in mind. But whoever wrote it sits on the side that
can see: it is the vendor, not the user, who can count decisions the decider never
saw.

This piece is about that route — what its stages are, and what makes a product move
faster or slower between them.

## The funnel has three stages, and I had proposed the wrong ones

When I wrote about the decision, the price and what to measure, I proposed candidacy,
recommendation and adoption. I kept investigating, and one of the three was
classified wrong.

**Recommendation is not a stage. It is one of the forces acting inside candidacy.**

The difference matters and is easy to check. Candidacy and adoption describe **where
the product is**: inside the set under consideration, inside what was shipped.
Recommendation describes **what happens to it** in there. A funnel measures position,
not occurrence — and wedging an occurrence between two positions is what made the
model slippery.

The idea isn't without precedent. Everett Rogers, describing how an innovation
spreads, separates knowledge, persuasion, **decision**, **implementation** and
**confirmation** ([review of the
theory](https://files.eric.ed.gov/fulltext/ED501453.pdf)). In his model the decision
is a point moment between two states that last. It is the same distinction, drawn
decades earlier, for a decider who was still only human.

The three stages I hold to from here on:

**Candidacy** — your product is in the set that gets chosen from. You are known,
findable, and nobody has needed you yet.

**Construction** — your product has left the corpus and entered the code. Somebody
is assembling something, and you are part of what is being assembled. It can still
be taken out.

**Adoption** — your product has become a premise. It is in what was shipped to the
market, and taking it out costs refactoring, migration and risk.

And one correction that applies to all three, because it was another error of mine:
**the transition between stages is not a single mechanism.** It is a set of actions,
the same way you move through the pirate funnel of product-led growth — acquisition,
activation, retention, revenue and referral — where nobody looks for the button that
moves a user from one stage to the next. In the pieces that follow I detail which
actions those are at each stage; here the job is to explain the stages.

![The three stages of the builder's funnel — candidacy, construction and adoption — with the cost of removal rising at each one and the degree of delegation as the accelerator of the crossing](../../visuais/arco2-parte-01/a2p1-stages-en.png)

## Candidacy: being in the set that gets chosen from

The first stage decides nothing. It defines who is entitled to be considered.

Picture a team that needs to send transactional email — the "confirm your account"
message that goes out automatically. Dozens of services do that. In practice three
or four will be considered. The others didn't lose the comparison: they never
entered it.

**It is the most decisive stage and the only one where the loss is invisible.** If
you don't make the set, there is no abandoned cart, no half-finished signup, no
complaint. The project went ahead with something else and nobody recorded a thing.

### The forces acting here, and recommendation is one of them

I won't detail the tactics in this piece — they are the subject of the next one,
which goes into this stage alone. What belongs here is naming the forces in play, so
it is clear what the next piece will cover:

**Being in the corpus.** The public material that trained the model determines
whether your name shows up attached to the problem it is solving.

**Having canonical documentation.** One definition of what you do, written once,
consistent everywhere, understandable without context.

**The community.** What third parties write about you is the raw material for all of
this, and it is the subject I covered when describing community as the well everyone
drinks from ([Part 5](05-community-and-validation-signal.md)).

**AEO and GEO** — answer engine and generative engine optimisation, the work of
being found and cited correctly by systems that answer instead of listing.

**And recommendation**, which is the force that moves a product out of the set and
into construction. The better the candidacy, the faster and more precise it is.

### How much gets delegated at this stage, measured

There are four useful public measurements, and it is worth saying what they measure:
**the situation where the machine assembles a shortlist and the person picks.** They
do not measure the case where a company narrowed the set by policy, and they cannot
measure the case where nobody saw a set at all — about that one, nobody has anything
to answer.

Consumer willingness to let AI **make** the purchase decision **tops out at 11%** —
the wording is the survey's own, *"topped out at 11%"*, and the ceiling occurs in the
lowest-stakes categories, such as personal care. Willingness to let AI **narrow** the
options reaches **31%** in cleaning and household products ([Gartner, 27 May
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

Four measurements, four cuts, the same shape: **when a list exists, what gets
delegated is assembling it, not choosing within it.**

![When a shortlist exists, what gets delegated is assembling it: an 11% ceiling for letting AI decide the purchase, 31% for letting it narrow, 86% who check against another source, and 69% of B2B buyers who prefer to validate with a person](../../visuais/arco2-parte-01/a2p1-axis-en.png)

One caveat applies to all four: they are self-reported, and self-reporting about work
with AI has a documented problem. In a randomised experiment with 16 experienced
developers and 246 real tasks from their own repositories, people were **19% slower**
with the tool. Beforehand they expected to be 24% faster. After being measured as
slower, they still estimated they had been 20% faster ([METR, 10 July
2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)).
That is **twenty points between the measured and the believed**, and from the inside
the gap is invisible. I come back to this study at the end, because it says one more
thing.

## Construction: being inside what is being made

The second stage starts at a material point, and it is worth fixing because the wrong
boundary is what confused me before: **construction begins when there is a first line
of code that calls your product.**

Before that, however short the list, you are still a candidate. Being on a shortlist
is still being in a set.

Here the product stops being a name in the corpus and becomes technology inside what
somebody is trying to create. An MVP, a proof of concept, the weekend test of someone
doing *vibe coding* — programming by describing what you want and accepting what the
machine writes.

And here is the property that defines the stage: **it can still be taken out, and
taking it out is cheap.** A few hours of rework, no data migrated, no users affected.

### An example that shows the whole decision

A system needs secure sign-in with **MFA** — multi-factor authentication, the kind
where the password alone isn't enough and a second code arrives.

There are two routes. Write the code, using the cryptography libraries that already
exist. Or adopt a market solution that handles it as a service.

Both work. Both are defensible. **What decides which one happens is the degree of
delegation.**

With little delegation, somebody weighs it up: what does maintaining this cost, who
handles it when it breaks, which audit will we have to pass. With a lot of
delegation, the machine settles it with whatever it reaches first — and what it
reaches first is a function of the harness, of what was asked, of the security and
compliance policies in force, and of the review loops that do or don't exist along
the way.

The pair didn't change. The product didn't change. What changed is how much of the
decision passed through a person.

### What helps convert here

I won't detail this either — it gets its own piece. But the forces at this stage
differ from candidacy, and they are worth naming:

**Familiar documentation, organised and machine-readable.** Not the same thing as
documentation that is good for a human: what counts here is being retrievable,
unambiguous, and sufficient without context.

**Speaking the language of whoever operates the gate.** Expressing readiness in the
terms of the technical standards the buyer already uses is what makes your compliance
checkable rather than merely declared.

**Information management.** Where the information lives, how it is versioned, and
what happens to the old version when the new one ships.

**The community again** — because it is where the working example comes from, the one
the agent finds when it needs to integrate you.

## Adoption: having become a premise

The third stage is where the product stops being a choice and becomes part of the
thing.

It went to production. It is in what the builder shipped. There is data stored in its
format, there are other parts of the system depending on its behaviour, there are
people using it without knowing it exists.

**Here the cost of removal stops being a few hours and becomes a project.**
Refactoring, data migration, the risk of breaking what works, and the awkward question
of why replace something that is standing.

It is the same force that jobs-to-be-done theory calls **habit** — the inertia of what
is already installed, one of the forces Bob Moesta describes as working against any
switch. Under BLG it is stronger than in traditional software, for a specific reason:
the product isn't merely in somebody's workflow, it is in the work that person shipped
and answers for.

Out of that comes this stage's most valuable consequence for anyone selling, and it is
uncomfortable to write:

> **Reaching adoption creates a competitive barrier that was never won in a
> comparison.** The competitor may be better and never be considered, because the cost
> of firing what is already there exceeds the difference between the two.

### And the veto changes in kind

When delegation is low, the veto is a choice among visible alternatives: the person
sees three, prefers one, and the others go on existing should the first disappoint.

When it is high, there are no alternatives on screen. There is a finished result.

> **The veto stops being a choice among alternatives and becomes acceptance or
> rejection of an already-built result** — cheaper to give, and more expensive to
> undo.

Cheaper because accepting requires evaluating nothing: it requires that nothing look
wrong. That is what I did with the database. More expensive to undo because, the
moment the person accepts, the thing is already written into the code.

![The veto in two states: with the decision in view it is a choice among visible alternatives, and with the decision delegated it is accepting or rejecting an already-built result, cheaper to give and more expensive to undo](../../visuais/arco2-parte-01/a2p1-veto-en.png)

## Delegation is the accelerator

Now the part that ties the three stages together, and it is this piece's thesis.

Delegation is a degree, not a switch, and both ends of that degree need names:

> **AI-assisted decision: the person chooses among options the machine assembled.
> Delegated decision: the person accepts or rejects a result the machine has
> already built.**

I looked for an existing name before coining one. Conversational commerce describes
buying through a messaging app, and predates language models. Zero-click search
describes the absence of the click. Generative engine optimisation names what
publishers do. And the Agentic Commerce Protocol, from Stripe and OpenAI
([openai.com](https://openai.com/index/buy-it-in-chatgpt/)), names the far end where
the agent buys on its own. None names the middle case, which is the machine
mediating with the human decision intact. If someone coined an equivalent before me,
the credit is theirs and I will swap mine for it.

**The more the pair delegates to the machine, the faster a product crosses the
funnel.** And not only because the person stops choosing. It is because the set the
choice would come from gets smaller, and concentrates on what is already familiar.

Four independent mechanisms push in that direction.

**The first is the one that surprised me most, because it shows the size of the
shortlist is an engineering decision, not a market one.** In a study measuring how
many tools an agent should see before choosing, over the same benchmark data, the
learned depth was **1.4 candidates with one embedding retriever and 7.4 with another
method** ([arXiv 2605.24660](https://arxiv.org/abs/2605.24660)). Swapping one piece
of infrastructure changes from roughly one to roughly seven how many products the
model gets to see — with nothing changing in the product, the market or the question
asked. The authors declare the limit: the scope is whether the right tool appears in
the set, not whether it is then used correctly.

**The second is degradation by catalogue size.** With around 50 tools available,
accuracy in selecting the right one sits between 84% and 95%. With 200, it falls to a
range between 41% and 83%. With 740, it lands between 0% and 20% for most models
([BiasBusters, arXiv 2510.00307](https://arxiv.org/html/2510.00307)). The more
options exist, the less the machine can choose between them — and what remains is
what it already knew.

**The third is order.** In the same work, a tool in the middle of a long list is
selected correctly in 22% to 52% of cases, and ordering alone moves performance
between 13% and 85%. Worth saying these are laboratory results with synthetic
catalogues, and the reading that they transfer to real use is mine.

**The fourth is the search that doesn't happen.** In one measured configuration,
**57.8% of repetitions did not trigger a web search** (Schulte, Bleeker and Kaufmann,
[arXiv 2604.07585](https://arxiv.org/pdf/2604.07585), 10 April 2026 — the figure
comes via a citation in a critical review, not from the primary table). Without a
search, the set comes entirely from what the model already carries.

Add it up and the result is measurable in behaviour: in a study across eight models,
popular libraries appear unnecessarily in up to **48%** of cases, and Python is chosen
in **58%** including where it is suboptimal. The authors' conclusion, in their words:
*"LLMs may prioritise familiarity and popularity over suitability"* ([Twist, Zhang,
Harman, Syme, Noppen, Yannakoudakis and Nauck, Findings of ACL 2026, arXiv
2503.17181](https://arxiv.org/abs/2503.17181)).

> **Delegation doesn't only take the choice away from the person. It shrinks the set
> the choice would have come from.**

For whoever is already the category default, that is pure acceleration: the whole
funnel gets crossed in minutes, with no comparison and no objection. For whoever is
fighting for second place it is the opposite — not chosen, and not compared either,
which is how you improve in a contest.

![Four mechanisms shrink the set as delegation rises: the retriever sets how many candidates exist, catalogue size destroys the accuracy of choosing, order decides within what is left, and with no search triggered the set comes entirely from the model](../../visuais/arco2-parte-01/a2p1-removal-en.png)

### Two speeds that must not be conflated

Here I need to dismantle an easy and wrong conclusion, because it would be far too
comfortable for anyone selling.

Delegation accelerates the **vendor's** funnel. There is no evidence that it
accelerates the work of **whoever is building**.

Back to the randomised experiment I cited above: the developers were 19% slower with
the tool and believed they had been 20% faster. The authors are explicit that the
result does not extend beyond that group and those repositories, and in the 24
February 2026 update, with 57 participants, the confidence intervals cross zero
([METR](https://metr.org/blog/2026-02-24-uplift-update/)).

These are two different accounts. Your product may be crossing the funnel faster than
ever, inside projects that are moving slower than their owners think.

And out of that comes the question I leave for anyone building a product: if low
delegation makes the crossing slower, **how much better does the experience have to be
for the pair to advance anyway?** I don't know, and I suspect the answer differs at
each stage.

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

Look at what that does to speed: **the project's memory is the brake the person
controls.** Writing the choice down reintroduces a human decision into the route,
without depending on a committee or a company policy.

For anyone selling, it opens a position this series had not yet named: **being written
into the customer's memory artefact is a more durable position than being in the
training data, which refreshes, and a cheaper one than switching cost, which needs the
code to already exist.** The ethical line is clear: you write the documentation, the
customer decides whether to reference it.

![The three layers of what crosses from one decision to the next: the ownerless session, the project memory controlled by whoever builds, and the public corpus that accumulates slowly and erodes](../../visuais/arco2-parte-01/a2p1-funnel-and-layers-en.png)

## What holds

The builder's funnel has three stages, and they describe where the product is, not
what happens to it. **Candidacy**: you are in the set that gets chosen from.
**Construction**: you are in the code of something being made, and taking you out
costs hours. **Adoption**: you have become a premise of what was shipped, and taking
you out costs a project.

Recommendation still exists, and still matters — but as one of the forces acting
inside candidacy, alongside the corpus, canonical documentation, community, and
optimisation for the engines that answer.

And the speed of the crossing is a function of delegation. The more the pair
delegates, the smaller the considered set becomes, the more it concentrates on the
familiar, and the faster a product covers all three stages — with nobody having
compared anything. That is why this account matters both to whoever builds and to
whoever sells, and it is what I think companies are not yet looking at.

The pieces that follow go in stage by stage: what to measure at each one, and which
actions convert to the next.

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
- Arc 2, part 1 — The more you delegate, the faster the funnel moves (this text)

The first arc, for anyone who wants the full route:

- [Part 1 — When the machine is also your customer](01-when-the-machine-is-the-customer.md)
- [Part 2 — The decision, the price and what to measure](02-decision-price-and-measurement.md)
- [Part 3 — The tax the machine charges and the human never sees](03-machine-legibility.md)
- [Part 4 — How many times the agent has to call a human](04-operational-accessibility.md)
- [Part 5 — The well everyone drinks from](05-community-and-validation-signal.md)
- [Part 6 — The machine is press and reader at once](06-public-relations.md)
- [Part 7 — What makes an agent trust you, and why its competence is the problem](07-trust-and-safety.md)
