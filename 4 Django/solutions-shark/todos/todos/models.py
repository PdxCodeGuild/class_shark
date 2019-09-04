from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    text = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text