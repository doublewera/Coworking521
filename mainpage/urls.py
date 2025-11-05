# Локальный диспетчер путей приложения mainpage
from django.urls import path

from . import views
urlpatterns = [
    # Путь: пустой, потому что главная страница
    # Функция: index, потому что именно её мы научили рендерить нужный для главной страницы шаблон
    path('', views.index),
]