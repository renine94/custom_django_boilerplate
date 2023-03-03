from django.db import models

from core.base.models import BaseModel


# Create your models here.

class Config(BaseModel, models.Model):
    """
    Server 에서 동적으로 사용하는 ServerConfig 값들을 저장시킨다. feature flag 역할 on/off
    """
    mileage_duration = models.PositiveIntegerField('마일리지 유효기간', default=0)
