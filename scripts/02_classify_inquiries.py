from pathlib import Path

import pandas as pd

INPUT_PATH = Path("data/processed/aicc_inquiry_dataset.csv")
OUTPUT_PATH = Path("data/processed/aicc_inquiry_scored.csv")
SUMMARY_PATH = Path("outputs/final/aicc_kpi_summary.csv")
REPORT_PATH = Path("outputs/final/aicc_kpi_summary.md")

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)


KPI_SCORE_RULES = {
    "FAQ/단순 안내": {
        "automation_score": 90,
        "handoff_need_score": 20,
        "auto_qa_need_score": 30,
        "scenario_complexity_score": 40,
        "main_scenario_need": 20,
        "global_scenario_need": 90,
        "repair_scenario_need": 30,
    },
    "업무 처리 요청": {
        "automation_score": 75,
        "handoff_need_score": 45,
        "auto_qa_need_score": 45,
        "scenario_complexity_score": 80,
        "main_scenario_need": 90,
        "global_scenario_need": 35,
        "repair_scenario_need": 55,
    },
    "상담원 연결": {
        "automation_score": 25,
        "handoff_need_score": 95,
        "auto_qa_need_score": 60,
        "scenario_complexity_score": 50,
        "main_scenario_need": 30,
        "global_scenario_need": 85,
        "repair_scenario_need": 50,
    },
    "장애/오류": {
        "automation_score": 35,
        "handoff_need_score": 80,
        "auto_qa_need_score": 85,
        "scenario_complexity_score": 70,
        "main_scenario_need": 60,
        "global_scenario_need": 40,
        "repair_scenario_need": 85,
    },
    "불만/클레임": {
        "automation_score": 20,
        "handoff_need_score": 85,
        "auto_qa_need_score": 95,
        "scenario_complexity_score": 65,
        "main_scenario_need": 45,
        "global_scenario_need": 35,
        "repair_scenario_need": 80,
    },
    "결제/청구": {
        "automation_score": 60,
        "handoff_need_score": 55,
        "auto_qa_need_score": 60,
        "scenario_complexity_score": 70,
        "main_scenario_need": 75,
        "global_scenario_need": 40,
        "repair_scenario_need": 55,
    },
    "계정/인증": {
        "automation_score": 55,
        "handoff_need_score": 60,
        "auto_qa_need_score": 65,
        "scenario_complexity_score": 75,
        "main_scenario_need": 80,
        "global_scenario_need": 35,
        "repair_scenario_need": 65,
    },
    "기타": {
        "automation_score": 40,
        "handoff_need_score": 50,
        "auto_qa_need_score": 50,
        "scenario_complexity_score": 50,
        "main_scenario_need": 50,
        "global_scenario_need": 50,
        "repair_scenario_need": 50,
    },
}


def add_kpi_scores(df: pd.DataFrame) -> pd.DataFrame:
    scored = df.copy()

    for score_col in [
        "automation_score",
        "handoff_need_score",
        "auto_qa_need_score",
        "scenario_complexity_score",
        "main_scenario_need",
        "global_scenario_need",
        "repair_scenario_need",
    ]:
        scored[score_col] = scored["aicc_label"].apply(
            lambda label: KPI_SCORE_RULES.get(label, KPI_SCORE_RULES["기타"])[score_col]
        )

    scored["operation_priority_score"] = (
        scored["handoff_need_score"] * 0.25
        + scored["auto_qa_need_score"] * 0.25
        + scored["scenario_complexity_score"] * 0.20
        + scored["repair_scenario_need"] * 0.15
        + scored["automation_score"] * 0.15
    ).round(1)

    return scored


def make_label_summary(scored: pd.DataFrame) -> pd.DataFrame:
    summary = (
        scored.groupby("aicc_label")
        .agg(
            inquiry_count=("aicc_label", "size"),
            automation_score=("automation_score", "mean"),
            handoff_need_score=("handoff_need_score", "mean"),
            auto_qa_need_score=("auto_qa_need_score", "mean"),
            scenario_complexity_score=("scenario_complexity_score", "mean"),
            main_scenario_need=("main_scenario_need", "mean"),
            global_scenario_need=("global_scenario_need", "mean"),
            repair_scenario_need=("repair_scenario_need", "mean"),
            operation_priority_score=("operation_priority_score", "mean"),
        )
        .reset_index()
    )

    total = summary["inquiry_count"].sum()
    summary["inquiry_ratio"] = (summary["inquiry_count"] / total * 100).round(2)

    score_columns = [
        "automation_score",
        "handoff_need_score",
        "auto_qa_need_score",
        "scenario_complexity_score",
        "main_scenario_need",
        "global_scenario_need",
        "repair_scenario_need",
        "operation_priority_score",
    ]

    for col in score_columns:
        summary[col] = summary[col].round(1)

    summary = summary.sort_values(
        ["operation_priority_score", "inquiry_count"],
        ascending=[False, False],
    )

    return summary


