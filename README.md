# [School Talks] DRF를 활용한 입시정보 커뮤니티 서비스

![logo](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/5fe3d797-5b4d-42e3-bca7-49baef1ffeaf)

## 1. 목표와 기능

### 1.1 목표

-   고등학생들의 입시정보 및 생활정보 공유 서비스
-   대입에 대한 입시정보를 찾고, 일상생활을 공유하며 공감대를 형성하는 서비스
-   공부하다 지친 학생들이 편히 찾을 수 있는 커뮤니티

### 1.2 기능

-   기본 기능

    -   회원가입, 로그인, 프로필 기능
    -   커뮤니티 게시판 기능(입시게시판, 자유게시판 2개)
    -   AI 티칭 기능


-   선택 기능
    -   실시간 채팅 기능
    -   문의 기능

### 1.3 팀 구성

-   실제 사진을 업로드 하시길 권합니다.
<table>
    <tr>
        <th>김정원</th>
        <th>김동후</th>
        <th>김찬양</th>
        <th>황진경</th>
        <th>김창수</th>
    </tr>
    <tr>
        <td><img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/fe51e6d1-e413-450e-9187-6ee80eaa1546" width="100%"></td>
        <td><img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/d2fd4777-ff32-4187-b31c-162463a1745f" width="100%"></td>
        <td><img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/176a30ad-043b-4e61-a120-d46a1e213cf3" width="90%"></td>
	<td><img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/75780140/d6ca16e7-71d7-43ef-91b0-ac2768fc6eb6" width="100%"></td>
        <td><img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/4e1dc27b-ae91-4a2e-bdca-d17a1e74566a" width="100%"></td>
    </tr>
    <tr>
	<td>
            - Study, Qna, Chat BE & FE<br>
            - Accounts FE 연결<br>
            - 전체 프론트 효율 개선<br>
	    - 문서작업 	
        </td>
        <td>
            - AIchat 메인 담당 BE & FE<br>
	    - 문서작업	
        </td>
        <td>
            - Post 메인 담당 BE & FE<br>
            - 전체 프론트 코드 효율 개선<br>
	    - 문서작업
        </td>
        <td>
	    - Chat, AIChat 서브: 구현방법조사 및 FE수정<br>
	    - 문서작업
        </td>
        <td>
            - Accounts 메인 담당 BE<br>
	    - 문서작업
	</td>
    </tr>
</table>

## 2. 요구사항 명세와 기능 명세

<img width="665" alt="스크린샷 2023-12-25 오후 6 08 58" src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/abb1bd04-bec3-49bb-8fb3-5ca2ad9270d5">

-   기본 요구사항

    -   회원 관련 기능
    -   기능 최소 3가지 이상 구현 (회원 기능 포함)

-   선택 사항

    -   UI 추가

-   필수 결과물

    -   데이터베이스 구조(ERD)
    -   API 명세서(마크업, 노션, swagger… 등)
    -   발표 자료

-   평가 지표
    -   기술성: 모놀리식, 마이크로식, FBV와 CBV의 적절한 사용 등 Django의 적절한 사용
    -   DB설계: 데이터베이스 설계, DB 복잡도, 적절성(예를 들어 1개 모델에 1개 필드만 수십개 X)
    -   배포: nginx, gunicorn, django 등 연계하여 배포
    -   설계와 구현: 설계와 구현 복잡도(요구사항 작성, 와이어프레임, 기간 내 설계한 것들이 모두 구현이 되어 있는지 등)

## 3. 개발 환경 및 배포 URL

### 3.1 개발 환경

