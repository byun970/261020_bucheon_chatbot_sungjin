from dotenv import load_dotenv
import os
from groq import Groq
from termcolor import colored

# 1. 환경 변수 불러오기
load_dotenv()

# 2. API 클라이언트 만들기
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. 대화 기록 맨 앞에 AI 성격 지정 (할일 관리 비서)
messages = [
    {
        "role": "system",
        "content": "너는 사용자의 할일(todo)을 관리해주는 친절한 비서야. "
                    "할일 추가/목록/완료/삭제는 명령어로 처리되니, "
                    "그 외의 일반적인 대화나 조언 요청에만 짧고 친절하게 답해줘."
    }
]

# 4. 할일 목록 (번호: 내용, 완료 여부)
todos = []


# 5. 할일 목록 출력 함수
def print_todos():
    if not todos:
        print(colored("할일이 없습니다.", "yellow"))
        return
    for i, todo in enumerate(todos, start=1):
        check = "완료" if todo["완료"] else "진행중"
        color = "green" if todo["완료"] else "cyan"
        print(colored(f"{i}. [{check}] {todo['내용']}", color))


# 6. 명령어 사용법 출력 함수
def print_help():
    print(colored(
        "사용 가능한 명령어\n"
        "  추가 <할일 내용>  : 할일 추가\n"
        "  목록              : 할일 목록 보기\n"
        "  완료 <번호>        : 해당 번호 할일 완료 처리\n"
        "  삭제 <번호>        : 해당 번호 할일 삭제\n"
        "  exit              : 종료\n"
        "  (그 외 입력은 AI와 자유롭게 대화)",
        "magenta"
    ))


print_help()

# 7. 대화 및 명령어 처리 루프
while True:
    # 7-1. 입력 받기
    q = input("\n나 : ").strip()

    # 7-2. 종료
    if q == "exit":
        print("대화를 종료합니다.")
        break

    # 7-3. 할일 추가
    if q.startswith("추가"):
        content = q[len("추가"):].strip()
        if content:
            todos.append({"내용": content, "완료": False})
            print(colored(f"'{content}' 할일을 추가했습니다.", "green"))
        else:
            print(colored("추가할 내용을 입력해주세요. 예) 추가 숙제하기", "red"))
        continue

    # 7-4. 할일 목록 보기
    if q == "목록":
        print_todos()
        continue

    # 7-5. 할일 완료 처리
    if q.startswith("완료"):
        num = q[len("완료"):].strip()
        if num.isdigit() and 1 <= int(num) <= len(todos):
            todos[int(num) - 1]["완료"] = True
            print(colored(f"{num}번 할일을 완료 처리했습니다.", "green"))
        else:
            print(colored("완료할 할일 번호가 올바르지 않습니다. 예) 완료 1", "red"))
        continue

    # 7-6. 할일 삭제
    if q.startswith("삭제"):
        num = q[len("삭제"):].strip()
        if num.isdigit() and 1 <= int(num) <= len(todos):
            removed = todos.pop(int(num) - 1)
            print(colored(f"'{removed['내용']}' 할일을 삭제했습니다.", "green"))
        else:
            print(colored("삭제할 할일 번호가 올바르지 않습니다. 예) 삭제 1", "red"))
        continue

    # 7-7. 그 외 입력은 AI와 대화
    messages.append({
        "role": "user",
        "content": q
    })

    res = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.3,
        max_completion_tokens=300,
        reasoning_effort="low"
    )

    answer = res.choices[0].message.content
    print(colored(f"AI 비서 : {answer}", "blue"))

    messages.append({
        "role": "assistant",
        "content": answer
    })
