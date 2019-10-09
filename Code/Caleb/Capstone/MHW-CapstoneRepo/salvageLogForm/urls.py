from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'salvageLogForm' # for namespacing
urlpatterns = [
    path('salvageLogForm/', views.salvageLogForm, name='salvageLogForm'),
    path('PersonalContactInfoForm/', views.contactUsForm, name='personalInfoForm'),
    path('', TemplateView.as_view(template_name='ContactUsforms/ContactUsForm.html'), name='ContactUsForm')
]