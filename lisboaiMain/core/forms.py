from django import forms
from django.forms import ModelForm
from lisboaiMain.core.models import Post



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['name', 'email','message',]


