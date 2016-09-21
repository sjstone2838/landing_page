# run with: python manage.py runserver --settings=platform.settings.local

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# serve static files (e.g. js locally)
# so that collecstatic does not need to be run
# each time a .js file is edited
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    'static/',
)
