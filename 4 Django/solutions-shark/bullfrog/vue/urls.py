from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from . import views

# register drf viewsets
router = routers.DefaultRouter()
router.register(r'blogposts', views.BlogpostViewSet, 'blogpost')

app_name = 'vue'
urlpatterns = [
    path('', TemplateView.as_view(template_name='vue/index.html'), name='index'),
    path('api/', include(router.urls), name='api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]