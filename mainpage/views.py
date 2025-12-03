from django.shortcuts import render
from . import models

def index(request):
    context = {
        'all_admins': [
            {
                'name': 'Вася',  # Позже эти данные можно взять из БД
                'age': 25,
            },
            {
                'name': 'Ася',
                'age': 32,
            }
        ]
    }
    return render(  # Функция "рендерит" шаблон - наполняет данными шаблон html страницы
        request,                 # так всегда
        'mainpage/index.html',   # путь к шаблону после templates 
        context
    )

# ВЫЗОВ ЭТОЙ ФУНКЦИИ ПРОИСХОДИТ В МОМЕНТ ОБРАЩЕНИЯ ПО ПУТИ В БРАУЗЕРЕ!
def show_tasks(request):
    my_tasks = models.Task.objects.all()  # Класс, дай нам все свои объекты, хранящиеся в БД
    # это аналог select *
    # Просмотрим циклом все полученные задачи
    for t in my_tasks:
        # t - один объект класса Task! можно вывести на печать его поле!
        print(t.deadline, t.description)
    context = {
        'all_tasks': my_tasks
    }
    return render(  # создание страница сайта по шаблону
        request,
        'mainpage/task.html',
        context
    )
