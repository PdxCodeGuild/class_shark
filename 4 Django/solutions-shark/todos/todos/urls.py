from django.urls import path
from django.views.generic import TemplateView

from . import controller_views

app_name = 'todos' # for namespacing
urlpatterns = [
    path('', TemplateView.as_view(template_name='todos/template_view.html')), 
]