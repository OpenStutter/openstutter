# OpenStutter — working notes for Claude

OpenStutter is a free, local-first macOS speech-assistance tool for people who stutter:
capture speech → produce a fluent version → speak it in the user's own cloned voice
through a virtual mic, so any app receives clean speech. Everything runs on-device.

- **Primary source of truth:** `docs/DIRECTION.md` (direction, architecture, flow, roadmap,
  decision log). Keep it updated as decisions are made; it wins over the brief on conflicts.
- **Original spec / background:** `docs/BRIEF.md`.
- **Planning rationale / history:** `docs/CONVERSATION.md`.
- These are starting points, **not** a contract. We change direction when there's a better
  approach — update `DIRECTION.md` deliberately rather than drifting.

## Who I'm working with (the maintainer)

- 17+ years as a software developer: databases, systems, infra, frontend. Has built
  production RAG apps, MCP servers, and agentic workflows.
- A few months of Python (FastAPI). **New to ML/PyTorch, audio/DSP, and research-style work.**
  This project is a deliberate learning curve for him.
- Strong engineering instincts — explain ML/audio concepts by analogy to backend/infra/
  systems ideas he already knows (services, streams/buffers, queues, cold-start, backpressure).

## How we work together

- **Include him in decisions.** Before making a non-trivial technical choice, explain *why*,
  with a brief pros/cons/tradeoffs. He wants to understand enough to read, judge, review, and
  write the code himself — not just accept conclusions.
- **Discuss approach and tooling before installing/implementing.** Don't charge into doing-mode;
  align first. (He stopped an install once to ask for exactly this.)
- He wants to **learn as we build** and code/experiment alongside me. Point to canonical docs
  and resources when introducing a new area.
- Be blunt and honest — pushback and reality-checks are welcomed over cheerleading.
- He dislikes endless planning once a decision is sound; balance teaching with momentum.
