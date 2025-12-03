# Глобальный конфигурационный файл путей проекта

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainpage.urls')),  # те пути, которые прописаны в mainpage/urls.py
    path('admin/', admin.site.urls),     # сразу после IP и порта - admin  127.0.0.1:8000/admin/
]
