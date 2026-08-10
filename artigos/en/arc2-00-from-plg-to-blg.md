<!--
Arc 2, part 0 of the Builder-Led Growth series, by Matheus Ramos.
CANONICAL VERSION (English).
Portuguese counterpart: ../pt-br/arco2-00-do-plg-ao-blg.md
Text frozen. No LinkedIn date set yet.
Generated from the private working repository. Do not edit here.
-->

# From PLG to BLG: what still holds when the one choosing is a pair

*Opens the second arc of this series. It doesn't require having read the first —
the concepts that matter are picked up again here. The first arc asked what the
machine decides; the second asks how the pair decides, and what to do about it.*

---

## Two acronyms, before we start

**PLG** is product-led growth: the idea that the product itself does the work that
used to belong to sales and marketing — the person tries it, sees the value on
their own, and decides.

**BLG** is builder-led growth, the name I gave in July 2026 to a specific
phenomenon: **a code agent recommends or adopts your tool while building
something else.** There's no buyer evaluating vendors, no evaluation process, no
one out shopping. Adoption happens as an instrumental by-product of a build task —
and whoever wins there grows, while whoever loses doesn't exist for that project.

The rest of this piece is about what those two have in common and where they stop
having it.

## A stronger lens on the most important word

When I named this discipline, in July 2026, I wrote that "builder" precisely named
who makes the decision: not a buyer evaluating vendors, not your own product being
operated without a UI, but a building agent choosing, mid-construction, what to
use.

The word was right and still is. **What was missing was detail.** That version
described the phenomenon from a distance, enough to name it; this one changes the
lens and looks at exactly who is standing there.

I got to the detail along three paths that only made sense together.

The first came from practice. Anyone who builds with agents knows the scene: the
agent stops for the third time to ask for a credential, and the person watching
loses patience and switches tools. That switch went through no criterion the
machine ever evaluated. It happened from the outside.

