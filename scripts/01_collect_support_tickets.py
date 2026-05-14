from pathlib import Path
from typing import Optional

import pandas as pd
from datasets import DatasetDict, load_dataset


RAW_DIR = Path("data/raw/huggingface")
PROCESSED_DIR = Path("data/processed")

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


DATASET_CANDIDATES = [
    {
        "dataset_name": "Tobi-Bueck/customer-support-tickets",
        "short_name": "customer_support_tickets_tobi",
        "reason": "Customer support ticket dataset for CS issue/category/priority-style analysis.",
    },
    {
        "dataset_name": "gorkemsevinc/customer_support_tickets",
        "short_name": "customer_support_tickets_gorkem",
        "reason": "Alternative customer support ticket dataset candidate.",
    },
]


TEXT_COLUMN_CANDIDATES = [
    "text",
    "body",
    "message",
    "description",
    "ticket",
    "ticket_text",
    "ticket_description",
    "Ticket Description",
    "customer_message",
    "Customer Message",
    "instruction",
    "question",
    "query",
    "subject",
    "Subject",
]

CATEGORY_COLUMN_CANDIDATES = [
    "category",
    "Category",
    "issue_category",
    "Issue Category",
    "type",
    "Type",
    "ticket_type",
    "Ticket Type",
    "queue",
    "Queue",
    "intent",
    "topic",
]

PRIORITY_COLUMN_CANDIDATES = [
    "priority",
    "Priority",
    "ticket_priority",
    "Ticket Priority",
    "urgency",
    "severity",
    "Severity",
]

RESPONSE_COLUMN_CANDIDATES = [
    "response",
    "Response",
    "answer",
    "Answer",
    "agent_response",
    "Agent Response",
    "resolution",
    "Resolution",
    "reply",
]


def pick_first_existing_column(df: pd.DataFrame, candidates: list[str]) -> Optional[str]:
    for col in candidates:
        if col in df.columns:
            return col
    return None


def load_first_available_split(dataset_name: str):
    """
    Hugging Face datasets may return either:
    - DatasetDict: {"train": Dataset, ...}
    - Dataset: directly

    This function picks train split first.
    If train does not exist, it picks the first available split.
    """
    loaded = load_dataset(dataset_name)

    if isinstance(loaded, DatasetDict):
        split_name = "train" if "train" in loaded else list(loaded.keys())[0]
        return loaded[split_name], split_name

    return loaded, "default"


def normalize_ticket_dataset(
    df: pd.DataFrame,
    dataset_name: str,
    short_name: str,
) -> pd.DataFrame:
    text_col = pick_first_existing_column(df, TEXT_COLUMN_CANDIDATES)
    category_col = pick_first_existing_column(df, CATEGORY_COLUMN_CANDIDATES)
    priority_col = pick_first_existing_column(df, PRIORITY_COLUMN_CANDIDATES)
    response_col = pick_first_existing_column(df, RESPONSE_COLUMN_CANDIDATES)

    normalized = pd.DataFrame()
    normalized["source_dataset"] = [dataset_name] * len(df)
    normalized["source_short_name"] = [short_name] * len(df)

    normalized["ticket_text"] = df[text_col].astype(str) if text_col else ""
    normalized["source_category"] = df[category_col].astype(str) if category_col else ""
    normalized["source_priority"] = df[priority_col].astype(str) if priority_col else ""
    normalized["agent_response"] = df[response_col].astype(str) if response_col else ""

    normalized["detected_text_column"] = text_col or ""
    normalized["detected_category_column"] = category_col or ""
    normalized["detected_priority_column"] = priority_col or ""
    normalized["detected_response_column"] = response_col or ""

    return normalized


def collect_one_dataset(
    dataset_name: str,
    short_name: str,
    reason: str,
    sample_size: int = 3000,
):
    print("=" * 80)
    print(f"Loading: {dataset_name}")
    print(f"Reason: {reason}")

    ds, split_name = load_first_available_split(dataset_name)
    df = ds.to_pandas()

    print(f"Split used: {split_name}")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(df.head(3))

    sample_df = df.head(sample_size).copy()

    raw_sample_path = RAW_DIR / f"{short_name}_sample.csv"
    sample_df.to_csv(raw_sample_path, index=False, encoding="utf-8-sig")

    normalized_df = normalize_ticket_dataset(
        sample_df,
        dataset_name=dataset_name,
        short_name=short_name,
    )

    report = {
        "dataset_name": dataset_name,
        "short_name": short_name,
        "split_used": split_name,
        "row_count_total": len(df),
        "row_count_sample_saved": len(sample_df),
        "columns": ", ".join(df.columns.tolist()),
        "raw_sample_path": str(raw_sample_path),
        "detected_text_column": normalized_df["detected_text_column"].iloc[0]
        if len(normalized_df)
        else "",
        "detected_category_column": normalized_df["detected_category_column"].iloc[0]
        if len(normalized_df)
        else "",
        "detected_priority_column": normalized_df["detected_priority_column"].iloc[0]
        if len(normalized_df)
        else "",
        "detected_response_column": normalized_df["detected_response_column"].iloc[0]
        if len(normalized_df)
        else "",
        "status": "success",
        "error": "",
    }

    return normalized_df, report


def main():
    all_normalized = []
    reports = []

    for item in DATASET_CANDIDATES:
        try:
            normalized_df, report = collect_one_dataset(
                dataset_name=item["dataset_name"],
                short_name=item["short_name"],
                reason=item["reason"],
            )

            all_normalized.append(normalized_df)
            reports.append(report)

        except Exception as e:
            print(f"[SKIP] Failed to load {item['dataset_name']}: {e}")

            reports.append(
                {
                    "dataset_name": item["dataset_name"],
                    "short_name": item["short_name"],
                    "split_used": "",
                    "row_count_total": 0,
                    "row_count_sample_saved": 0,
                    "columns": "",
                    "raw_sample_path": "",
                    "detected_text_column": "",
                    "detected_category_column": "",
                    "detected_priority_column": "",
                    "detected_response_column": "",
                    "status": "failed",
                    "error": str(e),
                }
            )

    report_df = pd.DataFrame(reports)
    report_path = PROCESSED_DIR / "support_tickets_dataset_report.csv"
    report_df.to_csv(report_path, index=False, encoding="utf-8-sig")

    if all_normalized:
        merged = pd.concat(all_normalized, ignore_index=True)

        # ticket_text가 비어 있는 행은 분석 가치가 낮으므로 제거
        merged = merged[merged["ticket_text"].astype(str).str.strip() != ""].copy()

        output_path = PROCESSED_DIR / "support_tickets_normalized.csv"
        merged.to_csv(output_path, index=False, encoding="utf-8-sig")

        sample_output_path = PROCESSED_DIR / "support_tickets_normalized_sample.csv"
        merged.head(500).to_csv(sample_output_path, index=False, encoding="utf-8-sig")

        print("=" * 80)
        print(f"Saved normalized support tickets: {output_path}")
        print(f"Saved sample support tickets: {sample_output_path}")
        print(f"Saved dataset report: {report_path}")
        print(f"Final normalized shape: {merged.shape}")
    else:
        print("=" * 80)
        print("No support ticket dataset was successfully loaded.")
        print(f"Saved dataset report: {report_path}")


if __name__ == "__main__":
    main()