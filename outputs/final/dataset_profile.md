# Dataset Profile

## 1. Source Summary

- Main input: `data/processed/customer_support_inquiries.csv`
- Support ticket input: `data/processed/support_tickets_normalized.csv`
- Output file: `data/processed/aicc_inquiry_dataset.csv`
- Total rows: `29,872`

## 2. Dataset Source Distribution

데이터 없음

## 3. AICC Label Distribution

| aicc_label   |   count |   ratio |
|:-------------|--------:|--------:|
| 업무 처리 요청     |    9896 |   33.13 |
| 결제/청구        |    7468 |   25    |
| 계정/인증        |    5469 |   18.31 |
| 상담원 연결       |    2092 |    7    |
| 장애/오류        |    1412 |    4.73 |
| FAQ/단순 안내    |    1384 |    4.63 |
| 기타           |    1151 |    3.85 |
| 불만/클레임       |    1000 |    3.35 |

## 4. Operation Insight Distribution

| operation_insight      |   count |   ratio |
|:-----------------------|--------:|--------:|
| Main Scenario 설계 필요    |    9896 |   33.13 |
| 정산/청구 문의 관리 필요         |    7468 |   25    |
| 본인확인/인증 플로우 관리 필요      |    5469 |   18.31 |
| Human Handoff 정책 필요    |    2092 |    7    |
| 상담 어시스턴트 및 장애 대응 필요    |    1412 |    4.73 |
| Global Scenario 자동화 후보 |    1384 |    4.63 |
| 추가 분류 검토 필요            |    1151 |    3.85 |
| Auto QA 및 품질 모니터링 필요   |    1000 |    3.35 |

## 5. Automation Fit Distribution

| automation_fit   |   count |   ratio |
|:-----------------|--------:|--------:|
| 중간               |   12937 |   43.31 |
| 높음               |   11280 |   37.76 |
| 낮음               |    4504 |   15.08 |
| 검토 필요            |    1151 |    3.85 |

## 6. Quality Management Need Distribution

| quality_management_need   |   count |   ratio |
|:--------------------------|--------:|--------:|
| 중간                        |   22833 |   76.44 |
| 높음                        |    4504 |   15.08 |
| 낮음                        |    2535 |    8.49 |

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
