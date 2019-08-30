from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Todo
import json


def todos(request):
    '''
    api endpoint for todos
    '''
    # check if user is logged in
    if request.user.is_authenticated:
        # create a new todo from request.body
        if request.method == 'POST':
            # deserialize json string
            data = json.loads(request.body)
            # set owner as request.user
            todo = Todo(text=data['text'], owner=request.user) 
            todo.save()
            return HttpResponse(status=201)        

        # filter by todos by user
        todos = Todo.objects.filter(owner=request.user).order_by('completed', '-created_date')
        todo_list = []
        for todo in todos:
            todo_dict = {
                'pk': todo.pk,
                'owner': todo.owner.username,
                'text': todo.text,
                'completed': todo.completed,
                'created_date': todo.created_date,
                'completed_date': todo.completed_date
            }
            todo_list.append(todo_dict)
        return JsonResponse(todo_list, safe=False)
    # give client not authorized error if user is not logged in
    return HttpResponse('User not authenticated', status=401)

def todo(request, pk):
    '''
    api endpoint for todos
    '''
    # check if user is logged in
    if request.user.is_authenticated:    
        # todo = Todo.objects.get(pk=pk)
        # query todo by pk and check if the owner is request.user
        todo = get_object_or_404(Todo, pk=pk)
        if todo.owner != request.user:
            return HttpResponse(status=401)
        # todo = get_object_or_404(Todo, pk=pk, owner=request.user)

        if request.method == 'DELETE':
            todo.delete()
            return HttpResponse(status=204)

        if request.method == 'PUT':
            data = json.loads(request.body)
            todo.text = data['text']
            todo.completed = data['completed']
            todo.completed_date = data['completed_date']
            todo.save()
            return HttpResponse(status=204)    

        if request.method == 'PATCH':
            # using kwargs
            todo = Todo.objects.filter(pk=pk)
            data = json.loads(request.body)
            todo.update(**data)
            todo.first().save()
            return HttpResponse(status=204)    

        # get single todo
        todo_dict = {
            'pk': todo.pk,
            'text': todo.text,
            'completed': todo.completed,
            'created_date': todo.created_date,
            'completed_date': todo.completed_date
        } 
        return JsonResponse(todo_dict)

    # give client not authorized error if user is not logged in
    return HttpResponse('User not authenticated', status=401)        