from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import menuSerializer, bookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import UserForm
# from rest_framework.authentication import 

# Create your views here.
def login(req):
    return render(req, 'login.html', {})

def sign_up(req):
    return render(req, 'signup.html', {'form': UserForm})

class menuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class singleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class view_all_create_bookings(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
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


