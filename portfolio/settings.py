import os
from pathlib import Path
from corsheaders.defaults import default_headers  # ✅ Required for CORS headers

BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key & Debug
SECRET_KEY = os.environ.get('SECRET_KEY', 'insecure-dev-key')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Allowed Hosts
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".railway.app",
    "djangoportfolio-production-6822.up.railway.app",
]

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'rest_framework',
    'corsheaders',  # ✅ CORS support
]

# Middleware (corsheaders must be first)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # ✅ MUST BE FIRST
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

# Database (use Railway PostgreSQL if env vars present)
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'railway',
            'USER': 'postgres',
            'PASSWORD': 'FkDaFxJxVkUXKfjxjJDMHYfzLlQQIEsK',
            'HOST': 'gondola.proxy.rlwy.net',
            'PORT': '28122',
            }
}
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }


# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CORS Settings
CORS_ALLOWED_ORIGINS = [
    "https://mskcode.netlify.app",  # ✅ React frontend deployed on Netlify
    "http://localhost:3000",

]



CSRF_TRUSTED_ORIGINS = [
    "https://mskcode.netlify.app",  # ✅ Required for safe POST requests
    "http://localhost:3000",
    "https://djangoportfolio-production-6822.up.railway.app",
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'content-disposition',
]

CORS_ALLOW_CREDENTIALS = True  # ✅ If you're using sessions or cookies

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
