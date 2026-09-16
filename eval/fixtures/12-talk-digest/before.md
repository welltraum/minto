<!-- Fixture modeled on real usage: a single long spoken source (a conference talk
     transcript) digested to its key thought and what it rests on. The text is a
     condensed English translation of a public 2026 conference talk on agent-driven
     development; filler and repetitions of the spoken original are removed, every
     figure, example and claim is kept. The speaker is anonymized; one company named
     in an example is replaced by "a large marketplace". Tool and method names
     (Cursor, Jira, MCP, ReAct, IDEF0, ML System Design Doc) are as spoken. -->

# Fixture 12: talk digest

**Mode:** `digest`
**Language:** `en`

## Context

You are assisting the head of engineering at a product company whose teams started
working with coding agents this year. They did not watch the talk below and will
not; next week they run a process review and must decide which of the speaker's
claims, if any, to bring to it. The speaker is an outsider — a year earlier they
took over an AI engineering unit at a software consultancy — so nothing in the talk
is to be taken on authority; the reader wants to know what the speaker claims and
what each claim rests on.

## Before

Auto-generated transcript of a 26-minute conference talk, cleaned of filler.
Bracketed markers are minutes from the start.

```text
[00:00] Good afternoon. Briefly about myself: a year ago I took the position of
technical director, then head of AI, at our company. We started assembling teams
and building new processes from scratch, working out how they change when you
develop systems with AI. Today I want to share that experience and the pains I ran
into. We will look at
how AI helps in the classical setting, where we build ordinary services with a
coding assistant; then at how the process itself changes when what we build is an
agent system — it looks like the same development, but it is not; and at the end we
will speculate a little about the future.

The theme I want to concentrate on: where is the 10x acceleration we were promised
about a year ago? Those of you who measure know that a tenfold increase did not
happen. The market ran into many problems,
and I kept asking myself what stopped us. I split the SDLC into two approaches:
first, building classical systems without AI inside, but with AI as an assistant.

[00:02] First experience. Around summer we assembled our own teams, started
developing, and bought everyone a Cursor subscription so everyone would start
coding. A question for you: what do you think was the most popular mode of use? They called it "auto". Most
users did not try to look inside and understand what was happening; they took the
default settings and worked with those. The conclusion we drew: one tool is not
enough. There are now approaches to configuring an agent properly — Plan/Act
approaches. You have to understand what an agent is, because for it to work well
it has to be set up: how it works with MCP servers, which skills to plug in, and so
on. And the last point: if you have developers who sat down to write with AI only
today, then despite all the information we have and everything we roll out, they
still need time to master it — three to six months, depending on how ready they
are to dive in. I know cases in international companies where there was talk of
banning developers from using the old IDE, so that they would switch to this and
start learning, because the resistance is large. Such experiments were at least
proposed; I do not know whether they were run.

[00:04] Naturally, the simplest path is training. Thanks to the people at
Anthropic and OpenAI — they have a huge amount of material you can teach from. We
also built a whole course on agentic development inside the company and now help
every employee master the new technology. But the resistance remains, I warn you
up front. Next: why the resistance? The price of code has dropped below any level.
A line of code costs nothing now. It was falling all along; now it has fallen
sharply. But developers who build systems watch very fiercely what happens in
there. We have the notion of clean architecture; we split code into components; we
make sure nothing crawls where it should not; we look at the code all the time. In
the era of coding agents that became impossible. I cannot imagine watching line by
line what is happening now, especially when you see it generate endless pieces of
code and fix them. And from this, patterns emerge. First: we move up to the level
of management. Everyone who understands well what is happening under the hood
starts managing agents. There is a small case here: I do not quite understand how
juniors are supposed to live in this. A manager's position is a position of
maturity — you understand what is under the hood, you can rise to the level of
giving others commands. How young developers enter this kind of development, where
you have to manage agents that do who knows what, remains an open question. And,
like it or not, the only way out today is still

[00:06] to teach that we hold certain control points. Everything related to
changing contracts, APIs, and the database — that is the foundation everything
stands on. Around it the code can dance left and right; that is not so frightening.
What is frightening is losing control of the points we are accountable for. Today I
cannot entrust those to agents. I have a real-life example of why, which I will
tell later. Next. Imagine a manager who is now told: "Here is your tech lead, you
have a black box, the rest of the developers are building something with these
agents." What is actually going on? How do you control it? The mistake, in my
view, is to start thinking up new restrictions. The most vivid example I have met:
"We will put an agent into CI/CD that reviews all our developers who write code
with an agent." That is a classic; a large marketplace presented exactly this
recently. What is the flaw? Sure, it is great: it
checks, it starts piling comments on us, and we go and read those comments. That is
not needed, because our code is written by an agent. If an agent reviews, it should
pass that information not to people but to the coding agents themselves. So at some
point we have to arrive at a paradigm — and we are slowly moving there — where
everything that happens inside an application where agents work

[00:08] falls on the agent's role. The human stands outside and says: "Here are my
requirements, here is what I want to get," and looks at the results — a set of
unit tests or something else. Inside, the agent checks how the UI looks, how the
code is written, what happens in the database; all of that falls on it. A little
about feedback. I have an engineering background — I worked on systems for
aircraft, where there is the notion of a feedback system. When an aircraft flies,
it constantly drifts off course and has to be corrected all the time, and there are
mechanisms that collect that feedback. To do it well you install very expensive
instruments, gyroscopes and accelerometers. If we want it to fly autonomously in
space, we install expensive systems; but with GPS, an external source, the machine
can move on very cheap instruments, because it is corrected from the outside all
the time. Here the human is that external source. We are now in the situation where
feedback is being implemented, and our task is to understand how actively we take
part in the correction. There is a household example we worked out with GPT.
Anyone with underfloor heating knows it is regulated: you set 20 degrees and it is
comfortable. But imagine you have just come back from a run. The same 20 degrees is
hot for you; you want it cooler. The agent does not know that; it needs information
from the outside world. And here the human steps in.

[00:10] I am trying to focus you on this: it cannot be done without a human, but we
must give agents a fairly large autonomy. Next, something that has fired brightly
many times — I kept tripping over it. Classical Agile, which was supposed to speed
us up, slows us down today: the handoffs. Imagine analysts, developers, product
people, each working with an agent — absolutely everyone. Each now works several
times faster: the developer finished in two hours, the analyst finished the
analysis in half an hour. But the transfer of responsibility along the classical
process takes time — waiting time, handoff time. The second element, from a real
case: we decided to live by Agile and build agents, and ran into this — if people
poorly understand what an agent is, it is a new thing to work with, and it is
easier for them to do what they know. A person always finds it easier to do what
they know, so they start filing tasks in Jira and writing requirements, but not
writing agents. That process helps do anything at all except what is needed — at
least where we do not understand how to move forward. What replaced it today is the
era of product engineers. Many people are breaking through who take the whole
development process on themselves, from inventing the idea to implementation, and
with them the speed is incredible. In our company we kept running into this: a
classical team can go a month without writing a single line of code, getting
carried away with all sorts of other things. And a good product engineer assembles
a mobile app and a website in a couple of days and can live with that

[00:12] and keep going. That is a mad gap. But there are few such product
engineers, and you have to live somehow. The world has come to T-shaped-ness. Many
large companies are cutting Agile teams down to two or three people who split
certain roles among themselves but each covers more than before. That is today's
way out of a situation where you really have to move fast and live in uncertainty.
I cannot say it is the ideal option yet, but it works. To summarize development of
systems using AI: we ran into people not being ready to work with these new tools,
trying to live by the old rules. I periodically met
teams who considered unit tests optional. That is nonsense even now, but with
agents it becomes impossible to live. An agent without feedback cannot exist. It
needs to constantly check how the code executes, what happens in the browser, what
happens on the server, what errors come from users. If we give it all of that as
feedback, it starts to understand well how our system works and can correct it
without us.

Let us move on to probabilistic systems. I will concentrate on agent systems here —
we have done both. Who do you think should develop agents? Honestly — our classical
roles.

[00:14] because if you give it to backend developers, they start writing
frameworks. We gave backenders the task several times: they build their own
frameworks, they do not want to take the unfinished open-source ones; they build
their frameworks for several months and nothing comes of it. A good option, you
would think: we have AI engineers — they are agents, everything is fine. I walked
into one team: a product manager and an NLP engineer. I looked at the backlog:
authorization, integration, database work. I asked: "Where is the agent?" The NLP
engineer was doing all that plumbing, and the manager did not understand why he
could not cope with the task — after all he has a coding agent, he is an NLP
engineer, done. In many companies either classical teams are tried — we have a good
Java team, let us give it to them by inertia, let them write — or there are
enthusiasts who try to push it all forward on their own. Here is where I want you
to concentrate. An agent
consists of two parts. The first is the engineering approach: it has integrations,
it must understand what MCP is, what the pitfalls are. And a big question is now
arising about access rights, because a third actor has appeared: we know how a user
uses a system; what about an agent, what rights should it have? Everyone is
improvising a bit. These are the tasks usually put on developers and DevOps
engineers, and infrastructure — where to deploy agents. But an agent is a
probabilistic system, and it has another side. We have to collect datasets of the
questions we

[00:16] ask it, set up benchmarks, measure metrics, develop methodologies for
measuring business metrics. That is research work; a backend developer does not
know how to live with it. So today, if you think about it, one role is not enough
to make agents. You need two roles. If one person has both, you get a superhuman
who can build these agents without problems. If you have no such person, you need
two. Next, a pain I really ran into. Has anyone tried to describe, from an
analyst's point of view, what an agent is and how it should integrate? I saw the
poor eyes of analysts trying to describe agents with everything they had been
taught classically. Neither the business nor the team understands them; everyone
gets lost. Usually the task is: "Let us make an analyst agent." "And what will it
do?" "Well — an analyst. Let us think about it as a team." And these ideas start
between teams, everyone inventing their own way. When we broke it down inside everyone draws
agents differently. I split it into two parts. What do we have? Control points that
let us manage the agent: prompts, skills, its loop — the agentic cycle that lets it
exist, usually ReAct or its analogues. And integration with the outside world:
memory, subagents and the like. And we understand there is something on the input

[00:18] and something on the output. That maps very well onto the IDEF0
methodology of business analysis, which describes what a business function is. When
we start talking to analysts — let us talk not about agents but about the business
functions we want to automate for the client — it becomes much easier to
communicate with the client. He knows what business processes are, what business
functions are. It becomes easy to talk to the team. In my experience we really moved
teams from zero this way. A team comes to me and says: "We do not know where to
start." They want an analyst agent or a raw-materials agent — what to do? I say:
"Let us write out the business functions there are, and think a little about which
integrations and tasks it should have." And that moves teams off the dead point.
Second case: we came to an agent that had about a hundred tools. It was powerful,
it could do everything — and did nothing well. The open-source assistants of that
kind are similar. When we started breaking it down into the functions it should
perform, we understood how much extra had been piled on it, and we could calmly cut
and say "we do not need this, we do not need this," and simplify the ideology. The next pain I
experienced when we lived in an Agile process and developed

[00:20] agents. The manager says: "Hooray, the
agent exists, it works." It is quick to write. Then we look at what questions users
ask; the agent does not cope; "it must be fixed." And he starts writing these
errors into Jira: this query is bad, this query is bad, this query is bad. And the
team stalls. The engineers — the researchers — do not understand what to do with
these bugs in Jira, how to code them one by one. The managers think it is all
normal: the engineers just did not manage. But in fact a research process has
appeared inside the classical development process, marked in grey here. Developing
agents by the classical scheme, there is a cycle of experiments with that agent
inside, to bring it to certain metrics. The agent's errors are data collection for
improving its evaluation — we will assemble benchmarks and so on. Many managers used
to classical development turned out to be unready for this. What appears for them
now? Before, they thought: "A sprint — ten features. Great, let us do it." Now a
sprint is not only ten features but also ten experiments, or ten hypotheses. How do
you prove those ten hypotheses to the client — what worked, what did not? Teams that develop agent systems, or systems tied to LLMs, run into
this. How to live with it? Clearly it has to be introduced and measured: we and
the business must understand what tasks it has, what the business metrics are,
learn to measure them, have a platform for measuring metrics, and

[00:22] learn to talk to the client in the language of hypotheses: "We will test
this many hypotheses; something will work, something will not." A tool that
helped us a lot last year is the ML System Design Doc. We applied it in exactly these research processes. The most useful thing:
we can record all our experiments there, and the client we work with sees all our
work; we understand why we agreed to do this and why we did not agree to that.
Very useful, but it requires a certain culture of keeping the document. The last
thing I wanted to talk about from the SDLC point of view: we are used to building
systems for people. We even make agents now for people — services and so on. But
look closer: the agent is a new actor. It connects to services, it connects to
other agents, it connects to the outside world through tools. And our services are
very much not ready for it. We are thinking about this, and I urge you to think
too: what does it mean for the services you work with? An agent has appeared, a
new actor; it needs new entry points; it must interact differently. How does it
interact with the user? What about security? Imagine a person has an assistant
agent that shops for them; a retailer has released an MCP server and says "buy
from our store." What if that agent is compromised? How do you defend against it?
How do you help the user

[00:24] whose agent is compromised? These are new tasks that are appearing now.
You can only solve them, think about them — or not give the user an agent, which
is hardly an option; everyone wants Jarvis. I have no right answers yet. The big
people at OpenAI talk a lot about harness — that is exactly this theme, automating
everything for agents. A new creature has appeared, and services have to be made
for it — not for the human, for the agent. Here are our conclusions, what I want to
concentrate on precisely. Most important: an agent has a dualism, as I put it — you
have to solve engineering tasks and research tasks at once, which is why a research
cycle appears in development. Agents have to be described somehow, and things have
to be developed for them. And in the production process it is all the same: Jira is
a convenient tool for a human, but for an agent it is not very convenient; you have
to do certain contortions. Looking at all of this and where we are heading, we can
speculate a little about what the production process will be in the future. Our
thesis: the agent has become a new component we have to be friends with. The
human's role has shifted: the human is responsible for exploring the boundaries. We
stop watching lines of code; we are no longer interested in what happens with them.
It is like assembler: code goes into assembler and none of us looks at it any more.
We start to become a little

[00:26] like researchers. It is no longer enough to be just an engineer; we have to
research a little, develop in that direction. We now
work around context: that is all our pain; any agent becomes smart only from the
context it works with. Thinking about this, one idea I have is that people will
remain only to maintain the agent layer that does the developing. Product owners
throw ideas into the agent layer, which develops features. Most likely QA will
still answer for quality at the end. But the main task of people will be to
maintain that agent layer: they will develop UI kits so the picture stays coherent,
certain skills, watch the infrastructure to some degree — that the database does not
balloon, that it does not eat too much. We had a case: a product owner deployed an
open-source assistant and was happily experimenting with it; the disk ran out; but
it is smart, so it cleaned up all its skills on its own and deleted all its memory.
That has to be watched and helped. For that you need a team. In fact all the
development and all the experiments can already be done automatically; only a few
things have to be tightened here and there, and we will get it. So — we started
today with 10x acceleration. Probably the main conclusion is that the only one
standing in the way of that acceleration is the human. The human has to find their
new place in this development process, because agents already cope quite well.
```

## Task

Give the reader a digest of this talk in chat: its key thought and what it rests
on. The reader will decide from your digest which of the speaker's claims to bring
to next week's process review.
