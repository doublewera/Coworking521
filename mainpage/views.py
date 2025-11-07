from django.shortcuts import render

def index(request):
    context = {
        'admin_today': 'Вася'  # Позже эти данные можно взять из БД
    }
    return render(  # Функция "рендерит" шаблон - наполняет данными шаблон html страницы
        request,                 # так всегда
        'mainpage/index.html',   # путь к шаблону после templates 
        context
    )
