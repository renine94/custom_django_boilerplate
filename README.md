# Django 폴더구조 보일러플레이트

## 사용기술
  - python 3.8.11
  - django >= 4.11
  - django-rest-framework
  - token login
  - Dynamic Query
  - DB : sqlite3 (mysql or postgresql 설치 후 연결시, 도커 설정이 필요할것 같아 일단 sqlite3 로 진행했습니다.)


## 실행 방법
-  `python -m venv venv`
-  `source venv/bin/activate`
-  `pip install -r requirements/local.txt`
-  `export DJANGO_SETTINGS_MODULE=core.settings.local` (개발당시 pycharm 따로 설정, vscode 나 터미널에서 서버 띄우려면 따로 설정필요)
-  `python manage.py makemigrations`
-  `python manage.py migrate`
-  `python mange.py runserver`

## Docker Image
- `docker build -t test:0.0.4 -f ./deploy/Dockerfile . --no-cache`

위에 . 이 중요
