from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu, User
from .serializers import menuSerializer, bookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import UserForm, BookingForm
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.
def home(req):
    return render(req, 'home.html', {})

def sign_up(req):
    return render(req, 'signup.html', {'form': UserForm})

def validate_sign_up(req):
    if req.method == 'POST':
        new_user = UserForm(req.POST)
        if new_user.is_valid():
            new_user.save()
            print('User has been saved')
            return redirect('/login/')

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

def booking_redirect(req):
    if req.user.is_authenticated: bookings = Booking.objects.filter(user=req.user).all()
    else: bookings = {}
    serialized_bookings = bookingSerializer(bookings, many=True)
    return render(req, 'booking.html', {'bookings': serialized_bookings.data})

class view_all_create_bookings(ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'make_booking.html'
    def get(self, req):
        return Response({'form': BookingForm})

def process_booking(req):
    print(req.POST)
    if not req.user.is_authenticated:
        post_data = {'name': req.POST['name'], 'no_of_guests': req.POST['no_of_guests'], 'bookingDate': req.POST['bookingDate']}
        print(post_data)
        #save post_data before redirecting
        return redirect(f'/login?next={req.path}&data=${post_data}', post_data=post_data)
    if req.method == 'POST':
        new_booking_form = BookingForm(req.POST)
        if new_booking_form.is_valid:
            if req.user.is_authenticated:
                new_booking = new_booking_form.save(commit=False)
                new_booking.user = req.user
                new_booking.save() 
    return redirect('/booking/')

class single_booking_two(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer


