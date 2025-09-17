DEBUG = True  # Временно включаем DEBUG
ALLOWED_HOSTS = ['BogdanKozintsov.pythonanywhere.com', 'localhost', '127.0.0.1']

# Включим логирование
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/BogdanKozintsov/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}