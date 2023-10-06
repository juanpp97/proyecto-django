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
    id_hab = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'hidden'}), error_messages=default_errors)

    num_people = forms.IntegerField(label="Número de personas", widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'value': 1}), error_messages=default_errors)

    room_view = forms.CharField(label="Vista", widget=forms.Select(attrs={'class': 'form-control'}, choices=choices), error_messages=default_errors)

    date_in = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), label="Fecha de Ingreso", error_messages=default_errors)

    date_out = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), label="Fecha de Salida", error_messages=default_errors)

    def clean_id_hab(self):
        data = self.cleaned_data["id_hab"]
        if data != self.fields["id"].widget.attrs["value"]:
            raise ValidationError("Tipo de habitación no válido")
        
    def clean_num_people(self):
        num_people = self.cleaned_data["num_people"]
        min = self.fields["num_people"].widget.attrs["min"]
        max = self.fields["num_people"].widget.attrs["max"]
        if num_people < min or num_people > max:
            raise ValidationError("El número ingresado no es válido")


    def __init__(self, *args, **kwargs):
        id_hab = kwargs.pop("id_hab", None)
        capacity = kwargs.pop("capacity", None)
        room_view = kwargs.pop("room_view", None)
        min_date_in = kwargs.pop("min_date_in", None)
        max_date_in = kwargs.pop("max_date_in", None)
        max_date_out = kwargs.pop("max_date_out", None)
        
        super(ReservationForm, self).__init__(*args, **kwargs)
        if id_hab:
            self.fields['id_hab'].widget.attrs['value'] = id_hab
        if capacity:
            self.fields['room_view'].widget.attrs['max'] = capacity
        if room_view:
            self.fields['room_view'] = forms.CharField(label="Vista", widget=forms.TextInput(attrs={'class': 'form-control-plaintext', 'readonly': 'True', 'value': room_view}), error_messages=default_errors)
        if max_date_in and min_date_in:
            self.fields['date_in'].widget.attrs['max'] = max_date_in
            self.fields['date_in'].widget.attrs['min'] = min_date_in
            




        

    