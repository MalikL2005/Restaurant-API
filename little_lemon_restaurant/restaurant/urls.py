from django.urls import path 
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('booking/', views.booking_two.as_view()),
    path('booking/<int:pk>', views.single_booking_two.as_view()),
    path('menu/', views.menuItemsView.as_view()),
    path('menu/<int:pk>', views.single_booking_two.as_view()),
]
