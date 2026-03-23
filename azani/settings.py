from pathlib import Path
from decimal import Decimal
from dotenv import load_dotenv
import os
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ── SECURITY ──────────────────────────────────────────────────────────────────
SECRET_KEY = os.getenv('SECRET_KEY', 'azani-ispo-secret-key-change-in-production-do-not-use-as-is')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Accept all hosts by default — lock down via ALLOWED_HOSTS env var in production
_allowed = os.getenv('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = _allowed.split(',') if _allowed else ['*']

# Required in Django 4.0+ for HTTPS form submissions (POST requests)
_csrf = os.getenv('CSRF_TRUSTED_ORIGINS', '')
CSRF_TRUSTED_ORIGINS = [h.strip() for h in _csrf.split(',') if h.strip()]

# ── APPS ──────────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

# ── MIDDLEWARE ────────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # right after SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ── URLS ──────────────────────────────────────────────────────────────────────
ROOT_URLCONF = 'azani.urls'

# ── TEMPLATES ─────────────────────────────────────────────────────────────────
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'core' / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]
    },
}]

WSGI_APPLICATION = 'azani.wsgi.application'

# ── DATABASE ──────────────────────────────────────────────────────────────────
# Falls back to local SQLite when DATABASE_URL is not set (local dev)
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', f'sqlite:///{BASE_DIR / "azani_ispo.db"}'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# ── INTERNATIONALISATION ──────────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Nairobi'
USE_I18N = True
USE_TZ = True

# ── STATIC FILES (WhiteNoise serves them on both Render & Vercel) ─────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'core' / 'static']

# STORAGES replaces the deprecated STATICFILES_STORAGE (Django 4.2+)
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# ── DEFAULT PK ────────────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── AZANI BUSINESS CONSTANTS ──────────────────────────────────────────────────
REGISTRATION_FEE  = Decimal('8500.00')
INSTALLATION_FEE  = Decimal('10000.00')
PC_UNIT_COST      = Decimal('40000.00')
UPGRADE_DISCOUNT  = Decimal('0.10')
OVERDUE_FINE_RATE = Decimal('0.15')
RECONNECTION_FEE  = Decimal('1000.00')

BANDWIDTH_COSTS = {
    4:  Decimal('1200.00'),
    10: Decimal('2000.00'),
    20: Decimal('3500.00'),
    25: Decimal('4000.00'),
    50: Decimal('7000.00'),
}
