"""Rewrite openings and closings as health policy pleas."""

import re
from pathlib import Path

ARTICLES = Path(__file__).resolve().parent.parent / "articles"

OPENINGS = {
    "01-pack-year-lung-screening.md": (
        "The U.S. Preventive Services Task Force and the Centers for Medicare and "
        "Medicaid Services regulate the lung cancer scanner but not the formula that "
        "decides who may use it. A patient who falls one pack-year short of the cutoff "
        "can be denied a scan and later diagnosed at stage IV with a cancer the "
        "technology might have caught at stage I."
    ),
    "02-racial-math-lung-screening.md": (
        "Guideline bodies across American medicine apply lung screening rules that "
        "flag Black patients' future cancers at rates as low as 46 percent while "
        "catching 72 to 80 percent of white patients in the same cohort. This is not "
        "a failure of patient behavior. It is a failure of policy that has not "
        "required subgroup accountability."
    ),
    "03-lung-screening-stigma.md": (
        "Medicare and private insurers have built lung cancer screening behind a "
        "reimbursement checkpoint that no other covered cancer test carries. The same "
        "patients who accept mammography and colonoscopy at rates of 65 percent accept "
        "lung screening at 17 to 18 percent, not because the test fails, but because "
        "policy gates it behind confession."
    ),
    "04-breast-cancer-global-survival.md": (
        "Global health funders finance breast cancer detection without requiring "
        "treatment at the end of the referral line. A woman in a low-income country "
        "can receive a diagnosis she cannot complete, and her five-year survival "
        "odds remain less than half what they would be elsewhere."
    ),
    "05-cervical-cancer-elimination.md": (
        "Health ministries and donors still fund cervical cancer elimination as a "
        "series of pilot projects even though the World Health Organization has "
        "endorsed one-dose HPV vaccination, self-sampling, and same-day treatment. "
        "The tools to eliminate the disease exist. The financing structure does not."
    ),
    "06-global-cancer-aid-metrics.md": (
        "Global cancer donors report screenings delivered while treatable deaths "
        "remain unchanged. A woman in a rural clinic can test positive and still "
        "never reach treatment because the program that found her cancer was never "
        "required to fund the bridge to care."
    ),
    "07-young-onset-colorectal-cancer.md": (
        "Federal screening policy lowered the colorectal cancer start age to 45 in "
        "2021, but delivery policy never followed. Young adults with red-flag symptoms "
        "still wait months for a diagnosis because payers and health systems have "
        "no mandatory clock for symptomatic workup."
    ),
    "08-prostate-psa-baseline.md": (
        "The U.S. Preventive Services Task Force restricted PSA screening in 2012 "
        "using harm models from an era before active surveillance and MRI-first "
        "pathways. Metastatic prostate cancer then rose more than 40 percent among "
        "men 45 to 74, and guideline policy has not caught up to modern treatment."
    ),
    "09-positive-test-follow-up.md": (
        "The Centers for Medicare and Medicaid Services and private insurers pay for "
        "colorectal cancer screening tests but not for the colonoscopy that gives a "
        "positive result its meaning. In many health systems, barely half of patients "
        "with a positive stool test receive follow-up within a year."
    ),
    "10-breast-density-follow-up.md": (
        "Federal policy now requires every mammography report to disclose breast "
        "density, but Congress and insurers have not required coverage for the "
        "supplemental imaging that disclosure implies. The warning is universal. "
        "The answer remains means-tested."
    ),
    "11-mced-galleri-evidence.md": (
        "Congress is considering Medicare coverage for multi-cancer blood tests before "
        "the evidence shows they save lives, while the NHS enrolled 140,000 people in "
        "a randomized trial and declined to expand rollout until the data arrive. "
        "American health policy is preparing to pay first and ask later."
    ),
}

