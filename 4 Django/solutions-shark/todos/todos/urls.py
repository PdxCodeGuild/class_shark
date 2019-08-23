from django.urls import path
from django.views.generic import TemplateView

from . import controller_views

app_name = 'todos' # for namespacing
urlpatterns = [
    path('', TemplateView.as_view(template_name='todos/template_view.html'), name='index'), 
    path('weather/', TemplateView.as_view(template_name='todos/weather_app.html'), name='weather'), 
    path('api/todos/', controller_views.todos, name='todos'),
    path('api/todos/<int:pk>/', controller_views.todo, name='todo'),
]