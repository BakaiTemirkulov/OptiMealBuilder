from django import forms
from .models import SuccessStory

class SuccessStoryForm(forms.ModelForm):
    class Meta:
        model = SuccessStory
        fields = ['user_name', 'description']

