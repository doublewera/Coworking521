# Локальный диспетчер путей приложения mainpage
from django.urls import path

from . import views
urlpatterns = [
    # Путь в браузере: пустой, потому что главная страница
    # Функция: index, потому что именно её мы научили рендерить нужный для главной страницы шаблон
    path('',       views.index),
    path('tasks/', views.show_tasks),    # 127.0.0.1:8000/tasks/ - вызов функции show_tasks
]