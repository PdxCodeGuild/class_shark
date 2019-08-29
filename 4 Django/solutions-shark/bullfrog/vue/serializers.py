from rest_framework import serializers 
from django.contrib.auth.models import User
from blog.models import *

class BlogpostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='vue:blogpost-detail'
    )    
    author = serializers.PrimaryKeyRelatedField(read_only=True, source='author.username')

    class Meta:
        model = Post
        fields = ['url', 'author', 'title', 'text', 'created_date', 'published_date']