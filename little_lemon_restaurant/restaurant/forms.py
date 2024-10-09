from django.forms import ModelForm
from .models import Booking, User
from django import forms

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ('user',)
        fields = '__all__'
        widgets = {
            'bookingDate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }
