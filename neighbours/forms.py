from django import forms
from .models import Neighbourhood, CustomUser, Bussiness, Post


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['user']

class NeighbourhoodForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['neighbourhood', 'created_by']


class BussinessForm(forms.ModelForm):
    class Meta:
        model = Bussiness
        exclude = ['neighbourhood', 'created_by']
