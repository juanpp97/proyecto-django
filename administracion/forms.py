from typing import Any
from django import forms
from django.forms import ValidationError 
from dateutil.relativedelta import relativedelta
from re import match
from .models import RoomView, RoomImg, RoomType, Price, Room
from os import path

default_errors = {
    'required': 'Este campo es obligatorio',
    'invalid': 'El dato ingresado es inválido',
    'max_length': 'Se superó el número máximo de caracteres',
    'min_length': 'Ha ingresado muy pocos caracteres',
}


class RoomTypeForm(forms.ModelForm):
    view = forms.ModelMultipleChoiceField(queryset=RoomView.objects.all(), widget=forms.CheckboxSelectMultiple(), error_messages = default_errors, label="Vista de la habitacion")
    
    imgs = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True}), required=False, label="Imagenes de la habitacion")
    
    imgs_delete = forms.ModelMultipleChoiceField(queryset=RoomImg.objects.none(), widget = forms.CheckboxSelectMultiple(), error_messages = default_errors, required = False, label="Seleccione la imagen que quiera eliminar")
    
    class Meta:
        model = RoomType
        fields = ['name', 'capacity', 'view', 'num_beds']
        widgets  = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Habitación Doble'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Ingrese un número'}),
            'num_beds': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1 cama simple - 1 cama doble'})
        }
        error_messages  = {
            'name': default_errors,
            'capacity': default_errors,
            'num_beds': default_errors,
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if RoomImg.objects.filter(room = self.instance):
            self.fields["imgs_delete"].queryset = RoomImg.objects.filter(room = self.instance)
        else:
            del self.fields["imgs_delete"]
    def clean_name(self):
        if not all(char.isalpha() or char.isspace() for char in self.cleaned_data["name"]):
            raise ValidationError("El nombre ingresado no es correcto")
        
        if RoomType.objects.exclude(name = self.instance.name).filter(name__icontains = self.cleaned_data["name"]).exists():
            raise ValidationError("La habitación ingresada ya existe en la base de datos")
        
        return self.cleaned_data["name"]
    
    def clean_capacity(self):
        if self.cleaned_data["capacity"] <= 0:
            raise ValidationError("El número no puede ser menor a 0")
        return self.cleaned_data["capacity"]


class RoomViewForm(forms.ModelForm):
    class Meta:
        model = RoomView
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            'name': default_errors
        }
    def clean_name(self):
        if not all(char.isalpha() or char.isspace() for char in self.cleaned_data["name"]):
            raise ValidationError("El nombre ingresado no es correcto")
        
        if RoomView.objects.exclude(name = self.instance.name).filter(name__icontains = self.cleaned_data["name"]).exists():
            raise ValidationError("La vista ingresada ya existe en la base de datos")
        return self.cleaned_data["name"]

class PriceForm(forms.ModelForm):
    room_type = forms.ModelChoiceField(widget=forms.Select(attrs={"class": 'form-select'}), label='Tipo de Habitación', queryset=RoomType.objects.all())
    room_view = forms.ModelChoiceField(widget=forms.Select(attrs={"class": 'form-select'}), queryset=RoomView.objects.all(), label="Vista de la habitación")

    class Meta:
        model = Price
        fields = ['date_from', 'date_to', 'price', 'room_type', 'room_view']
        widgets = {
            'date_from': forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
            'date_to': forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
            'price': forms.TextInput(attrs={"class": 'form-control'}),

        }
        error_messages = {
            'date_from': default_errors, 
            'date_to': default_errors, 
            'price': default_errors,
            'room_type': default_errors,
            'room_view': default_errors,

            }
    def clean_price(self):
        if self.cleaned_data["price"] < 0:
            raise ValidationError("El valor ingresado no es válido")
        return self.cleaned_data["price"]
    

    def clean(self):
        if self.cleaned_data["date_to"] < self.cleaned_data["date_from"]:
            self.add_error('date_to', f'La fecha ingresada debe ser mayor a "Desde"')
            raise ValidationError("La fecha ingresada debe ser mayor a \"Desde\"")
        
        prices = Price.objects.filter(room_type = self.cleaned_data["room_type"], room_view = self.cleaned_data["room_view"]).exclude(date_from = self.instance.date_from, date_to = self.instance.date_to, price = self.instance.price)
        date_from = self.cleaned_data["date_from"]
        date_to = self.cleaned_data["date_to"] 
        
        for price in prices:
            if(price.date_from <= date_to <= price.date_to) or (price.date_from <= date_from <= price.date_to) or (date_from <= price.date_from and date_to >= price.date_to):
                self.add_error(None, f'Rango de fecha inválido. Rango superpuesto: {price.date_from.strftime("%d/%m/%Y")} a {price.date_to.strftime("%d/%m/%Y")}')
                raise ValidationError("")
        if not RoomType.objects.filter(name = self.cleaned_data["room_type"].name, view = self.cleaned_data["room_view"]).exists():
            self.add_error('room_view', f'La vista seleccionada no corresponde a la habitación')

        return super().clean()
    
    def __init__(self, *args, **kwargs):
        super(PriceForm, self).__init__(*args, **kwargs)
        self.fields['room_type'].label_from_instance = lambda obj: f"{obj.name}"


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name}"

class RoomForm(forms.ModelForm):
    type = MyModelChoiceField(widget=forms.Select(attrs={"class": 'form-select'}), label='Tipo de Habitación', queryset=RoomType.objects.all())
    view = MyModelChoiceField(widget=forms.Select(attrs={"class": 'form-select'}), queryset=RoomView.objects.all(), label="Vista de la habitación")

    class Meta:
        model = Room
        fields = ['number', 'status', 'type', 'view']
        widgets = {
            'number': forms.TextInput(attrs={"class": "form-control"}), 
            'status': forms.Select(attrs={"class": "form-select"}), 

        }
        error_messages = {
            'number': default_errors, 
            'status': default_errors, 
            'type': default_errors,
            'view': default_errors,

            } 
    def clean_number(self):
        if Room.objects.filter(number = self.cleaned_data["number"]).exclude(number = self.instance.number).exists():
            raise ValidationError("Ese número de habitación ya existe")
        return self.cleaned_data["number"]
    def clean(self):
        if not RoomType.objects.filter(name = self.cleaned_data["type"].name, view = self.cleaned_data["view"]).exists():
            self.add_error('view', f'La vista seleccionada no corresponde a la habitación')

        return super().clean()
