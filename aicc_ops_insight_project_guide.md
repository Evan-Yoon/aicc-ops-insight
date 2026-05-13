# CLOVA AiCall 도입 문의·운영 KPI 기반 AICC 운영 인사이트 분석 프로젝트 가이드

> 목적: NAVER Cloud `AI Solution 운영 지원/관리` 직무 지원용 대표 프로젝트를 **일요일 제출 가능 수준**으로 완성한다.  
> 최종 산출물은 “개발 포트폴리오”가 아니라 **AI PaaS 상품 운영/CS/경쟁사 분석/품질관리 관점의 분석 포트폴리오**다.

---

## 0. 최종 프로젝트 정의

### 프로젝트명

**CLOVA AiCall 도입 문의·운영 KPI 기반 AICC 운영 인사이트 분석**

### 한 줄 설명

Hugging Face 공개 고객지원 데이터셋과 NAVER CLOVA AiCall 공식 가이드, 경쟁사 공개자료를 바탕으로 AICC 고객 문의 유형을 분류하고, 운영 KPI와 품질관리 개선안을 도출한 프로젝트.

### 지원 직무와의 연결

공고 담당업무와 프로젝트의 연결은 아래와 같다.

| 공고 담당업무 | 프로젝트에서 보여줄 것 |
|---|---|
| AI PaaS 상품의 계약, 정산 등 운영 관리 | 상담사 수, 평균 콜 수, 채널 수, 통화량을 기반으로 운영 규모와 계약/과금 검토 포인트를 정리 |
| 상품별 고객 문의 및 CS 운영 현황 관리 | 고객지원 데이터셋을 기반으로 문의 유형을 분류하고 FAQ/불만/장애/상담원 연결 비중을 분석 |
| 주요 이슈 기반 인사이트 도출 | 문의 유형별 빈도와 자동화 가능성을 기준으로 음성봇, 상담 어시스턴트, Auto QA 필요도를 도출 |
| 경쟁사 동향 모니터링 및 시장 리서치 | KT, LGU+, SKT/SK AX의 AICC 공개 지표와 NAVER 지표를 비교 |
| 상품 기획 및 운영 워크플로우 문서화 | 도입 문의 양식 → 운영 KPI → 개선 리포트 템플릿으로 문서화 |
| 솔루션별 품질 평가 및 운영 품질 관리 | Main/Global/Repair 시나리오, 상담원 연결, 무응답/불명확 발화, Auto QA 필요도를 품질관리 항목으로 연결 |

---

## 1. 프로젝트 범위

### 유지할 것

- AICC 중심 분석
- NAVER CLOVA AiCall 중심
- 경쟁사: KT, LGU+, SKT/SK AX
- Hugging Face 고객지원 데이터셋 활용
- 공개자료 기반 경쟁사 지표 수집
- Python으로 문의 유형 분류/점수화
- 운영 개선안 도출

### 줄이거나 버릴 것

- eKYC 심층 분석
- 클로바노트 테스트
- 모든 CLOVA 제품 비교
- 너무 무거운 ML 모델 학습
- 실제 고객사처럼 보이는 가짜 데이터 과다 생성
- 기술 구현 중심 설명

### 최종 분석 질문

1. 고객지원 데이터에서 반복적으로 나타나는 문의 유형은 무엇인가?
2. 이 문의 유형은 CLOVA AiCall의 Main / Global / Repair 시나리오와 어떻게 연결되는가?
3. AiCall 도입 문의 양식의 상담사 수, 평균 콜 수, 기존 솔루션, 희망 기능은 어떤 운영 KPI로 전환될 수 있는가?
4. NAVER AiCall은 경쟁사 대비 어떤 공개 운영 지표가 강하고, 어떤 지표가 상대적으로 부족한가?
5. 운영 담당자 관점에서 어떤 CS 분류 체계, 리포트, 품질관리 개선안을 제안할 수 있는가?

---

## 2. 왜 AICC를 분석 대상으로 선택했는가

자기소개서와 포트폴리오에서 반드시 설명해야 하는 핵심 논리다.

### 선정 기준

| 기준 | 설명 |
|---|---|
| 직무 적합성 | AICC는 고객 문의, CS 운영, 품질 평가, 상담원 연결, 자동화율 등 운영 지표가 직접적으로 드러나는 상품이다. |
| 공개 데이터 확보 가능성 | 경쟁사인 KT, LGU+, SKT/SK AX의 수주액, 고객사 수, 매출 목표, 기능 고도화 자료가 비교적 많이 공개되어 있다. |
| NAVER 상품 구조와의 연결성 | CLOVA AiCall은 Contact Center, Agent, Channel, Dashboard, Scenario 구조를 갖고 있어 운영 KPI 분석에 적합하다. |
| 개선안 도출 가능성 | 고객사별 도입 효과 리포트, 문의 유형 분류, Auto QA 필요도, 시나리오 개선안 등으로 연결 가능하다. |
| 지원자의 강점과 연결 | 호텔 HR/총무 운영 경험 + AI 교육/프로젝트 경험을 “AI 서비스 운영 품질 개선”으로 연결할 수 있다. |

### 포트폴리오에 넣을 선정 이유 문장

> NAVER Cloud의 AI PaaS 상품은 CLOVA Speech, Voice, AiCall, eKYC 등으로 구성되어 있으나, 이번 프로젝트에서는 고객 문의·CS 운영·품질 평가·경쟁사 분석과 가장 직접적으로 연결되는 AICC 영역을 분석 대상으로 선정했다. 특히 CLOVA AiCall은 도입 문의 단계에서 상담사 수, 평균 콜 수, 기존 솔루션, 희망 기능을 요구하고 있어 고객사의 운영 규모와 도입 성숙도를 사전에 진단하는 구조를 가진다고 판단했다. 따라서 AICC를 중심으로 공개 고객지원 데이터와 경쟁사 지표를 수집하고, 운영 KPI 및 개선안을 도출했다.

