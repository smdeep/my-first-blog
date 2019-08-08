"""Forms for our Blog"""
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form for the Post Model"""
    class Meta:
        model = Post
        fields = ('title', 'text')
