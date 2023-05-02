from django import forms
from second_app.models import User
from django.forms import PasswordInput


class NewUserForm(forms.ModelForm):
    
    class Meta():
        model = User
        fields = '__all__'
        widgets = {
            'password': PasswordInput(),
        }
