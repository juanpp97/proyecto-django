from django import forms
from django.forms import ValidationError
from datetime import date

#Sobreescribo los mensajes de error por defecto del form
default_errors = {
    'required': 'Este campo es obligatorio',
    'invalid': 'Debe ingresar un dato válido',
    'max_length': 'Se superó el número máximo de caracteres',
    'min_length': 'Ha ingresado muy pocos caracteres',
}

choices = (('frente', 'Frente'), ('playa', 'Playa'))


class ReservationForm(forms.Form):

    num_people = forms.IntegerField(label="Número de personas", widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'value': '1',}), error_messages=default_errors)

    room_view = forms.CharField(label="Vista", widget=forms.Select(attrs={'class': 'form-control'}, choices=choices), error_messages=default_errors)

    date_in = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "max": "2023-12-31"}), label="Fecha: ", error_messages=default_errors)


    def clean_num_people(self):
        num_people = self.cleaned_data["num_people"]
        min = self.fields["num_people"].widget.attrs["min"]
        max = self.fields["num_people"].widget.attrs["max"]
        if num_people < min or num_people > max:
            raise ValidationError("El número ingresado no es válido")


    def __init__(self, *args, **kwargs):
        capacity = kwargs.pop("capacity", None)
        room_view = kwargs.pop("room_view", None)
        super(ReservationForm, self).__init__(*args, **kwargs)
        if capacity:
            self.fields['room_view'].widget.attrs['max'] = capacity
        if room_view:
            self.fields['room_view'].widget.choices = capacity




        

    