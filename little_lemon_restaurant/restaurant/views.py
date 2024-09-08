from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import menuSerializer, bookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import UserForm
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.
def home(req):
    return render(req, 'home.html', {})

def sign_up(req):
    return render(req, 'signup.html', {'form': UserForm})

def logout(req):
    if req.user.is_authenticated:
        auth.logout(req)
        return render(req, 'registration/logout.html')
    else:
        return redirect('home')

class menuItemsView(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu.html'
    def get(self, req):
        queryset = Menu.objects.all()
        serialized_menu = menuSerializer(queryset, many=True)
        return Response({'menu': serialized_menu.data})

class singleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

# User should only see own bookings 
class view_all_create_bookings(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'booking.html'
    def get(self, req):
        queryset = Booking.objects.all()
        serialized_booking = bookingSerializer(queryset, many=True)
        return Response({'bookings': serialized_booking.data})

class single_booking_two(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer


