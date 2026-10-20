from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify, send_from_directory
from groq import Groq

# 1. 환경 변수 불러오기
load_dotenv()

# 2. API 클라이언트 만들기
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. AI 성격(시스템 프롬프트) 지정
SYSTEM_PROMPT = {
    "role": "system",
    "content": "너는 아주 개발을 잘하는 개발자야"
}

app = Flask(__name__, static_folder=".", static_url_path="")


# 4. 메인 페이지(index.html) 제공
@app.route("/")
def index():
    return send_from_directory(".", "index.html")


# 5. 챗봇 API
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    history = data.get("history", [])  # [{role, content}, ...] (이전 대화 기록)
    question = (data.get("message") or "").strip()

    if not question:
        return jsonify({"error": "메시지를 입력해주세요."}), 400

    messages = [SYSTEM_PROMPT] + history + [{"role": "user", "content": question}]

    res = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.1,
        max_completion_tokens=300,
        reasoning_effort="low"
    )

    answer = res.choices[0].message.content
    return jsonify({"reply": answer})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
