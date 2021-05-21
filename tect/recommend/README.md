### 책 추천 알고리즘 샘플 프로젝트

> 프로젝트 경로의 ReadMe를 완료함을 가정하고 설명한다. <br>

- Recommend app Setup

  ```
  (venv) $ python3 manage.py makemigrations recommend
  (venv) $ python3 manage.py migrate recommend
  ```
> DB 생성 이후, tect/scripts/db.py 의 12번째 줄 csv_path를 해당 로컬 컴퓨터의 book.csv 경로로 바꾼다.<br>

- Runserver

```
(venv) $ python3 manage.py runserver
```

> runserver 이후, url 경로에 **http://localhost:8000/recommend/important/dbinstall** 를 입력하여 책 데이터베이스를 장고 내장 DB에 설치한다. <br>
  install 은 한번만 시행해야한다. 시행 시간은 30초 이상 걸릴 수 있다.
> install을 두 번 이상 시행하여 추천 참조 관계가 중복된 경우,  **http://localhost:8000/recommend/important/dbdelete** 를 통해 DB를 초기화하고, 다시 install 한다.<br>
