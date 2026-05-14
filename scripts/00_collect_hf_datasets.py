from pathlib import Path

import pandas as pd
from datasets import load_dataset

DATASET_NAME = "bitext/Bitext-customer-support-llm-chatbot-training-dataset"

RAW_DIR = Path("data/raw/huggingface")
PROCESSED_DIR = Path("data/processed")

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def main():
    print(f"Loading dataset: {DATASET_NAME}")

    ds = load_dataset(DATASET_NAME, split="train")
    df = ds.to_pandas()

    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)
    print(df.head())

    # 원본 전체 저장: GitHub에는 올리지 말 것
    raw_path = RAW_DIR / "bitext_customer_support_full.csv"
    df.to_csv(raw_path, index=False, encoding="utf-8-sig")

    # 분석용 샘플 저장
    sample_path = RAW_DIR / "bitext_customer_support_sample.csv"
    df.head(3000).to_csv(sample_path, index=False, encoding="utf-8-sig")

    # 프로젝트 분석에 필요한 컬럼만 정리
    expected_columns = ["instruction", "category", "intent", "response"]
    available_columns = [col for col in expected_columns if col in df.columns]

    cleaned = df[available_columns].copy()
    cleaned = cleaned.rename(
        columns={
            "instruction": "customer_text",
            "category": "source_category",
            "intent": "source_intent",
            "response": "agent_response",
        }
    )

    processed_path = PROCESSED_DIR / "customer_support_inquiries.csv"
    cleaned.to_csv(processed_path, index=False, encoding="utf-8-sig")

    print(f"Saved raw full file: {raw_path}")
    print(f"Saved raw sample file: {sample_path}")
    print(f"Saved processed file: {processed_path}")


if __name__ == "__main__":
    main()