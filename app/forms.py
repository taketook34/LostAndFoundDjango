from django import forms
from django.core.exceptions import ValidationError

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'photo', 'founder_contact']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

