from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from django.forms import fields, PasswordInput
from django.utils.translation import gettext_lazy as _


class RegistroForm(UserCreationForm):
    password1 = fields.CharField(
        label= _("Password"),
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Ingresa una contraseña segura."
    )
    password2 = fields.CharField(
        label=_("Password confirmation"),
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Confirma tu contraseña."),
    )


class InicioSesionForm(AuthenticationForm):
    pass
