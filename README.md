# 261020_bucheon_chatbot_sungjin

Groq API를 활용한 챗봇 실습 프로젝트입니다. 콘솔 기본 예제와, Flask + HTML로 만든 웹 챗봇으로 구성되어 있습니다.

## 파일 구성

| 파일 | 설명 |
|---|---|
| `261020_bucheon_chatbot_sungjin.py` | 콘솔에서 `input()`으로 질문을 입력받아 대화 기록을 쌓아가며 답하는 기본 챗봇 |
| `app.py` | Flask 서버. `index.html`을 제공하고, `/api/chat` API로 Groq에 질문을 전달 |
| `index.html` | 웹 챗봇 화면 (말풍선 UI, 대화 기록 유지, 입력 중 표시 등) |

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

### 1) 웹 챗봇 (추천)

```bash
python app.py
```

실행 후 브라우저에서 `http://localhost:5000` 접속하면 채팅창이 나타납니다.

### 2) 콘솔 챗봇

```bash
python 261020_bucheon_chatbot_sungjin.py
```

`나의 질문 :` 프롬프트에 질문을 입력하면 답변을 받을 수 있고, `exit`를 입력하면 종료됩니다.

## 주의사항

- `.env`, `groq_api_key.txt` 파일은 절대 깃허브에 커밋/푸시하지 않습니다. (`.gitignore`에 이미 등록됨)
- API 키는 타인에게 공유하지 않습니다.

- 코드 실행법 : .venv\Scripts\python.exe app.py
- http://127.0.0.1:5000/ 접속