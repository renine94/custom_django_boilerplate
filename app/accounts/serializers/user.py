from rest_framework import serializers

from app.accounts.models import User
from app.accounts.models.signup_phone_code import SignUpPhoneCode


class UserInfoSerializer(serializers.ModelSerializer):
    """유저 데이터를 직렬화"""

    class Meta:
        model = User
        exclude = ['id', 'password']  # 식별 값이나 보안 관련 값 제외


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'name',
            'nickname',
            'phone_number',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data) -> User:
        """serializer.save() 호출시 실행"""
        user = self.Meta.model(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    password = serializers.CharField()


class PasswordResetSerializer(serializers.ModelSerializer):
    code = serializers.CharField(write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('code', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password1 and password2 should be same!')
        return data
