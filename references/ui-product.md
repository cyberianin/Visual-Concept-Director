# UI / Product / Frontend Execution

Use this reference for functioning interfaces, application mockups, websites, dashboards, product cards, forms, landing pages, and design systems. Translate the foundational principle—meaning before styling—into information architecture and behavior. Do not treat a functional product as a poster.

## Product before screen

Identify the user's primary job, expected inputs, intended result, and point of decision. Separate essential information from supporting and incidental information. Remove duplication; do not split the main action across multiple competing calls to action. The visual system should make the product's structure legible, not conceal the absence of one. Evaluate whether cards, tables, lists, tabs, sidebars, step-by-step flows, or a single-page flow are appropriate. None is mandatory.

For a new page, internally consider at least three distinct information-architecture or interaction concepts—not three CSS skins. For example, an infrastructure dashboard could prioritize an operational exception overview, a focused workspace for the current task, or a sequential diagnostic flow. Select one rather than building all directions in parallel. Preserve the established product model when making a narrow edit.

## Audit the existing project

Before editing, identify the actual framework, component architecture, styling conventions, UI library, icons, fonts, themes, grid, routes, data sources, and available verification commands. Read relevant source files and adjacent screens. Determine the invariants of public APIs, behavior, and the existing visual system. Reuse or deliberately adjust existing design tokens instead of introducing unexplained magic values. Do not refactor unrelated components or update dependencies without a concrete need.

## Build a coherent visual system

Define an intentional type scale, spacing rhythm, radii, separators, color roles, focus styles, and information density. A coherent system does not require identical cards everywhere: hierarchy may come from tables, forms, typography, whitespace, or layout. Distinguish interactive surfaces from static ones. Ensure real data, long copy, numbers, and metrics remain readable. Do not equate "premium" with gradients, glow, blur, or arbitrary shadows.

Establish one primary focal point per screen or local region, depending on context. For dense professional tools, optimize signal detection and scan paths. For editorial and marketing pages, optimize reading rhythm and meaning. Do not fabricate information to occupy empty areas. Do not substitute lorem ipsum for available real content.

## Behavior and edge states

Every element styled as a control must do something meaningful. Cover relevant loading, empty, error, success, disabled, hover, focus, active, and validation states; long strings; zero and extreme values; network failure; and permission denial when applicable. For asynchronous actions, represent progress and outcome and prevent accidental duplicate submissions. Define how the UI behaves with no data and with partial data. Never hide a critical action behind hover alone, or describe a placeholder as a completed integration.

## Responsive design, accessibility, localization

Check genuine reflow rather than only a desktop screenshot. Account for narrow viewports, large text, long localized labels, and browser zoom. Choose breakpoints based on content constraints rather than fashionable device widths. Avoid horizontal overflow, clipped calls to action, disappearing form labels, undersized touch targets, and overlapping fixed elements. Use semantic elements, associated form labels, visible keyboard focus, logical tab order, accessible control names, and keyboard operability. Follow WCAG AA contrast guidance where applicable: 4.5:1 for normal text and 3:1 for large text and required non-text UI indicators. Respect reduced-motion settings, writing direction, number formatting, and locale-specific dates. Do not add theme or language toggles by default; when requested, implement their real states and behavior. Preserve the user's language and any exact strings required by the project.

## Performance and engineering discipline

Do not sacrifice initial render performance for excessive animation, unnecessary client JavaScript, huge background images, 3D scenes, or stacked blur effects without clear benefit. Prefer the established stack, shared tokens, and simple DOM/CSS composition. Guard against layout shifts, load below-the-fold assets lazily when appropriate, size images correctly, handle failures, and use memoization only when it addresses demonstrated work. Consider the bundle and maintenance cost of new dependencies. Real behavior and semantics take priority over a convincing but fake UI.

## Validate the shipped interface

When a runnable environment is available, launch the project and inspect actual routes, console output, network behavior, key actions, and form submission. Inspect at least a narrow and wide viewport on the rendered UI; test relevant empty/error states, contrast, keyboard paths, overflow, and regressions in neighboring components. Run existing tests, type checks, and lint when available, but do not treat passing them as a substitute for visual inspection. Explicitly identify checks that could not be performed. Never call a static mockup a finished application.
