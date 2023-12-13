from django.db import models
from django.contrib.auth.models import User

class Auditorium(models.Model):
    number = models.CharField(max_length=10, unique=True)  # Номер аудиторії, наприклад, A101
    description = models.TextField()  # Опис аудиторії

    def __str__(self):
        return self.number  # Повертає номер аудиторії при виведенні об'єкта у консоль або адмінці



class Reservation(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активне'),
        ('cancelled', 'Скасоване'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Користувач, який здійснює бронювання
    auditorium = models.ForeignKey('reserv.Auditorium', on_delete=models.CASCADE)  # Номер аудиторії
    start_time = models.DateTimeField()  # Час початку бронювання
    duration = models.IntegerField()  # Тривалість бронювання у годинах

    def __str__(self):
        return f'{self.user.username} - {self.auditorium.number} - {self.start_time}'

