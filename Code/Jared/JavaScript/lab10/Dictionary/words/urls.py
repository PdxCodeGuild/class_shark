from django.urls import path
from . import views

app_name = 'words'
urlpatterns = [
	path('', views.dictionary, name='dictionary'),
	path('api_keys/', views.api_keys, name='api_keys'),
]