---

## 3. 참고 근거 정리

### 3.1 NAVER CLOVA AiCall 공식 문서에서 가져올 근거

사용자가 업로드한 CLOVA AiCall PDF에서 다음 내용을 근거로 사용한다.

#### AiCall 개요

- CLOVA AiCall은 음성 인식, 자연어 처리 및 대화 모델, 음성 합성을 활용하여 Inbound/Outbound Call 업무를 AI Bot으로 처리하는 서비스다.
- CLOVA AiCall 빌더를 통해 고객 응대 흐름을 생성할 수 있고, 고객 응대 규모에 따라 Contact Center 확장/축소를 관리할 수 있다.
- 구성 요소는 Contact Center, Agent, Channel이다.
- Channel은 Contact Center의 최대 동시 통화 수를 의미한다.
- Inbound는 고객 문의 전화를 AI Callbot Agent가 받는 구조이고, Outbound는 캠페인을 통해 대상 고객에게 자동 발신하는 구조다.

#### AiCall 통계 정보

- Contact Center별 주요 콜 지표:
  - 통화 건 수
  - 통화 시간
  - 서비스 이용 시간
  - 채널 수
- Agent별 주요 콜 지표:
  - 통화 시간
  - 통화 건 수
- 실시간 운영 현황:
  - 키워드 포함 세션
  - 진행 중 세션
  - Agent 수
  - 전화번호 수
  - 채널 수
  - 진행 중 캠페인 수

#### AiCall 시나리오 작성 구조

- Main 시나리오:
  - 핵심 업무 처리 흐름
  - 예: 예약, 정보 확인, 업무 처리
- Global 시나리오:
  - 자주 들어오는 문의와 요청
  - 예: FAQ, 상담원 연결 요청, 통화 종료 요청
- Repair 시나리오:
  - 무응답, 의도 불명확, 재발화 요청 등 정상 흐름 이탈을 복구하는 구조

#### AiCall 생성 프로세스

- Contact Center 생성
- 전화번호 발급 및 등록
- 고객 응대 시나리오 생성 및 등록
- Agent 생성
- 캠페인 대상 등록 및 캠페인 생성
- 대시보드 확인

#### 권한·감사 운영

- Sub Account를 통해 관리형 정책과 사용자 정의 정책을 설정할 수 있다.
- Resource Manager는 리소스 유형과 작업 내역을 정의한다.
- Cloud Activity Tracer는 사용자 활동 이력을 수집해 모니터링이나 감사 보고서 작성에 활용할 수 있다.

---

## 4. 최종 산출물 목록

일요일 제출 기준으로 아래 4개만 완성한다.

| 산출물 | 파일명 | 목적 |
|---|---|---|
| 원천 데이터 정리 | `data/sources.csv` | 경쟁사 기사, NAVER 문서, 데이터셋 출처 기록 |
| 분석 결과 데이터 | `outputs/result_summary.csv` | 문의 유형별 비중, 운영 KPI 점수, 경쟁사 지표 |
| Python 분석 코드 | `src/main.py` 또는 `notebooks/analysis.ipynb` | 데이터 로드, 분류, 점수화, 차트 생성 |
| 포트폴리오 PDF | `outputs/portfolio_summary.pdf` | 지원서 첨부용 4페이지 요약 자료 |

---

## 5. 프로젝트 폴더 구조

아래 구조 그대로 만든다.

```bash
aicc-ops-insight/
├─ README.md
├─ requirements.txt
├─ .env.example
├─ data/
│  ├─ raw/
│  │  └─ README.md
│  ├─ sources.csv
│  ├─ competitor_sources.csv
│  ├─ synthetic_leads.csv
│  └─ hf_customer_support_sample.csv
├─ src/
│  ├─ 01_load_hf_dataset.py
│  ├─ 02_classify_inquiries.py
│  ├─ 03_score_operational_kpis.py
│  ├─ 04_competitor_benchmark.py
│  └─ 05_make_charts.py
├─ outputs/
│  ├─ classified_inquiries.csv
│  ├─ operational_kpi_summary.csv
│  ├─ competitor_benchmark.csv
│  ├─ chart_inquiry_types.png
│  ├─ chart_kpi_scores.png
│  └─ portfolio_summary.pdf
└─ docs/
   ├─ portfolio_outline.md
   ├─ self_introduction_answer_draft.md
   └─ project_answer_draft.md
```

---

## 6. 맥북 개발 환경 세팅

### 6.1 프로젝트 폴더 생성

```bash
mkdir aicc-ops-insight
cd aicc-ops-insight
mkdir -p data/raw src outputs docs
```

### 6.2 Python 가상환경 생성

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 6.3 requirements.txt 생성

```bash
cat > requirements.txt <<'EOF'
pandas
numpy
datasets
python-dotenv
matplotlib
scikit-learn
transformers
torch
sentencepiece
accelerate
EOF
```

설치:

```bash
pip install -r requirements.txt
```

> 시간이 부족하거나 `transformers/torch` 설치가 오래 걸리면, 처음에는 `datasets pandas numpy matplotlib scikit-learn`만 설치하고 룰 기반 분류로 먼저 결과를 만든다. 모델 분류는 선택 사항이다.

---

## 7. 데이터 수집 전략

### 7.1 데이터는 4종류로 나눈다

| 데이터 | 실제/합성 | 목적 |
|---|---|---|
| Hugging Face 고객지원 데이터셋 | 실제 공개 데이터 | 고객 문의 유형 분석 |
| NAVER CLOVA AiCall PDF/문의 양식 | 실제 공식 자료 | 운영 KPI 설계 근거 |
| 경쟁사 뉴스/공식자료 | 실제 공개 자료 | 시장성·기능·성과지표 비교 |
| 도입 문의 양식 기반 샘플 리드 | 합성 데이터 | 실제 B2B 문의 데이터가 공개되어 있지 않으므로, 운영 진단 시뮬레이션용으로만 사용 |

