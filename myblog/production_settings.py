from .settings import *

DEBUG = False
ALLOWED_HOSTS = [
    '.pythonanywhere.com',  # точка в начале разрешает все поддомены
    'localhost',
    '127.0.0.1'
]

# Настройки базы данных для PythonAnywhere
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
