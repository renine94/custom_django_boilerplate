# Project

## 사용기술
  - python 3.8.11
  - django >= 4.11
  - django-rest-framework
  - token login
  - Dynamic Query
  - DB : sqlite3 (mysql or postgresql 설치 후 연결시, 도커 설정이 필요할것 같아 일단 sqlite3 로 진행했습니다.)


## 강조 하고싶은 점
> 목요일 하루밖에 과제를 할시간이 없어서 다소 코드 퀄리티가 나쁠 수 있는점 양해 부탁드립니다.

- 최대한 Django 프로젝트 디렉토리 구조를 모듈화 했습니다.
  - 추후 서비스가 확장됨에 따라 유연하게 대처하기 위함입니다.
  - 공통으로 사용되는 부분들은 core 패키지아래에 모듈화 했습니다.
  - 개발에서만 사용하는 패키지를 따로 분리하기 위해 requirement 를 따로 구성했습니다.
    - `django-debug-toolbar`
    - `black`
  - 추후 API 버저닝을 위해 view 를 패키지화하여 파일이름으로 구분하고 있습니다. 
- 유저 정보 단일조회 건에서는 인증된 사용자 (로그인 상태) 만 API 요청이 가능하도록 하였습니다.


## 특별히 신경쓴 부분
- 실제 서비스에서 사용하기 무리없는 프로젝트를 구성했습니다.
  - 각 환경별로 settings 분리
  - env 변수들도 분리가 가능하나, 추후 AWS Secret Manager 를 사용할거라 판단하여 따로 작업안했습니다.

## 실행 방법
-  `python -m venv venv`
-  `source venv/bin/activate`
-  `pip install -r requirements/local.txt`
-  `export DJANGO_SETTINGS_MODULE=core.settings.local` (개발당시 pycharm 따로 설정, vscode 나 터미널에서 서버 띄우려면 따로 설정필요합니다.)
-  `python manage.py makemigrations`
-  `python manage.py migrate`
-  `python mange.py runserver`

