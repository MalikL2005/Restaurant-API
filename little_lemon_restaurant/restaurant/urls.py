from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('sign-up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('booking/', views.view_all_create_bookings.as_view()),
    path('booking/<int:pk>', views.single_booking_two.as_view()),
    path('menu/', views.menuItemsView.as_view()),
    path('menu/<int:pk>', views.single_booking_two.as_view()),
    path('token-auth', obtain_auth_token),
]
