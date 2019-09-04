from django.shortcuts import render
from rest_framework import viewsets

from django.contrib.auth.models import User
from todos.models import Todo
from .serializers import TodoSerializer, UserSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    """
    serializer_class = TodoSerializer

    def get_queryset(self):
        # defines what is returned when you send a GET request to this API endpoint        
        return Todo.objects.filter(owner=self.request.user).order_by('completed', '-created_date')

    def perform_create(self, serializer):
        # defines what is returned when you send a POST request to this API endpoint        
        return serializer.save(owner=self.request.user)        

    # def perform_update(self, serializer):
    #     # defines what is done when you send a PUT/PATCH request to this endpoint        
    #     serializer.save()

    # def perform_destroy(self, instance):
    #     # defines what is done when you send a DELETE request to this endpoint        
    #     instance.delete()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that displays users and their todos.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        # defines what is returned when you send a GET request to this API endpoint
        return User.objects.filter(username=self.request.user.username)