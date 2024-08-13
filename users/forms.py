from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = True  
        if commit:
            user.save()
        return user

class UserEditForm(UserChangeForm):
    password = None 
    first_name = forms.CharField(label="Nombre:")
    last_name = forms.CharField(label="Apellido:")
    email = forms.EmailField(label="Email:")
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "imagen"]
