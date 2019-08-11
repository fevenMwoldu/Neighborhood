from django import forms
from .models import Neighbourhood, CustomUser, Bussiness, Post

'''
   Form for the Custom user
'''
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['user']

'''
   Form for the Neighbourhood
'''

class NeighbourhoodForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


'''
   Form for Posting of events or anythng else
'''

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['neighbourhood', 'created_by']


'''
   Form for Adding bussinesesses
'''

class BussinessForm(forms.ModelForm):
    class Meta:
        model = Bussiness
        exclude = ['neighbourhood']

'''
   Form for changing Neighbourhood
'''
class ChangeNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['first_name', 'last_name', 'bio', 'profile_pic', 'user']

 
