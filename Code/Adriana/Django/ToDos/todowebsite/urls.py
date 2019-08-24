from django.urls import path
from django.views.generic import TemplateView

app_name = 'todowebsite' # for namespacing
urlpatterns = [
    path('', TemplateView.as_view(template_name='todowebsite/template_view.html', name='index')),
    path('weather/', TemplateView.as_view(template_name='todowebsite/weather_app.html', name='weather')),
]