from pathlib import Path

import pandas as pd

BITEXT_PATH = Path("data/processed/customer_support_inquiries.csv")
TICKETS_PATH = Path("data/processed/support_tickets_normalized.csv")

OUTPUT_PATH = Path("data/processed/aicc_inquiry_dataset.csv")
REPORT_PATH = Path("outputs/final/dataset_profile.md")

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)


AICC_LABEL_RULES = {
    "상담원 연결": [
        "contact_customer_service",
        "contact_human_agent",
        "talk_to_agent",
        "customer_service",
        "agent",
        "representative",
    ],
    "결제/청구": [
        "invoice",
        "payment",
        "billing",
        "refund",
        "charge",
        "price",
        "cost",
    ],
    "업무 처리 요청": [
        "cancel_order",
        "change_order",
        "track_order",
        "place_order",
        "change_shipping_address",
        "set_up_shipping_address",
        "order",
        "delivery",
        "shipping",
        "cancel",
        "change",
        "return",
    ],
    "계정/인증": [
        "create_account",
        "delete_account",
        "recover_password",
        "registration",
        "account",
        "password",
        "login",
        "sign in",
        "authentication",
    ],
    "장애/오류": [
        "technical",
        "error",
        "bug",
        "issue",
        "not working",
        "problem",
        "failed",
        "failure",
        "broken",
    ],
    "불만/클레임": [
        "complaint",
        "angry",
        "frustrated",
        "dissatisfied",
        "bad service",
        "not satisfied",
    ],
    "FAQ/단순 안내": [
        "delivery_period",
        "shipping",
        "policy",
        "information",
        "check",
        "newsletter",
        "how",
        "what",
        "where",
        "when",
    ],
}


def map_aicc_label(text: str, category: str = "", intent: str = "", priority: str = "") -> str:
    source = f"{text} {category} {intent} {priority}".lower()

    for label, keywords in AICC_LABEL_RULES.items():
        if any(keyword.lower() in source for keyword in keywords):
            return label

    return "기타"


def map_operation_insight(aicc_label: str) -> str:
    mapping = {
        "FAQ/단순 안내": "Global Scenario 자동화 후보",
        "업무 처리 요청": "Main Scenario 설계 필요",
        "상담원 연결": "Human Handoff 정책 필요",
        "장애/오류": "상담 어시스턴트 및 장애 대응 필요",
        "불만/클레임": "Auto QA 및 품질 모니터링 필요",
        "결제/청구": "정산/청구 문의 관리 필요",
        "계정/인증": "본인확인/인증 플로우 관리 필요",
        "기타": "추가 분류 검토 필요",
    }
    return mapping.get(aicc_label, "추가 분류 검토 필요")


def map_quality_need(aicc_label: str) -> str:
    if aicc_label in ["불만/클레임", "장애/오류", "상담원 연결"]:
        return "높음"
    if aicc_label in ["결제/청구", "업무 처리 요청", "계정/인증"]:
        return "중간"
    return "낮음"


def map_automation_fit(aicc_label: str) -> str:
    if aicc_label in ["FAQ/단순 안내", "업무 처리 요청"]:
        return "높음"
    if aicc_label in ["결제/청구", "계정/인증"]:
        return "중간"
    if aicc_label in ["상담원 연결", "장애/오류", "불만/클레임"]:
        return "낮음"
    return "검토 필요"


def load_bitext() -> pd.DataFrame:
    if not BITEXT_PATH.exists():
        raise FileNotFoundError(
            f"{BITEXT_PATH} 파일이 없습니다. 먼저 scripts/00_collect_hf_datasets.py를 실행하세요."
        )

    df = pd.read_csv(BITEXT_PATH)

    normalized = pd.DataFrame()
    normalized["source_type"] = "main_intent_dataset"
    normalized["source_dataset"] = "bitext_customer_support"
    normalized["customer_text"] = df["customer_text"].astype(str)
    normalized["source_category"] = df["source_category"].astype(str)
    normalized["source_intent"] = df["source_intent"].astype(str)
    normalized["source_priority"] = ""
    normalized["agent_response"] = df["agent_response"].astype(str)

    return normalized


def load_tickets() -> pd.DataFrame:
    if not TICKETS_PATH.exists():
        print(f"[WARN] {TICKETS_PATH} 파일이 없습니다. Support Tickets는 제외합니다.")
        return pd.DataFrame(
            columns=[
                "source_type",
                "source_dataset",
                "customer_text",
                "source_category",
                "source_intent",
                "source_priority",
                "agent_response",
            ]
        )

    df = pd.read_csv(TICKETS_PATH)

    normalized = pd.DataFrame()
    normalized["source_type"] = "support_ticket_dataset"
    normalized["source_dataset"] = df["source_short_name"].astype(str)
    normalized["customer_text"] = df["ticket_text"].astype(str)
    normalized["source_category"] = df["source_category"].astype(str)
    normalized["source_intent"] = ""
    normalized["source_priority"] = df["source_priority"].astype(str)
    normalized["agent_response"] = df["agent_response"].astype(str)

    return normalized


