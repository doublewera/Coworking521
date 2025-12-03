from django.contrib import admin

from . import models

@admin.register(models.Task)
class AdminTask(admin.ModelAdmin):
    list_display = [
        'description',
        'deadline',
        'done',
    ]
