from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token

from app.accounts.models import User
from app.accounts.models.signup_phone_code import SignUpPhoneCode
from app.accounts.serializers.user import (
    UserInfoSerializer,
    LoginSerializer,
    UserSignUpSerializer,
    PasswordResetSerializer,
)
from core.handlers.SmsHandler import SnsHandler
from core.utils.accounts import get_random_number


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

        serializer = UserInfoSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: Request) -> Response:
        """
        회원 가입
        1. 전화 번호 인증 후 회원가입 이 가능 해야 한다.
            - 아직 회원 데이터가 만들어지지 않아, 휴대폰번호와 인증번호를 임시로 저장할 테이블이 필요
        """
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        token = Token.objects.create(user=instance)
        return Response({"Token": token.key}, status=status.HTTP_201_CREATED)


class UserDetailAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Request, pk: int) -> Response:
        """단일 회원 조회 (내 정보 보기 기능)"""
        user = get_object_or_404(User, pk=pk)
        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginAPI(APIView):
    def post(self, request):
        """
        유저 로그인
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 방법 1 ( 확장성은 좋으나, 내부 구현로직을 뜯어서 고쳐야 하므로 러닝커브 존재 )
        # user = authenticate(**serializer.validated_data)  # TODO CustomBackend 만들어서 authenticate 구현
        # 방법 2
        email = serializer.validated_data.get('email')
        phone_number = serializer.validated_data.get('phone_number')
        password = serializer.validated_data.get('password')

        qs = User.objects.filter(Q(email=email) | Q(phone_number=phone_number))
        if qs.exists():
            user = qs.first()
            # 입력 받은 비밀번호 일치하는지 체크
            if not user.check_password(password):
                return Response({'message': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'data': '일치하는 회원정보를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)


class PasswordResetAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        """email 과 phone_number를 받아 인증번호 전송"""
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')

        user = get_object_or_404(User, email=email)
        if user.phone_number == phone_number:
            confirm_code = user.send_confirm_code()
            return Response({'message': f'인증번호 [{confirm_code}] 전송 완료'}, status=status.HTTP_200_OK)
        return Response({'입력하신 이메일주소와 핸드폰번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """인증번호와 변경할 비밀번호 받아서 pw변경"""
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        confirm_code = serializer.validated_data['code']
        try:
            user = User.objects.get(confirm_code=confirm_code)
        except User.DoesNotExist:
            return Response({'message': '해당 인증번호가 유효한지 다시 한번 확인해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['password'])
        user.confirm_code = None
        user.save()
        return Response({'message': '비밀번호 재설정 완료'}, status=status.HTTP_200_OK)


class ConfirmCodeRequestAPI(APIView):
    """
    회원가입시, 휴대전화 인증번호 발송 API
    """

    def get(self, request):
        phone_number = request.data.get('phone_number')
        random_number = get_random_number()

        # TODO 인증번호 보내는 모듈 구현
        # SnsHandler.send(phone_number, random_number)

        SignUpPhoneCode(phone_number=phone_number, confirm_code=random_number).save()
        return Response({'message': f'인증번호 [{random_number}] 전송 완료'}, status=status.HTTP_200_OK)


class ConfirmCodeCheckAPI(APIView):
    """
    회원가입시, 휴대전화 인증번호 확인 체크 API
    """

    def post(self, request):
        confirm_code = request.data.get('confirm_code')

        try:
            signup_phone_code = SignUpPhoneCode.objects.get(confirm_code=confirm_code, is_confirm=False)
            signup_phone_code.is_confirm = True
            signup_phone_code.save()
        except SignUpPhoneCode.DoesNotExist:
            return Response({'data': False}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'data': True}, status=status.HTTP_200_OK)
