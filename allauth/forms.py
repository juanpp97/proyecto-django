from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form
class CustomUserCreationForm(UserCreationForm):
    # Agrega campos personalizados si es necesario
    class Meta:
        model = User
        fields = ['username']

#class CustomUserCreationFormm(UserCreationForm):
    # Agrega campos personalizados si es necesario
 #   class Meta:
  #      model = User
   #     fields = ['username','password']
