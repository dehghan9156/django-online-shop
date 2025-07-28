from django.forms.models import ModelForm
from django import forms
from .models import Product


class ProductCreateUpdateForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ["category","name","color","price","quantity","discount","image"]
        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'discount': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 100,
                'step': 0.1,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            })
        }