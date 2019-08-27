from django.shortcuts import render
from rest_framework import viewsets

from todos.models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('completed', '-created_date')
    serializer_class = TodoSerializer