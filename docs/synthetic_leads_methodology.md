# Synthetic Lead Methodology

## Purpose

실제 기업의 CLOVA AiCall 도입 문의 데이터는 공개되어 있지 않습니다.
따라서 `data/synthetic_leads.csv`는 실제 고객사 현황을 추정하기 위한 데이터가 아니라,
도입 문의 단계에서 수집될 수 있는 항목이 어떤 운영 KPI로 전환되는지 검증하기 위한
시뮬레이션 데이터입니다.

## Source Structure

합성 리드는 NAVER Cloud CLOVA AiCall 도입 문의에서 운영 진단에 활용될 수 있는 항목을 기준으로 구성했습니다.

| Inquiry field | KPI interpretation |
| --- | --- |
| `lead_stage` | 신규 도입, 재구축, 고도화에 따른 도입 성숙도 |
| `operation_model` | 자체 운영/아웃소싱 여부에 따른 운영 전환 난이도 |
| `agent_count_range` | 상담 조직 규모 |
| `avg_daily_call_range` | 예상 콜 처리량 |
| `current_solution` | 기존 솔루션 유무와 마이그레이션 난이도 |
| `desired_features` | 기능 수요와 시나리오 설계 범위 |
| `pain_point` | 주요 운영 이슈와 품질관리 필요 영역 |

## Score Fields

| Score | Meaning |
| --- | --- |
| `estimated_call_volume_score` | 평균 일 콜 수 범위 기반 처리량 부담 |
| `operation_scale_score` | 상담사 수 범위 기반 운영 규모 |
| `migration_complexity_score` | 기존 솔루션 전환 난이도 |
| `feature_demand_score` | 희망 기능의 범위와 복잡도 |
| `automation_fit_score` | FAQ, 예약, 주문 조회 등 자동화 적합도 |

## Usage Note

이 데이터는 포트폴리오 내 운영 프레임워크 검증용입니다.
실제 NAVER Cloud 고객 데이터, 실제 매출 기회, 실제 업종별 수요를 의미하지 않습니다.
