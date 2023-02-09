from django.urls import path

from app.accounts.views.user.v1 import UserDetailAPI

app_name = 'accounts_v2'

urlpatterns = [
    # User
    path('/v2', UserDetailAPI.as_view()),  # 회원 가입
]
