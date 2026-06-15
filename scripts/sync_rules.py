#!/usr/bin/env python3
"""Materialize IDE-agnostic project rules into each supported IDE's native
rules directory.

Single source of truth:
    shared/rules/<slug>.md   (frontmatter: title / slug / activation / globs? / description + body)
        activation: always | glob   (default: always)
        globs:      comma-separated patterns (only when activation: glob)

Generated targets (do NOT hand-edit):
    .cursor/rules/<slug>.mdc     (Cursor rules; alwaysApply / globs)
    .windsurf/rules/<slug>.md    (Windsurf rules; trigger: always_on | glob)

Devin consumes project rules via AGENT_GUIDE.md (Rule Zero), so there is no
.devin/rules/ target — the old .devin/rules/ files used Windsurf's `trigger:`
syntax and are superseded by shared/rules/ + AGENT_GUIDE.md.

Usage:
    python scripts/sync_rules.py            # regenerate all IDE copies
    python scripts/sync_rules.py --check     # verify no drift (CI / pre-commit), exit 1 if stale

To add an IDE, append an entry to TARGETS with its filename suffix + render fn.
"""
from __future__ import annotations
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "shared", "rules")

GEN_NOTE = (
    "<!-- AUTO-GENERATED from {src}. Do not edit here; "
    "edit the source and run `python scripts/sync_rules.py`. -->"
)


def parse(text: str) -> tuple[dict[str, str], str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("missing frontmatter")
    fm_raw, body = m.group(1), m.group(2).lstrip("\n")
    fm: dict[str, str] = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, body.rstrip() + "\n"


def render_cursor(slug: str, fm: dict[str, str], body: str) -> str:
    note = GEN_NOTE.format(src=f"shared/rules/{slug}.md")
    always = fm.get("activation", "always") == "always"
    lines = [
        f"description: {fm.get('description', '')}",
        f"globs: {fm.get('globs', '')}",
        f"alwaysApply: {'true' if always else 'false'}",
    ]
    block = "---\n" + "\n".join(lines) + "\n---\n"
    return f"{block}\n{note}\n\n{body}"


def render_windsurf(slug: str, fm: dict[str, str], body: str) -> str:
    note = GEN_NOTE.format(src=f"shared/rules/{slug}.md")
    activation = fm.get("activation", "always")
    if activation == "glob":
        lines = ["trigger: glob", f"globs: {fm.get('globs', '')}"]
    else:
        lines = ["trigger: always_on"]
    block = "---\n" + "\n".join(lines) + "\n---\n"
    return f"{block}\n{note}\n\n{body}"


# Per-IDE materialization rules: output filename suffix + render function.
TARGETS = {
    "cursor": {"dir": ".cursor/rules", "ext": ".mdc", "render": render_cursor},
    "windsurf": {"dir": ".windsurf/rules", "ext": ".md", "render": render_windsurf},
}


def build() -> dict[str, str]:
    if not os.path.isdir(SRC):
        sys.exit(f"source dir not found: {SRC}")
    out: dict[str, str] = {}
    slugs = sorted(
        f[:-3]
        for f in os.listdir(SRC)
        if f.endswith(".md") and f != "README.md"
    )
    for slug in slugs:
        with open(os.path.join(SRC, slug + ".md"), encoding="utf-8") as f:
            fm, body = parse(f.read())
        for target in TARGETS.values():
            path = os.path.join(ROOT, target["dir"], slug + target["ext"])
            out[path] = target["render"](slug, fm, body)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="verify no drift; exit 1 if stale")
    args = ap.parse_args()

    out = build()
    drift = []
    for path, content in out.items():
        existing = None
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                existing = f.read()
        if existing != content:
            drift.append(path)
        if not args.check:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(content)

    if args.check:
        if drift:
            print("Rule IDE copies are OUT OF SYNC with shared/rules/:")
            for p in sorted(drift):
                print("   -", os.path.relpath(p, ROOT))
            print("Fix: python scripts/sync_rules.py")
            sys.exit(1)
        print(f"OK: {len(out)} generated rule files in sync across {len(TARGETS)} IDE targets.")
    else:
        print(f"Synced {len(out)} files across {len(TARGETS)} IDE targets "
              f"({', '.join(TARGETS)}).")


if __name__ == "__main__":
    main()