### 7.2 합성 데이터 사용 원칙

합성 데이터는 써도 된다. 단, 반드시 아래 문장을 포트폴리오에 넣는다.

> 실제 기업의 AiCall 도입 문의 데이터는 공개되어 있지 않기 때문에, NAVER Cloud CLOVA AiCall 문의 양식에서 요구하는 항목을 기준으로 합성 고객사 데이터를 구성했다. 이 데이터는 실제 고객사 현황을 추정하기 위한 목적이 아니라, 도입 문의 단계에서 수집되는 정보가 어떤 운영 KPI로 전환될 수 있는지 검증하기 위한 시뮬레이션 데이터로 사용했다.

---

## 8. Hugging Face 데이터셋 사용

### 8.1 기본 사용 데이터셋

1. `bitext/Bitext-customer-support-llm-chatbot-training-dataset`
   - 고객지원 intent detection 데이터셋
   - 27개 intent
   - 10개 category
   - 26,872개 Q/A pair
   - 고객 문의 유형 분류 기준으로 사용

2. 선택 데이터셋: `AIxBlock/92k-real-world-call-center-scripts-english`
   - 실제 콜센터 대화 전사 데이터
   - 크기가 클 수 있으므로 필수는 아니다.
   - 시간이 부족하면 Bitext만 사용한다.

### 8.2 데이터셋 로드 스크립트

파일 생성:

```bash
cat > src/01_load_hf_dataset.py <<'EOF'
import pandas as pd
from datasets import load_dataset

DATASET_ID = "bitext/Bitext-customer-support-llm-chatbot-training-dataset"
OUTPUT_FILE = "data/hf_customer_support_sample.csv"

def pick_column(columns, candidates):
    for c in candidates:
        if c in columns:
            return c
    return None

def main():
    print(f"Loading dataset: {DATASET_ID}")
    ds = load_dataset(DATASET_ID, split="train")
    df = ds.to_pandas()

    print("Columns:", list(df.columns))
    print("Rows:", len(df))

    text_col = pick_column(
        df.columns,
        ["instruction", "customer_request", "text", "utterance", "question", "input"]
    )
    intent_col = pick_column(df.columns, ["intent", "label", "intent_name"])
    category_col = pick_column(df.columns, ["category", "category_name", "group"])

    if text_col is None:
        raise ValueError("문의 문장 컬럼을 찾지 못했습니다. 데이터셋 컬럼을 확인하세요.")

    result = pd.DataFrame()
    result["source"] = "huggingface_bitext"
    result["customer_text"] = df[text_col].astype(str)

    if intent_col:
        result["original_intent"] = df[intent_col].astype(str)
    else:
        result["original_intent"] = ""

    if category_col:
        result["original_category"] = df[category_col].astype(str)
    else:
        result["original_category"] = ""

    # 너무 많으면 포트폴리오 분석용으로 샘플링
    result = result.sample(n=min(3000, len(result)), random_state=42)

    result.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"Saved: {OUTPUT_FILE}")
    print(result.head())

if __name__ == "__main__":
    main()
EOF
```

실행:

```bash
python src/01_load_hf_dataset.py
```

---

## 9. 문의 유형 분류 설계

### 9.1 AICC 운영 관점 문의 유형

아래 유형으로 분류한다.

| 분류명 | 설명 | AiCall 운영 연결 |
|---|---|---|
| FAQ | 단순 정보 문의 | Global 시나리오 |
| MAIN_TASK | 주문/예약/변경/취소 등 업무 처리 | Main 시나리오 |
| BILLING_CONTRACT | 결제, 청구, 계약, 정산 | 계약/정산 운영 관리 |
| TECH_ISSUE | 장애, 오류, 서비스 미작동 | CS 이슈 관리 |
| HUMAN_HANDOFF | 상담원 연결 필요 | 상담 전환 정책 |
| COMPLAINT_QA | 불만, 클레임, 품질 문제 | Auto QA / 품질관리 |
| REPAIR_RISK | 불명확, 반복, 재확인 필요 | Repair 시나리오 |
| LOW_PRIORITY | 단순 일반 문의 | 자동화 후보 |

### 9.2 룰 기반 분류 스크립트

모델 분류 전에 반드시 룰 기반 결과부터 만든다.  
이유: 시간이 부족해도 결과물을 낼 수 있기 때문이다.

```bash
cat > src/02_classify_inquiries.py <<'EOF'
import re
import pandas as pd

INPUT_FILE = "data/hf_customer_support_sample.csv"
OUTPUT_FILE = "outputs/classified_inquiries.csv"

RULES = {
    "BILLING_CONTRACT": [
        "invoice", "payment", "refund", "charge", "billing", "paid", "price", "subscription",
        "계약", "정산", "청구", "결제", "환불", "요금"
    ],
    "MAIN_TASK": [
        "order", "cancel", "change", "update", "track", "delivery", "return", "book", "reservation",
        "주문", "예약", "변경", "취소", "배송", "반품"
    ],
    "TECH_ISSUE": [
        "error", "issue", "problem", "not working", "bug", "login", "access", "crash", "failed",
        "오류", "장애", "문제", "접속", "로그인", "실패"
    ],
    "HUMAN_HANDOFF": [
        "agent", "human", "representative", "call me", "speak to", "manager",
        "상담원", "담당자", "사람", "직원", "연결"
    ],
    "COMPLAINT_QA": [
        "complaint", "angry", "bad", "poor", "dissatisfied", "unhappy", "terrible",
        "불만", "클레임", "품질", "나쁘", "화가", "불편"
    ],
    "REPAIR_RISK": [
        "repeat", "again", "unclear", "what do you mean", "don't understand",
        "다시", "반복", "이해", "무슨", "모르"
    ],
    "FAQ": [
        "how", "what", "when", "where", "help", "information", "available", "policy",
        "방법", "무엇", "언제", "어디", "안내", "정보", "정책"
    ],
}

def classify_rule(text: str) -> str:
    t = str(text).lower()

    # 우선순위가 중요하다. 불만/장애/상담원 연결은 단순 FAQ보다 먼저 잡는다.
    priority = [
        "COMPLAINT_QA",
        "TECH_ISSUE",
        "HUMAN_HANDOFF",
        "BILLING_CONTRACT",
        "MAIN_TASK",
        "REPAIR_RISK",
        "FAQ",
    ]

    for label in priority:
        for kw in RULES[label]:
            if kw.lower() in t:
                return label

    return "LOW_PRIORITY"

def map_to_aicall_scenario(label: str) -> str:
    mapping = {
        "FAQ": "Global",
        "MAIN_TASK": "Main",
        "BILLING_CONTRACT": "Main",
        "TECH_ISSUE": "Global/Human Handoff",
        "HUMAN_HANDOFF": "Global",
        "COMPLAINT_QA": "Auto QA / Human Handoff",
        "REPAIR_RISK": "Repair",
        "LOW_PRIORITY": "Global",
    }
    return mapping.get(label, "Global")

def main():
    df = pd.read_csv(INPUT_FILE)
    df["ops_label"] = df["customer_text"].apply(classify_rule)
    df["aicall_scenario"] = df["ops_label"].apply(map_to_aicall_scenario)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"Saved: {OUTPUT_FILE}")
    print(df["ops_label"].value_counts())
    print(df["aicall_scenario"].value_counts())

if __name__ == "__main__":
    main()
EOF
```

