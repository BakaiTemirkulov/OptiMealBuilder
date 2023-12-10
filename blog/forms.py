from django import forms
from . import models

class FoodForm(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = "__all__"

