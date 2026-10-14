"""Check local skill layout and referenced files; no third-party packages needed."""

from pathlib import Path
import re
import sys


root = Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
errors = []

if root.name != "visual-concept-director":
    errors.append("skill directory must be named visual-concept-director")

if not skill.is_file():
    errors.append("SKILL.md is missing")
else:
    content = skill.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", content, re.S)
    if not frontmatter:
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        header = frontmatter.group(1)
        if not re.search(r"(?m)^name: visual-concept-director$", header):
            errors.append("frontmatter name does not match directory")
        if not re.search(r"(?m)^description:\s*\S", header):
            errors.append("frontmatter description is missing")

for document in [skill, *sorted((root / "references").glob("*.md"))]:
    if not document.is_file():
        continue
    body = document.read_text(encoding="utf-8")
    for relative in set(re.findall(r"references/[a-z0-9-]+\.md", body)):
        if not (root / relative).is_file():
            errors.append(f"{document.relative_to(root)}: missing {relative}")

expected = {
    "references/original-art-direction.md",
    "references/ui-product.md",
    "references/graphic-production.md",
    "agents/openai.yaml",
    "LICENSE",
}
for relative in sorted(expected):
    if not (root / relative).is_file():
        errors.append(f"missing {relative}")

if errors:
    print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
    raise SystemExit(1)

print("Skill layout and local references: OK")
