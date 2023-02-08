from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": 'mydb',
        "USER": 'root',
        "PASSWORD": '0000',
        "HOST": '127.0.0.1',
        "PORT": '3306',
        "OPTIONS": {"charset": "utf8mb4"},
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "TEST": {
            'NAME': 'mytestdb',
        },
    },
    # 'replica': {
    #     "ENGINE": "django.db.backends.mysql",
    #     "NAME": os.getenv("DB_NAME"),
    #     "USER": os.getenv("DB_USER"),
    #     "PASSWORD": os.getenv("DB_PASSWORD"),
    #     "HOST": os.getenv("DB_HOST"),
    #     "PORT": os.getenv("DB_PORT"),
    #     "OPTIONS": {"charset": "utf8mb4"},
    # },
}

DATABASE_ROUTERS = ['core.routers.ReadReplicaRouter']
