import random


def get_random_number(length=6):
    """랜덤 난수 length 만큼 생성하여 리턴"""
    return ''.join([str(random.choice(range(10))) for _ in range(length)])