PLEAS = {
    "01-pack-year-lung-screening.md": """We urge the U.S. Preventive Services Task Force to replace fixed pack-year cutoffs with validated risk-prediction models tested against long-term outcomes.

We urge the Centers for Medicare and Medicaid Services to align coverage with model-based eligibility so reimbursable patients match the patients the evidence identifies.

We urge every guideline body to adopt an audit clock for screening criteria: no eligibility rule without published expected performance, subgroup sensitivity, and scheduled re-testing against real-world outcomes.

We urge hospital regulators and accrediting bodies to require the same post-market accountability for eligibility algorithms that federal law already demands of the scanners themselves.""",
    "02-racial-math-lung-screening.md": """We urge the U.S. Preventive Services Task Force and the American Cancer Society to adopt race-calibrated lung screening thresholds now, because they are the only tested approach that closes the documented gap.

We urge every guideline body to prohibit adoption of screening algorithms without published performance broken out by race, sex, and other subgroups.

We urge the National Institutes of Health and the National Cancer Institute to fund diverse cohort studies large enough to replace race in formulas with the real predictors it currently stands in for.

We urge every health system receiving federal dollars to audit quarterly whom its lung screening criteria flag, by race, and publish the results.""",
    "03-lung-screening-stigma.md": """We urge the Centers for Medicare and Medicaid Services to remove the shared-decision-making visit as a prerequisite for lung cancer screening payment and treat the scan like any other covered cancer test.

We urge Medicare and Medicaid to require smoking history as structured electronic health record data and to reimburse opt-out mailed screening invitations.

We urge the U.S. Preventive Services Task Force and state Medicaid programs to align outreach policy with mammography and colorectal screening defaults, not stigma-based disclosure.

We urge the Department of Health and Human Services to require patient-facing materials stating that patients with a smoking history already qualify and need not justify past behavior to access screening.""",
    "04-breast-cancer-global-survival.md": """We urge PEPFAR, the Global Fund, and bilateral health agencies to finance breast cancer care on ten-to-fifteen-year horizons, not three-year grant cycles.

We urge the World Health Organization's Global Breast Cancer Initiative targets to become binding funding conditions: 60 percent early-stage diagnosis, workup within 60 days, and 80 percent treatment completion.

We urge Gavi and pooled procurement bodies to extend the vaccine procurement model to off-patent cancer medicines so treatment is not priced as a luxury import.

We urge every donor to adopt a treatment-anchored rule: no detection rollout without a verified, financed treatment endpoint in the referral network.""",
    "05-cervical-cancer-elimination.md": """We urge every health ministry that has not yet switched to single-dose HPV vaccination to do so immediately.

We urge national screening programs to adopt self-sampling and same-day treat protocols as the default model, not the pilot exception.

We urge Gavi and the Global Fund to fund cervical cancer elimination as a permanent, multi-decade budget line rather than a renewable experiment.

We urge WHO member states to report elimination progress against vaccination coverage and screened-and-treated rates, not pilot counts alone.""",
    "06-global-cancer-aid-metrics.md": """We urge every global cancer donor to replace screenings-delivered metrics with days from positive test to treatment initiation.

We urge the World Bank, bilateral agencies, and philanthropic funders to withhold screening scale-up until a financed treatment endpoint is verified in the referral network.

We urge WHO and national health ministries to finance oncology workforce development on decade horizons, not election-cycle grants.

We urge pooled procurement bodies to negotiate off-patent essential cancer medicines the way global health already pools vaccines and antiretrovirals.""",
    "07-young-onset-colorectal-cancer.md": """We urge the Centers for Medicare and Medicaid Services and commercial payers to require mailed stool-based screening at age 45 with uptake in the 45-to-49 bracket reported separately from older adults.

We urge state Medicaid programs and Medicare Advantage plans to adopt a red-flag guarantee: defined symptoms at any age, a scheduled colonoscopy within a fixed number of weeks, publicly reported.

We urge the Office of the National Coordinator for Health Information Technology to require family history as structured data that automatically triggers earlier screening when guidelines already say it should.

We urge the U.S. Preventive Services Task Force to treat symptomatic young adults as a distinct policy problem, not a footnote to age-based screening.""",
    "08-prostate-psa-baseline.md": """We urge the U.S. Preventive Services Task Force to re-review PSA screening using harm models based on active surveillance and MRI-first pathways, not 2009 treatment patterns.

We urge the task force to adopt baseline risk-stratified screening: one PSA at 45 for average-risk men, at 40 for Black men and men with family history, with intervals set by the baseline result.

We urge guideline bodies to establish an automatic re-review trigger when metastatic incidence rises for a decade after a restriction.

We urge Medicare to cover baseline PSA and risk-stratified follow-up as a defined preventive benefit, not an unfunded discussion in a fifteen-minute visit.""",
    "09-positive-test-follow-up.md": """We urge the Centers for Medicare and Medicaid Services to create a national quality metric for follow-up colonoscopy within 90 days of a positive stool test, publicly reported and tied to Medicare star ratings.

We urge Medicare and Medicaid to bundle payment for a positive stool test and its colonoscopy as one screening episode, with full payment contingent on loop closure.

We urge CMS to require patient navigation reimbursement for positive screening results in every screening program it funds.

We urge the Department of Health and Human Services to mandate auto-scheduling of colonoscopy at the time of a positive result and to publicize existing federal rules eliminating cost-sharing on follow-up colonoscopy.""",
    "10-breast-density-follow-up.md": """We urge Congress to pass the Find It Early Act and require insurers to cover supplemental and diagnostic breast imaging without cost-sharing.

We urge the Centers for Medicare and Medicaid Services to add no-cost supplemental imaging for extremely dense breasts to the Medicare preventive benefit, beginning with the DENSE trial population.

We urge state legislatures to adopt the model laws already operating in states that mandate no-cost dense-breast follow-up.

We urge the Food and Drug Administration and CMS to require that density notification letters include information on covered next steps, not only risk disclosure.""",
    "11-mced-galleri-evidence.md": """We urge Congress to reject a Medicare benefit category for multi-cancer early detection tests until FDA approval and mortality evidence are established.

We urge the Food and Drug Administration to require every MCED advertisement and result letter to state that the test does not replace colonoscopy, mammography, or any proven screening.

We urge the National Cancer Institute to fund the Vanguard study as the primary venue for population-scale evaluation, not lobbying-driven coverage.

We urge CMS to adopt a symmetric evidentiary standard: if the NHS-Galleri trial shows benefit, expand coverage quickly; until then, restrict payment to registry and trial settings only.""",
}

