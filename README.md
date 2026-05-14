# AICC Ops Insight

AI 컨택센터(AICC) 시장이 확대되면서, 실제 운영 현장에서는 어떤 지표를 중심으로 움직이는지 궁금해졌습니다.  
이 프로젝트는 NAVER Cloud CLOVA AiCall을 중심으로 고객 문의 패턴과 경쟁사 지표를 직접 분석한 작업입니다.

> NAVER Cloud 또는 NAVER와 공식적으로 관련된 프로젝트가 아닙니다.

---

## Overview

CLOVA AiCall은 Contact Center / Agent / Channel 구조를 기반으로 Inbound·Outbound 콜을 AI Bot으로 처리하는 서비스입니다.  
이 서비스를 실제로 운영한다면 어떤 지표를 봐야 할지, 고객 문의 데이터를 KPI로 어떻게 연결할 수 있는지 탐구했습니다.

- 고객 문의 유형 분류 및 운영 인사이트 도출
- AICC 운영 KPI 정의
- KT, LGU+, SKT/SK AX 경쟁사 공개 지표 수집 및 비교
- 운영 개선 방향 제안

---

## Why CLOVA AiCall?

국내 AICC 시장에서 CLOVA AiCall은 네이버 클라우드의 주요 AI 상품 중 하나입니다.  
KT, LGU+, SKT/SK AX 등 경쟁사의 공개 자료가 비교적 풍부해 벤치마킹이 가능했고,  
고객 문의부터 운영 리포트까지 이어지는 흐름을 분석하기에 구조가 명확한 서비스라고 판단했습니다.

---

## Data Sources

직접 크롤링한 데이터는 사용하지 않았습니다.

**공개 데이터셋**
- Hugging Face 고객지원 데이터셋 — 문의 문장, intent, category 기반 분류에 활용

**공개 시장 자료**
- NAVER Cloud CLOVA AiCall 공식 문서
- KT / LGU+ / SKT·SK AX 관련 공개 기사 및 보도자료

**합성 데이터**  
실제 기업의 AICC 도입 문의 데이터는 공개되어 있지 않아, CLOVA AiCall 문의 양식 항목을 기반으로  
도입 문의 단계 정보가 운영 KPI로 어떻게 전환되는지 검증하기 위한 시뮬레이션 데이터를
`data/synthetic_leads.csv`에 별도로 구성했습니다.

---

## Analysis Framework

### 문의 유형 분류

고객 문의 문장을 아래 유형으로 분류합니다.

- FAQ / 단순 안내
- 업무 처리 요청
- 장애 / 오류
- 불만 / 클레임
- 상담원 연결 요청
- 결제 / 청구
- 계정 / 인증
- 캠페인 / 해피콜

### KPI 매핑

| 문의 유형        | 운영 관점 인사이트          |
| ---------------- | --------------------------- |
| FAQ              | Global Scenario 자동화 후보 |
| 업무 처리 요청   | Main Scenario 설계 필요     |
| 장애 / 오류      | 상담 어시스턴트 필요        |
| 불만 / 클레임    | Auto QA 필요                |
| 상담원 연결 요청 | Human Handoff 정책 필요     |
| 불명확 발화      | Repair Scenario 중요        |

---

## Competitor Benchmarking

| Company     | Product                  | Key Metrics                          |
| ----------- | ------------------------ | ------------------------------------ |
| NAVER Cloud | CLOVA AiCall / HappyCall | 자동화율, 대기시간 감소, 처리율 향상 |
| KT          | AICC                     | 수주액, 고객사 수, 월 콜 처리량      |
| LGU+        | AICC                     | 매출 목표, 고객사 수, Auto QA        |
| SKT / SK AX | AI CCaaS / AICC          | 도입 문의, 고객사, 상담 자동화 기능  |

---

## Outputs

