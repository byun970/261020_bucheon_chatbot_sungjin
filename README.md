# 261020_bucheon_chatbot_sungjin

Groq API를 활용한 콘솔 챗봇 실습 프로젝트입니다. 기본 호출부터 페르소나 적용, 할일(todo) 관리 챗봇까지 단계별로 구성되어 있습니다.

## 파일 구성

| 파일 | 설명 |
|---|---|
| `v07_01_basic_call.py` | Groq API에 질문 1건을 보내고 답변을 받는 가장 기본적인 예제 |
| `v07_02_basic_call.py` | `input()`으로 질문을 직접 입력받아 Groq API에 보내는 예제 |
| `v07_03_chatbot.py` | 대화 기록(`messages`)을 쌓아가며 대화를 이어가는 기본 챗봇 |
| `v07_04_chatbot_persona.py` | 시스템 프롬프트로 AI 페르소나를 지정하고, 답변 길이/일관성 옵션을 조절하는 챗봇 |
| `v07_05_chatbot_todo.py` | 할일 추가/완료/삭제/목록 조회 명령어와 AI 대화를 함께 제공하는 할일 관리 챗봇 |

## 사전 준비

1. Python 3.9 이상 (개발 환경: Python 3.11)
2. [Groq](https://console.groq.com/) 계정 및 API 키

## 설치 방법

```bash
# 1. 저장소 클론
git clone https://github.com/byun970/261020_bucheon_chatbot_sungjin.git
cd 261020_bucheon_chatbot_sungjin

# 2. (권장) 가상환경 생성 및 활성화
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # macOS/Linux

# 3. 필요 라이브러리 설치
pip install -r requirements.txt
```

## 환경 변수 설정 (.env)

프로젝트 루트에 `.env` 파일을 만들고 아래와 같이 API 키를 작성합니다. `.env`는 `.gitignore`에 등록되어 있어 깃허브에 올라가지 않습니다.

```env
GROQ_API_KEY=여기에_본인의_groq_api_key_입력
```

> Groq API 키가 소진되었다면 [Gemini API](https://ai.google.dev/) 키로 대체해 사용할 수 있습니다. (Gemini 사용 시 `google-generativeai` 라이브러리와 모델 호출 코드로 교체 필요)

## 실행 방법

```bash
python v07_05_chatbot_todo.py
```

## 할일 관리 챗봇 사용법 (`v07_05_chatbot_todo.py`)

실행 후 아래 명령어를 입력해서 사용합니다.

| 명령어 | 설명 | 예시 |
|---|---|---|
| `추가 <내용>` | 할일을 추가합니다 | `추가 보처너 과제 제출` |
| `목록` | 전체 할일 목록을 보여줍니다 | `목록` |
| `완료 <번호>` | 해당 번호의 할일을 완료 처리합니다 | `완료 1` |
| `삭제 <번호>` | 해당 번호의 할일을 삭제합니다 | `삭제 2` |
| `exit` | 프로그램을 종료합니다 | `exit` |
| 그 외 입력 | 명령어가 아니면 AI와 자유롭게 대화합니다 | `오늘 기분이 어때?` |

## 주의사항

- `.env`, `groq_api_key.txt` 파일은 절대 깃허브에 커밋/푸시하지 않습니다. (`.gitignore`에 이미 등록됨)
- API 키는 타인에게 공유하지 않습니다.
