from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Auditorium, Reservation

class AuditoriumViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.auditorium = Auditorium.objects.create(number='101')

    def test_reserve_auditorium_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('reserve_auditorium'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reserve_auditorium.html')

    def test_available_auditoriums_view(self):
        response = self.client.get(reverse('available_auditoriums'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'available_auditoriums.html')

    def test_view_reservations_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('view_reservations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_reservations.html')

    def test_reservation_success_view(self):
        response = self.client.get(reverse('reservation_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation_success.html')


    def test_reserve_auditorium_response(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('reserve_auditorium'))
        self.assertEqual(response.status_code, 200)

    def test_available_auditoriums_response(self):
        response = self.client.get(reverse('available_auditoriums'))
        self.assertEqual(response.status_code, 200)

    def test_view_reservations_response(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('view_reservations'))
        self.assertEqual(response.status_code, 200)

    def test_reservation_success_response(self):
        response = self.client.get(reverse('reservation_success'))
        self.assertEqual(response.status_code, 200)


