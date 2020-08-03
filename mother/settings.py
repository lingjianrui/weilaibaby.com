"""
Django settings for mother project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import datetime as dt

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2)#v@%30eyqzbr1(4(42(e89c2*90nt2w*cf62b$22_8%fa%*1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'markdownx',
    'markdown_deux',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mother.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'mother.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'

# 上传配置
MEDIA_URL = '/uploads/'
THUMB_URL = '/uploads/thumbs/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
THUMB_WIDTH = 200  # 缩略图的宽度
THUMB_HEIGHT = 100  # 缩略图的高度
THUMB_FORMAT = 'JPEG'  # 缩略图处理的格式
# 注意：滑动条上传的图片尺寸建议为：700px * 300px

# 自定义用户model
AUTH_USER_MODEL = 'app.User'

# 分页器设置
PER_PAGE = 20

# markdownx编辑器设置
# Markdownify
MARKDOWNX_MARKDOWNIFY_FUNCTION = 'markdownx.utils.markdownify'  # Default function that compiles markdown using defined extensions. Using custom function can allow you to pre-process or post-process markdown text. See below for more info.

# Markdown extensions
# MARKDOWNX_MARKDOWN_EXTENSIONS = []
# 'markdown.extensions.extra',
# 'markdown.extensions.nl2br',
# 'markdown.extensions.smarty',
# 'markdown.extensions.codehilite',
# ] # List of used markdown extensions. See below for more info.
MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra'
]

MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS = {}  # Configuration object for used markdown extensions

# Markdown urls
MARKDOWNX_URLS_PATH = '/markdownx/markdownify/'  # URL that returns compiled markdown text.
MARKDOWNX_UPLOAD_URLS_PATH = '/markdownx/upload/'  # URL that accepts file uploads, returns markdown notation of the image.

# Media path
today = dt.datetime.today()
MARKDOWNX_MEDIA_PATH = 'markdownx/' + '%d/%d/' % (
    today.year, today.month)  # Path, where images will be stored in MEDIA_ROOT folder

# Image
MARKDOWNX_UPLOAD_MAX_SIZE = 52428800  # 50MB - maximum file size
MARKDOWNX_UPLOAD_CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/svg+xml',
                                  'image/gif']  # Acceptable file content types
MARKDOWNX_IMAGE_MAX_SIZE = {'size': (600, 600), 'quality': 90, }
# MARKDOWNX_IMAGE_MAX_SIZE = {'quality': 90,} # Different options describing final image processing: size, compression etc. See below for more info. Dimensions are not applied to SVG files.

# Editor
MARKDOWNX_EDITOR_RESIZABLE = True  # Update editor's height to inner content height while typing
