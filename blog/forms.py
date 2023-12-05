from django import forms
from .models import Food

class FoodConsumedForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name']  # Добавьте другие поля, если нужно