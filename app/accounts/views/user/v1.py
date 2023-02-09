from rest_framework.views import APIView
from rest_framework.response import Response


class AccountAPI(APIView):
    """
    회원 가입 Controller
    """

    def get(self, request):
        return Response('hello world')

    def post(self, request):
        """회원 가입"""
        return Response('hello world')


class LoginAPI(APIView):
    """
    로그인 Controller
    """

    def post(self, request):
        return "Login API"
