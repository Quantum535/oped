"""Remove stigmatizing and harsh language from op-eds."""

from pathlib import Path

ARTICLES = Path(__file__).resolve().parent.parent / "articles"
README = Path(__file__).resolve().parent.parent / "README.md"

REPLACEMENTS = [
    ("The graveyard of screening history", "A familiar pattern in screening history"),
    ("a test that is seductive, expensive", "a test that is heavily marketed, expensive"),
    ("months of dread", "months of uncertainty"),
    ("sits scandalously underused", "remains far below clinical need"),
    ("collapses into cheerleading unless", "collapses into uncritical promotion unless"),
    ("THE ANSWER TO THE PSA MESS IS ONE BLOOD TEST AT 45", "THE PSA POLICY ANSWER IS ONE BLOOD TEST AT 45"),
    ("two camps shouting past each other", "two camps locked in opposition"),
    ("answered a genuine catastrophe:", "answered a period of widespread overtreatment:"),
    ("would never have killed them", "would never have caused them serious harm"),
    ("are killing patients while", "are causing preventable deaths while"),
    ("difference between medicine and paperwork", "difference between medicine and administrative counts"),
    ("keep funding billboards while", "keep funding screening volume metrics while"),
    ("a shrug dressed as realism", "a dismissal offered as realism"),
    ("that swallows patients in", "that loses patients in"),
    ("drug-pricing war to fight", "drug-pricing barriers to overcome"),
    ("wearing the costume of one", "functioning only as an incomplete version of one"),
    ("The reflex is to file", "The default assumption is to file"),
    ("positive result dies in an electronic inbox", "positive result remains unacted upon in an electronic inbox"),
    ("on the honor system", "without formal oversight"),
    ("turns fatal-stage lung cancer", "turns advanced-stage lung cancer"),
    ("hardened into a reflex:", "hardened into an automatic response:"),
    ("the flaw in the reflex", "the flaw in that response"),
    ("colorblindness is not neutrality", "race-blind policy is not neutrality"),
    ("the moral logic all support", "the equity logic all support"),
    ("before it kills", "before it advances"),
    ("THE ONLY CANCER SCREENING THAT REQUIRES A CONFESSION", "THE ONLY CANCER SCREENING THAT REQUIRES DISCLOSURE FIRST"),
    ("policy gates it behind confession", "policy gates it behind mandatory disclosure"),
    ("stigmatized disclosure rather than", "mandatory disclosure rather than"),
    ("gated behind a confession", "gated behind mandatory disclosure"),
    ("decades of moral weight", "a difficult personal history"),
    ("stigma checkpoint", "eligibility checkpoint"),
    ("Smoking carries social stigma that breast density", "Smoking history carries access barriers that breast density"),
    ("told to feel ashamed of before", "discouraged from discussing before"),
    ("depends on confession rather than", "depends on disclosure rather than"),
    ("system that punishes disclosure", "system that discourages disclosure"),
    ("The confession requirement is", "The disclosure requirement is"),
    ("There is nothing to justify", "No further explanation is required"),
    ("as a moral referendum on a patient's past", "as a prolonged review of a patient's past"),
    ("before stigma blocks the door", "before access barriers block the door"),
    ("need not justify past behavior", "need not provide additional documentation of past smoking"),
    ("You do not need to justify past smoking", "You do not need additional documentation of past smoking"),
    ("  - stigma", "  - uptake"),
    ("stigma-based disclosure", "barrier-based disclosure"),
]

README_REPLACEMENTS = [
    ("| 01 | [The Pack-Year Is Killing People]", "| 01 | [The Unregulated Pack-Year Formula]"),
    ("| 03 | [We Screen the Cancers We Don't Blame Patients For]", "| 03 | [The Only Screening That Requires Disclosure First]"),
    ("- [03 - Stigma, confession, and low uptake]", "- [03 - Disclosure barriers and low uptake]"),
]


def main():
    for path in sorted(ARTICLES.glob("*.md")):
        text = path.read_text(encoding="utf-8-sig")
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")
        print(f"Updated {path.name}")

    if README.exists():
        text = README.read_text(encoding="utf-8-sig")
        for old, new in README_REPLACEMENTS:
            text = text.replace(old, new)
        README.write_text(text, encoding="utf-8")
        print("Updated README.md")


if __name__ == "__main__":
    main()
