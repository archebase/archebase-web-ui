#!/usr/bin/env python3
"""Small deterministic checks for the ArcheBase Web UI skill bundle."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "NOTICE.md",
    "skill-dependencies.json",
    "templates/web-ui-brief.md",
    "templates/component-contract.yaml",
    "templates/decision-trace.md",
    "checklists/web-ui.md",
    "checklists/component.md",
    "evals/evals.json",
]
REQUIRED_REFS = [
    "references/architecture.md",
    "references/system-selection.md",
    "references/component-contract.md",
    "references/anti-slop.md",
    "references/motion-and-accessibility.md",
    "references/content-and-localization.md",
    "references/redesign-protocol.md",
    "references/evidence-and-provenance.md",
    "references/logo-operating-rules.md",
]

# Logo size, clear-space and spacing values are asset-derived upstream operating rules.
# A live doc may route to them but must never restate the number without the upstream reference.
LOGO_WORD = r"(?:logo|标志|图形标|组合标|favicon|app\s?icon|touch\s?icon|avatar|图标|\bmark\b)"
LOGO_METRIC = re.compile(
    rf"(?:{LOGO_WORD}[^。\n]{{0,40}}[0-9]+(?:\.[0-9]+)?\s?(?:px|mm|dp|pt|em))"
    rf"|(?:[0-9]+(?:\.[0-9]+)?\s?(?:px|mm|dp|pt|em)[^。\n]{{0,40}}{LOGO_WORD})",
    re.IGNORECASE,
)
UPSTREAM_RULE_REF = re.compile(r"references/logo-(?:usage-rules\.md|combination-matrix\.(?:md|json))")
SCAN_GLOBS = [
    "SKILL.md",
    "README.md",
    "NOTICE.md",
    "CHANGELOG.md",
    "references/*.md",
    "checklists/*.md",
    "templates/*.md",
    "templates/*.yaml",
    "skill-dependencies.json",
    "evals/evals.json",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def check_logo_metric_routing() -> list[str]:
    """Every Logo size/clear-space metric must route to an upstream operating-rule document."""
    violations: list[str] = []
    for pattern in SCAN_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            if not path.is_file():
                continue
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                match = LOGO_METRIC.search(line)
                if not match:
                    continue
                if UPSTREAM_RULE_REF.search(line) or "待确认" in line or "do not infer" in line.lower():
                    continue
                violations.append(f"{path.relative_to(ROOT)}:{number}: {match.group(0)}")
    return violations


def main() -> int:
    missing = [p for p in REQUIRED_FILES + REQUIRED_REFS if not (ROOT / p).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter = skill.split("---\n", 2)
    if len(frontmatter) < 3:
        fail("SKILL.md frontmatter is not closed")
    header = frontmatter[1]
    for key in ("name:", "description:", "license:", "metadata:", "core_max_lines:"):
        if not re.search(rf"^{re.escape(key)}", header, re.MULTILINE):
            fail(f"SKILL.md missing frontmatter key: {key}")
    body_lines = len(skill.splitlines())
    max_lines = int(re.search(r"^core_max_lines:\s*(\d+)", header, re.MULTILINE).group(1))
    if body_lines > max_lines:
        fail(f"SKILL.md has {body_lines} lines, over core_max_lines={max_lines}")
    if "archebase-vi-guide" not in skill or "archebase-visual-design" not in skill:
        fail("SKILL.md must declare both upstream skill dependencies")
    if "可发布" not in skill or "修复后复审" not in skill or "阻塞，待确认" not in skill:
        fail("SKILL.md must define all three release verdicts")

    deps = json.loads((ROOT / "skill-dependencies.json").read_text(encoding="utf-8"))
    if deps.get("schema_version") != 1 or len(deps.get("dependencies", [])) != 2:
        fail("skill-dependencies.json must contain schema_version=1 and exactly two dependencies")
    names = {d.get("name") for d in deps["dependencies"]}
    if names != {"archebase-vi-guide", "archebase-visual-design"}:
        fail("dependency names do not match the declared upstream skills")

    evals = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
    if evals.get("skill_name") != "archebase-web-ui" or len(evals.get("evals", [])) < 3:
        fail("evals/evals.json must name this skill and contain at least three cases")

    logo_violations = check_logo_metric_routing()
    if logo_violations:
        fail(
            "Logo size/clear-space metric without an upstream operating-rule reference "
            "(add references/logo-usage-rules.md or references/logo-combination-matrix.md on the same line, "
            "or mark it 待确认): " + "; ".join(logo_violations)
        )

    # This skill must not silently ship official brand assets.
    forbidden_dirs = ["assets/logos", "智域基石vi基础.pdf", "archebase-design-workspace"]
    for token in forbidden_dirs:
        if (ROOT / token).exists():
            fail(f"bundle must not copy proprietary upstream assets: {token}")

    print(
        f"PASS: {body_lines} SKILL.md lines; {len(REQUIRED_FILES + REQUIRED_REFS)} required files; "
        f"dependencies, evals and Logo metric routing valid"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
