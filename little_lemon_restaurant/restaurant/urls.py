from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('', views.login, name='index'),
    path('booking/', views.booking_two.as_view()),
    path('booking/<int:pk>', views.single_booking_two.as_view()),
    path('menu/', views.menuItemsView.as_view()),
    path('menu/<int:pk>', views.single_booking_two.as_view()),
    path('token-auth', obtain_auth_token)
]
