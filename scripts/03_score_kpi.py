from pathlib import Path
import platform
import matplotlib.pyplot as plt
import pandas as pd

INPUT_PATH = Path("data/processed/aicc_inquiry_scored.csv")

OUTPUT_CSV = Path("outputs/final/aicc_operation_priority.csv")
OUTPUT_MD = Path("outputs/final/aicc_operation_priority.md")

CHART_DIR = Path("outputs/final/charts")
PRIORITY_CHART = CHART_DIR / "aicc_operation_priority.png"
AUTOMATION_CHART = CHART_DIR / "aicc_automation_fit.png"
QUALITY_CHART = CHART_DIR / "aicc_quality_need.png"

OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
CHART_DIR.mkdir(parents=True, exist_ok=True)

def set_korean_font():
    system = platform.system()

    if system == "Darwin":  # macOS
        plt.rcParams["font.family"] = "AppleGothic"
    elif system == "Windows":
        plt.rcParams["font.family"] = "Malgun Gothic"
    else:
        plt.rcParams["font.family"] = "DejaVu Sans"

    plt.rcParams["axes.unicode_minus"] = False
    
def load_scored_data() -> pd.DataFrame:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"{INPUT_PATH} 파일이 없습니다. 먼저 scripts/02_classify_inquiries.py를 실행하세요."
        )

    df = pd.read_csv(INPUT_PATH)

    required_columns = {
        "aicc_label",
        "automation_score",
        "handoff_need_score",
        "auto_qa_need_score",
        "scenario_complexity_score",
        "main_scenario_need",
        "global_scenario_need",
        "repair_scenario_need",
        "operation_priority_score",
    }

    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"필수 컬럼이 없습니다: {missing}")

    return df


