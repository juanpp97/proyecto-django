from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from allauth.forms import CustomUserCreationForm

class RegistroView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/registro.html'
    success_url = reverse_lazy('index')  # Redirige a la página de inicio después del registro

    def form_valid(self, form):
        # Este método se llama cuando el formulario es válido, antes de guardar el usuario
        # Aquí puedes realizar acciones adicionales si es necesario
        response = super().form_valid(form)
        login(self.request, self.object)  # Inicia sesión al usuario después del registro
        return response

class CustomLoginView(LoginView):
    template_name = 'accounts/custom_login.html'
    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
class CombinedRegistrationLoginView(TemplateView):
    template_name = 'accounts/combined_registration_login.html'
    extra_context = {
            'login_form': UserCreationForm,
            'registration_form': UserCreationForm,
            }
