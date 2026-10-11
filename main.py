"""
В терминале
1. django-admin startproject koytus-shop .
2. python manage.py migrate

Для создание суперадмина
python manage.py createsuperuser

Команда для запуска проекта(terminal)
python manage.py runserver


Создание приложение в джанго
1. python manage.py startapp koytus_products
2. Саздем папку templates где будем хранить html файлы, в файле settings.py добавляем нашу папку
"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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
"
3. 





"""


