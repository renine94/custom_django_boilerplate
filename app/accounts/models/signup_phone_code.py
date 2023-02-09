from django.db import models

from core.base.models import BaseDateTime


class SignUpPhoneCode(BaseDateTime, models.Model):
    class Meta:
        db_table = 'accounts_signup_phone_code'
        unique_together = (('phone_number', 'confirm_code'),)

    phone_number = models.CharField('휴대폰번호', max_length=11)
    confirm_code = models.CharField('회원가입시 전송한 코드', max_length=6)
    is_confirm = models.BooleanField('인증완료 여부', default=False)
