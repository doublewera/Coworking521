from django.shortcuts import render

def index(request):
    return render(  # Функция "рендерит" шаблон - наполняет данными шаблон html страницы
        request,                 # так всегда
        'mainpage/index.html',   # путь к шаблону после templates 
    )
