from django.contrib import admin
from django.urls import path, include
from . import controller_views

urlpatterns = [
    path('', include('blog.urls')),
    path('vue/', include('vue.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', controller_views.signup, name='signup'),
    # path('accounts/signup/', controller_views.SignUp.as_view(), name='signup')
]