실행:

```bash
python src/02_classify_inquiries.py
```

---

## 10. 운영 KPI 점수화

### 10.1 KPI 정의

| KPI | 계산 기준 | 해석 |
|---|---|---|
| 자동화 적합도 | FAQ + MAIN_TASK + LOW_PRIORITY 비율 | 음성봇/챗봇으로 처리 가능한 문의 비중 |
| Main 시나리오 필요도 | MAIN_TASK + BILLING_CONTRACT 비율 | 핵심 업무 처리 시나리오 복잡도 |
| Global 시나리오 필요도 | FAQ + HUMAN_HANDOFF 비율 | 반복 문의/상담원 연결 정책 중요도 |
| Repair 시나리오 필요도 | REPAIR_RISK 비율 | 무응답/불명확 발화 대응 필요도 |
| Auto QA 필요도 | COMPLAINT_QA + TECH_ISSUE 비율 | 품질 평가/상담 리뷰 필요도 |
| 상담원 연결 필요도 | HUMAN_HANDOFF + COMPLAINT_QA + TECH_ISSUE 비율 | Human handoff 정책 필요도 |

### 10.2 KPI 산출 스크립트

```bash
cat > src/03_score_operational_kpis.py <<'EOF'
import pandas as pd

INPUT_FILE = "outputs/classified_inquiries.csv"
OUTPUT_FILE = "outputs/operational_kpi_summary.csv"

def pct(count, total):
    if total == 0:
        return 0
    return round(count / total * 100, 2)

def main():
    df = pd.read_csv(INPUT_FILE)
    total = len(df)

    counts = df["ops_label"].value_counts().to_dict()

    def c(label):
        return counts.get(label, 0)

    kpis = [
        {
            "kpi": "자동화 적합도",
            "score_percent": pct(c("FAQ") + c("MAIN_TASK") + c("LOW_PRIORITY"), total),
            "meaning": "음성봇/챗봇으로 처리 가능한 반복·단순·업무 처리 문의 비중",
            "operation_action": "FAQ/단순 업무를 Global/Main 시나리오로 우선 자동화"
        },
        {
            "kpi": "Main 시나리오 필요도",
            "score_percent": pct(c("MAIN_TASK") + c("BILLING_CONTRACT"), total),
            "meaning": "예약·변경·취소·계약·정산 등 업무 처리 흐름이 필요한 문의 비중",
            "operation_action": "업무 처리 프로세스, 변수 수집, API 연동 포인트 정의"
        },
        {
            "kpi": "Global 시나리오 필요도",
            "score_percent": pct(c("FAQ") + c("HUMAN_HANDOFF"), total),
            "meaning": "FAQ·상담원 연결·통화 종료 등 공통 요청 비중",
            "operation_action": "공통 FAQ와 상담원 연결 정책을 표준화"
        },
        {
            "kpi": "Repair 시나리오 필요도",
            "score_percent": pct(c("REPAIR_RISK"), total),
            "meaning": "불명확·반복·재확인 필요 문의 비중",
            "operation_action": "무응답/의도불명확 발화의 재질문·종료 정책 설계"
        },
        {
            "kpi": "Auto QA 필요도",
            "score_percent": pct(c("COMPLAINT_QA") + c("TECH_ISSUE"), total),
            "meaning": "불만·장애·오류 등 상담 품질 확인이 필요한 문의 비중",
            "operation_action": "상담 품질 평가, 키워드 모니터링, 클레임 리뷰 체계 설계"
        },
        {
            "kpi": "상담원 연결 필요도",
            "score_percent": pct(c("HUMAN_HANDOFF") + c("COMPLAINT_QA") + c("TECH_ISSUE"), total),
            "meaning": "AI 단독 응대보다 상담사 전환이 필요한 문의 비중",
            "operation_action": "Human handoff 기준과 상담사 지원 기능 정의"
        },
    ]

    result = pd.DataFrame(kpis)
    result.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

    print(f"Saved: {OUTPUT_FILE}")
    print(result)

if __name__ == "__main__":
    main()
EOF
```

실행:

```bash
python src/03_score_operational_kpis.py
```

---

## 11. 경쟁사 공개자료 수집

### 11.1 비교 대상

| 기업 | 상품/영역 | 분석 포인트 |
|---|---|---|
| NAVER Cloud | CLOVA AiCall / HappyCall | 금융권 해피콜 자동화, Contact Center 운영 구조 |
| KT | KT AICC | NH농협은행 수주, 금융권 구축 실적, 고객사 수, 월 콜 처리량 |
| LGU+ | LGU+ AICC | 매출 목표, 상담 어드바이저, Auto QA, 고객사 수 |
| SKT/SK AX | SKT AI CCaaS / SK AX AICC | 올인원 CCaaS, 가입 기업 수, 도입 문의 수, 상담 품질 표준화 |

### 11.2 경쟁사 자료 CSV 생성

```bash
cat > data/competitor_sources.csv <<'EOF'
company,product,metric_type,evidence_text,value,url,source_grade,memo
NAVER Cloud,CLOVA HappyCall,운영효율,"신한은행 사례에서 아웃바운드 콜 업무 95% 수행, 전화 대기시간 4분의 1 감소, 고객센터 업무 처리율 15% 상승 효과가 보도됨","95%;1/4;15%","https://zdnet.co.kr/view/?no=20210129170339","A","성과지표가 수치로 공개됨"
KT,KT AICC,시장성,"NH농협은행 400억 원 규모 차세대 컨택센터 사업 수주, 약 30건 금융권 AICC 구축 실적, 300개 이상 고객사, 월 1500만 콜 처리 역량 보도","400억;30건;300개;1500만콜","https://www.thelec.kr/news/articleView.html?idxno=37612","A","수주액·고객사 수·처리량 공개"
LGU+,LGU+ AICC,시장성,"AICC 매출 350억 원 목표, AI 상담 어드바이저와 Auto QA 도입 계획 보도","350억","https://www.etnews.com/20250527000189","A","매출 목표와 기능 고도화 공개"
LGU+,LGU+ AICC,시장성,"현재 200억 원 수준의 AICC B2B 매출을 350억 원으로 확대, 70여 개 고객사 공급 보도","200억;350억;70개","https://www.sisajournal-e.com/news/articleView.html?idxno=412073","A","매출·고객사 수 공개"
SKT,SKT AI CCaaS,시장성,"출시 3개월 만에 10여 개 기업 고객 가입, 50여 개 고객사 도입 문의 보도","10개;50개","https://news.sktelecom.com/208852","A","가입·문의 수 공개"
SK AX,SK AX AICC,기능범위,"콜봇·챗봇 자동 처리, AI 상담 지원, KMS 검색, 상담요약, Hot 키워드 추출 등 AI 상담 지원 및 분석 자동화 기능 제공","기능범위","https://www.skax.co.kr/ax-services/aicc/","B","공식 제품 페이지 기반 기능 근거"
EOF
```

### 11.3 경쟁사 벤치마크 점수 기준

| 지표 | 배점 | 설명 |
|---|---:|---|
| 시장성 공개 근거 | 25 | 수주액, 매출 목표, 고객사 수 등 |
| 도입 레퍼런스 | 20 | 금융권, 대기업, 공공기관 등 |
| 운영 효율 성과 | 20 | 자동화율, 대기시간 감소, 처리율 상승 |
| 기능 고도화 | 20 | 상담 어시스턴트, Auto QA, 상담 요약, KMS |
| 운영 품질 관리 | 15 | 상담 평가, 리포트, 품질관리 기능 |

### 11.4 경쟁사 점수화 스크립트

```bash
cat > src/04_competitor_benchmark.py <<'EOF'
import pandas as pd
import re

INPUT_FILE = "data/competitor_sources.csv"
OUTPUT_FILE = "outputs/competitor_benchmark.csv"

WEIGHTS = {
    "시장성 공개 근거": 25,
    "도입 레퍼런스": 20,
    "운영 효율 성과": 20,
    "기능 고도화": 20,
    "운영 품질 관리": 15,
}

KEYWORDS = {
    "시장성 공개 근거": ["억", "매출", "수주", "고객사", "문의", "가입", "콜"],
    "도입 레퍼런스": ["은행", "금융", "보험", "대기업", "공공", "고객사", "도입"],
    "운영 효율 성과": ["자동화", "대기시간", "처리율", "감소", "상승", "수행", "효율"],
    "기능 고도화": ["상담 어드바이저", "Auto QA", "상담요약", "KMS", "콜봇", "챗봇", "STT", "TTS"],
    "운영 품질 관리": ["QA", "평가", "품질", "피드백", "표준화", "모니터링", "리포트"],
}

def has_keyword(text, words):
    text = str(text)
    return any(w.lower() in text.lower() for w in words)

def main():
    df = pd.read_csv(INPUT_FILE)

    rows = []
    for company, g in df.groupby("company"):
        full_text = " ".join(g["evidence_text"].fillna("").tolist()) + " " + " ".join(g["memo"].fillna("").tolist())

        row = {
            "company": company,
            "source_count": len(g),
            "evidence_values": " / ".join(g["value"].fillna("").astype(str).tolist()),
        }

        total = 0
        for metric, weight in WEIGHTS.items():
            score = weight if has_keyword(full_text, KEYWORDS[metric]) else 0
            row[metric] = score
            total += score

        row["total_score"] = total
        rows.append(row)

    result = pd.DataFrame(rows).sort_values("total_score", ascending=False)
    result.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

    print(f"Saved: {OUTPUT_FILE}")
    print(result)

if __name__ == "__main__":
    main()
EOF
```

실행:

```bash
python src/04_competitor_benchmark.py
```

---

## 12. 차트 생성

