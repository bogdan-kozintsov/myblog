from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['BogdanKozintsov.pythonanywhere.com']

# Настройки базы данных для PythonAnywhere
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
