# 자율운항선박 테러대응 시스템

이 프로젝트는 2023년 캡스톤디자인에 사용할 프로그램입니다. "Level 3 자율운항선박의 물리적 해상 테러대응 시스템"이 주제이며, 이 리포지토리에 올리는 내용은 관제센터 시스템 부분입니다.

## 개발환경

-   언어: Python(3.9v), HTML, CSS, Javascript
-   라이브러리: Django(4.1v), django-bootstrap5, channels, daphne, selenium, BeautifulSoup, requests
-   데이터베이스: MySQL

## 기능

-   실시간 선박의 상태 확인
-   선박의 테러 대응 수동 제어
-   선박과 실시간 통신을 통한 관제
-   관제할 선박 선택
-   주변 해역에서 일어나는 해적 정보 확인

## 사용법

1. git clone
2. Python 3.9 환경에서 종속성 설치
3. 터미널에 <pre><code> daphne controlsystem.asgi:application --port 8080
   </code></pre>로 서버 실행

## 라이선스

MIT License

Copyright (c) [2023] [Pupba]
