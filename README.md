# AICC Ops Insight

AICC 고객 문의 데이터와 공개 경쟁사 자료를 활용해  
NAVER Cloud CLOVA AiCall 관점의 운영 KPI, 고객 문의 유형, 경쟁사 지표, 운영 개선안을 분석한 포트폴리오 프로젝트입니다.

> 본 프로젝트는 NAVER Cloud 지원 포트폴리오 목적으로 수행한 비공식 분석입니다.  
> NAVER Cloud 또는 NAVER와 공식적으로 관련된 프로젝트가 아닙니다.

---

## 1. Project Overview

본 프로젝트는 AI PaaS 상품 운영 직무에서 필요한 다음 역량을 보여주기 위해 설계했습니다.

- 상품별 고객 문의 및 CS 운영 현황 분석
- 주요 이슈 기반 운영 인사이트 도출
- 경쟁사 동향 모니터링 및 시장 리서치
- 운영 KPI 정의 및 문서화
- 솔루션별 품질 평가 및 운영 품질 관리 관점 도출

분석 대상은 NAVER Cloud의 AI Contact Center 상품인 **CLOVA AiCall**을 중심으로 설정했습니다.  
CLOVA AiCall은 Contact Center, Agent, Channel 구조를 기반으로 Inbound/Outbound Call 업무를 AI Bot으로 처리하는 AICC 서비스입니다.

---

## 2. Why AICC?

여러 AI PaaS 상품 중 AICC를 분석 대상으로 선정한 이유는 다음과 같습니다.

1. 고객 문의, CS 운영, 품질 평가, 운영 리포트와 직접 연결되는 상품입니다.
2. 상담사 수, 평균 콜 수, 채널 수, 통화 건수 등 운영 KPI로 전환 가능한 정보가 많습니다.
3. KT, LGU+, SKT/SK AX 등 경쟁사의 공개 수주액, 고객사 수, 매출 목표 자료가 존재합니다.
4. 지원 직무의 담당업무인 고객 문의 관리, 경쟁사 모니터링, 운영 개선 인사이트 도출과 가장 직접적으로 연결됩니다.

---

## 3. Scope

### Included

- AICC 중심 분석
- NAVER Cloud CLOVA AiCall 중심
- 경쟁사: KT, LGU+, SKT/SK AX
- Hugging Face 고객지원 데이터셋 활용
- 공개자료 기반 경쟁사 지표 수집
- Python 기반 문의 유형 분류 및 점수화
- 운영 개선안 도출

### Excluded

- eKYC 심층 분석
- CLOVA Note 사용 테스트
- 모든 CLOVA 제품 비교
- 무거운 ML 모델 학습
- 실제 고객사처럼 보이는 과도한 합성 데이터 생성
- 개발 구현 중심 설명

---

## 4. Data Sources

본 프로젝트는 무단 크롤링을 하지 않고, 다음 데이터만 활용합니다.

### Public Dataset

- Hugging Face 고객지원 데이터셋
- 고객 문의 문장, intent, category 기반 문의 유형 분석

### Public Market Sources

- NAVER Cloud CLOVA AiCall 공식 문서
- KT AICC 관련 공개 기사 및 보도자료
- LGU+ AICC 관련 공개 기사 및 보도자료
- SKT/SK AX AICC 관련 공개 기사 및 보도자료

### Synthetic Data

실제 기업의 AICC 도입 문의 데이터는 공개되어 있지 않기 때문에,  
CLOVA AiCall 문의 양식에서 요구하는 항목을 참고해 제한적인 시뮬레이션 데이터를 사용할 수 있습니다.

합성 데이터는 실제 고객사를 추정하기 위한 목적이 아니라,  
도입 문의 단계의 정보가 운영 KPI로 어떻게 전환될 수 있는지 검증하기 위한 목적입니다.

---

## 5. Analysis Framework

### Customer Inquiry Classification

고객 문의 문장을 다음 유형으로 분류합니다.

- FAQ
- 업무 처리 요청
- 장애 / 오류
- 불만 / 클레임
- 상담원 연결 요청
- 결제 / 청구
- 계정 / 인증
- 단순 안내
- 캠페인 / 해피콜

### Operation KPI Mapping

분류된 문의 유형을 AICC 운영 지표로 변환합니다.

| Inquiry Type     | Operation Insight           |
| ---------------- | --------------------------- |
| FAQ              | Global Scenario 자동화 후보 |
| 업무 처리 요청   | Main Scenario 설계 필요     |
| 장애 / 오류      | 상담 어시스턴트 필요        |
| 불만 / 클레임    | Auto QA 필요                |
| 상담원 연결 요청 | Human Handoff 정책 필요     |
| 불명확 발화      | Repair Scenario 중요        |

---

## 6. Competitor Benchmarking

경쟁사는 다음 기준으로 비교합니다.

| Company     | Product / Area           | Key Metrics                          |
| ----------- | ------------------------ | ------------------------------------ |
| NAVER Cloud | CLOVA AiCall / HappyCall | 자동화율, 대기시간 감소, 처리율 향상 |
| KT          | AICC                     | 수주액, 고객사 수, 월 콜 처리량      |
| LGU+        | AICC                     | 매출 목표, 고객사 수, Auto QA        |
| SKT / SK AX | AI CCaaS / AICC          | 도입 문의, 고객사, 상담 자동화 기능  |

---

## 7. Expected Outputs

최종 산출물은 다음과 같습니다.

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