```bash
cat > src/05_make_charts.py <<'EOF'
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

Path("outputs").mkdir(exist_ok=True)

def chart_inquiry_types():
    df = pd.read_csv("outputs/classified_inquiries.csv")
    counts = df["ops_label"].value_counts().sort_values(ascending=True)

    plt.figure(figsize=(9, 5))
    plt.barh(counts.index, counts.values)
    plt.title("Customer Inquiry Type Distribution")
    plt.xlabel("Count")
    plt.tight_layout()
    plt.savefig("outputs/chart_inquiry_types.png", dpi=200)
    plt.close()

def chart_kpi_scores():
    df = pd.read_csv("outputs/operational_kpi_summary.csv")
    df = df.sort_values("score_percent", ascending=True)

    plt.figure(figsize=(9, 5))
    plt.barh(df["kpi"], df["score_percent"])
    plt.title("AICC Operational KPI Scores")
    plt.xlabel("Score (%)")
    plt.tight_layout()
    plt.savefig("outputs/chart_kpi_scores.png", dpi=200)
    plt.close()

def chart_competitor_scores():
    df = pd.read_csv("outputs/competitor_benchmark.csv")
    df = df.sort_values("total_score", ascending=True)

    plt.figure(figsize=(9, 5))
    plt.barh(df["company"], df["total_score"])
    plt.title("AICC Competitor Public Evidence Score")
    plt.xlabel("Score")
    plt.tight_layout()
    plt.savefig("outputs/chart_competitor_scores.png", dpi=200)
    plt.close()

def main():
    chart_inquiry_types()
    chart_kpi_scores()
    chart_competitor_scores()
    print("Charts saved to outputs/")

if __name__ == "__main__":
    main()
EOF
```

실행:

```bash
python src/05_make_charts.py
```

---

## 13. 전체 실행 순서

아래 순서대로만 진행한다.

```bash
# 1. 가상환경 활성화
source .venv/bin/activate

# 2. 데이터셋 로드
python src/01_load_hf_dataset.py

# 3. 문의 유형 분류
python src/02_classify_inquiries.py

# 4. 운영 KPI 산출
python src/03_score_operational_kpis.py

# 5. 경쟁사 벤치마크
python src/04_competitor_benchmark.py

# 6. 차트 생성
python src/05_make_charts.py
```

실행 후 확인할 파일:

```bash
ls outputs
```

정상 결과:

```text
classified_inquiries.csv
operational_kpi_summary.csv
competitor_benchmark.csv
chart_inquiry_types.png
chart_kpi_scores.png
chart_competitor_scores.png
```

---

## 14. 결과 해석 방법

### 14.1 문의 유형 분포 해석

`outputs/classified_inquiries.csv`와 `outputs/chart_inquiry_types.png`를 확인한다.

예상 해석 예시:

> 고객지원 데이터셋에서는 FAQ, 업무 처리, 결제/청구, 장애/오류성 문의가 반복적으로 나타났다. 이는 AICC 도입 시 단순 반복 문의는 Global 시나리오로 자동화하고, 주문/예약/변경/취소처럼 절차가 필요한 문의는 Main 시나리오로 설계해야 함을 보여준다. 장애/오류와 불만성 문의는 상담원 연결 및 Auto QA 관리 대상으로 분류할 수 있다.

### 14.2 운영 KPI 해석

`outputs/operational_kpi_summary.csv`를 확인한다.

해석 구조:

1. 자동화 적합도가 높으면:
   - 음성봇/챗봇 도입 우선순위가 높다.
   - FAQ/반복 문의 자동화 효과를 기대할 수 있다.

2. Main 시나리오 필요도가 높으면:
   - 단순 FAQ보다 업무 처리 프로세스 설계가 중요하다.
   - 고객 정보 수집, 유효성 검증, API 연동, 최종 확인 절차가 필요하다.

3. Global 시나리오 필요도가 높으면:
   - 상담원 연결, 통화 종료, 영업시간 안내 등 공통 요청 처리가 중요하다.

4. Repair 시나리오 필요도가 높으면:
   - 무응답, 불명확 발화, 재질문 흐름을 설계해야 한다.

5. Auto QA 필요도가 높으면:
   - 상담 품질 평가와 클레임/장애 키워드 모니터링이 중요하다.

### 14.3 경쟁사 벤치마크 해석

`outputs/competitor_benchmark.csv`와 `outputs/chart_competitor_scores.png`를 확인한다.

주의: 이 점수는 실제 시장점유율이 아니다.  
공개자료에 나타난 지표의 풍부함과 운영 관점의 비교 점수다.

해석 문장 예시:

> 공개자료 기준으로 KT는 수주액, 금융권 구축 실적, 고객사 수, 월 콜 처리량 등 시장성 지표가 강하게 나타났다. LGU+는 AICC 매출 목표, 상담 어드바이저, Auto QA 등 기능 고도화와 수익화 지표가 뚜렷했다. NAVER는 CLOVA HappyCall의 금융권 자동화 성과가 확인되지만, 최근 수주액, 고객사 수, 매출 목표, Auto QA 등 외부 공개 운영 지표는 경쟁사 대비 상대적으로 적게 확인되었다. 따라서 고객사별 도입 효과와 운영 KPI를 구조화한 케이스 스터디를 강화하면 시장 커뮤니케이션 측면에서 보완 효과가 있을 것으로 판단했다.

---

## 15. 운영 개선안 도출

최종 포트폴리오에서 아래 개선안을 제시한다.

### 개선안 1. 도입 문의 양식 기반 AICC 도입 적합도 점수화

문의 양식의 항목을 아래 지표로 변환한다.

| 문의 항목 | 운영 지표 |
|---|---|
| 신규 도입 / 재구축 / 고도화 | 도입 성숙도 |
| 자체 운영 / 아웃소싱 | 운영 전환 난이도 |
| 상담사 수 | 운영 규모 |
| 평균 콜 수 | 예상 처리량 |
| 기존 솔루션 | 마이그레이션 난이도 |
| 희망 기능 | 기능 수요 |
| 상세 문의 내용 | Pain point / 이슈 유형 |

### 개선안 2. 고객 문의 유형별 운영 워크플로우 표준화

| 문의 유형 | 운영 액션 |
|---|---|
| FAQ | Global 시나리오 자동화 |
| 업무 처리 | Main 시나리오 설계 |
| 불명확 발화 | Repair 시나리오 개선 |
| 장애/오류 | 상담원 연결 + 기술지원 라우팅 |
| 불만/클레임 | Auto QA + 관리자 리뷰 |
| 상담원 연결 | Human handoff 정책 수립 |

