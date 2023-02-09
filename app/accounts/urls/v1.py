from django.urls import path

from app.accounts.views.user.v1 import UserDetailAPI, UserAPI

app_name = 'accounts_v1'

# fmt: off
urlpatterns = [
    path('', UserAPI.as_view()),                    # 유저 전체 조회
    path('/<int:pk>', UserDetailAPI.as_view()),     # 유저 단일 조회
]
# fmt: on
