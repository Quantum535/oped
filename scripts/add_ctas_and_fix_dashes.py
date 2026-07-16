"""Remove em dashes and append Take Action CTAs to each op-ed."""

import re
from pathlib import Path

ARTICLES = Path(__file__).resolve().parent.parent / "articles"

CTAS = {
    "01-pack-year-lung-screening.md": (
        "If you have a smoking history, ask your clinician whether you qualify "
        "for lung cancer screening under a validated risk model, not just the "
        "pack-year cutoff. Hospital leaders and Medicare policymakers should "
        "require the same post-market accountability for eligibility formulas "
        "that we already demand of the scanners themselves."
    ),
    "02-racial-math-lung-screening.md": (
        "If you lead a health system, audit this quarter how many eligible Black "
        "and white patients your lung screening criteria actually flag. Guideline "
        "bodies should adopt race-calibrated thresholds now and publish subgroup "
        "performance for every screening algorithm before it reaches patients."
    ),
    "03-lung-screening-stigma.md": (
        "If you smoked, you may already qualify for a lung scan. Ask for the "
        "referral directly. Clinicians and Medicare administrators should remove "
        "the confession checkpoint: capture smoking history once in the record, "
        "mail the invitation, and treat lung screening like every other cancer "
        "test we actually deliver."
    ),
    "04-breast-cancer-global-survival.md": (
        "Funders and health ministers should tie every breast cancer dollar to "
        "outcomes: early-stage diagnosis, workup within 60 days, and treatment "
        "completion. No new screening rollout without a funded treatment path "
        "already in place. The PEPFAR playbook exists. Apply it."
    ),
    "05-cervical-cancer-elimination.md": (
        "Health ministries that have not switched to single-dose HPV vaccination "
        "should do it now. Donors at Gavi and the Global Fund should fund cervical "
        "cancer elimination as a multi-decade line item, not another pilot. "
        "Elimination is a budget decision, and the price has already dropped."
    ),
    "06-global-cancer-aid-metrics.md": (
        "Every global cancer program should publish one number: days from positive "
        "screen to first treatment. Funders should withhold scale-up money until "
        "a financed treatment endpoint exists in the referral network. Measure "
        "the bridge, not the billboard."
    ),
    "07-young-onset-colorectal-cancer.md": (
        "If you are 45 or older, get screened on schedule. If you have rectal "
        "bleeding, anemia, or persistent bowel changes at any age, insist on a "
        "timely workup. Payers and health systems should adopt a red-flag clock "
        "with public reporting, and wire family history in the chart to earlier "
        "screening automatically."
    ),
    "08-prostate-psa-baseline.md": (
        "Men at average risk should discuss a baseline PSA at 45. Black men and "
        "men with family history should start at 40. The USPSTF should re-review "
        "screening using modern harm data and adopt risk-stratified follow-up, "
        "not a blanket yes or no."
    ),
    "09-positive-test-follow-up.md": (
        "If your stool test is positive, book the colonoscopy now and ask whether "
        "follow-up is covered without cost-sharing. Hospital executives and CMS "
        "should report follow-up completion within 90 days, bundle payment around "
        "the full screening episode, and fund navigators who close the loop."
    ),
    "10-breast-density-follow-up.md": (
        "If your mammogram report says you have dense breasts, ask what supplemental "
        "imaging you need and what it will cost. Tell your representatives to pass "
        "the Find It Early Act so the federally mandated warning comes with a "
        "covered next step, not a thousand-dollar invoice."
    ),
    "11-mced-galleri-evidence.md": (
        "Do not skip colonoscopy, mammography, or any proven screening for a multi-"
        "cancer blood test that has not yet shown it saves lives. Tell Congress to "
        "withhold a Medicare benefit category until FDA approval and mortality "
        "evidence are in. If the NHS trial shows benefit, adopt fast. Until then, "
        "demand answers before billions in coverage."
    ),
}


