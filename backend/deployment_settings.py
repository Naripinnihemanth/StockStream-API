import os
import dj_database_url

from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
CSRF_TRUSTED_ORIGINS=["https://"+os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

DEBUG = False

SECRET_KEY=os.environ.get('SECRET_KEY')


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]


CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}


CLOUDINARY_URL = (
    f"cloudinary://{os.getenv('CLOUDINARY_API_KEY')}:"
    f"{os.getenv('CLOUDINARY_API_SECRET')}@"
    f"{os.getenv('CLOUDINARY_CLOUD_NAME')}"
)


# STORAGES={
#     "default":{
#         "BACKEND":"django.core.files.storage.FileSystemStorage"
#     },
#     "staticfiles":{
#         "BACKEND":"whitenoise.storage.CompressedStaticFilesStorage",
#     }
# }

DATABASES={
    "default":dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=60
    )
}