def build_priority_table(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("aicc_label")
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

    total_count = summary["inquiry_count"].sum()
    summary["inquiry_ratio"] = (summary["inquiry_count"] / total_count * 100).round(2)

    score_cols = [
        "automation_score",
        "handoff_need_score",
        "auto_qa_need_score",
        "scenario_complexity_score",
        "main_scenario_need",
        "global_scenario_need",
        "repair_scenario_need",
        "operation_priority_score",
    ]

    for col in score_cols:
        summary[col] = summary[col].round(1)

    summary = summary.sort_values(
        ["operation_priority_score", "inquiry_count"],
        ascending=[False, False],
    ).reset_index(drop=True)

    summary["priority_rank"] = range(1, len(summary) + 1)

    return summary[
        [
            "priority_rank",
            "aicc_label",
            "inquiry_count",
            "inquiry_ratio",
            "operation_priority_score",
            "automation_score",
            "handoff_need_score",
            "auto_qa_need_score",
            "scenario_complexity_score",
            "main_scenario_need",
            "global_scenario_need",
            "repair_scenario_need",
        ]
    ]


def infer_action(row: pd.Series) -> str:
    label = row["aicc_label"]

    if label == "FAQ/단순 안내":
        return "Global Scenario와 FAQ 자동화 우선 검토"
    if label == "업무 처리 요청":
        return "Main Scenario 설계와 API 연동 프로세스 검토"
    if label == "상담원 연결":
        return "Human Handoff 정책과 상담원 연결 조건 정교화"
    if label == "장애/오류":
        return "상담 어시스턴트와 장애 대응 지식베이스 강화"
    if label == "불만/클레임":
        return "Auto QA와 상담 품질 모니터링 우선 적용"
    if label == "결제/청구":
        return "정산/청구 문의 분류와 민감 문의 대응 기준 수립"
    if label == "계정/인증":
        return "본인확인/인증 실패 케이스 대응 플로우 정리"

    return "추가 문의 유형 정의 및 수동 검토 필요"


def add_recommended_actions(summary: pd.DataFrame) -> pd.DataFrame:
    enriched = summary.copy()
    enriched["recommended_operation_action"] = enriched.apply(infer_action, axis=1)
    return enriched


def save_bar_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str,
    output_path: Path,
):
    plot_df = df.sort_values(y_col, ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(plot_df[x_col], plot_df[y_col])
    plt.xlabel(y_col)
    plt.ylabel(x_col)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    plt.close()


def write_markdown_report(summary: pd.DataFrame):
    top = summary.iloc[0]

    report = f"""# AICC Operation Priority Report

## 1. Purpose

본 문서는 공개 고객지원 데이터셋과 보조 티켓 데이터를 AICC 운영 관점으로 재분류한 뒤,
문의 유형별 운영 우선순위와 개선 액션을 정리한 결과입니다.

분석 목적은 실제 NAVER Cloud 고객 현황을 추정하는 것이 아니라,
CLOVA AiCall 운영 담당자가 고객 문의와 CS 운영 현황을 어떤 지표로 구조화할 수 있는지 검토하는 것입니다.

---

## 2. Final Operation Priority Table

{summary.to_markdown(index=False)}

---

## 3. Top Priority Insight

가장 높은 운영 우선순위로 분류된 문의 유형은 **{top["aicc_label"]}**입니다.

- 운영 우선순위 점수: `{top["operation_priority_score"]}`
- 문의 건수: `{int(top["inquiry_count"]):,}`
- 전체 비중: `{top["inquiry_ratio"]}%`
- 추천 운영 액션: `{top["recommended_operation_action"]}`

---

## 4. How to Interpret Scores

| Score | Meaning |
|---|---|
| operation_priority_score | 운영 담당자가 우선적으로 관리해야 할 종합 점수 |
| automation_score | 음성봇/챗봇 자동화 적합도 |
| handoff_need_score | 상담원 연결 정책 필요도 |
| auto_qa_need_score | Auto QA 및 품질 모니터링 필요도 |
| scenario_complexity_score | Main/Global/Repair 시나리오 설계 복잡도 |
| main_scenario_need | 핵심 업무 처리 시나리오 필요도 |
| global_scenario_need | FAQ/상담원 연결 등 Global Scenario 필요도 |
| repair_scenario_need | 무응답/의도 불명확/오류 복구 시나리오 필요도 |

---

## 5. Operation Improvement Ideas

### 5.1 Global Scenario 고도화

FAQ성 문의와 단순 안내성 문의가 많은 경우,
CLOVA AiCall의 Global Scenario를 활용해 자주 들어오는 문의를 별도 흐름으로 분리할 수 있습니다.

### 5.2 Main Scenario 표준화

업무 처리 요청이 많은 경우,
예약, 변경, 취소, 결제, 배송 확인 등 핵심 업무를 Main Scenario로 정의하고,
각 단계에서 필요한 정보 수집 항목과 API 연동 조건을 문서화해야 합니다.

### 5.3 Human Handoff 정책 정교화

상담원 연결 요청이 높은 경우,
단순 연결 요청인지, 실패 이후 연결 요청인지, 민감 문의로 인한 연결 요청인지 구분해야 합니다.

### 5.4 Auto QA 적용 후보 식별

장애/오류, 불만/클레임 유형은 상담 품질 모니터링과 Auto QA 적용 후보입니다.
이 유형은 상담 로그, 키워드, 응대 결과를 기준으로 품질 평가 항목을 설계할 수 있습니다.

### 5.5 Repair Scenario 강화

의도 불명확, 오류, 실패성 문의가 많은 경우,
무응답/오인식/불완전 발화에 대한 Repair Scenario를 강화해야 합니다.

---

## 6. Limitation

- 본 분석은 공개 고객지원 데이터셋 기반입니다.
- 실제 NAVER Cloud 고객 문의 데이터가 아닙니다.
- 영어 데이터셋을 기반으로 하므로 국내 콜센터 표현과 차이가 있을 수 있습니다.
- 점수는 운영 분석을 위한 rule-based score이며 실제 상품 성능이나 시장 점유율을 의미하지 않습니다.
- 후속 분석에서는 AI Hub 한국어 콜센터 데이터셋과 실제 운영 로그 구조를 반영할 수 있습니다.
"""

    OUTPUT_MD.write_text(report, encoding="utf-8")


def main():
    set_korean_font()
    df = load_scored_data()

    summary = build_priority_table(df)
    summary = add_recommended_actions(summary)

    summary.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    save_bar_chart(
        summary,
        x_col="aicc_label",
        y_col="operation_priority_score",
        title="AICC Operation Priority Score by Inquiry Type",
        output_path=PRIORITY_CHART,
    )

    save_bar_chart(
        summary,
        x_col="aicc_label",
        y_col="automation_score",
        title="AICC Automation Fit Score by Inquiry Type",
        output_path=AUTOMATION_CHART,
    )

    save_bar_chart(
        summary,
        x_col="aicc_label",
        y_col="auto_qa_need_score",
        title="AICC Auto QA Need Score by Inquiry Type",
        output_path=QUALITY_CHART,
    )

    write_markdown_report(summary)

    print(f"Saved final operation priority CSV: {OUTPUT_CSV}")
    print(f"Saved final operation priority report: {OUTPUT_MD}")
    print(f"Saved chart: {PRIORITY_CHART}")
    print(f"Saved chart: {AUTOMATION_CHART}")
    print(f"Saved chart: {QUALITY_CHART}")
    print()
    print(summary)


if __name__ == "__main__":
    main()