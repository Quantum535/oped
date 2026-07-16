"""Reflow op-ed markdown for readable line width and polished structure."""

import re
import textwrap
from pathlib import Path

WRAP = 72
ARTICLES = Path(__file__).resolve().parent.parent / "articles"

FIX_INTRO_STARTERS = (
    "the fix is",
    "so finish it",
    "getting the sequence",
    "closing that void",
    "what has to happen",
    "here is how",
    "stopping this requires",
    'so the "how"',
    "so the single",
    "applied to breast",
    "none of this needs",
    "none of this waits",
)

LIST_PARAGRAPH = re.compile(
    r"^(First|Second|Third|Fourth|Fifth|Start with|Then invert|Then finish|Then the|Then |And fix)",
    re.I,
)

CLOSING_STARTERS = (
    "screening guidelines",
    "every year the current",
    "two out of three",
    "that symmetry",
    "a five-year survival",
    "the february 2026",
    "insurers'",
    "the skeptics were right",
    "the cause of the surge",
    "the test has never",
    "telling a woman",
    "the next century",
    "none of this is exotic",
)


def wrap(text: str) -> str:
    return textwrap.fill(text.strip(), width=WRAP)


def wrap_list_item(number: int, text: str) -> list[str]:
    """Return markdown list item lines with wrapped continuation."""
    prefix = f"{number}. "
    indent = " " * len(prefix)
    lines = textwrap.wrap(text.strip(), width=WRAP - len(indent))
    if not lines:
        return [prefix.strip()]
    result = [prefix + lines[0]]
    result.extend(indent + line for line in lines[1:])
    return result


def format_action_paragraph(para: str, number: int) -> list[str]:
    m = re.match(r"^((?:First|Second|Third|Fourth|Fifth),)\s*(.+)$", para, re.I | re.S)
    if m:
        rest = m.group(2).strip()
        dot = rest.find(". ")
        if dot == -1:
            lead = rest if rest.endswith(".") else rest + "."
            tail = ""
        else:
            lead, tail = rest[: dot + 1], rest[dot + 2 :].strip()
        lead = lead[0].upper() + lead[1:] if lead else lead
        body = f"**{lead}** {tail}" if tail else f"**{lead}**"
        return wrap_list_item(number, body)

    m = re.match(r"^((?:Start with|Then invert|Then finish|Then the|Then|And fix)[^.]*\.)", para, re.I)
    if m:
        lead = m.group(1)
        rest = para[len(lead) :].strip()
        body = f"**{lead}** {rest}" if rest else f"**{lead}**"
        return wrap_list_item(number, body)

    return wrap_list_item(number, para)


def parse_front_matter(text: str):
    if not text.startswith("---"):
        return "", text
    end = text.find("---", 3)
    if end == -1:
        return "", text
    return text[: end + 3], text[end + 3 :].lstrip("\n")


def split_paragraphs(body: str):
    paras = []
    current = []
    for line in body.splitlines():
        if line.strip() == "":
            if current:
                paras.append(" ".join(current))
                current = []
        elif line.startswith("#") or line.startswith("**By") or line.startswith("*By"):
            if current:
                paras.append(" ".join(current))
                current = []
            paras.append(line.strip())
        else:
            current.append(line.strip())
    if current:
        paras.append(" ".join(current))
    return paras


def is_fix_intro(para: str) -> bool:
    return para.lower().startswith(FIX_INTRO_STARTERS)


def is_closing(para: str, idx: int, total: int) -> bool:
    return idx == total - 1 and para.lower().startswith(CLOSING_STARTERS)


def format_article(path: Path):
    raw = path.read_text(encoding="utf-8")
    front, body = parse_front_matter(raw)
    items = split_paragraphs(body)

    out = [front, ""] if front else []
    i = 0
    in_actions = False
    action_number = 0

    while i < len(items):
        item = items[i]

        if item.startswith("#"):
            out.append(item)
            out.append("")
            i += 1
            continue

        if item.startswith("**By") or item.startswith("*By"):
            author = re.sub(r"^\*?By\s*", "", item.strip("* "))
            out.append(f"*By {author}*")
            out.append("")
            out.append("---")
            out.append("")
            i += 1
            continue

        if is_closing(item, i, len(items)):
            in_actions = False
            out.append("---")
            out.append("")
            out.append(wrap(item))
            i += 1
            continue

        if is_fix_intro(item):
            in_actions = True
            action_number = 0
            out.append("---")
            out.append("")
            out.append("## What to Do")
            out.append("")
            out.append(wrap(item))
            out.append("")
            i += 1
            continue

        if in_actions and LIST_PARAGRAPH.match(item):
            action_number += 1
            out.extend(format_action_paragraph(item, action_number))
            out.append("")
            i += 1
            continue

        if in_actions:
            in_actions = False
            out.append("")

        out.append(wrap(item))
        out.append("")
        i += 1

    while out and out[-1] == "":
        out.pop()

    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    long_lines = [ln for ln in out if len(ln) > WRAP + 10]
    print(f"{path.name}: {len(long_lines)} lines over {WRAP + 10} chars")


def main():
    for md in sorted(ARTICLES.glob("*.md")):
        format_article(md)


if __name__ == "__main__":
    main()
