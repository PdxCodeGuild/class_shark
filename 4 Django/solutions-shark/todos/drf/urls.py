from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from . import controller_views

router = routers.DefaultRouter()
router.register(r'todos', controller_views.TodoViewSet, base_name='todo')
router.register(r'users', controller_views.UserViewSet, base_name='user')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', TemplateView.as_view(template_name='drf/template_view.html'), name='index'), 
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]