from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Todo
import json

def todos(request):
    '''
    api endpoint for todos
    '''
    # create a new todo from request.body
    if request.method == 'POST':
        # deserialize json string
        data = json.loads(request.body)
        # data = {'text': 'new todo'}
        todo = Todo(text=data['text'])
        # todo = Todo(**todo) # same as above
        todo.save()
        return HttpResponse(status=201)        

    todos = Todo.objects.all().order_by('-created_date')
    todo_list = []
    for todo in todos:
        todo_dict = {
            'pk': todo.pk,
            'text': todo.text,
            'completed': todo.completed,
            'created_date': todo.created_date,
            'completed_date': todo.completed_date
        }
        todo_list.append(todo_dict)

    return JsonResponse(todo_list, safe=False)

def todo(request, pk):
    '''
    api endpoint for todos
    '''
    # todo = Todo.objects.get(pk=pk)
    todo = get_object_or_404(Todo, pk=pk)

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