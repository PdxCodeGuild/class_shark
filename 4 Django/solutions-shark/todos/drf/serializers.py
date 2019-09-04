from rest_framework import serializers

from django.contrib.auth.models import User
from todos.models import Todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.StringRelatedField() # you need to specify related fields
    class Meta:
        model = Todo
        fields = ('url', 'owner', 'text','completed','created_date','completed_date')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # this adds an array of todos into our user api endpoint
    todos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='todo-detail')
    class Meta:
        model = User
        fields = ('username', 'todos')