def make_markdown_table(df: pd.DataFrame) -> str:
    if df.empty:
        return "데이터 없음"
    return df.to_markdown(index=False)


def main():
    bitext_df = load_bitext()
    tickets_df = load_tickets()

    merged = pd.concat([bitext_df, tickets_df], ignore_index=True)

    merged = merged[merged["customer_text"].astype(str).str.strip() != ""].copy()

    merged["aicc_label"] = merged.apply(
        lambda row: map_aicc_label(
            text=str(row["customer_text"]),
            category=str(row["source_category"]),
            intent=str(row["source_intent"]),
            priority=str(row["source_priority"]),
        ),
        axis=1,
    )

    merged["operation_insight"] = merged["aicc_label"].apply(map_operation_insight)
    merged["automation_fit"] = merged["aicc_label"].apply(map_automation_fit)
    merged["quality_management_need"] = merged["aicc_label"].apply(map_quality_need)

    merged.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    label_counts = merged["aicc_label"].value_counts().reset_index()
    label_counts.columns = ["aicc_label", "count"]
    label_counts["ratio"] = (label_counts["count"] / len(merged) * 100).round(2)

    source_counts = merged["source_type"].value_counts().reset_index()
    source_counts.columns = ["source_type", "count"]
    source_counts["ratio"] = (source_counts["count"] / len(merged) * 100).round(2)

    operation_counts = merged["operation_insight"].value_counts().reset_index()
    operation_counts.columns = ["operation_insight", "count"]
    operation_counts["ratio"] = (operation_counts["count"] / len(merged) * 100).round(2)

    quality_counts = merged["quality_management_need"].value_counts().reset_index()
    quality_counts.columns = ["quality_management_need", "count"]
    quality_counts["ratio"] = (quality_counts["count"] / len(merged) * 100).round(2)

    automation_counts = merged["automation_fit"].value_counts().reset_index()
    automation_counts.columns = ["automation_fit", "count"]
    automation_counts["ratio"] = (automation_counts["count"] / len(merged) * 100).round(2)

    report = f"""# Dataset Profile

## 1. Source Summary

- Main input: `{BITEXT_PATH}`
- Support ticket input: `{TICKETS_PATH}`
- Output file: `{OUTPUT_PATH}`
- Total rows: `{len(merged):,}`

## 2. Dataset Source Distribution

{make_markdown_table(source_counts)}

## 3. AICC Label Distribution

{make_markdown_table(label_counts)}

## 4. Operation Insight Distribution

{make_markdown_table(operation_counts)}

## 5. Automation Fit Distribution

{make_markdown_table(automation_counts)}

## 6. Quality Management Need Distribution

{make_markdown_table(quality_counts)}

## 7. Interpretation

본 데이터셋은 실제 NAVER Cloud 고객 데이터가 아니라 공개 고객지원 데이터셋과 보조 티켓 데이터셋을 통합한 분석용 데이터입니다.

이 프로젝트에서는 실제 고객 현황을 추정하기보다, AICC 운영 관점에서 고객 문의를 어떻게 분류하고 운영 KPI로 전환할 수 있는지 검증하는 데 목적이 있습니다.

| AICC Label | Operation Meaning |
|---|---|
| FAQ/단순 안내 | Global Scenario 자동화 후보 |
| 업무 처리 요청 | Main Scenario 설계 필요 |
| 상담원 연결 | Human Handoff 정책 필요 |
| 장애/오류 | 상담 어시스턴트 및 장애 대응 필요 |
| 불만/클레임 | Auto QA 및 품질 모니터링 필요 |
| 결제/청구 | 정산/청구 문의 관리 필요 |
| 계정/인증 | 본인확인/인증 플로우 관리 필요 |
| 기타 | 추가 분류 검토 필요 |

## 8. Limitation

- 주 데이터는 영어 고객지원 데이터셋입니다.
- 국내 AICC 운영 환경을 더 정확히 반영하려면 AI Hub 한국어 상담/콜센터 데이터셋으로 확장할 필요가 있습니다.
- 본 분석은 운영 지표 설계용이며, 실제 NAVER Cloud 고객 문의 현황을 의미하지 않습니다.
"""

    REPORT_PATH.write_text(report, encoding="utf-8")

    print(f"Saved merged AICC dataset: {OUTPUT_PATH}")
    print(f"Saved dataset profile: {REPORT_PATH}")
    print()
    print(label_counts)


if __name__ == "__main__":
    main()
