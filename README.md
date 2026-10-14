# Visual Concept Director

Visual Concept Director is an [Agent Skill](https://agentskills.io/specification) for art direction and visual design work. It helps an agent turn a specific message, audience, and task into a deliberate visual concept, then make and inspect the requested result. It can guide UI and frontend implementation, websites, posters, cards, covers, banners, and advertising graphics. It is a set of instructions, not a design generator or a runtime package.

## Why it exists

A polished template can still fail to explain a product, direct attention, or express what makes a subject distinctive. This skill asks the agent to establish the idea before choosing a style. For a new independent design, it compares different semantic or interaction concepts, checks whether the result would still look the same with an unrelated subject, and chooses a direction that fits the audience and medium. Neutral templates remain valid when the task calls for neutrality.

It then defines the first, second, and third things a viewer should notice; plans composition, typography, spacing, and assets; and inspects the actual output. References are used to understand intent and constraints, with faithful reproduction when requested. Existing brand, product, and project conventions take precedence over the agent's aesthetic preferences.

For functional UI, concept-first means a clear user journey, meaningful controls, responsive reflow, accessible semantics and contrast, relevant states, and maintainable implementation. For expressive graphics, it allows stronger metaphor and composition while preserving exact copy, factual claims, supplied identity, and production constraints. A request to change one button or color is a local edit, not an invitation to redesign the page.

The skill is language-agnostic: it preserves user-provided visible text and follows the language, locale, and localization conventions of the user or project. It never changes content language merely because its instructions are written in English. Verification is evidence-based: an agent should inspect rendered UI or graphics when tools permit and identify what was not checked.

## When to use it

- “Design and implement a landing page for this product, using the existing brand and real copy.”
- “This dashboard feels generic. Rework the hierarchy and make the primary action clearer.”
- “Create a poster from this event text and these visual references.”
- “Make a social card that keeps the supplied headline and portrait intact.”
- “Adjust this button's color without changing the rest of the interface.”

It is not intended for backend-only changes with no visual result, data processing, repository maintenance, or requests that only need prose editing or translation.

## How it works

`SKILL.md` contains the shared principles and routes the agent to only the references relevant to the task. UI and frontend work loads `references/ui-product.md`; substantial art direction also loads `references/original-art-direction.md`. Static graphics load the complete art-direction foundation and `references/graphic-production.md`. Mixed deliverables use both specialist references. The optional `agents/openai.yaml` supplies Codex interface metadata. There are no runtime dependencies or bundled assets.

The same canonical `SKILL.md` and references are used by Codex, Claude Code, Cursor, Gemini CLI, and other clients that implement the Agent Skills format. The `agents/openai.yaml` file is optional client metadata; the core instructions do not depend on it. Each client controls its own discovery, activation, and tool access, so compatibility with the file format does not guarantee identical behavior.

```text
visual-concept-director/
├── SKILL.md
├── README.md
├── LICENSE
├── .gitignore
├── agents/
│   └── openai.yaml
├── scripts/
│   └── check_structure.py
└── references/
    ├── original-art-direction.md
    ├── ui-product.md
    └── graphic-production.md
```

## Installation

The primary distribution route is the [skills CLI](https://github.com/vercel-labs/skills). It requires Node.js and `npx`. Run these commands once the skill files are available on GitHub. With no agent flag, the CLI selects a detected agent or prompts for a target, depending on the environment.

```sh
# Choose an agent interactively for the current project
npx skills add cyberianin/Visual-Concept-Director

# Install for all projects for one agent
npx skills add cyberianin/Visual-Concept-Director -g -a codex
npx skills add cyberianin/Visual-Concept-Director -g -a claude-code
npx skills add cyberianin/Visual-Concept-Director -g -a cursor

# Install for Codex in the current project
npx skills add cyberianin/Visual-Concept-Director -a codex
```

Project installation is scoped to the directory where the command runs and is suitable for sharing with a project. Global installation is available across projects for the chosen agent. The CLI may use links to a canonical copy or copy files, depending on the selected method. To refresh an installed copy, run `npx skills update visual-concept-director` (use `-g` for a global installation or `-p` for a project installation). [CLI options and update behavior](https://github.com/vercel-labs/skills#other-commands).

Gemini CLI also has an [official skill installer](https://geminicli.com/docs/cli/using-agent-skills/). Its default scope is the user profile; use `--scope workspace` for only the current project:

```sh
gemini skills install https://github.com/cyberianin/Visual-Concept-Director
gemini skills install https://github.com/cyberianin/Visual-Concept-Director --scope workspace
```

### Manual Git installation

Clone the standalone skill repository directly into the agent's skill directory. This keeps the checkout updateable with `git pull`. These examples install for Codex; use `.claude/skills/visual-concept-director` or `.cursor/skills/visual-concept-director` for project installations in those agents, or their documented user directories for global use. Do not install the same skill in multiple discovery directories for one agent unless you intend to manage precedence.

Unix-like shell, project scope:

```sh
mkdir -p .agents/skills
git clone https://github.com/cyberianin/Visual-Concept-Director.git .agents/skills/visual-concept-director
```

Unix-like shell, global Codex scope:

```sh
mkdir -p ~/.codex/skills
git clone https://github.com/cyberianin/Visual-Concept-Director.git ~/.codex/skills/visual-concept-director
```

Windows PowerShell, project scope:

```powershell
New-Item -ItemType Directory -Force -Path '.agents\skills' | Out-Null
git clone https://github.com/cyberianin/Visual-Concept-Director.git '.agents\skills\visual-concept-director'
```

Windows PowerShell, global Codex scope:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.codex\skills" | Out-Null
git clone https://github.com/cyberianin/Visual-Concept-Director.git "$HOME\.codex\skills\visual-concept-director"
```

For manual installs, run `git pull` inside that cloned skill directory to update it. Restart or reload the agent's skill discovery if it does not see a newly installed skill. Manual installation paths and activation details can vary by client version; consult the relevant client's documentation.

## Usage

Ask naturally: “Build a responsive product page around this brief and inspect it at narrow and wide widths,” or “Create an event poster from this exact copy and photo, with a distinct visual idea.” Agents that support automatic skill selection may activate Visual Concept Director when the request matches its description. Discovery, activation, and consent behavior depend on the client and its settings.

Where explicit skill invocation is supported, include `$visual-concept-director` in the request, for example: “Use `$visual-concept-director` to improve this dashboard without changing its data or workflows.” Check your agent's syntax if it uses a different invocation form.

## Validation and limitations

The skill follows the [Agent Skills format](https://agentskills.io/specification). Run `python scripts/check_structure.py` to check the local layout and references without extra packages. From the parent directory, run `skills-ref validate visual-concept-director` to check frontmatter and naming with the official reference validator. From this repository's root, run `npx skills add . --list` to check discovery. None of these commands measures the quality of a generated design. Actual design outcomes depend on the agent, its tools, the supplied brief and assets, and inspection of the produced artifact.

## License

[MIT](LICENSE) © 2026 cyberianin.
