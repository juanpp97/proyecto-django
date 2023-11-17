from django import forms
from django.forms import ValidationError 
from dateutil.relativedelta import relativedelta
from re import match
# Autenticación
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields, PasswordInput
from django.utils.translation import gettext_lazy

#Sobreescribo los mensajes de error por defecto del form
default_errors = {
    'required': 'Este campo es obligatorio',
    'invalid': 'El dato ingresado es inválido',
    'max_length': 'Se superó el número máximo de caracteres',
    'min_length': 'Ha ingresado muy pocos caracteres',
}

choices = (('frente', 'Frente'), ('playa', 'Playa'))


class ReservationForm(forms.Form):
    id_hab = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'hidden'}), 
        error_messages=default_errors
        )

    num_people = forms.IntegerField(
        label="Número de personas", 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'value': 1}), 
        error_messages=default_errors
        )

    room_view = forms.CharField(
        label="Vista", 
        widget=forms.Select(attrs={'class': 'form-select'}, choices=choices), 
        error_messages=default_errors
        )

    date_in = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
        label="Fecha de Ingreso", 
        error_messages=default_errors
        )

    date_out = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
        label="Fecha de Salida", 
        error_messages=default_errors
        )

    comments = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'comment form-control', 'rows': '4'}), 
        label="Comentarios", 
        max_length=1000, 
        error_messages=default_errors, 
        required=False
        )

    def clean_id_hab(self):
        data = self.cleaned_data["id_hab"]
        if data != self.fields["id_hab"].widget.attrs["value"]:
            raise ValidationError("Tipo de habitación no válido")
        return data
    
    def clean_num_people(self):
        data = self.cleaned_data["num_people"]
        min = self.fields["num_people"].widget.attrs["min"]
        max = self.fields["num_people"].widget.attrs["max"]
        if data < min or data > max:
            raise ValidationError("El número ingresado no es válido")
        return data
    
    def clean_room_view(self):
        data = self.cleaned_data["room_view"]
        if not any(data == choice[0] for choice in self.fields['room_view'].widget.choices):
            raise ValidationError("Se seleccionó una opción no válida")
        return data

    def clean_date_in(self):
        data = self.cleaned_data["date_in"]
        min_date = self.fields["date_in"].widget.attrs["min"]
        max_date = self.fields["date_in"].widget.attrs["max"]
        if data > max_date or data < min_date:
            raise ValidationError("La fecha seleccionada es inválida")
        return data
    
    def clean_date_out(self):
        data = self.cleaned_data["date_out"]
        date_in = self.cleaned_data["date_in"]
        if data <= date_in or data > (date_in + relativedelta(months=2)):
            raise ValidationError("Fecha de Salida no válida")
        return data
    
    def clean_comments(self):
        data = self.cleaned_data["comments"]
        if len(data) > self.fields["comments"].max_length:
            raise ValidationError("Se supero el número máximo de caracteres")
        
    def __init__(self, *args, **kwargs):
        id_hab = kwargs.pop("id_hab", None)
        capacity = kwargs.pop("capacity", None)
        room_view = kwargs.pop("room_view", None)
        min_date_in = kwargs.pop("min_date_in", None)
        max_date_in = kwargs.pop("max_date_in", None)
        
        super(ReservationForm, self).__init__(*args, **kwargs)
        if id_hab:
            self.fields['id_hab'].widget.attrs['value'] = id_hab

        if capacity:
            self.fields['num_people'].widget.attrs['max'] = capacity

        if room_view:
            self.fields['room_view'].widget.choices = ((room_view.lower(), room_view),)
            self.fields['room_view'].widget.attrs['readonly'] = True

        if max_date_in and min_date_in:
            self.fields['date_in'].widget.attrs['max'] = max_date_in
            self.fields['date_in'].widget.attrs['min'] = min_date_in
            
def alfabetico(data):
    reg_exp = r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$'
    if not match(reg_exp, data):
        raise ValidationError('El campo solo puede contener letras ')


class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        required=True,
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'}),
        error_messages=default_errors,
        validators = (alfabetico, )
        )
    apellido = forms.CharField(
        max_length=100,
        required=True,
        label="Apellido",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu apellido'}),
        error_messages=default_errors,
        validators = (alfabetico, )
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu correo electrónico'}),
        error_messages=default_errors
    )
    comentario = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu comentario aquí', 'rows': 4}),
        required=True,
        max_length=1000,
        label="Comentario",
        error_messages=default_errors
    )
    def clean_email(self):
        data = self.cleaned_data["email"]
        reg_exp = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not match(reg_exp, data):
            raise ValidationError('El correo ingresado no es válido')
        return data
    

class RegistroForm(UserCreationForm):
    password1 = fields.CharField(
        label= gettext_lazy("Password"),
        strip=False,
        widget=PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Ingresa una contraseña segura"
    )
    password2 = fields.CharField(
        label = gettext_lazy("Password confirmation"),
        widget = PasswordInput(attrs={"autocomplete": "new-password"}),
        strip = False,
        help_text = gettext_lazy("Confirma tu contraseña"),
    )


class InicioSesionForm(AuthenticationForm):
    pass
