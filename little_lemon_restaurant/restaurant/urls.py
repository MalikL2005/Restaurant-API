from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('booking/', views.bookingview.as_view()),
    path('menu/', views.menuview.as_view()),
]
