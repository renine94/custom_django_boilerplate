from core.base.enum import BaseEnum


class TestEnum(BaseEnum):
    """테스트 관련 상수 모음"""
    TEST1 = "TEST1"
    TEST2 = "TEST2"


class RoleEnum(BaseEnum):
    """역할 관련 상수 모음"""
    HR = 'HR'
    MD = 'MD'
    SELLER = 'SELLER'
    DEVELOPER = 'DEVELOPER'
    ADMIN = 'ADMIN'