The second came from an established instrument that kept working when I expected
it to break. **[Sean Ellis](https://www.linkedin.com/in/seanellis)** formulated a
question that became the reference for measuring product-market fit: how would you
feel if you could no longer use this product? **[Rahul
Vohra](https://www.linkedin.com/in/rahulvohra/)**, founder of Superhuman,
describes on 13 November 2018 how that question gave him part of what he needed
and not all of it — and how he built a whole method around it in order to act on
the answer ([First Round
Review](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/)).

I was betting that Ellis's question would lose its meaning once the one operating
the product is a machine. It didn't. It still works — and the respondent stopped
being whoever operates and became whoever receives the result.

The third came from the constraints. Training, the harness — the scaffolding that
runs the agent and bounds what it can call and see —, the guardrail — the limit
that blocks certain actions before they happen — and the compliance rule don't act
on the agent. They act on the pair. They describe how the pair was assembled.

Together, the three say the same thing, and this is how I use the term from here
on:

> **A builder is the pair: the person and the agent together.** The agent selects,
> the person validates, and neither of them decides alone.

It's what the word already meant in the market — on assisted-building platforms, a
builder is whoever builds with AI, and nobody needs to be told there's a person
there. The difference is that the person now enters the model instead of being
taken for granted.

And forgive me the terrible pun: the BLG customer is, literally, a superhuman. The
case I just cited is Superhuman, and the coincidence was too good to let pass. Joke
made, I'll stick with "builder".

![A builder is the pair: the agent selects, the person validates, and neither decides alone](../../visuais/arco2-parte-00/arco2-parte-00/a2p0-the-pair-en.png)

## The human-machine hybrid is not an invention of this decade

Worth reining in the enthusiasm before it spoils the argument.

Pairs of person and machine have existed for a long time. A spreadsheet used to
decide where to invest is one: the person frames it, the tool computes, and the
decision comes out of the pair. Tools have always existed, have always changed
what a person can decide, and will keep changing it.

What changed is the nature of the tool. **It became probabilistic.**

The spreadsheet fails the way it was built to fail — sum the wrong column and it
will sum wrong every time, the same way, until someone fixes it. The assistant
fails differently on each run, and sometimes gets right on the second attempt the
same question it got wrong on the first.

That carries a practical consequence across this whole arc: **governance designed
for a deterministic tool doesn't cover a probabilistic one.** A rule like "check
the formula before approving" works when the formula is stable. When what you're
approving is a tendency rather than a step, the same procedure starts delivering a
sense of control it no longer provides.

Look at what that does to the idea of checking: you're no longer approving an
answer, you're approving a distribution of possible answers.

## The job is the same. The hiring is what changed

Here comes a concept I use throughout the arc, and its parentage is disputed —
worth telling properly, because the lineages say different things.

**[Tony Ulwick](https://www.linkedin.com/in/tonyulwick)** conceived the approach in 1990, applying
Six Sigma thinking to the innovation process, and named the method Outcome-Driven
Innovation in 1999
([Strategyn](https://strategyn.com/jobs-to-be-done/history-of-jtbd/)). **[Bob Moesta](https://www.linkedin.com/in/bobmoesta)**, **Rick Pedi** and **John
Palmer** arrived, in the same decade, at the notion that
customers have jobs to get done. And **Clayton Christensen** coined the term
*jobs-to-be-done* in *The Innovator's Solution*, from 2003, and is the one who
popularised it.

Christensen's contribution that serves us most is swapping "outcome" for
**progress**: a job is the progress someone is trying to make in a particular
circumstance. People hire products to make progress, and fire the ones that don't
deliver it.

From the point of view of whoever builds, the progress being sought hasn't changed
much. Get the product live. Get the site running with people on it. Ship by
Friday.

**What changed was the process — and, with it, the needs. Because a new hirer
showed up.**

Under the builder there are two hirers, each with a job of its own, specific and
legitimate. The machine hires a database that comes up and connects. The person
hires having the product live by Friday. Neither is a sub-job of the other — they
are nested in execution and independent in theory. And that's exactly why the
Christensen and Moesta school insists a job doesn't decompose: the milkshake from
the classic example is a whole job, and a job can be tiny and still be a job.

And this is where the theory changes who you think your competitors are.

**The set competing with you is defined by the job, not by the category.** Someone
who wants to be entertained for a couple of hours, without hassle, can go to the
cinema, turn on the console, open a book or take the kids for a walk in the park.
None of that sits in the same industry. All of it competes for the same progress.
The cinema's competitor isn't only another screening room — it's everything the
person picks to solve that.

Bringing it here: when the builder needs a database that comes up and connects,
you aren't only competing with other databases. You're competing with the managed
service already bundled into the platform, with the local file that does for now,
with the instance the team already runs for something else — and with the agent
writing it themselves.

**That last option is the one whose price changed.** Doing it yourself always
competed; what collapsed was its cost, for one of the two members of the pair. And
when it wins, you didn't lose anyone's preference: you lost before preference was
ever consulted.

One precision the definition of builder demands, and worth carrying through the
whole arc: **the machine doesn't solve it alone.** It selects; the pair decides.
Even when the agent writes the two hundred lines that replace your product, it was
the pair that accepted that path — through the action of whoever was watching, or
through the omission of whoever wasn't called.

## The weight doesn't sit still in the middle of the pair

Saying the pair decides together can suggest an even split. It isn't that. **The
weight tips, and it tips according to who is on the human side.**

A story went around among builders that describes this better than any definition
of mine. Someone tells how they started building a website, have already redone
ten versions, none ready to show — and how, in the middle of that mess, they ended
up building an entire platform for a psychology clinic. Scheduling, records,
payments, messaging, telehealth, reporting, automations, and even AI helping to
draft the records. And they close by admitting they have no idea what they're
doing: there's a room with no door, a staircase leading nowhere, a window with no
wall. But it's moving.

Look at what happened there. Nearly every architectural decision was delegated.
That person didn't pick the database, or the authentication method, or the folder
structure — they described what they wanted and validated what showed up working.

Now picture the same build run by someone with fifteen years of platform work.
Everything shifts: the architectural decisions move back to the human side, and
the agent executes more while choosing less.

**And there is data supporting that this difference is real.** In Stack Overflow's
2025 survey of developers ([Developer Survey
2025](https://survey.stackoverflow.co/2025/ai)), high trust in AI output runs at
**6.1% among those learning to code** and drops to **2.5% among the experienced**.
It isn't an opinion about the tool: it's nearly three fifths of the trust
disappearing with time on the road. And in no group, none, does it clear 6.1%.

It's worth saying where that number comes from, because the survey itself leaves a
piece out. The four published answers add up to 78.5% of respondents — roughly a
fifth picked something Stack Overflow doesn't disclose, and the percentages are
figured against the total number of people, not against the four options shown. The
contrast between the two groups is what matters here, and it holds. The absolute
level is what asks for care, because there's no telling how that fifth splits
between the people starting out and the ones with road behind them.

The same thing shifts by environment. Where there's little governance and little
written rule, the agent decides more. Where there's an approved registry, a
committee and mandatory review, it decides less and proposes more.

> **The less experience the watcher has, and the less rule around them, the more
> the decision tips toward the machine.** The pair is the same; the centre of
> gravity isn't.

For whoever sells, that has a direct consequence: the same product is judged by
different criteria depending on who's on the other side. Whoever delegates almost
everything judges by the result that appeared. Whoever delegates little judges by
the decision they would have made alone — and asks you to explain yourself.

![High trust in AI output: 6.1% among those learning to code against 2.5% among the experienced](../../visuais/arco2-parte-00/arco2-parte-00/a2p0-weight-tips-en.png)

## What came before: growth hacking, and what PLG built

Nothing that follows is criticism. It's recognition of what worked, and of what
BLG inherits whole.

**[Sean Ellis](https://www.linkedin.com/in/seanellis)** coined "growth hacker" in a
2010 post, after running growth at Dropbox, LogMeIn and Eventbrite through each
company's inflection years. His definition: someone whose true north is growth, and
who subjects everything they do to its potential impact on scalable growth. In
2017 he published *Hacking Growth* with **[Morgan Brown](https://www.linkedin.com/in/morganb/)**.

The book's central contribution isn't a list of tricks. It's an operating system
for a growth team: a weekly cadence of hypothesis, prioritisation, experiment and
learning loop after each test.

**PLG** came next, popularised in the mid-2010s by OpenView, with [Blake Bartlett](https://www.linkedin.com/in/blakebartlett), and codified in a book by [Wes
Bush](https://www.linkedin.com/in/wesbush) in 2019. From it we inherit four
instruments that still stand:

- **The pirate metrics**, the AARRR that
  [Dave McClure](https://www.linkedin.com/in/davemcclure) presented in 2007 —
  acquisition, activation, retention, revenue and referral
  — which split the journey into stages of observable behaviour.
- **The product-qualified lead**: a user who completed a core action and saw the
  value first-hand. Swaps the declared signal for the behavioural one.
- **Time to value**: how long until the person reaches the moment the thing works.
- **The three motions** — pure self-serve, sales-assisted self-serve, and
  enterprise sales — today run in combination by most of the market.

And here comes something I have to admit about my own lineage. I called BLG a form
of hacking, in the disposition of looking at the mechanism instead of the
convention. The disposition is the same. **But growth hacking's main instrument
doesn't port over here**, for three reasons.

You can't split the sample: the agent isn't a population that divides into group A
and group B, it consults the model that exists at that moment. The loss is
invisible: when the agent doesn't pick you, nobody records anything, because
there's no abandoned cart and no interrupted session — the project simply carried
on with something else. And the feedback loop is broken, because the machine
stacks the roles of medium and recipient, and the reply gets lost inside the
channel.

That doesn't invalidate the lineage. It forces us to invent the missing
instrument, and it's one of the debts this arc carries out in the open.

## The limit PLG itself acknowledges

This is the finding that surprised me most, and it doesn't come from outside
criticism: it's in the PLG literature.

Pure self-serve works in a narrow band — individual-user or small-company product,
pricing in the order of zero to thirty dollars per user per month, and **no
compliance complexity**. Above thirty thousand dollars in annual contract value,
with a multi-person committee, security review and procurement, pure self-serve
stops working ([Digital
Applied](https://www.digitalapplied.com/blog/product-led-growth-2026-plg-strategy-playbook)).
Worth saying where that comes from: it's market consultancy material, not a survey
with published methodology.

Hold on to that condition — no compliance complexity. It comes back, and what
happens to it is one of the most consequential things in this piece.

## Where the two meet

What PLG built and BLG inherits without reservation:

**The product is the channel.** Holds entirely. What changes is that the interface
description becomes the marketing piece the machine reads.

**No gatekeeper at the door.** Worth more, not less. The agent doesn't fill in a
card form or click "talk to sales".

**Land and expand.** Survives, and perhaps improves: the small integration hardens
inside the code and becomes the base for the next one.

**Behavioural signal instead of declared.** The logic survives whole. What changes
is that the signal stopped coming from a person.

## Where PLG stops serving

Also not criticism. It's recognising that these techniques were designed for a
human at the end, and they do exactly what they promise when there is one.

**The moment of perceiving value changes recipient.** I did write, in an earlier
draft, that this moment stopped existing. It doesn't: value exists and is
perceived, by other criteria. Watching the database come up with no manual
provisioning, already connected and with the security rules applied, is
unmistakable perception of value.

What changes isn't the existence of value. It's whose moment it is. **The agent
doesn't feel value: it produces the state in which the person feels it.** The
concept survives whole and the recipient moves — you stop designing the moment for
whoever operates the product and start designing for whoever receives the result.

The practical consequence inverts the target of onboarding. PLG optimises the path
of whoever clicks. Here, whoever clicks is the machine and whoever judges is the
person who only sees the end. Designing becomes minimising what the machine has to
cross and maximising what the person finds ready when they look.

**Progressive disclosure inverts.** Showing a little at a time, so as not to
overwhelm, has been established interface-design practice since the 1980s, and the
reference text is [Jakob
Nielsen's](https://www.nngroup.com/articles/progressive-disclosure/). To the
machine, withheld information is ambiguity. Look at what that means: one's best practice is the other's defect.
It holds for tooltips, empty states, guided tours and getting-started checklists,
which are all instruments of attention and motivation. The machine has neither.

**Referral doesn't happen.** People refer for social reasons — looking useful,
belonging, reciprocating. The agent doesn't refer. What takes its place is
something else: the choice becomes public code, a forum answer, a tutorial, and
that settles into the material training the next model. It isn't referral, it's
sedimentation. It's slower, it isn't social, and no referral programme incentivises
it.

**Freemium meets a consumer with no sense of budget.** The model bets the free user
converts when they feel the limit. The agent doesn't feel the limit — it consumes
until the bill reaches a human.

**And the compliance floor came down.** Here's the condition I asked you to hold.
Pure PLG lived precisely where there was no compliance complexity. Under BLG,
corporate registry, allowlist and gateway place themselves in front of any tool,
regardless of price.

> The enterprise gate starts existing without the enterprise contract.

With a caveat on scale that the numbers impose, and that I handle in detail in the
piece on candidacy: only 27% of organisations enforce strict governance, and 68%
don't know which AI tools their developers use
([Northflank](https://northflank.com/blog/enterprise-ai-coding-agent-deployment)).
The gate is real where it exists, and the two numbers describe adoption that is
still partial. I found no measure of how fast it is spreading, so I won't claim a
direction — what can be said is that it isn't a universal condition today.

![The five PLG techniques that stop serving once the machine is the one operating](../../visuais/arco2-parte-00/arco2-parte-00/a2p0-where-plg-stops-en.png)

## Two phenomena that look alike and aren't the same

I need to separate two things before going on, because we're talking about a
funnel and mixing them scrambles the stages.

**The first: the machine recommends to a human.** You ask the assistant which
sneakers to buy, which tool to use, and it hands back a short list with a reason
for each. In 2026 this happens at scale: ChatGPT operates in the region of 900
million weekly users, and a Semrush survey from December 2025 puts half of US
shoppers as having bought something after researching it with AI
([Darkroom](https://www.darkroomagency.com/observatory/how-chatgpt-shopping-transforms-online-purchasing),
[Crescitaly](https://blog.crescitaly.com/chatgpt-shopping-search-optimization-2026-brand-playbook/)).
Agency material, worth saying, not an independent survey.

**The second: the agent selects, integrates and uses.** Nobody asks it anything
about brands. It's building, it needs a piece, it picks one, writes the code that
uses it, and moves on. The choice becomes a dependency before it becomes a
conversation.

In both, the one deciding is the pair. **The difference is where the person sits in
the sequence.**

- **In recommendation**, the one executing is the person: they get the suggestion,
  go there and buy. They enter **before** execution.
- **In selection during construction**, the one executing is the agent: it writes
  the code and integrates. The person enters **after**, looking at a result that
  already became a dependency.

And there's a number showing how much that difference weighs. A 2026 Idea Grove
study of a thousand US consumers found that **98% verify the AI recommendation
before buying. Only 2% buy without checking**
([Opascope](https://opascope.com/insights/ai-shopping-assistant-guide-2026-agentic-commerce-protocols/)).

Hold on to that 98%, because it says something that runs through this entire arc:
even in the case where the machine only suggests, almost nobody goes ahead without
looking. **Human validation isn't a quirk of people who build software. It's the
norm.** What changes, when the agent executes, is that validation arrives later —
and looking at a result, not at an option.

**And the two aren't separate boxes: they're points on one gradient.** The role the
machine takes on shifts with the size and the specificity of what's being built.

If I want to know which switch to buy for the network at home, I ask and get a
pointer — there it points, and I go. If I want to build a set of six programming
interfaces that together handle the creation and management of structured text
files, it stops pointing: it chooses, integrates, tests, hires on my behalf.

And there's a pattern worth registering as a hypothesis, because it explains both
ends:

- **The more generic the task, the more the machine leans on the corpus** — on what
  it learned, on what is consensus, on what shows up a lot.
- **The more specific, the more it is bounded by the harness, the context and what
  was asked** — and the less the consensus of training decides.

That's my own reasoning, and I found no one measuring it. If it's right, it carries
a large practical consequence: whoever sells into generic tasks competes for
presence in the corpus; whoever sells into specific tasks competes for presence in
the harness and in the files the agent reads while working.

**No point on the gradient is dispensable, and this thesis covers the whole
gradient.** Being recommended is the territory of what the market calls GEO and AEO
— generative engine optimisation and answer engine optimisation, the effort of
being found and correctly cited by systems that answer rather than list. The first
piece of this series already dealt with that under machine legibility, because it
all rests on the same base: if the model doesn't understand what you do, it neither
recommends nor chooses you.

What shifts along the gradient is the rest of the funnel. At the recommendation
end, your work finishes when the person clicks. At the construction end, it starts
there.

![The gradient between recommending and building, and the finding that 98% verify the AI recommendation before buying](../../visuais/arco2-parte-00/arco2-parte-00/a2p0-gradient-en.png)

## What the buyer calls value

If the decision passes through a person, it's worth knowing what that person is
after.

A Gartner survey of 204 finance leaders, in March 2026, shows 45% of AI investment
in that function leaning toward productivity and 20% toward decision quality. The
finding with more weight is another: organisations that invested in initiatives
that **create a new value proposition, product or market** were more than twice as
likely to report high realised value. And the same survey registers a ceiling
effect on productivity-oriented use — once the process is automated, the
incremental gain flattens
([Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-07-20-gartner-survey-shows-45-percent-of-cfos-say-their-ai-investments-lean-towwards-productivity-while-20-percent-say-these-investments-lean-towards-decision-quality)).
It's a survey of one function, with a declared sample, and "high realised value" is
self-reported.

Behind that sits an older and more durable layer. **Alfred Rappaport**, in *Creating Shareholder Value*, from 1986, proposed
seven drivers management can
operate to create value: sales growth, operating margin, effective tax rate,
working capital investment, fixed asset investment, cost of capital, and — the
seventh — **the duration of competitive advantage**.

The first six are contested by everyone. The seventh is the one BLG operates, and
it's the least discussed in growth conversation: how long the return keeps running
above the cost of capital.

And there's a number from the model itself that supports much of this arc: **as
much as two thirds of a business's value comes from cash flows beyond the normal
planning horizon.** Before leaning on it, it's worth saying where it comes from:
the model dates from 1986 and grows out of the shareholder-value tradition, which
carries its own critique and is far from settled. I use it as finance vocabulary,
not as a position on what a company is for. The standard objection to BLG is that
it's slow. Whether it
actually is remains under debate — and finding which engines accelerate that growth
is precisely the course of this arc. What can be said already is that the
instrument the firm itself uses places most of the value beyond the horizon it
plans for.

Out of that comes a repositioning that changes how you ask for budget for this:

> **BLG is an argument about acquisition cost as well as an argument about
> growth.** Being recommended by an agent is acquiring a customer without spending
> on media — and payback on acquisition is what the board examines before it looks
> at growth rate. Whoever presents only the growth half is leaving half the
> argument on the table.

![The competitive set defined by the job: another database, the bundled service, the local file, the existing instance, and the agent writing it themselves](../../visuais/arco2-parte-00/arco2-parte-00/a2p0-competitive-set-en.png)

## Adding the two approaches isn't free

The thesis I hold here is that PLG and BLG add up, because they are distinct
customers with distinct needs. With the human veto established, it gains a
mechanism instead of staying a slogan:

> **BLG without PLG fails at validation. PLG without BLG fails at candidacy.**

The agent never gets to consider whoever isn't legible to it. And whoever does get
considered, but delivers a result that irritates the watcher, is removed. Each
approach covers the other's blind spot.

Except the sum charges you, in three places.

**First, in the vocabulary.** Calling BLG a leap beyond PLG suggests it's a more
advanced stage, and that doesn't hold. A command-line tool with excellent
documentation and no interface can be excellent at BLG and non-existent at PLG.
They aren't rungs of maturity; they're different addresses.

**Second, and this is the one that hurts: the two collide at concrete points.**
Progressive disclosure improves the human experience and worsens machine
legibility. Freemium designed for human conversion becomes uncapped cost when the
consumer is an agent. The signup wall that improves intent-signal capture is a hard
stop for the agent. These are design decisions where you have to choose, and
promising a frictionless sum would be dishonest.

**Third, in the budget argument.** That 58% of SaaS companies run some form of PLG
and around 91% intend to increase the investment
([UserGuiding](https://userguiding.com/blog/state-of-plg-in-saas)) is evidence PLG
is working for them, not that they should divert funds. And it's worth saying where
those two numbers come from: an onboarding-tool vendor and an investment firm, both
with a stake in the thesis, rather than independent survey work. The stronger argument for
BLG isn't redirecting budget. It's that there's a stretch of the funnel nobody is
measuring, and it doesn't sit with whoever runs PLG today.

## Where product-market fit moves

Back to the Superhuman method, because it shows the whole displacement inside a
single instrument.

The metric came from Sean Ellis himself, and it's a leading indicator rather than a
lagging one: ask how the person would feel without the product, and measure the
share answering "very disappointed". After benchmarking close to a hundred
companies, Ellis found the 40% threshold — below it, growth almost always stalled.
Superhuman started at 22%, rose to 33% simply by segmenting to the people who
already loved the product, and reached 58% in three quarters.

The engine has four steps, and the first is segmenting to find your supporters. The
second is the one that matters here: analyse the feedback from the ones on the
fence, and **politely disregard those who wouldn't be disappointed** — because
those people are too far away and distort the roadmap.

And it's in that second step that the method meets its limit on our terrain.

Under BLG there's an equivalent group that is **invisible**: the agents that tried
you and moved on with something else. They don't answer surveys, don't abandon
carts, don't cancel anything. The whole engine depends on comparing who loves you
with who almost loves you — and here you only see the ones already inside.

I don't have the answer to this, and I'd rather say so plainly: **what replaces the
fit survey when part of the sample is structurally out of reach?** If you have an
idea, that's the conversation I'd most like to have after this piece.

## A case to think through together

Linear reached a 1.25 billion dollar valuation in an 82 million Series C, in June
2025 ([Built In San
Francisco](https://www.builtinsf.com/articles/linear-raises-82m-series-c-1b-valuation-20250611)).
The founder, [Karri Saarinen](https://www.linkedin.com/in/karrisaarinen/), published the operating
numbers: net revenue retention above 140%, with a team of 70 at the company's sixth
anniversary ([on X](https://x.com/karrisaarinen/status/1880314177165869284)). I use
his source because it's primary, and because aggregators diverge widely on
headcount.

What circulates about their method includes four absences: no A/B tests, no work on
activation, no growth dashboards, no retention tactics.

Looking at those four together, they share something. **They are all instruments
for measuring and influencing human behaviour in aggregate.** A/B testing needs
many people to have statistical power. Activation work optimises one person's first
session. A growth dashboard tracks human steps through a funnel. Retention tactics
fight human churn.

The explanation usually given is culture, and it's plausible. Here's an alternative
reading, and I'll flag that from here on this is speculation of mine, with no
validation: the list of things dropped coincides with the list of what BLG predicts
will weaken once the decisive judgement stops being the aggregate of human
sessions.

And one containment, which is for us and not for them. Net revenue retention
measures expansion inside accounts that already exist. It's a strong number, and it
says nothing about candidacy — the stage where BLG claims the contest is settled.
Using it as proof of winning at the entrance would be taking evidence from one
stage to assert something about another. Worth registering too that whoever buys
that product is an engineering team, the human buyer closest to the machine there
is. A method can be very well fitted to that category without being superior in
general.

## What comes next

What this piece established: the one deciding is a pair; the progress being sought
hasn't changed much, but the process and the needs did, because a new hirer showed
up; and what PLG built survives almost whole, with five points where it stops
serving and a gate that came down a level.

What it didn't answer, and the following pieces try to: how that pair decides, step
by step; which forces act inside the decision and who operates them; what can be
done at each stage so that machine and person decide in your favour; and how all of
that shifts depending on who's on the other side.

I'll close with the question left open above, because it's the one that bothers me
most and the one I'm least able to answer alone: **how do you measure what you lost
to someone who never knew they were competing with you?**

---

*Second arc of the Builder-Led Growth series, by Matheus Ramos.*

*The first arc, for anyone who wants the full route:*

- *Part 1 — When the machine is also your customer: [read](01-when-the-machine-is-the-customer.md)*
- *Part 2 — The decision, the price and what to measure: [read](02-decision-price-and-measurement.md)*
- *Part 3 — The tax the machine charges and the human never sees: [read](03-machine-legibility.md)*
- *Part 4 — How many times the agent has to call a human: [read](04-operational-accessibility.md)*
- *Part 5 — The well everyone drinks from: [read](05-community-and-validation-signal.md)*
- *Part 6 — The machine is press and reader at once: [read](06-public-relations.md)*
- *Part 7 — What makes an agent trust you, and why its competence is the problem:
  [read](07-trust-and-safety.md)*