-   FE:

    ![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
    ![CSS3](https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
    ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)

-   BE:

    ![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
    ![Django](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=django&logoColor=white)

-   Deployment:

    [![GitHub](https://img.shields.io/badge/GitHub-100000.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
    [![AWS Lightsail](https://img.shields.io/badge/AWS-Lightsail-FF9900.svg?style=for-the-badge&logo=amazon-aws)](https://aws.amazon.com/lightsail/)
    [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420.svg?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
    [![Gunicorn](https://img.shields.io/badge/Gunicorn-green.svg?style=for-the-badge&logo=gunicorn)](https://gunicorn.org/)
    [![Nginx](https://img.shields.io/badge/Nginx-blue.svg?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)
    [![DB SQLite](https://img.shields.io/badge/DB-SQLite-003B57.svg?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/)
    ![Netlify](https://img.shields.io/badge/Netlify-00C7B7.svg?style=for-the-badge&logo=netlify&logoColor=white)

### 3.2 배포 URL

-   BE : https://schooltalks.maxworld7070.net/
-   FE : https://schooltalks77.netlify.app/

### 3.3 CI/CD 구축 배포

-   BE Github Action 자동 배포
    <img width="1195" alt="스크린샷 2023-12-25 오후 6 23 26" src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/31dbf6c9-b795-42a8-b4d3-e75dc1d1dd6d">
-   FE Netlify 자동 배포
    <img width="1048" alt="스크린샷 2023-12-22 오후 11 18 21" src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/50db0517-7d74-4fcc-a21a-e9993337a6df">

## 4. URL 설계 & API 명세 및 사용 외부라이브러리

### 4.1 URL 설계 & API 명세

-   스웨거 문서(API 명세) : API 기능과 사용 방법을 명확히 전달 하기 위한 Swegger drf-yasg 사용하여 문서화

🖌 https://schooltalks.maxworld7070.net/schema/swagger-ui/

| 엔드포인트                    | HTTP 메서드             | 기능                                               | 앱             | 비고 |
| ----------------------------- | ----------------------- | -------------------------------------------------- | -------------- | ---- |
| /accounts/signup/             | POST                    | 새로운 User를 만들어주는 역할 (회원가입)           | Accounts       |      |
| /accounts/token/              | POST                    | 인증 토큰 생성 (로그인)                            | Authentication |      |
| /accounts/token/refresh/      | POST                    | 토큰 갱신                                          | Authentication |      |
| /accounts/token/verify/       | POST                    | 토큰 유효성 검사                                   | Authentication |      |
| /accounts/user/               | GET                     | 특정 사용자의 프로필 조회 (프로필 보기)            | User Profile   |      |
| /aichat/                      | GET, POST, DELETE       | AI와 채팅 (채팅 보기, 채팅 보내기, 전체 채팅 삭제) | AI Chat        |      |
| /chat/api/chat-messages/      | GET, POST               | 채팅 메시지 조회 및 생성                           | Chat           |      |
| /post/                        | GET, POST               | 글 목록 조회 및 글 작성                            | Posts          |      |
| /post/{id}/                   | GET, PUT, PATCH, DELETE | 특정 글 조회, 수정, 삭제                           | Posts          |      |
| /post/{post_id}/comment/{id}/ | DELETE, PUT, PATCH      | 특정 댓글 삭제, 수정                               | Comments       |      |
| /qna/inquiry/                 | GET, POST               | 문의 사항 조회 및 생성                             | QnA            |      |
| /qna/inquiry/{id}/            | GET, PUT, PATCH, DELETE | 특정 문의 사항 조회, 수정, 삭제                    | QnA            |      |
| /study/{id}/                  | GET, DELETE, PUT        | 특정 게시물 조회, 삭제, 수정                       | Study          |      |

### 4.2 사용 외부라이브러리

| 라이브러리                      | 버전    | 설명                                                                                            |
| ------------------------------- | ------- | ----------------------------------------------------------------------------------------------- |
| `djangorestframework`           | 3.14.0  | RESTful API 구축을 위한 강력한 툴킷을 Django에 제공                                             |
| `djangorestframework-simplejwt` | 5.3.1   | JWT 인증을 Django Rest Framework에 쉽게 통합할 수 있게 해주는 확장                              |
| `drf-spectacular`               | 0.26.5  | DRF 스키마 생성 및 문서화를 위한 확장으로, API 문서화 작업을 간소화                             |
| `channels[daphne]`              | ~4.0.0  | 비동기 웹소켓 처리 및 실시간 기능 구현의 지원을 위한 Django 확장으로, Daphne 서버를 포함        |
| `channels_redis`                | ~4.0.0  | Channels의 메시징 레이어에 대한 Redis 기반 백엔드 지원                                          |
| `redis`                         | !=4.4.0 | Redis 서버와의 통신을 위한 클라이언트 라이브러리, Channels의 백엔드로도 사용                    |
| `django-filter`                 | 23.5    | 강력한 필터링 기능을 제공하여, 동적으로 쿼리셋을 필터링, Django Rest Framework와 함께 많이 사용 |
| `python-dotenv`                 | 1.0.0   | `.env` 파일에서 환경 변수를 로드하여 Django 설정에 사용할 수 있게 해주는 도구                   |
| `openai`                        | 1.5.0   | OpenAI API를 사용하기 위한 공식 클라이언트 라이브러리, GPT-3 등의 AI 모델을 활용할 때 사용      |

## 5. 프로젝트 구조와 개발 일정

### 5.1 프로젝트 구조

```
# SCHOOLTALKS-BACKEND
├── 📁 .github
├── 📁 accounts
├── 📁 aichat
├── 📁 chat
├── 📁 media
├── 📁 post
├── 📁 project
├── 📁 qna
├── 📁 study
├── 📁 venv
├── 📄 .env
├── 📄 .gitignore
├── 📄 db.sqlite3
├── 📄 manage.py
├── 📘 README.md
└── 📄 requirements.txt

# SCHOOLTALKS-FRONTEND
├── 📁 .vscode
├── 📁 assets
│   ├── 📁 css
│   ├── 📁 fonts
│   ├── 📁 images
│   ├── 📁 js
│   └── 📁 mail
├── 📁 chat
├── 📁 gpt
├── 📁 post
├── 📁 study
├── 📄 header.html
├── 📄 index.html
├── 📄 license.txt
├── 📄 login.html
├── 📄 profile.html
├── 📄 qna.html
├── 📘 README.md
└── 📄 register.html

```

### 5.2 개발 일정(WBS)

![4545443](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/fd1869f3-60b9-457e-a813-e5c256d7f90d)

## 6. 데이터베이스 모델링(ERD)

![모델](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/95cf6f8a-b668-41a3-991f-27901be9983e)

-   학습 게시물 테이블:

    -   다대일 관계: 하나의 게시물은 여러 댓글(Study Comment)과 좋아요(Study Like)를 받을 수 있음.

-   일반 게시물 테이블

    -   다대일 관계: 하나의 게시물은 여러 댓글(Comment)과 좋아요(Like)를 받을 수 있음.

-   AI 대화 테이블(Conversation): AI 와의 대화 내용. 사용자의 입력(Prompt)와 AI의 답변(Response)를 저장.

-   채팅 테이블(Chat): 채팅방 정보 저장. 각 채팅방은 여러 사용자가 참여할 수 있음.

## 7. Architecture

![SchooltalksSystem drawio (1)](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/eb7111aa-c47a-4482-a789-4ac310aa2d9a)

-   프론트엔드: HTML, CSS, JavaScript, Bootstrap으로 구성되며, Netlify를 통해 배포
-   백엔드: Python과 Django를 사용하고, SQLite 데이터베이스, Gunicorn WSGI, Nginx 웹 서버와 함께 Ubuntu 시스템에 AWS Lightsail로 배포

## 8. 기술성
![슬라이드14](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/54328235-08bc-4392-90e7-9bce91f8af4a)

## 9. 와이어프레임 / UI / BM

### 9.1 와이어프레임
![슬라이드1](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/f38583cf-038a-4153-b228-aab783940390)

-  카카오 오븐을 통한 와이어프레임 제작
-  게시판, 챗, 로그인 등 메인 기능에 대한 개략적 프레임 작성
-  부트스트랩 활용 (출처 : GrayGrids)


### 9.2 화면 설계

-   Accounts 앱
<table>
    <tbody>
        <tr>
            <td>메인</td>
            <td>로그인</td>
        </tr>
        <tr>
            <td>
		<img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/b3007dc7-d276-40a5-89a7-0662bc3e2280" width="100%">
            </td>
            <td>
		<img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/bf097af1-0277-43bd-9425-ea781f4aeac0" width="100%">
            </td>
	</tr>
        <tr>
            <td>회원가입</td>
            <td>프로필</td>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/82467666-0739-4709-9395-e06a3d0bd13f" width="100%">
            </td>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/888c39fb-723a-42f6-a178-8cab78f7ee16" width="100%">
            </td>
        </tr>
        <tr>
	</tbody>
</table>


-   AI Chat 앱
<table>
    <tbody>
	<tr>
            <td>시작</td>
            <td>질문</td>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/142385973/0161ac0b-0329-4e59-81c9-326711efcf43" width="2000px">
            </td>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/b223d6ce-8bf9-4e02-ae3d-b5fd9aba59dc" width="2000px">
            </td>
        </tr>
    </tbody>
</table>

-   Post 앱
<table>
    <tbody>
        <tr>
            <td>자유게시판</td>
            <td>게시글 생성</td>
        </tr>
        <tr>
            <td>
                <img src="img/post/list.png" width="2000px">
            </td>
            <td>
                <img src="img/post/create.png" width="2000px">
            </td>
        </tr>
        <tr>
            <td>게시글 상세페이지</td>
            <td>게시글 수정</td>
        </tr>
        <tr>
            <td>
                <img src="img/post/read.png" width="2000px">
            </td>
            <td>
                <img src="img/post/update.png" width="2000px">
            </td>
        </tr>
	</tbody>
</table>

-   Study 앱
<table>
    <tbody>
        <tr>
            <td>입시 정보 게시판</td>
            <td>게시글 생성</td>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/1946aab9-6946-4271-bb0f-7228b4100ef4" width="95%">
            </td>
            <td>
	        <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/3f43d550-0e89-4ff7-b276-2e9b1f5e631b" width="100%">
            </td>
        </tr>
        <tr>
            <td>게시글 상세페이지</td>
            <td>게시글 수정</td>
        </tr>
        <tr>
            <td>
	        <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/6c217202-2cc9-4a67-a0ca-4f3cd61ab010" width="90%">
            </td>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/75887bd4-8cf9-45ba-bb64-47d431c3bd7e" width="100%">
            </td>
        </tr>
	</tbody>
</table>

-   Chat 앱

<table>
    <tbody>
	<tr>
            <td>익명실시간챗</td>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/75780140/27e35373-584b-40b9-88ef-399ffbfa8370" width="100%">
            </td>
        </tr>
    </tbody>
</table>


-   QNA 앱
<table>
    <tbody>
	<tr>
            <td>문의</td>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/142385973/0b8472a5-983e-47e0-93f0-7fe412a6e450" width="100%">
            </td>
        </tr>
    </tbody>
</table>

## 10. 메인 기능

📌 메인 페이지
![Main](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/75780140/482c3dfc-84a7-44f5-98b3-5d610137ce63)

- 서비스로 이동하는 아이콘이 반응할 수 있도록 함
- 사용자가 바로 이동할 수 있도록 네비게이션바와 배너를 생성

### accounts

📌 회원가입
<img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/142385973/a6d8f1f7-9e10-419b-bec5-3af6da6d155a" alt="회원가입" width="1000">

-   회원가입 성공시 성공 메시지 생성
-   로그인 버튼 클릭 후 로그인 화면으로 이동 가능

📌 로그인
<img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/142385973/2c542d9f-7a3b-4419-b7e5-d9eca7d23817" alt="회원가입" width="1000">

-   로그인 성공시 이전 페이지로 리다이렉트 됨
-   상단에 로그인 버튼이 사라지고 로그아웃 버튼이 생성됨

📌 로그아웃
<img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/142385973/17e25d06-f4f5-4dfe-9af4-9c77ff9efa62" alt="회원가입" width="1000">

-   로그아웃 성공시 로그아웃 버튼이 사라지고 로그인 버튼이 생성됨
-   다시 로그인 버튼을 클릭하여 로그인 하거나 회원가입을 할 수 있음

📌 프로필
<img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/142385973/dff99a62-c698-4d98-a06d-13608364a752" alt="회원가입" width="1000">

-   회원 가입시 입력 정보를 프로필로 불러옴
-   회원 가입시 이미지 정보도 불러 오기 가능
  

### AI 채팅 기능

📌 초기 화면
![초기 화면](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/1da60557-15fb-49da-8b87-6b58389c2d1d)

- AI 채팅을 시작할때, 이전 채팅 내역이 없다면 채팅 예시를 보여줌
  
📌 채팅
![채팅](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/ba2ac8c6-b593-4af3-8229-82e48f04a10e)

 - 질문을 입력하고 보내기 버튼을 누르면, AI의 말풍선이 생기고 잠시후 답변을 보여줌
  
📌 채팅 저장
![채팅 저장](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/856b280a-4602-4079-bbff-34d1e65fc643)

- 유저의 질문과 AI의 답변은 DB에 저장됨
- 다른 화면에서 AI 채팅방으로 다시 왔을때 이전 채팅 내역을 보여줌
  
📌 채팅 삭제
![채팅 삭제](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/b596081b-1ed7-4eef-9d79-87af28b1ac80)

- 삭제 버튼을 누르면 이전 채팅 내역이 모두 삭제되고 새로운 채팅을 시작함


### 자유게시판

📌 글 작성
![글 작성](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/f1d0247f-0120-4c43-b03a-8acf5dae85b9)


-   자유게시판에 새로운 글을 작성
-   제목과 내용으로 구성되어있으며, 따로 제한없이 자유롭게 글을 쓸 수 있음
-   로그인한 사용자만 작성 가능

📌 글 보기
![글 보기](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/6bc385a2-ece4-4251-bbbd-5b0292929465)


-   글 목록이 있음
-   글 제목을 클릭하면 상세보기로 들어가짐

📌 글 수정
![글 수정](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/06c59547-a8f7-4998-8011-e80ed43a26a9)


-   자유게시판 글을 수정함
-   기존에 작성햇던 내용이 미리 들어가있음
-   작성자만 수정 가능

📌 글 삭제
![글 삭제](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/6a395840-3545-4af6-9b6d-284a1c6c697a)


-   자유게시판 글을 삭제함
-   작성자만 삭제 가능

📌 글 검색
![글 검색](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/0d2372df-abf2-4ca6-9e54-06d8b52782e7)


-   제목, 내용, 제목+내용, 글쓴이 정보로 검색이 가능함

📌 좋아요
![글 좋아요](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/cc6158ac-979e-4e28-ba3f-3a811ff387a3)


-   회색일떄 좋아요을 클릭하면 빨갛게 활성화되고 카운트가 1 오름
-   빨간색일떄 좋아요를 클릭하면 회색으로 비활성화되고 카운트가 1 내려감
-   사용자마다 각기 다른 좋아요 정보가 있음


#### 자유게시판 댓글

📌 댓글 작성
![댓글 작성](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/b1799d8e-f967-4580-a382-752ce7645c2b)


-   로그인한 사용자는 글 상세보기에서 최하단에 댓글 작성이 있음
-   댓글내용을 적고 작성하면 등록됨

📌 댓글 수정
![댓글 수정](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/f711be8c-b7b1-4494-9bd9-513d446e266b)


-   댓글 내용을 수정함
-   기존 댓글 내용이 미리 들어가있음
-   작성자만 수정 가능함.
-   수정시 한번 확인 알람이 있음.

📌 댓글 삭제
![댓글 삭제](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/137512514/8cbda8d7-c42a-4b79-aed4-bb1e9f75c32e)


-   댓글을 삭제함
-   댓글 작성자만 삭제 가능함.


### 입시정보게시판
📌 게시판 리스트 검색 및 페이지네이션
![1](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/4a2df1ee-49a0-4495-9de2-364c74824d42)

- 메모지형식의 게시판 구현
- 페이지네이션 이전 다음 버튼으로 구현
- 리스트 검색 기능 제목, 작성자, 내용에 따라 검색 가능


📌 게시글 CRUD
![2](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/71594662-9e8f-4b1a-beac-53d87f9758b5)

- 게시글 작성, 수정, 삭제, 읽기 가능

📌 좋아요 및 댓글 CRUD
![3](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/ea55f917-07b3-4a4f-aaa1-89654a5f1dd6)

- 좋아요 기능 구현
- 댓글 CRUD 가능

## 11. 추가기능
### QNA 게시판
📌 Q&A
![QNA](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/75780140/891c1d87-b649-4ee1-8804-11bda3bfac04)
- 자주 찾는 질문은 배너를 활용하여 게시함
- 메일, 카테고리, 문의내용을 통해 문의할 수 있음

### 채팅방
📌 익명 채팅방
![Chat](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/75780140/ea10c85f-b623-406a-a556-6d887619df0c)

- 익명으로 채팅에 참여할 수 있음
- 로그인하지 않아도 채팅에 참여할 수 있음





## 12. 에러와 에러 해결

### 김정원

- 에러명 : 403 Forbidden 오류


- 문제점 : 웹 서버(Nginx)를 사용하는 웹 애플리케이션에서 403 Forbidden 오류 발생.


- 문제 원인 : Nginx 서버가 기본적으로 www-data 사용자로 실행되어 웹 애플리케이션의 파일에 접근할 때 권한 부족으로 인한 오류.


- 해결 방법 :
```
Nginx의 실행 사용자 변경

/etc/nginx/nginx.conf 파일을 열어서 Nginx의 실행 사용자를 ubuntu로 변경.
user ubuntu;

권한 변경

/media 디렉토리의 소유자와 그룹을 ubuntu로 변경.
sudo chown -R ubuntu:ubuntu /media
cat /etc/nginx/nginx.conf | grep user

Nginx 구성 파일 테스트
변경된 구성 파일의 유효성을 검사.
sudo nginx -t

Nginx 재시작
변경 사항이 적용되도록 Nginx 서버를 재시작.
sudo systemctl restart nginx

기타 정보
sudo systemctl status nginx 명령으로 Nginx 서버 상태 확인.
```

- 에러명 : 404 에러


- 문제 원인 :
교안에 따라 location / 위치 설정을 하였지만, 새로운 프로젝트와 url 주소가 맞지 않아서 그냥 location 부분을 '/'로 비워둠
proxy가 url 위치를 찾지 못해서 생기는 문제 


- 해결 방법 :
nginx의 default 값이 잘못 설정되어 다음과 같이 수정하여 해결

```
        location / {
        include proxy_params;
        proxy_pass http://unix:/tmp/gunicorn.sock;
       }
```


- 에러명 : 400에러 Bad Request


- 문제: 배포 이후 페이지는 찾지만, 보안 관련설정이 올바르지 않아서 뜨는 오류


- 해결 방법:
- ALLOWED_HOST를 임의로 비워둬서 발생했던 오류
- DEBUG = False로 보안상 두기


- 에러명 : 500에러 Internal Server Error


- 문제: 배포 이후 앱 몇 개가 500에러가 뜸


![image](https://github.com/maxkim77/CI/assets/141907655/f4299f8c-7758-46be-ae2e-13840b49f229)


![image](https://github.com/maxkim77/CI/assets/141907655/d9e2bbb6-b0b2-4ec0-a425-250b3e80147e)


- 문제 원인
- ls -a로 폴더 권한을 확인하던중 되던 앱은 migration이 있는데 없는앱은 migration이 없었음
- migrations이 안되었던 상황 gitignore에 migration을 추가해서 이후에 추가 된 앱들이 migration이 없는 체로 배포가됨


- 해결 방법


![image](https://github.com/maxkim77/CI/assets/141907655/d80c78a2-6ff6-48aa-82ec-bcd437968e00)


- mgirations 폴더를 다시 올리고 makemigrations 및 migrate 함
- 500 에러는 migrate가 안될 가능성이 있음 
- 배포를 위해선 git에 miration 폴더 및 init 도 추가해야 함



-   에러명 : NameError:

-   문제:

```
NameError: name 'Post' is not defined SystemCheckError: System check identified some issues: ERRORS: post.Comment.author: (fields.E304) Reverse accessor 'User.comments' for 'post.Comment.author' clashes with reverse accessor for 'study.StudyComment.author'. HINT: Add or change a related_name argument to the definition for 'post.Comment.author' or 'study.StudyComment.author'. post.Comment.author: (fields.E305) Reverse query name for 'post.Comment.author' clashes with reverse query name for 'study.StudyComment.author'. HINT: Add or change a related_name argument to the definition for 'post.Comment.author' or 'study.StudyComment.author'. study.StudyComment.author: (fields.E304) Reverse accessor 'User.comments' for 'study.StudyComment.author' clashes with reverse accessor for 'post.Comment.author'. HINT: Add or change a related_name argument to the definition for 'study.StudyComment.author' or 'post.Comment.author'. study.StudyComment.author: (fields.E305) Reverse query name for 'study.StudyComment.author' clashes with reverse query name for 'post.Comment.author'. HINT: Add or change a related_name argument to the definition for 'study.StudyComment.author' or 'post.Comment.author'.
```

-   문제 원인:

    -   Django 모델에서 역 관계(accessor)와 역 질의(reverse query) 이름이 충돌하는 경우 발생
    -   게시판 study와 게시판 post가 합쳐지면서 비슷한 이름끼리 충돌하면서 생긴문제라 각 모델 관계이름을 변경 해야 했음.

-   해결 방법:

각 모델의 역 관계 이름을 명시적으로 설정하여 충돌을 해결. related_name 매개변수를 사용하여 각 모델의 관계 이름을 고유하게 지정가능.

-   예제:

```
python Copy code class Comment(models.Model): author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comments') # 다른 필드들...

class StudyComment(models.Model): author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_comments') # 다른 필드들... 변경 후:
```

위와 같이 related_name을 설정한 후, makemigrations 및 migrate 명령을 실행하여 데이터베이스를 업데이트 -> 역 관계 이름 충돌 문제가 해결


### 김찬양
-   에러명 : NOT NULL constraint failed:

-   문제:

```
django.db.utils.IntegrityError: NOT NULL constraint failed: accounts_user.grade
```

-   문제 원인:

    -   accounts의 커스텀 사용자 앱에서 학년을 작은 양수만 저장시키기 위해 PositiveSmallIntegerField로 작성한것이 문제.
    -   해당 필드는 기본적으로 null값을 허용하지 않는것으로 보인다.
    -   기본값을 주던가, null을 허용하던가, REQUIRED_FIELDS를 사용해 지정해야했다.

-   해결 방법:

    - 처음엔 기본값을 주려고 했다가, REQUIRED_FIELDS를 사용해 입력받도록 하였다.
    - null=True는 함부로 설정하지 않는게 좋을것 같아서 이렇게했지만, 다른 팀원의 요청사항과 슈퍼유저 생성의 번거로움도 있고, 이가 없어서 에러가 나는경우는 없다고 판단했기에 null=True를 추가하는것으로 변경했다.

-   예제:

```
grade = models.PositiveSmallIntegerField(verbose_name="학년", null=True)

or

grade = models.PositiveSmallIntegerField(verbose_name="학년", default=1)

or

REQUIRED_FIELDS = [grade]
```

위와 같이 null=True항목을 추가하거나, 기본값으로 1을 주거나, REQUIRED_FIELDS를 설정하는것으로 해결된다.


### 김동후
-   에러명 : OPEN AI Version Issue

-   문제:

```
You can run 'openai migrate' to automatically upgrade your codebase to use the 1.0.0 interface.

Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`
```

-   문제 원인:

    -   Openai Api를 사용해서 인공지능 답변을 받아오기위한 views.py의 코드가 openai 버전에 맞지 않는다.
    -   Openai 라이브러리의 버전이 1.~ 버전으로 변경됨에 따라서 인공지능 모델을 생성하는 코드가 변경되었다.
    -   Openai 버전을 강제로 낮춰서 쓰거나 코드를 수정해야 했다.

-   해결 방법:

    - 처음엔 Openai 버전을 0.27로 낮추어서 사용했지만, pip 버전에 따라서 0.27이 설치되지 않는 문제가 발생했다.
    - 따라서 openai migrate를 통해서 모델을 생성하고, OPEN-AI-KEY를 가져오는 코드를 최대한 1.~ 버전에 맞게 수정하여서 최신 버전의 라이브러리 사용시에도 문제가 없도록 하였다.


## 13. 개발하며 알게 된 점 및 느낀점

### 김정원
-   가장 실무와 가까운 협업 프로젝트를 하는 건 처음이고, 특히 컨벤션 맞추는 부분이 어색하고 어려웠지만, 같이 문제를 해결하는 과정이 재미가 있었음.
-   또한 협업을 할 때 깃 환경을 어떻게 활용하는지 배우면서 팀프로젝트를 진행할 수 있었기 때문에 매우 도움이 되었던 팀프로젝트였음.
-   아직 부족한 점은 많지만 지난 DRF 개인 프로젝트에 비해 프론트서버랑 통신에서 오류잡는 시간이 단축 되었고, 또한 CI/CD 구축과 서버배포후 오류잡는 과정에서 더욱 성장 할 수 있었음

### 김창수
-   개인 프로젝트를 진행할 때와는 다르게 팀 프로젝트는 서로간의 커뮤니케이션이 많이 중요하다는걸 느낄수 있었음.
-   아직 부족하지만 이해하지 못했던 부분들을 계속 작업을 하면서 조금 더 이해할 수 있었고 노력하고 공부하는 만큼 발전되는 결과물을 볼 수 있었음.

### 김찬양
- 첫 chatGPT DRF 프로젝트에서 토큰에 과하게 시간을투자해서 아쉬웟던점이 많앗는데, 이번에 여럿이서 개발하면서 시간도 꽤 잇엇기떄문에 나름 만족할 수 있었던 프로젝트가 되었습니다.
- 장고에 꽤 많은 라이브러리를 봤다고 생각햇는데 그것보다 더 다양한 라이브러리와 편의기능이 잇다는것에 매우 놀랐습니다.
- 협업에 대해 팀원에 대한 참여율이나 컨벤션 등 걱정이 꽤 많앗는데 부드럽게 흘러간 것 같아서 좋은 결과물을 낸 것 같습니다.
- 코드를 짜다보니 욕심이 점점 생겨서 차근차근 이것저것 테스트해보면서 못써봣던 기능 등을 이후에도 개발해볼 생각입니다.

### 황진경
-  1:1 채팅 개발 경험이 있어 프로젝트 시작과 동시에 채팅을 맡아 프로젝트를 진행하였다. 그러나 첫 DRF 프로젝트였고 오류가 많아 프로젝트 기간내에 완수할 수 없다고 판단되어 포기한 것이 너무 아쉬웠고 부족한 점이 많으니 노력해야겠다고 생각했다.
- 맡은 임무를 완벽히 수행하지 못해 대부분 서브로 프로젝트를 진행하였다. 그러나 옆에서 팀원들이 개발하는 과정이나 배포하는 과정을 보며 공부할 수 있었으며 실제 서비스가 운용이 되니 신기했다.
- 협업을 진행하여 Git을 더 숙달할 수 있는 시간이었다.

### 김동후
- Git을 실무와 비슷하게 사용하는 법을 익히고 이를 통해서 배움이 늘어가는것이 눈에 뚜렷하게 보여서 뿌듯했고, 처음하는 팀 프로젝트이다보니까 많이 미숙하고 부족한 부분도 있었지만 만들어진 결과물을 보니 만족스럽다.
- Django에 조금 더 익숙해지고 특히 담당한 Open ai API를 사용하는 부분이나 채팅 관련 부분에서 많은 공부가 되어서 단순히 결과물을 위한 프로젝트가 아니라 성장하는 경험이 된거같아서 아주 의미있는 프로젝트가 된것 같다.

## 14. 마무리 및 시연 영상


https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/37a0c6d0-990f-4a94-8265-602bcc16af41

## 15. 참고 사항(로컬환경 실습)

- 깃폴더를 다운로드 후 아래와 같이 실행합니다.
```
python -m venv venv

Window: venv/Scripts/activate
Mac, Linux: source venv/bin/activate

.env 파일 생성

SECRET_KEY=YOUR_KEY
DEBUG=True
OPENAI_API_KEY=YOUR_KEY
REDIS_HOST=YOUR_HOST
REDIS_PORT=YOUR_PORT
REDIS_PASSWORD=YOUR_PWD
```

- 테스트용 더미데이터를 만드는 명령어를 추가하였습니다.
- faker 라이브러리를 이용해서, 랜덤한 가상의 데이터가 들어가서 보다 다양한 경우의수에 대한 테스트가 용이합니다.
- 현재 가상 사용자(비밀번호는 해싱되지 않은 데이터이므로 변경 필요)와 가상 자유게시판 글이 기능중에 있습니다.

1. 가상 유저 생성방법
    - 기본값은 2명 생성이고, 뒤에 --total (생성할 갯수)를 붙여주면 그만큼 생성해줍니다.
```shell
python manage.py seed-users
```


2. 가상 자유게시판 데이터 생성방법
    - 이것 역시 기본값은 2명 생성이고, 뒤에 --total (생성할 갯수)를 붙여주면 그만큼 생성해줍니다.
    - 사용자는 현재 가입된 사용자중 한명이 랜덤하게 선택되어 들어갑니다.
```shell
python manage.py fake-post
```


