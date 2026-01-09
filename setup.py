#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script Perbaikan Final Django Profile
Jalankan dengan: python final_fix.py
"""

import os

print("=" * 50)
print("  PERBAIKAN FINAL")
print("=" * 50)
print()

# 1. Perbaiki profile/apps.py
print("🔧 Memperbaiki apps.py...")
apps_content = """from django.apps import AppConfig


class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile'
"""

with open("profile/apps.py", "w", encoding="utf-8") as f:
    f.write(apps_content)

print("✅ apps.py diperbaiki!")

# 2. Perbaiki settings.py
print("🔧 Memperbaiki settings.py...")
settings_content = """from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-ganti-key-ini-di-production-12345678'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'profile',
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

ROOT_URLCONF = 'myprofile.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'myprofile.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'id-id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'profile' / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
"""

with open("myprofile/settings.py", "w", encoding="utf-8") as f:
    f.write(settings_content)

print("✅ settings.py diperbaiki!")

# 3. Migrasi database
print()
print("🗄️  Melakukan migrasi database...")
os.system("venv\\Scripts\\python manage.py migrate")

print()
print("=" * 50)
print("✅ PERBAIKAN SELESAI!")
print("=" * 50)
print()
print("🚀 Sekarang jalankan:")
print("   venv\\Scripts\\python manage.py runserver")
print()
print("🌐 Buka browser: http://127.0.0.1:8000/")
print("=" * 50)