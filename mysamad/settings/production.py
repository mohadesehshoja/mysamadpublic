import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


DEBUG = False

ALLOWED_HOSTS = ["*"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'samad',
        'USER': 'postgres',
        'PASSWORD': os.environ.get("db_password"),
        'HOST': 'localhost',
        'PORT': '5432'
    }
}