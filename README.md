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
도입 문의 단계 정보가 운영 KPI로 어떻게 전환되는지 검증하기 위한 시뮬레이션 데이터를 일부 사용했습니다.

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

```text
data/
  sources.csv
  classified_inquiries.csv
  competitor_metrics.csv
  final_scores.csv

outputs/
  final/
    aicc_kpi_summary.csv
    competitor_benchmark.csv
    portfolio_summary.pdf

scripts/
  01_load_dataset.py
  02_classify_inquiries.py
  03_score_kpi.py
  04_benchmark_competitors.py
```
