#!/usr/bin/env python
"""Файл запуска сайта и выполнения административных задач Django."""
import os

def main():
    """Главная функция, передающая управление Django:
    runserver          запустить веб-сервер разработчика
    startapp           создать новое приложение
    createsuperuser    создать суперпользователя (нужна БД!)
    makemigrations
    migrate
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coworking.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Не могу импортировать Django. Возможно, Вы забыли'
            'активировать среду. Для этого перейдите в папку проекта'
            'cd Coworking521'
            'И выполните активацию среды:'
            'py -m pipenv shell  # Для Windows'
            'python3 -m pipenv shell  # Для MacOS'
        ) from exc
    execute_from_command_line(os.sys.argv)


if __name__ == '__main__':
    main()
