from django import forms
from .models import Product
import re


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre del producto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa la descripción del producto'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el precio (00.00)'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona la categoría'}),
        }
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'category': 'Categoría',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 50:
            raise forms.ValidationError("El nombre debe tener menos de 50 caracteres.")
        if re.search(r'[!@#$%^&*(),._?":{}|<>]', name):
            raise forms.ValidationError("El nombre no puede contener caracteres especiales.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 100:
            raise forms.ValidationError("La descripción debe tener menos de 100 caracteres.")
        if re.search(r'[!@#$%^&*(),._?":{}|<>]', description):
            raise forms.ValidationError("La descripción no puede contener caracteres especiales.")
        return description

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre del producto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa la descripción del producto'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el precio (00.00)'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Selecciona la categoría'}),
        }
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'category': 'Categoría',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 50:
            raise forms.ValidationError("El nombre debe tener menos de 50 caracteres.")
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', name):
            raise forms.ValidationError("La descripción no puede contener caracteres especiales.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 100:
            raise forms.ValidationError("La descripción debe tener menos de 100 caracteres.")
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', description):
            raise forms.ValidationError("La descripción no puede contener caracteres especiales.")
        return description


