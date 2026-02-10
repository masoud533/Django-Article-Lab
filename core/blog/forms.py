from django import forms
from .models import Post

class CreatePost(forms.ModelForm):
    

    class Meta:
        model = Post
        fields = ['author','title','content', 'status', 'published_date']