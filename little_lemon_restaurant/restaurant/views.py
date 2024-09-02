from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import menuSerializer, bookingSerializer
# from rest_framework.authentication import 

# Create your views here.
def index(req):
    return render(req, 'index.html', {})

class menuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class singleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class booking_two(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

class single_booking_two(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
