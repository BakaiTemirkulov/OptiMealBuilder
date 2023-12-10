from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Enter your email')
    def save(self, commit=True):
        user = super(CustomUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user