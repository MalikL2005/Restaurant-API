from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns=[
    path('', views.home, name='home'),
    path('booking/', views.booking_redirect),
    path('booking/make_booking', views.view_all_create_bookings.as_view(), name='view_all_bookings/create'),
    path('booking/make_booking/process', views.process_booking),
    path('booking/<int:pk>', views.single_booking_two.as_view()),
    path('menu/', views.menuItemsView.as_view()),
    path('menu/<int:pk>', views.single_booking_two.as_view()),
    path('logout/', views.logout),
    path('sign-up/', views.sign_up),
    path('sign-up/validate/', views.validate_sign_up),
]
