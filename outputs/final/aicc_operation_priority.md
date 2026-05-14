# AICC Operation Priority Report

## 1. Purpose

본 문서는 공개 고객지원 데이터셋과 보조 티켓 데이터를 AICC 운영 관점으로 재분류한 뒤,
문의 유형별 운영 우선순위와 개선 액션을 정리한 결과입니다.

분석 목적은 실제 NAVER Cloud 고객 현황을 추정하는 것이 아니라,
CLOVA AiCall 운영 담당자가 고객 문의와 CS 운영 현황을 어떤 지표로 구조화할 수 있는지 검토하는 것입니다.

---

## 2. Final Operation Priority Table

|   priority_rank | aicc_label   |   inquiry_count |   inquiry_ratio |   operation_priority_score |   automation_score |   handoff_need_score |   auto_qa_need_score |   scenario_complexity_score |   main_scenario_need |   global_scenario_need |   repair_scenario_need | recommended_operation_action     |
|----------------:|:-------------|----------------:|----------------:|---------------------------:|-------------------:|---------------------:|---------------------:|----------------------------:|---------------------:|-----------------------:|-----------------------:|:---------------------------------|
|               1 | 장애/오류        |            1412 |            4.73 |                       73.2 |                 35 |                   80 |                   85 |                          70 |                   60 |                     40 |                     85 | 상담 어시스턴트와 장애 대응 지식베이스 강화         |
|               2 | 불만/클레임       |            1000 |            3.35 |                       73   |                 20 |                   85 |                   95 |                          65 |                   45 |                     35 |                     80 | Auto QA와 상담 품질 모니터링 우선 적용        |
|               3 | 계정/인증        |            5469 |           18.31 |                       64.2 |                 55 |                   60 |                   65 |                          75 |                   80 |                     35 |                     65 | 본인확인/인증 실패 케이스 대응 플로우 정리         |
|               4 | 결제/청구        |            7468 |           25    |                       60   |                 60 |                   55 |                   60 |                          70 |                   75 |                     40 |                     55 | 정산/청구 문의 분류와 민감 문의 대응 기준 수립      |
|               5 | 상담원 연결       |            2092 |            7    |                       60   |                 25 |                   95 |                   60 |                          50 |                   30 |                     85 |                     50 | Human Handoff 정책과 상담원 연결 조건 정교화  |
|               6 | 업무 처리 요청     |            9896 |           33.13 |                       58   |                 75 |                   45 |                   45 |                          80 |                   90 |                     35 |                     55 | Main Scenario 설계와 API 연동 프로세스 검토 |
|               7 | 기타           |            1151 |            3.85 |                       48.5 |                 40 |                   50 |                   50 |                          50 |                   50 |                     50 |                     50 | 추가 문의 유형 정의 및 수동 검토 필요           |
|               8 | FAQ/단순 안내    |            1384 |            4.63 |                       38.5 |                 90 |                   20 |                   30 |                          40 |                   20 |                     90 |                     30 | Global Scenario와 FAQ 자동화 우선 검토   |

---

## 3. Top Priority Insight

가장 높은 운영 우선순위로 분류된 문의 유형은 **장애/오류**입니다.

- 운영 우선순위 점수: `73.2`
- 문의 건수: `1,412`
- 전체 비중: `4.73%`
- 추천 운영 액션: `상담 어시스턴트와 장애 대응 지식베이스 강화`

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
