# pip install groq
# pip install python-dotenv 
from groq import Groq
from dotenv import load_dotenv  # .env 읽는 도구
import os

# 1. .env의 GROQ_API_KEY 키를 환경변수로 불러옴
load_dotenv()

# 2. 키로 Groq 클라이언트 만들기 (키를 통해서 요청)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. 질문 보내기
res = client.chat.completions.create(
    model="openai/gpt-oss-20b", # 무료, 빠름
    messages=[
        {
            "role": "user", # 질문이나 요청할 때
            "content": "groq가 뭐임?"   # 질문
        }
    ]
)

# 4. 답변 받기
result = res.choices[0].message.content
print(result)

# **Groq(그록)란?**

# | 항목 | 내용 |
# |------|------|
# | **정의** | “Graph-Relational Object Queries”의 줄임말로, JSON‑형태의 문서들을 효율적으로 조회하기 위해 Sanity.io가 만든 질의 언어입니다. |
# | **사용처** | 주로 **Sanity Headless CMS**에서 콘텐츠를 검색하거나, **Sanity.io를 사용한 웹/앱**에서 데이터를 가져올 때 사용됩니다. (Sanity 이외에도 일부 프로젝트에서 독립적으로 사용되는 경우가 있지만, 가장 흔한 활용처는 Sanity입니다.) |
# | **특징** | - **JSON 문서**를 그대로 다루며, 중첩 객체·배열에 대한 깊은 접근이 가능<br>- **필터, 정렬, 집계** 등 SQL 같은 기능이 있지만, 문서 구조에 맞게 설계<br>- **단순한 문법**: `*`(wildcard), `.`(dot), `[]`(배열 인덱스/조건), `->`(프로젝션) 등 사용<br>- **함수**: `date()`, `count()`, `sum()`, `min()`, `max()` 등 내장 함수 활용 가능 |

# ---

# ## 1. Groq가 왜 필요한가?

# 전통적인 **REST API**는 데이터를 요청할 때 필요한 필드를 한 번에 결정하기가 어렵습니다. 반면 **GraphQL**은 필요한 필드를 선택할 수 있지만, 복잡한 관계형 데이터를 탐색할 때 문법이 복잡해질 수 있습니다.Groq는 JSON 문서 구조에 최적화된 경량화된 질의 언어로, Sanity의 스키마 기반 데이터베이스에서 빠르고 직관적으로 데이터를 가져옵니다.

# ---

# ## 2. 기본 문법 예시

# ```groq
# // 1. 모든 블로그 포스트 가져오기
# *[_type == "post"]

# // 2. 제목(title)과 작성자(author)만 가져오기
# *[_type == "post"]{
#   title,
#   "authorName": author->name
# }

# // 3. 최신 5개 포스트
# *[_type == "post"] | order(publishedAt desc)[0...5]

# // 4. 특정 카테고리(category)를 가진 포스트
# *[_type == "post" && "tech" in categories[]->slug.current]

# // 5. 게시물마다 댓글 개수
# *[_type == "post"]{
#   title,
#   "commentCount": *[_type == "comment" && parentRef == ^._id].count()
# }
# ```

# - `*[_type == "post"]` : 모든 `post` 타입 문서 선택
# - `| order(publishedAt desc)` : 정렬
# - `[0...5]` : 슬라이스 (첫 5개)
# - `author->name` : `author` 레퍼런스를 따라가서 `name` 필드 가져오기
# - `... in categories[]->slug.current` : `categories` 배열에서 `slug.current` 값이 `"tech"`인 항목 필터링
# - `*[_type == "comment" && parentRef == ^._id]` : 현재 문서(`^`)의 `_id`와 일치하는 댓글 찾기

# ---

# ## 3. Groq vs GraphQL

# | 점 | Groq | GraphQL |
# |----|------|--------|
# | **데이터 형식** | JSON 그대로 | JSON‑형식 |
# | **문법 복잡도** | 직관적·간단 | 스키마 정의 필요·복잡할 수 있음 |
# | **프로젝션(필드 선택)** | `{ title, "authorName": author->name }` | `query { title author { name } }` |
# | **배열 필터** | `*[...].title` | `items(where: {title_contains: "foo"})` |
# | **집계** | `*[_type=="post"].count()` | 외부 스칼라 함수 필요 |
# | **사용처** | Sanity CMS (주로) | 거의 모든 API |

# ---

# ## 4. Sanity 프로젝트에서 Groq 사용하기

# 1. **Sanity 프로젝트 생성**  
#    ```bash
#    sanity init
#    ```

# 2. **스키마 정의**  
#    ```js
#    // schemas/post.js
#    export default {
#      name: 'post',
#      type: 'document',
#      fields: [
#        {name: 'title', type: 'string'},
#        {name: 'author', type: 'reference', to: [{type: 'author'}]},
#        {name: 'publishedAt', type: 'datetime'},
#        // …
#      ]
#    }
#    ```

# 3. **클라이언트에서 질의 실행**  
#    ```js
#    import sanityClient from '@sanity/client';

#    const client = sanityClient({
#      projectId: 'yourProjectId',
#      dataset: 'production',
#      useCdn: true
#    });

#    const posts = await client.fetch(`*[_type == "post"][0...10]{title, "authorName": author->name}`);
#    console.log(posts);
#    ```

# 4. **프론트엔드 프레임워크**(React, Next.js 등)와 함께 사용하면 페이지를 동적으로 렌더링할 수 있습니다.

# ---

# ## 5. Groq를 배우는 팁

# - **문서 구조 먼저 파악**: Sanity에서 정의한 스키마를 먼저 이해해 두면 질의를 쉽게 작성할 수 있습니다.
# - **간단한 질의부터 시도**: `*[_type == "post"]`처럼 전체를 가져와서, 점진적으로 필드 선택과 필터를 추가해보세요.
# - **콘솔에서 실험**: Sanity Studio의 **Inspect** 탭에서 바로 Groq를 입력해볼 수 있어 실시간 결과를 확인할 수 있습니다.
# - **공식 문서**: [Groq 공식 가이드](https://www.sanity.io/docs/groq)에서 예제와 함수 목록을 참고하세요.

# ---

# ### 정리

# - **Groq**는 **Sanity.io**와 같은 JSON‑기반 CMS에서 데이터를 조회하기 위한 경량 질의 언어입니다.
# - 직관적 문법과 JSON 친화성 덕분에 **복잡한 관계형 데이터를 쉽게 조회**할 수 있습니다.
# - GraphQL과 비교해 **설정이 적고 사용이 간단**하지만, 주로 Sanity 생태계에서 활용됩니다.

# 궁금한 부분이 있으면 언제든지 물어보세요! 🚀