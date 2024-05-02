from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre del producto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa la descripción del producto'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el precio (00.00)'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccona la categoría'}),
        }
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'price': 'Precio',
            'category': 'Categoría',
        }
