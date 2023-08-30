from django import forms
from .models import Customer
from .models import Trainer

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['username', 'password', 'full_name', 'dob', 'gender', 'email', 'phone_number', 'profile_picture']

class TrainerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:      
        model = Trainer
        fields = ['username','password','full_name', 'dob', 'gender', 'email', 'speciality', 'hourly_rate', 'phone_number', 'profile_picture'] 



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
