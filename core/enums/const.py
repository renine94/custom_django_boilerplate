from core.base.enum import BaseEnum


class AWSEnum(BaseEnum):
    """AWS 관련 상수 모음"""
    AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"


class RoleEnum(BaseEnum):
    """역할 관련 상수 모음"""
    HR = 'HR'
    MD = 'MD'
    SELLER = 'SELLER'
    DEVELOPER = 'DEVELOPER'
    ADMIN = 'ADMIN'
