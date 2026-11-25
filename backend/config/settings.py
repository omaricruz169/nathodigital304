
import os
import sys
from pathlib import Path
from pathlib import Path
import mimetypes

mimetypes.add_type("text/css", ".css", True)
mimetypes.add_type("text/javascript", ".js", True)

# =====================================================
# CONFIGURACIÓN PRINCIPAL
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# Agrega la carpeta 'apps' al path de Python para garantizar 
# que Django pueda importar 'apps.usuarios.urls'
sys.path.append(str(BASE_DIR / 'apps'))

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-clave-solo-para-desarrollo-local'
)

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# =====================================================
# APLICACIONES INSTALADAS
# =====================================================

INSTALLED_APPS = [
    # Aplicaciones Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django REST Framework
    'rest_framework',
    'rest_framework.authtoken',

    # CORS
    'corsheaders',

    # Aplicaciones propias
    'apps.usuarios',
    'apps.progreso.apps.ProgresoConfig',
]


# =====================================================
# MIDDLEWARE
# =====================================================

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =====================================================
# CONFIGURACIÓN DE URLS
# =====================================================

ROOT_URLCONF = 'config.urls'


# =====================================================
# PLANTILLAS
# =====================================================

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


# =====================================================
# WSGI
# =====================================================

WSGI_APPLICATION = 'config.wsgi.application'


# =====================================================
# BASE DE DATOS SQLITE
# =====================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =====================================================
# VALIDACIÓN DE CONTRASEÑAS
# =====================================================

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


# =====================================================
# IDIOMA Y ZONA HORARIA
# =====================================================

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True


# =====================================================
# ARCHIVOS ESTÁTICOS
# =====================================================

STATIC_URL = 'static/'


# =====================================================
# CONFIGURACIÓN DE CORREO
# =====================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# =====================================================
# CONFIGURACIÓN CORS PARA REACT
# =====================================================

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://localhost:5176',
    'http://127.0.0.1:5176',
]


# =====================================================
# DJANGO REST FRAMEWORK
# =====================================================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}


# =====================================================
# CAMPO AUTOMÁTICO DE IDENTIFICACIÓN
# =====================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'