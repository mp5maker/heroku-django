# Django #

    pip install django-admin
    pip install virtualenvwrapper
    pip install autopep8
    pip install pyling
    pip install pipenv
    mkvirtualenv django-tutorial
    workon django-tutorial
    django-admin startapp simpleapp

    cd simpleapp
    python manage.py migrate

    user: user
    email: user@gmail.com
    password: test1234

    python manage.py runserver
    python manage.py startapp pages

    os.path.join(BASE_DIR, 'templates')

### page.views ###

    from django.shortcuts import render
    from django.http import HttpResponse
    from django.views.generic import TemplateView


### page.urls ###

    from django.urls import path

### pages.test ###

    from django.test import SimpleTestCase
    python manage.py test

### config.urls ###

    from django.urls import include

### config.settings ###

    import django_heroku
    INSTALLED_APPS = [ ..., 'pages' ]
    TEMPLATES = [
        {
            'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
            ...
        },
    ]
    MIDDLEWARE_CLASSES = (
        'whitenoise.middleware.WhiteNoiseMiddleware',
        ...
    )
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    STATIC_URL = '/static/'
    django_heroku.settings(locals())

### Root ###

    pipenv lock
    pip freeze > requirements.txt
    touch Procfile

        web: gunicorn config.wsgi --log-file -

    pipenv install gunicorn
    pip install whitenoise
    pip install django-heroku
    cd config
    mkdir static
    cd static
    touch .keep