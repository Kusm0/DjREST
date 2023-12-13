from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('available/', available_auditoriums, name='available_auditoriums'),
    path('reserve/', reserve_auditorium, name='reserve_auditorium'),
    path('reservations/', view_reservations, name='view_reservations'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('reservation_success/', reservation_success, name='reservation_success'),
    path('reservations/edit/<int:reservation_id>/', edit_reservation, name='edit_reservation'),
    path('reservations/cancel/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    # Інші URL-маршрути
]
