FROM python:3.8-alpine

MAINTAINER @kyle-renine94

WORKDIR /src

ARG APP_ENV=$APP_ENV
ARG DJANGO_SETTINGS_MODULE=core.settings.$APP_ENV
ARG AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_ENV=$APP_ENV \
    DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE \
    AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

COPY . .

RUN apk update
RUN apk add --no-cache gcc musl-dev linux-headers mariadb-dev mariadb-client libffi-dev python3-dev make build-base
RUN pip install --upgrade pip
RUN pip install --no-cache -r requirements/prod.txt

# 물리 코어 개수 구하기
RUN export NUM_CORES=$(grep -c ^processor /proc/cpuinfo)

# 서버 실행
CMD sh -c "python manage.py makemigrations --noinput && python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:8000 --max-requests 1000 --max-requests-jitter 150 -w ${NUM_CORE} -k gevent"

# 포트개방
EXPOSE 8000
