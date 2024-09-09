from django.forms import ModelForm
from .models import Booking, User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
    
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        exclude = ('user',)
        fields = '__all__'
