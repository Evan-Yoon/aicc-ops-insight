# AICC KPI Summary

## 1. Purpose

본 분석은 공개 고객지원 데이터셋을 AICC 운영 관점으로 재분류하여,
CLOVA AiCall 운영에서 중요하게 볼 수 있는 자동화 적합도, 상담원 연결 필요도,
Auto QA 필요도, 시나리오 복잡도를 산출하기 위한 것입니다.

pandas의 `groupby`는 데이터를 특정 컬럼 기준으로 나눈 뒤 집계하는 데 사용되며,
본 프로젝트에서는 문의 유형별 평균 점수와 건수를 계산하는 데 사용했습니다. 

## 2. KPI Definition

| KPI | Meaning |
|---|---|
| automation_score | 음성봇/챗봇 자동화에 적합한 정도 |
| handoff_need_score | 상담원 연결 정책이 필요한 정도 |
| auto_qa_need_score | Auto QA 및 품질 모니터링이 필요한 정도 |
| scenario_complexity_score | Main/Global/Repair 시나리오 설계 복잡도 |
| main_scenario_need | 핵심 업무 처리 시나리오 필요도 |
| global_scenario_need | FAQ, 상담원 연결 등 Global Scenario 필요도 |
| repair_scenario_need | 무응답/오류/이탈 복구 시나리오 필요도 |
| operation_priority_score | 운영 우선순위 종합 점수 |

## 3. AICC Label KPI Summary

| aicc_label   |   inquiry_count |   automation_score |   handoff_need_score |   auto_qa_need_score |   scenario_complexity_score |   main_scenario_need |   global_scenario_need |   repair_scenario_need |   operation_priority_score |   inquiry_ratio |
|:-------------|----------------:|-------------------:|---------------------:|---------------------:|----------------------------:|---------------------:|-----------------------:|-----------------------:|---------------------------:|----------------:|
| 장애/오류        |            1412 |                 35 |                   80 |                   85 |                          70 |                   60 |                     40 |                     85 |                       73.2 |            4.73 |
| 불만/클레임       |            1000 |                 20 |                   85 |                   95 |                          65 |                   45 |                     35 |                     80 |                       73   |            3.35 |
| 계정/인증        |            5469 |                 55 |                   60 |                   65 |                          75 |                   80 |                     35 |                     65 |                       64.2 |           18.31 |
| 결제/청구        |            7468 |                 60 |                   55 |                   60 |                          70 |                   75 |                     40 |                     55 |                       60   |           25    |
| 상담원 연결       |            2092 |                 25 |                   95 |                   60 |                          50 |                   30 |                     85 |                     50 |                       60   |            7    |
| 업무 처리 요청     |            9896 |                 75 |                   45 |                   45 |                          80 |                   90 |                     35 |                     55 |                       58   |           33.13 |
| 기타           |            1151 |                 40 |                   50 |                   50 |                          50 |                   50 |                     50 |                     50 |                       48.5 |            3.85 |
| FAQ/단순 안내    |            1384 |                 90 |                   20 |                   30 |                          40 |                   20 |                     90 |                     30 |                       38.5 |            4.63 |

## 4. Source Type x AICC Label Summary

| source_type   | aicc_label   | count   |
|---------------|--------------|---------|

## 5. Key Insight

운영 우선순위가 가장 높은 문의 유형은 **장애/오류**입니다.

이 유형은 다음 이유로 우선 관리 대상입니다.

- 운영 우선순위 점수: `73.2`
- 문의 건수: `1,412`
- 전체 비중: `4.73%`

## 6. How This Connects to CLOVA AiCall

CLOVA AiCall 운영 관점에서 이 결과는 다음과 같이 해석할 수 있습니다.

| Data Result | AiCall Operation Meaning |
|---|---|
| FAQ/단순 안내 비중 | Global Scenario 자동화 후보 |
| 업무 처리 요청 비중 | Main Scenario 설계 필요 |
| 상담원 연결 요청 | Human Handoff 정책 필요 |
| 장애/오류 및 불만/클레임 | Auto QA 및 상담 어시스턴트 필요 |
| 높은 Repair 점수 | 무응답/의도 불명확 발화 대응 정책 필요 |

## 7. Limitation

- 본 데이터는 실제 NAVER Cloud 고객 데이터가 아닙니다.
- 영어 고객지원 데이터셋 기반이므로 국내 콜센터 표현과 차이가 있을 수 있습니다.
- 점수는 운영 분석을 위한 rule-based scoring이며, 실제 상품 성능이나 시장 점유율을 의미하지 않습니다.
- 후속 분석에서는 AI Hub 한국어 콜센터 데이터셋으로 확장할 수 있습니다.
