from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializers import menuSerializer, bookingSerializer
# Create your views here.
def index(req):
    return render(req, 'index.html', {})

class bookingview(APIView):
    def get(self, req):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, req):
        serialized_new_booking = bookingSerializer(data=req.data)
        if serialized_new_booking.is_valid():
            serialized_new_booking.save()
            return Response({'status': 'success', 'data': serialized_new_booking.data})

class menuview(APIView):
    def get(self, req):
        menu_items = Menu.objects.all()
        menu_item_serializer = menuSerializer(menu_items, many=True)
        return Response(menu_item_serializer.data)
    
    def post(self, req):
        serialized_new_menu_item = menuSerializer(data=req.data)
        if serialized_new_menu_item.is_valid():
            serialized_new_menu_item.save()
            return Response({'status': 'success', 'data': serialized_new_menu_item.data})