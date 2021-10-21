"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import rest_settings as rest_settings

import yaml


from api.object_detection.yolo_tester import YOLO


# C:\Users\~~~~\AI-Cashier\backend
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent  # C:\Users\~~~~\AI-Cashier
# C:\Users\~~~~\AI-Cashier\frontend\public
MEDIA_ROOT = os.path.join(ROOT_DIR, 'frontend', 'public')


SECRET_KEY = rest_settings.SECRET_KEY


DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',  # 추가
    'rest_framework',  # 추가
    'corsheaders',  # 추가
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',  # 추가
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',

)  # script안에서의 리소스 요청을 허용할 도메인 추가

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(ROOT_DIR, 'frontend', 'build'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = rest_settings.DATABASES


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [

    # C:\Users\~~~~\AI-Cashier\frontend\build\static
    os.path.join(ROOT_DIR, 'frontend', 'build', 'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# yolo 모델
''' 
with open(f'{BASE_DIR}/api/object_detection/model_property/model_environments.yaml', 'r', encoding='UTF8') as f:
    model_environment = yaml.load(f, Loader=yaml.FullLoader)

yolov3_property = model_environment['yolov3_model']
'''
model_property = dict({
    "config_file": "api/object_detection/output/customed_yolov3.cfg",
    "weight_file": "api/object_detection/model_property/yolo-model-9.weights",
    "labels": "api/object_detection/model_property/object.tags",
    "conf": 0.6,  # conf : Confidence threshold for predictions
    "nms": 0.4,  # nms : NMS threshold
    "resol": 416  # resol : Resolution of network. Higher increases accuracy but decreases speed
})

yolo = YOLO(model_property)