def make_source_summary(scored: pd.DataFrame) -> pd.DataFrame:
    source_summary = (
        scored.groupby(["source_type", "aicc_label"])
        .size()
        .reset_index(name="count")
        .sort_values(["source_type", "count"], ascending=[True, False])
    )

    return source_summary


def write_report(summary: pd.DataFrame, source_summary: pd.DataFrame):
    top_priority = summary.iloc[0]

    report = f"""# AICC KPI Summary

## 1. Purpose

본 분석은 공개 고객지원 데이터셋을 AICC 운영 관점으로 재분류하여,
CLOVA AiCall 운영에서 중요하게 볼 수 있는 자동화 적합도, 상담원 연결 필요도,
Auto QA 필요도, 시나리오 복잡도를 산출하기 위한 것입니다.

pandas의 `groupby`는 데이터를 특정 컬럼 기준으로 나눈 뒤 집계하는 데 사용되며,
본 프로젝트에서는 문의 유형별 평균 점수와 건수를 계산하는 데 사용했습니다. 

## 2. KPI Definition

| KPI | Meaning |
|---|---|
| automation_score | 음성봇/챗봇 자동화에 적합한 정도 |
| handoff_need_score | 상담원 연결 정책이 필요한 정도 |
| auto_qa_need_score | Auto QA 및 품질 모니터링이 필요한 정도 |
| scenario_complexity_score | Main/Global/Repair 시나리오 설계 복잡도 |
| main_scenario_need | 핵심 업무 처리 시나리오 필요도 |
| global_scenario_need | FAQ, 상담원 연결 등 Global Scenario 필요도 |
| repair_scenario_need | 무응답/오류/이탈 복구 시나리오 필요도 |
| operation_priority_score | 운영 우선순위 종합 점수 |

## 3. AICC Label KPI Summary

{summary.to_markdown(index=False)}

## 4. Source Type x AICC Label Summary

{source_summary.to_markdown(index=False)}

## 5. Key Insight

운영 우선순위가 가장 높은 문의 유형은 **{top_priority["aicc_label"]}**입니다.

이 유형은 다음 이유로 우선 관리 대상입니다.

- 운영 우선순위 점수: `{top_priority["operation_priority_score"]}`
- 문의 건수: `{int(top_priority["inquiry_count"]):,}`
- 전체 비중: `{top_priority["inquiry_ratio"]}%`

## 6. How This Connects to CLOVA AiCall

CLOVA AiCall 운영 관점에서 이 결과는 다음과 같이 해석할 수 있습니다.

| Data Result | AiCall Operation Meaning |
|---|---|
| FAQ/단순 안내 비중 | Global Scenario 자동화 후보 |
| 업무 처리 요청 비중 | Main Scenario 설계 필요 |
| 상담원 연결 요청 | Human Handoff 정책 필요 |
| 장애/오류 및 불만/클레임 | Auto QA 및 상담 어시스턴트 필요 |
| 높은 Repair 점수 | 무응답/의도 불명확 발화 대응 정책 필요 |

## 7. Limitation

- 본 데이터는 실제 NAVER Cloud 고객 데이터가 아닙니다.
- 영어 고객지원 데이터셋 기반이므로 국내 콜센터 표현과 차이가 있을 수 있습니다.
- 점수는 운영 분석을 위한 rule-based scoring이며, 실제 상품 성능이나 시장 점유율을 의미하지 않습니다.
- 후속 분석에서는 AI Hub 한국어 콜센터 데이터셋으로 확장할 수 있습니다.
"""

    REPORT_PATH.write_text(report, encoding="utf-8")


def main():
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"{INPUT_PATH} 파일이 없습니다. 먼저 scripts/01_load_dataset.py를 실행하세요."
        )

    df = pd.read_csv(INPUT_PATH)

    if "aicc_label" not in df.columns:
        raise ValueError("aicc_label 컬럼이 없습니다. scripts/01_load_dataset.py 결과를 확인하세요.")

    scored = add_kpi_scores(df)
    scored.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    summary = make_label_summary(scored)
    summary.to_csv(SUMMARY_PATH, index=False, encoding="utf-8-sig")

    source_summary = make_source_summary(scored)

    write_report(summary, source_summary)

    print(f"Saved scored inquiries: {OUTPUT_PATH}")
    print(f"Saved KPI summary: {SUMMARY_PATH}")
    print(f"Saved KPI report: {REPORT_PATH}")
    print()
    print(summary)


if __name__ == "__main__":
    main()