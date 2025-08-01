# Магазин мебели

## Описание
Учебный проект. Сервис, представляющий собой магазин мебели, с возможностью просмотра каталога товаров, просмотра карточек товара, регистрации и авторизации пользователей, добавления товаров в корзину, просмотр товаров в корзине, очищения корзины.

## Требования
* Python 3.12+
* Git
* PostgreSQL
## Работа с проектом
* Создайте рабочую папку и в ней выполните команду: git clone https://github.com/Olga-who/Django_project.git
* Спуститься в папку Django_project - cd Django_project
* Создание  и активация виртуального окружения:
* * python -m venv venv
  * source venv/bin/activate  # для Linux/MacOS
  * venv\Scripts\activate     # для Windows
* Установка зависимостей - pip install -r requirements.txt
* Настройка PostgreSQL - создание базы данных, я использовала PgAdmin, обновить файл settings.py (путь app1/app/settings.py) с вашими параметрами
* Создание миграций - py manage.py makemigrations
* Применение миграции - py manage.py migrate
* Создание суперюзера - py manage.py createsuperuser
## Запуск сервиса 
* Выполнить команду - py manage.py runserver
