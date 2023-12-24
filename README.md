# [SchoolTalks] DRF를 활용한 입시정보 커뮤니티 서비스

![배경사진](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/56ba5cd6-67a9-4841-b682-47cc4c4e6bf6)

## 1. 목표와 기능

### 1.1 목표
- 고등학생들의 입시정보 및 생활정보 공유 서비스
- 대입에 대한 입시정보를 찾고, 일상생활을 공유하며 공감대를 형성하는 서비스
  
### 1.2 기능
- 회원가입 기능
- 커뮤니티 게시판 기능
- 실시간 채팅 기능
- AI 티칭 기능

### 1.3 팀 구성
- 실제 사진을 업로드 하시길 권합니다.
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
        <td><img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/c8367fa4-d98f-4d73-906f-0eb0b8549f48" width="100%"></td>
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

![image](https://github.com/EstSoftOrmi3FinalProject/ESTSoftOrmi3FinalProject/assets/141907655/22a8b15c-a7e9-4ff0-84aa-ae0012d7b3da)

## 3. 개발 환경 및 배포 URL
### 3.1 개발 환경
- FE:


  ![HTML5](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS3](https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black)


- BE:


  ![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
  ![Django](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=django&logoColor=white)



- Deployment:


  [![GitHub](https://img.shields.io/badge/GitHub-100000.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
  [![AWS Lightsail](https://img.shields.io/badge/AWS-Lightsail-FF9900.svg?style=for-the-badge&logo=amazon-aws)](https://aws.amazon.com/lightsail/)
  [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420.svg?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
  [![Gunicorn](https://img.shields.io/badge/Gunicorn-green.svg?style=for-the-badge&logo=gunicorn)](https://gunicorn.org/)
  [![Nginx](https://img.shields.io/badge/Nginx-blue.svg?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/)
  [![DB SQLite](https://img.shields.io/badge/DB-SQLite-003B57.svg?style=for-the-badge&logo=sqlite)](https://www.sqlite.org/)


### 3.2 배포 URL
- https://www.studyin.co.kr/

## 4. URL 설계 및 API 명세


| 엔드포인트               | HTTP 메서드 | 기능                                  | 앱             | 비고 |
|--------------------------|-------------|--------------------------------------|----------------|------|
| /accounts/signup/        | POST        | 새로운 User를 만들어주는 역할 (회원가입) | Accounts       |      |
| /accounts/token/         | POST        | 인증 토큰 생성 (로그인)                  | Authentication |      |
| /accounts/token/refresh/ | POST        | 토큰 갱신                              | Authentication |      |
| /accounts/token/verify/  | POST        | 토큰 유효성 검사                       | Authentication |      |
| /accounts/user/          | GET         | 특정 사용자의 프로필 조회 (프로필 보기)   | User Profile   |      |
| /aichat/                 | GET, DELETE | AI와 채팅 (채팅 보기, 채팅 삭제)        | AI Chat        |      |
| /chat/api/chat-messages/ | GET, POST   | 채팅 메시지 조회 및 생성                | Chat           |      |
| /post/                   | GET, POST   | 글 목록 조회 및 글 작성                | Posts          |      |
| /post/{id}/              | GET, PUT, PATCH, DELETE | 특정 글 조회, 수정, 삭제       | Posts          |      |
| /post/{post_id}/comment/{id}/ | DELETE, PUT, PATCH | 특정 댓글 삭제, 수정        | Comments       |      |
| /qna/inquiry/            | GET, POST   | 문의 사항 조회 및 생성                | QnA            |      |
| /qna/inquiry/{id}/       | GET, PUT, PATCH, DELETE | 특정 문의 사항 조회, 수정, 삭제 | QnA            |      |
| /study/{id}/             | GET, DELETE, PUT | 특정 게시물 조회, 삭제, 수정     | Study          |      |



## 5. 프로젝트 구조와 개발 일정
### 5.1 프로젝트 구조
- 해당 프로젝트에서 폴더 트리 잘 다듬어 사용하세요. 필요하다면 주석을 달아주세요.
```bash
12/25 업데이트 예정
```
### 5.2 개발 일정(WBS)
![4545443](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/fd1869f3-60b9-457e-a813-e5c256d7f90d)

## 6. 데이터베이스 모델링(ERD)
![12 18](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/54ee5db8-5f40-4307-bd08-c366c658e8ec)


## 7. Architecture

![SchooltalksSystem drawio (1)](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/eb7111aa-c47a-4482-a789-4ac310aa2d9a)


## 8. 와이어프레임 / UI / BM

### 8.1 와이어프레임
- 아래 페이지별 상세 설명, 더 큰 이미지로 하나하나씩 설명 필요
![슬라이드1](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/f38583cf-038a-4153-b228-aab783940390)

- 와이어 프레임은 디자인을 할 수 있다면 '피그마'를, 디자인을 할 수 없다면 '카카오 오븐'으로 쉽게 만들 수 있습니다.

### 8.2 화면 설계 
- Accounts 앱
<table>
    <tbody>
        <tr>
            <td>메인</td>
            <td>로그인</td>
        </tr>
        <tr>
            <td>
		<img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/f0a25746-a5a7-41a3-98f7-388f063bfa0e" width="100%">
            </td>
            <td>
		<img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/86d154fe-9395-4576-adcd-04eece74e3eb" width="100%">
            </td>
	</tr>
        <tr>
            <td>회원가입</td>
            <td>프로필</td>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/c95c7cdf-d0eb-49e8-b2c1-c07feb4c202c" width="100%">
            </td>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/1ad1f6dd-e98f-4dfd-91b2-546b13dd0b7f" width="100%">
            </td>
        </tr>
        <tr>
	</tbody>
</table>

- Study 앱
<table>
    <tbody>
        <tr>
            <td>입시 정보 게시판</td>
            <td>게시글 생성</td>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/26b1edeb-61b6-4ed6-a5f7-8bdb52f55a93" width="95%">
            </td>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/e2142153-e018-4564-b6bc-31f355ba702c" width="100%">
            </td>
        </tr>
        <tr>
            <td>게시글 상세페이지</td>
            <td>게시글 수정</td>
        </tr>
        <tr>
            <td>
	        <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/4bc54f1c-34c2-4420-ad51-b818f39dfa62" width="90%">
            </td>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/0d2dc326-53a5-4546-93ef-3ca7bf3e4721" width="100%">
            </td>
        </tr>
	</tbody>
</table> 

- QNA 앱 & Chat 앱
<table>
    <tbody>
	<tr>
            <td>문의사항</td>
            <td>익명실시간챗</td>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/fa665613-6c57-4452-854f-479ba3a024e6" width="95%">
            </td>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/9d743ed8-7557-4fcf-8843-fb3c5b6ad494" width="80%">
            </td>
        </tr>
    </tbody>
</table>

- Study 앱
<table>
    <tbody>
	<tr>
            <td>글 상세보기</td>
            <td>댓글</td>
        </tr>
        <tr>
            <td>
                <img src="ui3.png" width="100%">
            </td>
            <td>
                <img src="ui3.png" width="100%">
            </td>
        </tr>
    </tbody>
</table>

- AI Chat 앱
<table>
    <tbody>
	<tr>
            <td>글 상세보기</td>
            <td>댓글</td>
        </tr>
        <tr>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/3f3162cc-686b-410f-9312-5e69ad7f223a" width="100%">
            </td>
            <td>
                <img src="https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/40dc826a-3625-4998-8a6d-a56673ffab01" width="100%">
            </td>
        </tr>
    </tbody>
</table>




## 9. 메인 기능


- accounts


📌 회원가입
![Register](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/3879f948-6ea5-4302-915c-57571177fb56)
- 회원가입 성공시 성공 메시지 생성
- 로그인 버튼 클릭 후 로그인 화면으로 이동 가능

📌 로그인
![Login](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/84ddfaae-0859-48bb-bd63-574391538421)

- 로그인 성공시 이전 페이지로 리다이렉트 됨
- 상단에 로그인 버튼이 사라지고 로그아웃 버튼이 생성됨

📌 로그아웃
![Logout](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/7d91c31f-70c0-4c35-aaca-cecca9b94bbd)

- 로그아웃 성공시 로그아웃 버튼이 사라지고 로그인 버튼이 생성됨
- 다시 로그인 버튼을 클릭하여 로그인 하거나 회원가입을 할 수 있음

📌 프로필
![프로필 재수정](https://github.com/EstSoftOrmi3FinalProject/SchoolTalks-Backend/assets/141907655/81d935af-bad8-4f98-9272-6f1be44ac30d)
- 회원 가입시 입력 정보를 프로필로 불러옴
- 회원 가입시 이미지 정보도 불러 오기 가능


## 10. 에러와 에러 해결
<김정원>
- 에러명 : NameError:

- 문제:
```
NameError: name 'Post' is not defined SystemCheckError: System check identified some issues: ERRORS: post.Comment.author: (fields.E304) Reverse accessor 'User.comments' for 'post.Comment.author' clashes with reverse accessor for 'study.StudyComment.author'. HINT: Add or change a related_name argument to the definition for 'post.Comment.author' or 'study.StudyComment.author'. post.Comment.author: (fields.E305) Reverse query name for 'post.Comment.author' clashes with reverse query name for 'study.StudyComment.author'. HINT: Add or change a related_name argument to the definition for 'post.Comment.author' or 'study.StudyComment.author'. study.StudyComment.author: (fields.E304) Reverse accessor 'User.comments' for 'study.StudyComment.author' clashes with reverse accessor for 'post.Comment.author'. HINT: Add or change a related_name argument to the definition for 'study.StudyComment.author' or 'post.Comment.author'. study.StudyComment.author: (fields.E305) Reverse query name for 'study.StudyComment.author' clashes with reverse query name for 'post.Comment.author'. HINT: Add or change a related_name argument to the definition for 'study.StudyComment.author' or 'post.Comment.author'. 
```

- 문제 원인:
    - Django 모델에서 역 관계(accessor)와 역 질의(reverse query) 이름이 충돌하는 경우 발생
    - 게시판 study와 게시판 post가 합쳐지면서 비슷한 이름끼리 충돌하면서 생긴문제라 각 모델 관계이름을 변경 해야 했음.

- 해결 방법:

각 모델의 역 관계 이름을 명시적으로 설정하여 충돌을 해결. related_name 매개변수를 사용하여 각 모델의 관계 이름을 고유하게 지정가능.

- 예제:
```
python Copy code class Comment(models.Model): author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comments') # 다른 필드들...

class StudyComment(models.Model): author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_comments') # 다른 필드들... 변경 후:
```

위와 같이 related_name을 설정한 후, makemigrations 및 migrate 명령을 실행하여 데이터베이스를 업데이트 -> 역 관계 이름 충돌 문제가 해결

## 11. 개발하며 알게 된 점 및 느낀점
<김정원>
- 가장 실무와 가까운 협업 프로젝트를 하는 건 처음이고, 특히 컨벤션 맞추는 부분이 어색하고 어려웠지만, 같이 문제를 해결하는 과정이 재미가 있었음.
- 또한 협업을 할 때 깃 환경을 어떻게 활용하는지 배우면서 팀프로젝트를 진행할 수 있었기 때문에 매우 도움이 되었던 팀프로젝트였음.
- 아직 부족한 점은 많지만 지난 DRF 개인 프로젝트에 비해 프론트서버랑 통신에서 오류잡는 시간이 단축 되었고, 또한 CI/CD 구축과 서버배포후 오류잡는 과정에서 더욱 성장 할 수 있었음


<김창수>
- 개인 프로젝트를 진행할 때와는 다르게 팀 프로젝트는 서로간의 커뮤니케이션이 많이 중요하다는걸 느낄수 있었음.
- 아직 부족하지만 이해하지 못했던 부분들을 계속 작업을 하면서 조금 더 이해할 수 있었고 노력하고 공부하는 만큼 발전되는 결과물을 볼 수 있었음.

## 12. 개발 주요 특징 및 시연 영상
