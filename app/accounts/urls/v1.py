from django.urls import path

from app.accounts.views.user.v1 import (
    UserDetailAPI,
    UserAPI,
    LoginAPI,
    PasswordResetAPI,
    ConfirmCodeRequestAPI,
    ConfirmCodeCheckAPI,
)

app_name = 'accounts_v1'

# fmt: off
urlpatterns = [
    path('', UserAPI.as_view()),                                    # 유저 전체 조회, 회원가입
    path('/<int:pk>', UserDetailAPI.as_view()),                     # 유저 단일 조회
    path('/confirm-code', ConfirmCodeRequestAPI.as_view()),         # 회원가입 휴대폰 인증 요청
    path('/confirm-code-check', ConfirmCodeCheckAPI.as_view()),   # 회원가입 휴대폰 인증 확인
    path('/login', LoginAPI.as_view()),                             # 로그인
    path('/password-reset', PasswordResetAPI.as_view()),            # 비밀번호 재설정
]
# fmt: on