POLICY_FIXES = [
    (r"\byou qualify\b", "patients qualify"),
    (r"\bMiss any one threshold\b", "Miss any one threshold in policy"),
    (r"\bIf you smoked\b", "Patients with a smoking history"),
    (r"\bIf you are 45 or older\b", "Federal policy should ensure adults 45 and older"),
    (r"\bIf you have rectal bleeding\b", "Payers should guarantee that patients with rectal bleeding"),
    (r"\bIf your stool test is positive\b", "When a stool test is positive, policy should require"),
    (r"\bIf your mammogram report says\b", "When a mammogram report shows"),
    (r"\bDo not skip colonoscopy\b", "Federal policy must not allow multi-cancer blood tests to displace colonoscopy"),
    (r"\bMen at average risk should discuss\b", "Medicare policy should cover"),
    (r"\bBlack men and men with family history should start at 40\b", "with baseline testing at 40 for Black men and men with family history"),
    (r"\bHealth ministries that have not switched\b", "We repeat our plea: health ministries that have not switched"),
]


def split_article(text: str):
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        raise ValueError("Missing front matter")
    end_fm = text.find("---", 3)
    if end_fm == -1:
        raise ValueError("Unclosed front matter")
    after_fm = text[end_fm + 3 :].lstrip("\n")
    by_marker = "*By "
    by_idx = after_fm.find(by_marker)
    if by_idx == -1:
        raise ValueError("Missing byline")
    divider = after_fm.find("---", by_idx)
    if divider == -1:
        raise ValueError("Missing content divider")
    header = text[: end_fm + 3] + "\n\n" + after_fm[: divider + 3] + "\n\n"
    body = after_fm[divider + 3 :].lstrip("\n")
    return header, body


def replace_opening(body: str, opening: str) -> str:
    marker = "The solution is straightforward"
    if marker not in body:
        raise ValueError("Missing solution marker")
    rest = body.split(marker, 1)[1]
    return opening + "\n\n" + marker + rest


def replace_closing(body: str, plea: str) -> str:
    body = re.sub(
        r"\n---\n\n## Take Action\n\n.*\Z",
        "",
        body,
        flags=re.DOTALL,
    ).rstrip()
    for old, new in POLICY_FIXES:
        body = re.sub(old, new, body)
    return body + "\n\n---\n\n## A Plea to Policymakers\n\n" + plea.strip() + "\n"


def main():
    for path in sorted(ARTICLES.glob("*.md")):
        text = path.read_text(encoding="utf-8-sig")
        header, body = split_article(text)
        body = replace_opening(body, OPENINGS[path.name])
        body = replace_closing(body, PLEAS[path.name])
        path.write_text(header + body, encoding="utf-8")
        print(f"Updated {path.name}")


if __name__ == "__main__":
    main()
