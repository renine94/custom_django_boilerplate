from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models

from core.base.models import BaseModel
from core.utils.accounts import get_random_number


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have a valid email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone_number_validator = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')

    email = models.EmailField('이메일', unique=True)
    nickname = models.CharField('닉네임', max_length=20)
    name = models.CharField('이름', max_length=30)
    phone_number = models.CharField('핸드폰번호', validators=[phone_number_validator], max_length=11, unique=True)
    confirm_code = models.CharField('인증코드', max_length=6, null=True, unique=True)
    is_active = models.BooleanField('활성유저 여부', default=True)
    is_staff = models.BooleanField('직원 여부', default=False)
    is_superuser = models.BooleanField('관리자 여부', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'name', 'phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """유저에게 이메일 전송"""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def send_confirm_code(self):
        """비밀번호 초기화 인증문자 전송"""
        random_number = get_random_number()

        # TODO 외부 API 연동 필요 (toast, sweetTracker etc...)
        # SnsHandler.send('01064139771', random_number)

        self.confirm_code = random_number
        self.save()

        return random_number
