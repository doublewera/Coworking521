from django.shortcuts import render

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
