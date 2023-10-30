from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields, TextInput, PasswordInput

from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']





class RegistroForm(UserCreationForm):
    email = fields.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo válida.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class InicioSesionForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']




class InicioSesionForm(AuthenticationForm):
    pass
    # username = fields.CharField(widget=TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    # password = fields.CharField(widget=PasswordInput(attrs={'placeholder': 'Contraseña'}))