from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','0.0.0.0']

# Use SQLite for local development (easier setup)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