def replace_em_dashes(text: str) -> str:
    text = text.replace("\u2014", ", ")

    # Fix common awkward comma inserts
    fixes = [
        (r", including pancreatic", ", including pancreatic"),
        (r"cancer, for all men", "cancer for all men"),
        (r"services\", in plain", "services,\" in plain"),
        (r"qualify, there is nothing", "qualify: there is nothing"),
        (r"letter, \"you qualify", "letter: \"you qualify"),
        (r"number\", exactly", "number,\" exactly"),
        (r"outcomes, and waiting, and Medicare", "outcomes, and waiting. Medicare"),
        (r"they do, and the fix", "they do. The fix"),
        (r"fairness, made the disparity", "fairness, made the disparity"),
        (r"lung function, and often rightly", "lung function, and often rightly"),
        (r"countries, confirmed the gap", "countries, confirmed the gap"),
        (r"workforce, and no one", "workforce, and no one"),
        (r"visit, disappears", "visit, disappears"),
        (r"room, no referral", "room: no referral"),
        (r"avoidable\", and \"unequal\"", "avoidable\" and \"unequal\""),
        (r"deaths, 4\.5 million, 48%, were", "deaths, 4.5 million (48%) were"),
        (r"deaths, breast and cervical cancer above all, cluster", "deaths (breast and cervical cancer above all) cluster"),
        (r"readers, have gotten", "readers, have gotten"),
        (r"money moves, time-limited", "money moves: time-limited"),
        (r"deployed, activity metrics", "deployed: activity metrics"),
        (r"initiation, how long", "initiation: how long"),
        (r"network, the oncology", "network, the oncology"),
        (r"48%, the share", "48% (the share"),
        (r"avoidable, and however", "avoidable) and however"),
        (r"failure lives, and early", "failure lives. Early"),
        (r"years, one to two percent", "years: one to two percent"),
        (r"running, and the", "running, and the"),
        (r"exposure, all under", "exposure, all under"),
        (r"detection, and while", "detection. While"),
        (r"2021, the right call", "2021: the right call"),
        (r"suggestion, a mailed", "suggestion: a mailed"),
        (r"no clock, a young", "no clock: a young"),
        (r"something, an automatic", "something: an automatic"),
        (r"fires, three fixes", "fires: three fixes"),
        (r"prostate cancer, five-year", "prostate cancer: five-year"),
        (r"localized, rose", "localized, rose"),
        (r"decade, and the way", "decade. The way"),
        (r"radiation, incontinence", "radiation: incontinence"),
        (r"reversal, a grade C", "reversal (a grade C"),
        (r"your doctor\", priced", "your doctor\") priced"),
        (r"cancer, his lifetime", "cancer: his lifetime"),
        (r"minority, who go on", "minority, who go on"),
        (r"deaths, get watched", "deaths, get watched"),
        (r"rested on, the major", "rested on: the major"),
        (r"framework, baseline-at-40", "framework: baseline-at-40"),
        (r"history, would build", "history, would build"),
        (r"asymmetry, the bar", "asymmetry: the bar"),
        (r"returned, full credit", "returned: full credit"),
        (r"complete, even if", "complete, even if"),
        (r"finish it, with four", "finish it: with four"),
        (r"Create one, follow-up", "Create one: follow-up"),
        (r"stool test, publicly", "stool test, publicly"),
        (r"person, not a portal", "person, not a portal"),
        (r"person, to shepherd", "person, to shepherd"),
        (r"decline, not generate", "decline, not generate"),
        (r"cancer, abnormal mammograms", "cancer. Abnormal mammograms"),
        (r"crack, and a positive", "crack. A positive"),
        (r"cancer, mammography's", "cancer: mammography's"),
        (r"cancers, the ones", "cancers (the ones"),
        (r"rounds, fell", "rounds) fell"),
        (r"idea, it was", "idea: it was"),
        (r"job, and why", "job, and why"),
        (r"MRI, a stripped-down", "MRI, a stripped-down"),
        (r"forty, detected", "forty, detected"),
        (r"tissue, the DENSE", "tissue (the DENSE"),
        (r"highest, then expand", "highest), then expand"),
        (r"trial, true", "trial, true"),
        (r"mandate, and the answer", "mandate. The answer"),
        (r"once, including pancreatic", "once, including pancreatic"),
        (r"show, was not designed to show, is whether", "show (and was not designed to show) is whether"),
        (r"trial, more than 200,000", "trial: more than 200,000"),
        (r"sequencing, because", "sequencing, because"),
        (r"arrives, enormous", "arrives: enormous"),
        (r"pathway, implying billions", "pathway, implying billions"),
        (r"spending, before", "spending, before"),
        (r"outcomes, with coverage-with-evidence", "outcomes, with coverage-with-evidence"),
        (r"screening, because", "screening, because"),
        (r"directions\.", "directions."),
        (r"screening, lung, colorectal, cervical, sits", "screening (lung, colorectal, cervical) sits"),
        (r"hypothesis, and hypotheses", "hypothesis. Hypotheses"),
        (r"device, tested", "device, tested"),
        (r"improvement, produced", "improvement, produced"),
        (r"analysis, they are", "analysis, they are"),
        (r"history, family history, already sit", "history, family history) already sit"),
        (r"history, 65% of them Black, through", "history (65% of them Black) through"),
        (r"entirely, the race-blind", "entirely (the race-blind"),
        (r"fairness, made", "fairness) made"),
        (r"way, by replacing", "way: by replacing"),
        (r"subgroup, the JNCI", "subgroup: the JNCI"),
        (r"weight, one that", "weight: one that"),
        (r"path, running", "path: running"),
        (r"pressure, not re-excavated", "pressure, not re-excavated"),
        (r"digits, for a disease", "digits, for a disease"),
        (r"curable, and whether", "curable, and whether"),
        (r"together, screening without", "together: screening without"),
        (r"impossible, the drugs", "impossible: the drugs"),
        (r"targets, 60% of", "targets: 60% of"),
        (r"treatment, and funders", "treatment, and funders"),
        (r"redrawn, deliberately", "redrawn, deliberately"),
        (r"immediately, it is", "immediately: it is"),
        (r"experiment, the modelling", "experiment: the modelling"),
    ]

    for old, new in fixes:
        text = text.replace(old, new)

    text = re.sub(r",\s+,", ", ", text)
    text = re.sub(r"  +", " ", text)
    return text


def append_cta(text: str, cta: str) -> str:
    if "## Take Action" in text:
        return text

    cta_block = (
        "\n\n---\n\n"
        "## Take Action\n\n"
        f"{wrap_cta(cta)}\n"
    )

    return text.rstrip() + cta_block


def wrap_cta(cta: str) -> str:
    import textwrap

    return textwrap.fill(cta, width=72)


def main():
    for path in sorted(ARTICLES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        text = replace_em_dashes(text)
        text = append_cta(text, CTAS[path.name])
        path.write_text(text, encoding="utf-8")
        assert "\u2014" not in text, f"Em dash remains in {path.name}"
        print(f"Updated {path.name}")


if __name__ == "__main__":
    main()
