"""
Django settings for zhihuer project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q8oz7zb$zr^ptqwr2j(w6ivdvfu%dcrh8y8tje#*)h3hwci&px'  # os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # True

ALLOWED_HOSTS = ['192.168.2.190', 'localhost', '127.0.0.1']  # []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zhihu',
    'user',
    # 第三方验证码
    'captcha',
    # 富文本编辑器
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    # caches
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # caches
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'zhihuer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 在模板中使用{{ MEDIA_URL }}
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'zhihuer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zhihuer',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}

'''
# pythonanywhere database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'taoing$zhihuer',
        'USER': 'taoing',
        'PASSWORD': 'tm180705',
        'HOST': 'taoing.mysql.pythonanywhere-services.com',
    }
}
'''

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  # 'en-us'

TIME_ZONE = 'Asia/Shanghai'  # 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 静态文件目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 自定用户模型
AUTH_USER_MODEL = 'user.User'

# 分页
ANSWER_PER_PAGE = 10
QUESTION_PER_PAGE = 5
COMMENT_PER_PAGE = 5
TOPIC_PER_PAGE = 4
TREND_PER_PAGE = 5
USER_PER_PAGE = 5
SEARCH_PER_PAGE = 5

# 边缘显示页数
MARGIN_PAGES = 2
# 中间显示页数
PAGE_RANGE = 4

# 邮箱配置
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'example@sina.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = False
EMAIL_FROM = EMAIL_HOST_USER

'''
# gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FROM = EMAIL_HOST_USER
'''

# 自定认证后端
AUTHENTICATION_BACKENDS = [
    'user.views.CustomModelBackend',
]

# login_required重定向url
LOGIN_URL = '/login/'

# 用户上传文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 富文本编辑器上传文件保存目录, 在media下
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
    }
}

# pythonanywhere nhttps
# SECURE_SSL_REDIRECT = True

# cache django-redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
            'CONNECTION_POOL_KWARGS': {'max_connections': 100},
        },

    }
}

# CACHE_MIDDLEWARE_SECONDS = 60
# CACHE_MIDDLEWARE_KEY_PREFIX = 'zhihuer'

# celery settings
# celery中间人, 使用redis数据库
BROKER_URL = 'redis://127.0.0.1:6379/2'
# celery结果返回，跟踪结果
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'

# celery内容消息的格式设置
CELERY_ACCEPT_CONTENT = ['application/json', ]
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# celery时区设置
CELERY_TIMEZONE = TIME_ZONE

# 尝试配置django的日志模块
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            # logging handler that outputs log messages to terminal
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',  # message level to be written to console
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'filename': 'logs/debug.log',
            'formatter': 'simple',
        },
        'rotating_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件, 根据时间自动切
            'filename': os.path.join(BASE_DIR, 'logs', "zhihuer_debug.log"),
            'backupCount': 10,  # 备份数为10
            'when': 'D',  # 每天一切,可选值有S/秒 M/分 H/小时 D/天 W0-W6/周(0=周一) midnight/如果没指定时间就默认在午夜
            'formatter': 'simple',
        },
    },
    'loggers': {
        '': {
            # this sets root level logger to log debug and higher level
            # logs to console. All other loggers inherit settings from
            # root level logger.
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False, # this tells logger to send logging message
                                # to its parent (will send if set to True)
        },
        'django.db': {
            # log raw sql of django orm
            'handlers': ['console', 'rotating_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
