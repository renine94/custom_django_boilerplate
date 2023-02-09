from django.urls import path

from .views.user.v1 import AccountAPI

app_name = 'accounts'

urlpatterns = [
    path('/v1', AccountAPI.as_view()),  # 회원 가입
]