### 개선안 3. 고객사별 운영 KPI 리포트 템플릿

리포트에 포함할 항목:

- 통화 건 수
- 통화 시간
- 서비스 이용 시간
- 채널 수
- Agent별 통화 건 수
- Agent별 통화 시간
- 상담원 연결 비율
- FAQ 자동화 비율
- 장애/오류 문의 비율
- 불만/클레임 키워드
- 캠페인 진행 현황
- Auto QA 필요 상담 비율

### 개선안 4. 경쟁사 동향 모니터링 템플릿

월 1회 아래 항목을 모니터링한다.

| 항목 | 예시 |
|---|---|
| 신규 수주 | KT NH농협은행 400억 규모 사업 |
| 매출 목표 | LGU+ AICC 350억 목표 |
| 고객사 수 | LGU+ 70여 개 고객사, KT 300개 이상 고객사 |
| 기능 출시 | Auto QA, 상담 어드바이저, 상담 요약 |
| 산업별 레퍼런스 | 금융, 보험, 공공, 리테일 |
| 품질관리 기능 | QA, 피드백, 전수평가, 상담요약 |

---

## 16. 포트폴리오 PDF 구성

최종 첨부용 PDF는 4페이지가 적당하다.

### 1페이지: 프로젝트 개요

제목:

> CLOVA AiCall 도입 문의·운영 KPI 기반 AICC 운영 인사이트 분석

내용:

- 목적
- 분석 범위
- 사용 데이터
- 분석 방법

넣을 문장:

> NAVER Cloud AI Solution 운영 지원/관리 직무를 준비하며, AICC 상품의 고객 문의 유형, 도입 문의 정보, 운영 KPI, 경쟁사 공개 지표를 연결해 운영 개선 인사이트를 도출했다.

### 2페이지: 데이터 수집 및 분석 방법

포함 내용:

- Hugging Face 고객지원 데이터셋 사용
- NAVER CLOVA AiCall 공식 가이드 기반 운영 구조 분석
- 경쟁사 공개자료 수집
- 합성 도입 문의 데이터 사용 시 명확히 표시

시각화:

- 데이터 흐름도

```text
공개 고객지원 데이터
→ 문의 유형 분류
→ AiCall Main/Global/Repair 구조 연결
→ 운영 KPI 산출
→ 경쟁사 지표 비교
→ 개선안 도출
```

### 3페이지: 분석 결과

포함 내용:

- 문의 유형 분포 차트
- 운영 KPI 점수표
- 경쟁사 벤치마크 표

핵심 문장:

> 고객 문의 유형은 FAQ·업무 처리·장애/오류·상담원 연결·불만/클레임으로 구분할 수 있었고, 이를 AiCall의 Main/Global/Repair 시나리오와 연결해 자동화 적합도, 상담원 연결 필요도, Auto QA 필요도를 정의했다.

### 4페이지: 운영 개선 제안

포함 내용:

1. 도입 문의 양식 기반 도입 적합도 점수화
2. 고객 문의 유형별 운영 워크플로우 표준화
3. 고객사별 운영 KPI 리포트 템플릿
4. 경쟁사 동향 모니터링 정기화
5. NAVER AiCall 공개 사례의 KPI 강화 제안

핵심 문장:

> NAVER는 금융권 해피콜 자동화 성과를 보유하고 있으나, 경쟁사 대비 최근 수주액·고객사 수·매출 목표·Auto QA 등 공개 운영 지표는 상대적으로 적게 확인된다. 따라서 고객사별 도입 효과를 자동화율, 대기시간 감소, 상담 처리율, 품질 평가 결과로 구조화한 케이스 스터디와 운영 리포트 체계를 강화할 필요가 있다.

---

## 17. README.md 초안

아래 내용을 `README.md`에 넣는다.

```markdown
# CLOVA AiCall 도입 문의·운영 KPI 기반 AICC 운영 인사이트 분석

## 1. 프로젝트 개요

본 프로젝트는 NAVER Cloud AI Solution 운영 지원/관리 직무를 준비하며 진행한 AICC 운영 분석 프로젝트입니다.  
CLOVA AiCall의 도입 문의 양식과 공식 가이드, 공개 고객지원 데이터셋, 경쟁사 공개자료를 바탕으로 고객 문의 유형을 운영 KPI로 전환하고, 경쟁사 대비 개선 가능한 운영 인사이트를 도출했습니다.

## 2. 분석 배경

AI PaaS 상품 운영은 단순 기능 이해보다 고객 문의, CS 현황, 주요 이슈, 경쟁사 동향, 품질관리 지표를 구조화하는 역량이 중요하다고 판단했습니다.  
CLOVA AiCall은 Contact Center, Agent, Channel, Scenario, Dashboard 구조를 갖고 있어 운영 KPI 분석에 적합한 상품이라고 보았습니다.

## 3. 사용 데이터

- Hugging Face Bitext Customer Support Dataset
- NAVER CLOVA AiCall 공식 가이드
- NAVER CLOVA AiCall 도입 문의 양식
- KT, LGU+, SKT/SK AX AICC 공개 기사 및 공식 자료
- 합성 도입 문의 데이터: 실제 고객사 데이터가 아닌, 문의 양식 구조 기반 시뮬레이션 데이터

## 4. 분석 방법

1. 고객지원 데이터셋 수집
2. 문의 유형 분류
3. AiCall Main / Global / Repair 시나리오와 연결
4. 운영 KPI 산출
5. 경쟁사 공개 지표 비교
6. 운영 개선안 도출

## 5. 주요 결과

- FAQ와 반복 업무 문의는 Global/Main 시나리오 자동화 대상으로 분류 가능
- 장애/오류, 불만/클레임, 상담원 연결 요청은 Auto QA 및 Human Handoff 관리 대상으로 분류 가능
- KT와 LGU+는 수주액, 고객사 수, 매출 목표 등 시장성 지표를 적극 공개
- NAVER AiCall은 금융권 해피콜 자동화 성과가 있으나, 최근 시장 확장 지표와 품질관리 지표 공개는 보완 여지가 있음

## 6. 개선 제안

- 도입 문의 양식 기반 AICC 도입 적합도 점수화
- 고객 문의 유형별 운영 워크플로우 표준화
- 고객사별 운영 KPI 리포트 템플릿 설계
- 경쟁사 동향 모니터링 항목 정례화
- Auto QA, 상담 어시스턴트, 상담 요약 기능 수요 추적
```

