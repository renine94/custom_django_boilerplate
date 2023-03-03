from django.db import models
from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    created_by = models.CharField(max_length=50, null=True, default=None, verbose_name='생성한 사람')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    updated_by = models.CharField(max_length=50, null=True, default=None, verbose_name='수정한 사람')
