"""Fix awkward comma replacements after em dash removal."""

import re
from pathlib import Path

ARTICLES = Path(__file__).resolve().parent.parent / "articles"

SENTENCE_BREAKS = [
    ("they do, and the fix", "they do. The fix"),
    ("decade, and the way out", "decade. The way out"),
    ("detection, and while the", "detection. While the"),
    ("crack, and a positive result", "crack. A positive result"),
    ("mandate, and the answer arrives", "mandate. The answer arrives"),
    ("hypothesis, and hypotheses with", "hypothesis. Hypotheses with"),
    ("failure lives, and early detection", "failure lives. Early detection"),
    ("waiting, and Medicare's", "waiting. Medicare's"),
    ("cancer, abnormal mammograms", "cancer. Abnormal mammograms"),
    ("arrives, enormous enthusiasm", "arrives: enormous enthusiasm"),
    ("48%, the share of the world's cancer", "48% (the share of the world's cancer"),
    ("deaths that were avoidable, and however", "deaths that were avoidable) and however"),
    ("prostate cancer, for all men", "prostate cancer for all men"),
    ("idea, it was a patient's", "idea: it was a patient's"),
    ("finish it, with four changes", "finish it: with four changes"),
    ("immediately, it is the rare", "immediately: it is the rare"),
    ("experiment, the modelling is", "experiment: the modelling is"),
    ("2021, the right call", "2021: the right call"),
    ("clock, a young patient's", "clock: a young patient's"),
    ("subgroup, the JNCI authors", "subgroup: the JNCI authors"),
    ("reversal, a grade C", "reversal (a grade C"),
    ("rested on, the major American", "rested on: the major American"),
    ("asymmetry, the bar for", "asymmetry: the bar for"),
    ("cancers, the ones that surface", "cancers (the ones that surface"),
    ("rounds, fell by half", "rounds) fell by half"),
    ("tissue, the DENSE trial's", "tissue (the DENSE trial's"),
    ("highest, then expand", "highest), then expand"),
    ("show, was not designed to show, is whether", "show (and was not designed to show) is whether"),
    ("show real benefit, adopt fast, the same", "show real benefit, adopt fast: the same"),
    ("entirely, the race-blind approach", "entirely (the race-blind approach"),
    ("fairness, made the disparity", "fairness) made the disparity"),
    ("person, not a portal notification, a person, to", "person (not a portal notification, a person) to"),
    ("impossible, the drugs cost", "impossible: the drugs cost"),
]


def main():
    for path in sorted(ARTICLES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        text = text.replace(" ,", ",")
        for old, new in SENTENCE_BREAKS:
            text = text.replace(old, new)
        text = re.sub(r",\s+,", ", ", text)
        path.write_text(text, encoding="utf-8")
        print(path.name)


if __name__ == "__main__":
    main()
