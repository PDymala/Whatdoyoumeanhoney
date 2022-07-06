
import os
from pathlib import Path
import uti

BASE_DIR = Path(__file__).resolve().parent.parent



# EMAIL_USE_TLS = uti.access_secret_version('projects/125510501046/secrets/wdymh_EMAIL_USE_TLS')
# EMAIL_HOST = uti.access_secret_version('projects/125510501046/secrets/wdymh_EMAIL_HOST')
# EMAIL_PORT = uti.access_secret_version('projects/125510501046/secrets/wdymh_PORT')
# EMAIL_HOST_USER = uti.access_secret_version('projects/125510501046/secrets/wdymh_EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = uti.access_secret_version('projects/125510501046/secrets/wdymh_EMAIL_HOST_PASSWORD')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = BASE_DIR / "sent_emails"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = uti.access_secret_version('projects/125510501046/secrets/wdymh_SECRET_KEY')








# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'whatdoyoumeanhoney-vpcuqkwkfq-ew.a.run.app', 'wdymbh.diplabs.app']


# # https://stackoverflow.com/questions/29573163/django-admin-login-suddenly-demanding-csrf-token
CSRF_TRUSTED_ORIGINS=['https://*.wdymbh.diplabs.app', 'https://*.whatdoyoumeanhoney-vpcuqkwkfq-ew.a.run.app']


# https://stackoverflow.com/questions/18247190/django-development-server-keeps-logging-out
#Cookie name. this can be whatever you want
SESSION_COOKIE_NAME='sessionid'  # use the sessionid in your views code
#the module to store sessions data
SESSION_ENGINE='django.contrib.sessions.backends.db'
#age of cookie in seconds (default: 2 weeks)
SESSION_COOKIE_AGE= 600 # the number of seconds for only 7 for example
#whether a user's session cookie expires when the web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE=False
#whether the session cookie should be secure (https:// only)
SESSION_COOKIE_SECURE=False


# Application definition

INSTALLED_APPS = [
     'members',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
   
    "crispy_forms",
    "crispy_bootstrap5",
    "captcha",
]

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = "home"
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'whatdoyoumeanhoney.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'whatdoyoumeanhoney.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# https://stackoverflow.com/questions/53643254/unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0
DATABASES = {
    'default': {
        'ENGINE': uti.access_secret_version('projects/125510501046/secrets/wdymbh_engine'),
        'NAME': uti.access_secret_version('projects/125510501046/secrets/wdymbh_name'),
        'USER': uti.access_secret_version('projects/125510501046/secrets/wdymbh_user'),
        'PASSWORD': uti.access_secret_version('projects/125510501046/secrets/wdymbh_password'),
        'HOST': uti.access_secret_version('projects/125510501046/secrets/wdymbh_host'),   # Or an IP Address that your DB is hosted on
        'PORT': uti.access_secret_version('projects/125510501046/secrets/wdymbh_port'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