프로젝트 가이드는 `src/`와 `outputs/` 루트 중심의 최소 제출 구조를 제안했지만,
이 저장소에서는 원천/가공/최종 산출물을 구분하기 위해 구조를 조금 확장했습니다.
분석 스크립트는 `scripts/`, 중간 가공 데이터는 `data/processed/`, 제출용 최종 산출물은
`outputs/final/`에 모았습니다.

```text
data/
  sources.csv
  synthetic_leads.csv
  manual/
    competitor_metrics.csv
  processed/
    customer_support_inquiries.csv
    support_tickets_normalized.csv
    aicc_inquiry_dataset.csv
    aicc_inquiry_scored.csv

outputs/
  final/
    aicc_kpi_summary.csv
    aicc_operation_priority.csv
    aicc_competitor_benchmark.csv
    result_summary.csv
    portfolio_summary.pdf
    charts/
      aicc_operation_priority.png
      aicc_automation_fit.png
      aicc_quality_need.png
      aicc_competitor_benchmark.png

scripts/
  00_collect_hf_datasets.py
  01_collect_support_tickets.py
  01_load_dataset.py
  02_classify_inquiries.py
  03_score_kpi.py
  04_benchmark_competitors.py
```

### Main Final Files

| File | Description |
| --- | --- |
| `data/sources.csv` | 데이터셋, NAVER 공식 자료, 경쟁사/시장 자료 출처 목록 |
| `data/synthetic_leads.csv` | AiCall 도입 문의 양식 기반 합성 리드 시뮬레이션 |
| `data/manual/competitor_metrics.csv` | 경쟁사 공개 지표 원천 테이블 |
| `data/processed/aicc_inquiry_dataset.csv` | 공개 고객지원 데이터를 AICC 운영 분류로 정리한 데이터 |
| `data/processed/aicc_inquiry_scored.csv` | 문의 유형별 운영 KPI 점수를 붙인 분석 데이터 |
| `outputs/final/result_summary.csv` | 프로젝트 가이드 방식의 비율 기반 KPI 요약 |
| `outputs/final/aicc_kpi_summary.csv` | 문의 유형별 건수, 비중, 운영 KPI 점수 요약 |
| `outputs/final/aicc_operation_priority.csv` | 운영 우선순위와 추천 액션 요약 |
| `outputs/final/aicc_competitor_benchmark.csv` | 경쟁사 공개자료 기반 벤치마크 결과 |
| `outputs/final/charts/` | 최종 보고서에 사용할 차트 이미지 |
| `outputs/final/portfolio_summary.pdf` | 최종 PDF 산출물 자리 |

### Guide File Mapping

| Guide example | Actual file in this repository |
| --- | --- |
| `src/01_load_hf_dataset.py` | `scripts/00_collect_hf_datasets.py`, `scripts/01_load_dataset.py` |
| `src/02_classify_inquiries.py` | `scripts/01_load_dataset.py` |
| `src/03_score_operational_kpis.py` | `scripts/02_classify_inquiries.py`, `scripts/03_score_kpi.py` |
| `src/04_competitor_benchmark.py` | `scripts/04_benchmark_competitors.py` |
| `outputs/classified_inquiries.csv` | `data/processed/aicc_inquiry_dataset.csv` |
| `outputs/operational_kpi_summary.csv` | `outputs/final/aicc_kpi_summary.csv` |
| `outputs/competitor_benchmark.csv` | `outputs/final/aicc_competitor_benchmark.csv` |
| `outputs/result_summary.csv` | `outputs/final/result_summary.csv` |

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python scripts/00_collect_hf_datasets.py
python scripts/01_collect_support_tickets.py
python scripts/01_load_dataset.py
python scripts/02_classify_inquiries.py
python scripts/03_score_kpi.py
python scripts/04_benchmark_competitors.py
```

`data/raw/`와 `resources/`는 Git 추적 대상에서 제외했습니다. 원천 PDF와 대용량 원본 데이터는 로컬에서만 관리하고,
제출용 분석 결과와 출처 요약만 저장소에 포함합니다.
