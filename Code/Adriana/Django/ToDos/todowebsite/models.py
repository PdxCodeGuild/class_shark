from django.db import models
from django.utils import timezone

class ToDo(models.Model):
    text = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now())
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text