---

## 18. 자기소개서 2번 문항 초안

문항:

> 지원 직무와 관련된 자신의 대표적인 프로젝트 한 가지를 적어 주시되, 어떠한 고민을 가지고 어떻게 결과물을 만들어 냈는지, 기여도는 어떠했는지 구체적으로 설명해 주세요.  
> 최대 1,000자

초안:

```text
NAVER Cloud AI Solution 운영 지원/관리 직무를 준비하며, CLOVA AiCall을 중심으로 AICC 도입 문의·운영 KPI 분석 프로젝트를 진행했습니다. AI PaaS 상품 운영은 단순 기능 이해보다 고객 문의와 CS 현황을 어떻게 지표화하고, 경쟁사 동향과 품질관리 개선안으로 연결하는지가 중요하다고 보았습니다.

먼저 CLOVA AiCall의 도입 문의 양식과 공식 가이드를 분석했습니다. 문의 양식에서 상담사 수, 평균 콜 수, 기존 솔루션, 희망 기능을 요구한다는 점을 확인했고, 이는 고객사의 운영 규모와 도입 성숙도, 기능 수요를 사전에 진단하기 위한 정보라고 판단했습니다. 또한 AiCall 가이드에서 Contact Center, Agent, Channel 구조와 통화 건 수, 통화 시간, 서비스 이용 시간, 채널 수, Main/Global/Repair 시나리오 구조를 확인했습니다.

이후 Hugging Face 공개 고객지원 데이터셋을 활용해 문의 유형을 FAQ, 업무 처리, 장애/오류, 상담원 연결, 불만/클레임 등으로 분류하고, Python으로 자동화 적합도, 상담원 연결 필요도, Auto QA 필요도, 시나리오 복잡도를 점수화했습니다. 또한 KT, LG유플러스, SKT/SK AX의 AICC 공개자료를 수집해 수주액, 고객사 수, 매출 목표, 기능 고도화 지표를 비교했습니다.

분석 결과 NAVER는 금융권 해피콜 자동화 성과가 확인되지만, 경쟁사 대비 최근 수주액·고객사 수·Auto QA 등 공개 운영 지표는 상대적으로 보완 여지가 있다고 판단했습니다. 이를 바탕으로 도입 문의 양식 기반 적합도 점수화, 고객 문의 유형별 운영 워크플로우, 고객사별 운영 KPI 리포트 템플릿을 제안했습니다. 데이터 수집 기준 정의, 지표 설계, Python 분석, 결과 해석과 문서화까지 전 과정을 직접 수행했습니다.
```

---

## 19. 프로젝트 완료 체크리스트

### 필수

- [ ] 프로젝트 폴더 생성
- [ ] Python 가상환경 생성
- [ ] requirements 설치
- [ ] Hugging Face 데이터셋 로드 완료
- [ ] `hf_customer_support_sample.csv` 생성
- [ ] 문의 유형 분류 완료
- [ ] `classified_inquiries.csv` 생성
- [ ] 운영 KPI 산출 완료
- [ ] `operational_kpi_summary.csv` 생성
- [ ] 경쟁사 자료 CSV 작성
- [ ] `competitor_benchmark.csv` 생성
- [ ] 차트 3개 생성
- [ ] README 작성
- [ ] 포트폴리오 PDF 4페이지 작성
- [ ] 자기소개서 2번 문항에 반영

### 선택

- [ ] Hugging Face zero-shot 모델로 분류 보조
- [ ] AI Hub 한국어 상담 데이터 추가
- [ ] 합성 도입 문의 데이터로 도입 적합도 점수화
- [ ] Notion 또는 Google Slides로 PDF 제작

---

## 20. 시간이 부족할 때 최소 완성 버전

시간이 부족하면 아래만 한다.

1. Bitext 데이터셋 로드
2. 룰 기반 문의 유형 분류
3. 운영 KPI 표 생성
4. 경쟁사 자료 CSV 6줄 작성
5. 차트 2개 생성
6. PDF 4페이지 작성

이 정도면 제출 가능하다.

---

## 21. 절대 하지 말 것

- eKYC까지 깊게 파지 말 것
- 클로바노트 테스트로 방향 전환하지 말 것
- 모든 CLOVA 제품을 다 비교하지 말 것
- 무거운 ML 모델 학습하지 말 것
- 합성 데이터를 실제 데이터처럼 표현하지 말 것
- Python 구현 자체를 프로젝트의 핵심으로 말하지 말 것
- 점수를 실제 시장점유율이나 실제 성과처럼 말하지 말 것
- 출처 없는 추측을 결론처럼 쓰지 말 것

---

## 22. 최종 메시지

이 프로젝트의 핵심은 “개발을 했다”가 아니다.

**AI PaaS 상품 운영자가 고객 문의, 운영 현황, 경쟁사 자료, 품질관리 지표를 어떻게 구조화해 운영 개선 인사이트로 바꿀 수 있는지 보여주는 것**이다.

따라서 모든 결과물의 주어는 Python이나 모델이 아니라 아래여야 한다.

- 고객 문의 유형
- CS 운영 현황
- 운영 KPI
- 경쟁사 공개 지표
- 품질관리 포인트
- 개선안
- 문서화

이 방향으로 끝까지 밀고 가면 된다.
