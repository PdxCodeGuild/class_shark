from django.contrib import admin
from .models import Post

"""
needs to register models to the admin page
"""
admin.site.register(Post)