from rest_framework import viewsets
from django.contrib.auth.models import User
from blog.models import *
from .serializers import *
import json

class BlogpostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blogposts to be viewed or edited.
    """    
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = BlogpostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)