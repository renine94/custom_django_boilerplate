from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny, IsAuthenticated

from app.accounts.models import User
from app.accounts.serializers.user import UserSerializer


class UserAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request) -> Response:
        """
        전체 회원 조회
        1. query_parameter
            - nickname : 포함되어 있으면 필터링
        """
        users = User.objects.all()

        # Filter, Ordering 필요시 구현 TODO: django-filter + DRF 구현
        if values := request.query_params:
            nickname = values.get('nickname')
            users = users.filter(nickname__icontains=nickname)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        """
        회원 가입
        1. 전화 번호 인증 후 회원가입 이 가능 해야 한다.
        """


class UserDetailAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """단일 회원 조회 (내 정보 보기 기능)"""
        user = get_object_or_404(User, pk=1)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginAPI(APIView):
    """
    로그인 Controller
    """

    def post(self, request):
        return "Login API"
