from django import forms
from .models import Post

#'PostForm' can be whatever I want
class PostForm(forms.ModelForm):
    # This HAS TO BE 'Meta'
    class Meta:
        #this HAS to be 'model' AND fields so it knows which class/model to make (like a template)
        model = Post 
        fields = ('title', 'text',)