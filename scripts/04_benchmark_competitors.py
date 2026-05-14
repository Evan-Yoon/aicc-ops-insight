from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import platform


def set_korean_font():
    system = platform.system()

    if system == "Darwin":
        plt.rcParams["font.family"] = "AppleGothic"
    elif system == "Windows":
        plt.rcParams["font.family"] = "Malgun Gothic"
    else:
        plt.rcParams["font.family"] = "DejaVu Sans"

    plt.rcParams["axes.unicode_minus"] = False

INPUT_PATH = Path("data/manual/competitor_metrics.csv")

OUTPUT_CSV = Path("outputs/final/aicc_competitor_benchmark.csv")
OUTPUT_MD = Path("outputs/final/aicc_competitor_benchmark.md")

CHART_DIR = Path("outputs/final/charts")
BENCHMARK_CHART = CHART_DIR / "aicc_competitor_benchmark.png"
GROUP_CHART = CHART_DIR / "aicc_metric_group_coverage.png"

OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
CHART_DIR.mkdir(parents=True, exist_ok=True)


SOURCE_GRADE_WEIGHT = {
    "A": 1.0,
    "B": 0.8,
    "C": 0.5,
    "D": 0.3,
}


METRIC_GROUP_WEIGHT = {
    "시장성": 1.25,
    "도입 레퍼런스": 1.15,
    "운영규모": 1.10,
    "운영효율": 1.05,
    "품질관리": 1.00,
    "제품구조": 0.90,
}


def load_metrics() -> pd.DataFrame:
    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"{INPUT_PATH} 파일이 없습니다. data/manual/competitor_metrics.csv를 먼저 작성하세요."
        )

    df = pd.read_csv(INPUT_PATH)

    required = {
        "company",
        "product",
        "metric_group",
        "metric_name",
        "value_numeric",
        "value_text",
        "evidence_text",
        "source_url",
        "source_grade",
    }

    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"필수 컬럼이 없습니다: {missing}")

    df["value_numeric"] = pd.to_numeric(df["value_numeric"], errors="coerce").fillna(0)
    df["source_weight"] = df["source_grade"].map(SOURCE_GRADE_WEIGHT).fillna(0.5)
    df["metric_group_weight"] = df["metric_group"].map(METRIC_GROUP_WEIGHT).fillna(1.0)

    return df


def normalize_within_metric_group(df: pd.DataFrame) -> pd.DataFrame:
    scored = df.copy()

    scored["normalized_metric_score"] = 0.0

    for metric_group, group_df in scored.groupby("metric_group"):
        max_value = group_df["value_numeric"].max()

        if max_value <= 0:
            scored.loc[group_df.index, "normalized_metric_score"] = 50
        else:
            scored.loc[group_df.index, "normalized_metric_score"] = (
                group_df["value_numeric"] / max_value * 100
            )

    scored["evidence_score"] = (
        scored["normalized_metric_score"]
        * scored["source_weight"]
        * scored["metric_group_weight"]
    ).round(1)

    return scored


def build_company_benchmark(scored: pd.DataFrame) -> pd.DataFrame:
    benchmark = (
        scored.groupby(["company", "product"])
        .agg(
            evidence_count=("evidence_text", "count"),
            covered_metric_groups=("metric_group", lambda x: ", ".join(sorted(set(x)))),
            market_score=("evidence_score", "sum"),
            avg_evidence_score=("evidence_score", "mean"),
        )
        .reset_index()
    )

    max_score = benchmark["market_score"].max()

    if max_score > 0:
        benchmark["benchmark_score"] = (
            benchmark["market_score"] / max_score * 100
        ).round(1)
    else:
        benchmark["benchmark_score"] = 0

    benchmark["avg_evidence_score"] = benchmark["avg_evidence_score"].round(1)

    benchmark = benchmark.sort_values(
        ["benchmark_score", "evidence_count"],
        ascending=[False, False],
    ).reset_index(drop=True)

    benchmark["rank"] = range(1, len(benchmark) + 1)

    return benchmark[
        [
            "rank",
            "company",
            "product",
            "benchmark_score",
            "evidence_count",
            "avg_evidence_score",
            "covered_metric_groups",
            "market_score",
        ]
    ]


def build_metric_group_summary(scored: pd.DataFrame) -> pd.DataFrame:
    summary = (
        scored.groupby(["company", "metric_group"])
        .agg(
            evidence_count=("evidence_text", "count"),
            score=("evidence_score", "sum"),
        )
        .reset_index()
    )

    pivot = summary.pivot_table(
        index="company",
        columns="metric_group",
        values="score",
        aggfunc="sum",
        fill_value=0,
    ).reset_index()

    return pivot


def infer_naver_insights(benchmark: pd.DataFrame, scored: pd.DataFrame) -> list[str]:
    insights = []

    naver_row = benchmark[benchmark["company"].str.contains("NAVER", case=False, na=False)]

    if naver_row.empty:
        return ["NAVER Cloud 행을 찾지 못했습니다. competitor_metrics.csv의 company 값을 확인해야 합니다."]

    naver_score = float(naver_row.iloc[0]["benchmark_score"])
    top_score = float(benchmark.iloc[0]["benchmark_score"])
    top_company = benchmark.iloc[0]["company"]

    insights.append(
        f"NAVER Cloud의 공개자료 기반 benchmark_score는 {naver_score}점이며, "
        f"가장 높은 점수의 비교 대상은 {top_company}입니다."
    )

    naver_groups = set(
        scored[scored["company"].str.contains("NAVER", case=False, na=False)]["metric_group"]
    )

    competitor_groups = set(scored["metric_group"])
    missing_groups = sorted(competitor_groups - naver_groups)

    if missing_groups:
        insights.append(
            "공개자료 기준 NAVER Cloud에서 상대적으로 덜 드러나는 지표 그룹은 "
            + ", ".join(missing_groups)
            + "입니다."
        )

    if naver_score < top_score:
        insights.append(
            "이는 실제 상품 성능이 낮다는 의미가 아니라, 공개 사례에서 수주액, 고객사 수, "
            "매출 목표, 운영규모 등 정량 지표가 경쟁사 대비 덜 노출되어 있다는 의미로 해석해야 합니다."
        )

    insights.append(
        "운영 개선 관점에서는 고객사별 도입 효과를 자동화율, 대기시간 감소, 처리율, "
        "통화량, 상담 품질 평가 지표로 표준화해 리포트화하는 방향이 유효합니다."
    )

    return insights


