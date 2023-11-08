from django import forms
from django.forms import ValidationError 
from dateutil.relativedelta import relativedelta
from re import match
from .models import RoomView, RoomImg, RoomType, Price
from os import path

default_errors = {
    'required': 'Este campo es obligatorio',
    'invalid': 'El dato ingresado es inválido',
    'max_length': 'Se superó el número máximo de caracteres',
    'min_length': 'Ha ingresado muy pocos caracteres',
}


class RoomForm(forms.ModelForm):
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
    class Meta:
        model = Price
        fields = ['date_from', 'date_to', 'price']
        widgets = {
            'date_from': forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
            'date_to': forms.DateInput(attrs={"class": "form-control", "type": "date"}), 
            'price': forms.TextInput(attrs={"class": 'form-control'})

        }
        error_messages = {
            'date_from': default_errors, 
            'date_to': default_errors, 
            'price': default_errors
            }
    def clean_price(self):
        if self.cleaned_data["price"] < 0:
            raise ValidationError("El valor ingresado no es válido")
        return self.cleaned_data["price"]
    
    def clean_date_to(self):
        if self.cleaned_data["date_to"] < self.cleaned_data["date_from"]:
            raise ValidationError("La fecha ingresada debe ser mayor a \"Desde\"")
        return self.cleaned_data["date_to"]