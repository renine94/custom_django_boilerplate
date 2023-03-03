from enum import Enum
from typing import List, Any


class BaseEnum(Enum):
    """
    Enum 기초 함수 상속용
    """

    @classmethod
    def has_value(cls, value: str) -> bool:
        return value in cls._value2member_map_

    @classmethod
    def get_names(cls) -> List[str]:
        """이름 목록 가져오기"""
        return [enum.name for enum in cls]

    @classmethod
    def get_name_by_value(cls, value: str):
        """값으로 이름 가져오기"""
        for enum in cls:
            if enum.value == value:
                return enum.name

    @classmethod
    def get_values(cls) -> List[Any]:
        """값 리스트 가져오기"""
        return [enum.value for enum in cls]

    @classmethod
    def get_value_by_name(cls, name: str):
        """이름으로 값 가져오기"""
        return cls[name].value

    @classmethod
    def get_name_and_value(cls) -> dict:
        """모든 Enum 목록 가져오기"""
        return {enum.name: enum.value for enum in cls}

    @classmethod
    def get_enum_by_value(cls, value: str):
        for enum in cls:
            if enum.value == value:
                return enum

