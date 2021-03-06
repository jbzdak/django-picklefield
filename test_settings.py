SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        }
}

DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = ':memory:'

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.admin',
    'picklefield',
    ]

SECRET_KEY = 'local'
