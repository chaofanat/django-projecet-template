"""
Django settings for  project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-1tccg@!ew+x-!6vc0p1=u5!%plz^%#yj^i)z1b9r6p4qnzx0er"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'simpleui',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # django-silk
    "silk",
    # django-request
    "request",

    # ninja api
    'ninja',
    'ninja_jwt',
    "ninja_extra",
    #bootstrap5
    "django_bootstrap5",
    # django-allauth
    # allauth三方身份认证
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    # app
    'appIndex',
    'appUser',
]

MIDDLEWARE = [
    'silk.middleware.SilkyMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # locale
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # allauth
    "allauth.account.middleware.AccountMiddleware",
    
    # django-request
    "request.middleware.RequestMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

ROOT_URLCONF = "MainConfig.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
            
        },
    },
]

WSGI_APPLICATION = "MainConfig.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# MYSQL_SERVER_URL = os.environ.get('MYSQL_SERVER_URL',"127.0.0.1")
# MYSQL_DATABASE_NAME = os.environ.get('MYSQL_DATABASE_NAME',"chaofanonline")
# MYSQL_USER_NAME = os.environ.get('MYSQL_USER_NAME',"SUPERVISOR")
# MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD',"441608")
# MYSQL_PORT_NUMBER = os.environ.get('MYSQL_PORT_NUMBER',"3306")

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': MYSQL_DATABASE_NAME,
#         'USER': MYSQL_USER_NAME,
#         'PASSWORD': MYSQL_PASSWORD,
#         'HOST': MYSQL_SERVER_URL,
#         'PORT': MYSQL_PORT_NUMBER
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['user', 'repo']
        
    },
}



# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

from django.utils.translation import gettext_lazy as _
LANGUAGE_CODE = "zh-hans" # 默认使用中国时区

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

LANGUAGES = (
("en", _("English")),
("zh-hans", _("Simplified Chinese")),
)

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django-allauth其他配置
# 用户登录
ACCOUNT_AUTHENTICATION_METHOD = "username_email" # 邮箱或用户名登录
# ACCOUNT_LOGIN_BY_CODE_ENABLED (default: False)
# “Login by email” offers an alternative method of logging in. Instead of entering an email address and accompanying password, the user only enters the email address. Then, a one-time code is sent to that email address which allows the user to login. This method is often referred to as “Magic Code Login”. This setting controls whether or not this method of logging in is enabled.
ACCOUNT_EMAIL_VERIFICATION =  "optional" # 注册邮箱验证, 可选值 "强制(mandatory)"、 "可选(optional)" 或 "否(none)" 之一
ACCOUNT_EMAIL_REQUIRED = True # 设置用户注册的时候必须填写邮箱地址
ACCOUNT_LOGOUT_ON_GET = False           # 用户登出(需要确认)
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3 # 邮箱确认邮件的截止日期(天数)
ACCOUNT_USERNAME_MIN_LENGTH = 4 # 用户名最小长度
ACCOUNT_USERNAME_BLACKLIST = ['admin'] # 用户名黑名单
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True # 登录是否自动跳转
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True # 修改密码后是否自动登出
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False # 重置密码后是否自动登录
ACCOUNT_SESSION_REMEMBER = None # 控制会话的生命周期。设置为无以询问用户（“还记得我吗？”），False 表示不记得，True 表示始终记住。
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False # 注册时是否需要确认两次邮箱
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True # 注册时是否需要确认两次密码
ACCOUNT_UNIQUE_EMAIL = True # 邮箱是否唯一
SOCIALACCOUNT_AUTO_SIGNUP = True # 社交账号是否自动注册,使用从社交账号提供者检索的字段(如用户名、邮件)来绕过注册表单
ACCOUNT_CHANGE_EMAIL = False # 禁用（False）时，用户可以将一个或多个电子邮件地址（最多 ACCOUNT_MAX_EMAIL_ADDRESSES）添加到他们的帐户并自由管理这些电子邮件地址。启用（True）时，用户只能拥有一个电子邮件地址，他们可以通过添加临时的第二个电子邮件地址来更改该地址，该地址在验证后替换当前电子邮件地址。
# ACCOUNT_MAX_EMAIL_ADDRESSES (default: None)
# The maximum amount of email addresses a user can associate to his account. It is safe to change this setting for an already running project – it will not negatively affect users that already exceed the allowed amount. Note that if you set the maximum to 1, users will not be able to change their email address.
ACCOUNT_EMAIL_NOTIFICATIONS = False # 启用（True）时，用户可以启用或禁用电子邮件通知(密码更改，登录地址变更等）。
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True # 将经过身份验证的用户在尝试访问登录 / 注册页面时重定向到 LOGIN_REDIRECT_URL。
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = False # 控制是通过跟踪电子邮件中的链接（False）还是通过输入代码（True）来执行电子邮件验证。

ACCOUNT_SIGNUP_FORM_HONEYPOT_FIELD = "phone_number" # 为注册表单增加一个额外的不需要的字段，对于用户是隐藏的，但是当机器人输入此字段后，服务器将不会真的创建用户。
# ACCOUNT_EMAIL_VERIFICATION_BY_CODE_MAX_ATTEMPTS (default: 3)
# This setting controls the maximum number of attempts the user has at inputting a valid code.

# ACCOUNT_EMAIL_VERIFICATION_BY_CODE_TIMEOUT (default: 900)
# The code that is emailed has a limited life span. It expires this many seconds after which it was sent.

# ACCOUNT_EMAIL_SUBJECT_PREFIX (default: "[Site] ")
# Subject-line prefix to use for email messages sent. By default, the name of the current Site (django.contrib.sites) is used.

# ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS (default: True)
# Configures whether password reset attempts for email addresses which do not have an account result in sending an email.

# ACCOUNT_DEFAULT_HTTP_PROTOCOL (default: "http")
# The default protocol used for when generating URLs, e.g. for the password forgotten procedure. Note that this is a default only – see the section on HTTPS for more information.

# 登录后跳转
LOGIN_REDIRECT_URL = "/accounts/profile/"
# 登出后跳转
ACCOUNT_LOGOUT_REDIRECT_URL = "/" 

ACCOUNT_RATE_LIMITS = {
    "change_password": "5/m/user",
    "manage_email": "10/m/user",
    "reset_password": "20/m/ip,5/m/key",
    "reauthenticate": "10/m/user",
    "reset_password_from_key": "20/m/ip",
    "signup": "20/m/ip",
    "login": "30/m/ip",
    "login_failed": "10/m/ip,5/5m/key",
    "confirm_email": "1/3m/key"
}

# email
#邮件配置,需要去三方邮箱开启授权服务
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 465
EMAIL_HOST_USER = 'chaofanat@qq.com'  # 发送邮件的邮箱帐号
EMAIL_HOST_PASSWORD = 'jlzarovrvdrtjbah'  # 授权码,各邮箱的设置中启用smtp服务时获取
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  #收件人显示发件人的邮箱
# DEFAULT_FROM_EMAIL = '<xxxxx@qq.com>' #也可以随意写
EMAIL_USE_SSL = True   # 使用ssl
# EMAIL_USE_TLS = False # 使用tls
# EMAIL_USE_SSL 和 EMAIL_USE_TLS 是互斥的，即只能有一个为 True




#从环境变量中读取服务网络
REDIS_SERVER_URL = os.environ.get('REDIS_SERVER_URL',"127.0.0.1")

# redis 配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_SERVER_URL}:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# celery
CELERY_BROKER_URL = f"redis://{REDIS_SERVER_URL}:6379/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_SERVER_URL}:6379/0"
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TIMEZONE = "Asia/Shanghai"
CELERY_ENABLE_UTC = True
#控制celery进程的并行数
#CELERY_WORKER_CONCURRENCY = 1
# 控制任务结果的存储时间
CELERY_RESULT_EXPIRES = 60 * 60 * 24 * 1  # 单位：秒，例如 3600 秒（1小时）