from django import forms
from django.core.exceptions import ValidationError

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'photo', 'founder_contact']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'photo': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'founder_contact': forms.TextInput(attrs={'class': 'form-input'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-input'}),
        }


class AskForm(forms.ModelForm):
    class Meta:
        model = FeedbackMessage
        fields = ['email', 'text']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'class': 'form-input'}),
        }

