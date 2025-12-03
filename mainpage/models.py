from django.db import models

class Task(models.Model):
    # id создается автоматически
    dt = models.DateTimeField(auto_now=True, null=True)
    deadline = models.DateTimeField()
    description = models.CharField(max_length=1024)
    done = models.BooleanField(default=False)