def save_bar_chart(df: pd.DataFrame, output_path: Path):
    plot_df = df.sort_values("benchmark_score", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(plot_df["company"], plot_df["benchmark_score"])
    plt.xlabel("benchmark_score")
    plt.ylabel("company")
    plt.title("AICC Competitor Benchmark Score")
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    plt.close()


def save_group_coverage_chart(group_summary: pd.DataFrame, output_path: Path):
    plot_df = group_summary.set_index("company")

    plt.figure(figsize=(11, 6))
    plot_df.plot(kind="bar", stacked=True, figsize=(11, 6))
    plt.xlabel("company")
    plt.ylabel("score")
    plt.title("AICC Metric Group Coverage by Company")
    plt.tight_layout()
    plt.savefig(output_path, dpi=180)
    plt.close()


def write_report(
    benchmark: pd.DataFrame,
    scored: pd.DataFrame,
    group_summary: pd.DataFrame,
    insights: list[str],
):
    evidence_table = scored[
        [
            "company",
            "product",
            "metric_group",
            "metric_name",
            "value_text",
            "evidence_text",
            "source_grade",
            "evidence_score",
            "source_url",
        ]
    ].sort_values(["company", "metric_group"])

    insight_text = "\n".join([f"- {item}" for item in insights])

    report = f"""# AICC Competitor Benchmark Report

## 1. Purpose

본 문서는 NAVER Cloud CLOVA AiCall을 중심으로 KT, LGU+, SKT/SK AX 계열 AICC 공개 지표를 비교한 결과입니다.

분석 목적은 실제 시장 점유율이나 상품 성능을 확정하는 것이 아니라,
공개자료에서 확인 가능한 수주액, 고객사 수, 매출 목표, 운영규모, 품질관리 기능, 제품 구조를 기준으로
AICC 운영 담당자가 어떤 경쟁사 지표를 모니터링할 수 있는지 검토하는 것입니다.

---

## 2. Benchmark Score

{benchmark.to_markdown(index=False)}

---

## 3. Metric Group Coverage

{group_summary.to_markdown(index=False)}

---

## 4. Evidence Table

{evidence_table.to_markdown(index=False)}

---

## 5. Key Insights

{insight_text}

---

## 6. Interpretation for NAVER Cloud CLOVA AiCall

NAVER Cloud CLOVA AiCall은 공식 문서 기준으로 Inbound/Outbound AI Callbot, Contact Center, Agent, Channel,
음성 인식/합성, 챗봇, 텍스트 분석 등 AI 콘택트센터 운영 구조를 갖고 있습니다.

다만 공개자료 기반 비교에서는 KT와 LGU+가 수주액, 고객사 수, 월 콜 처리량, 매출 목표, Auto QA 등
정량 지표를 더 적극적으로 노출하고 있습니다.

따라서 CLOVA AiCall 운영 개선 관점에서는 다음 방향을 고려할 수 있습니다.

1. 고객사별 도입 효과 리포트 표준화
2. 상담 자동화율, 대기시간 감소, 처리율 향상 등 운영 KPI 정리
3. Contact Center / Agent / Channel 단위 운영 리포트 템플릿 구성
4. 상담 어시스턴트, Auto QA, Repair Scenario 관련 품질 지표 강화
5. 경쟁사 수주액, 고객사 수, 매출 목표, 기능 고도화 계획 정기 모니터링

---

## 7. Limitation

- 본 분석은 공개자료 기반입니다.
- 실제 매출, 점유율, 고객 만족도, 제품 성능을 의미하지 않습니다.
- 회사별 공개자료의 양과 표현 방식에 따라 점수가 달라질 수 있습니다.
- NAVER Cloud 내부 자료를 사용하지 않았습니다.
- 본 점수는 운영 인사이트 도출을 위한 포트폴리오용 지표입니다.
"""

    OUTPUT_MD.write_text(report, encoding="utf-8")


def main():
    set_korean_font()

    df = load_metrics()

    scored = normalize_within_metric_group(df)
    benchmark = build_company_benchmark(scored)
    group_summary = build_metric_group_summary(scored)
    insights = infer_naver_insights(benchmark, scored)

    benchmark.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    save_bar_chart(benchmark, BENCHMARK_CHART)
    save_group_coverage_chart(group_summary, GROUP_CHART)

    write_report(benchmark, scored, group_summary, insights)

    print(f"Saved competitor benchmark CSV: {OUTPUT_CSV}")
    print(f"Saved competitor benchmark report: {OUTPUT_MD}")
    print(f"Saved chart: {BENCHMARK_CHART}")
    print(f"Saved chart: {GROUP_CHART}")
    print()
    print(benchmark)


if __name__ == "__main__":
    main()