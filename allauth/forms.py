from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']




class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class InicioSesionForm(AuthenticationForm):
    pass
