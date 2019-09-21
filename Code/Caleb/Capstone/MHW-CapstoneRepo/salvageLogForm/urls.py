from django.urls import path
from . import views

app_name = 'salvageLogForm' # for namespacing
urlpatterns = [
    path('salvageLogForm/', views.salvageLogForm, name='salvageLogForm')
]