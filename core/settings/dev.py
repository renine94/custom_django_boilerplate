from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases}
DATABASES = {
    "default": {
        "ENGINE": env('DB_ENGINE'),
        "NAME": env('DB_NAME'),
        "USER": env('DB_USER'),
        "PASSWORD": env('DB_PASSWORD'),
        "HOST": env('DB_HOST'),
        "PORT": env('DB_PORT'),
        "OPTIONS": {"charset": "utf8mb4"},
        "ATOMIC_REQUESTS": True,
        "TEST": {'NAME': 'mytestdb'},
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
