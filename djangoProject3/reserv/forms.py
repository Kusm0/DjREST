from django import forms
from .models import Auditorium

from .models import Reservation, Auditorium


from django import forms
from .models import Reservation, Auditorium

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['auditorium', 'duration']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['auditorium'].queryset = self.get_available_auditoriums()

    # Поле для вибору аудиторії
    auditorium = forms.ModelChoiceField(queryset=Auditorium.objects.all(), label='Номер аудиторії')

    # Поле для вибору тривалості бронювання
    DURATION_CHOICES = [
        (1, '1 година'),
        (2, '2 години'),
        (3, '3 години'),
        (4, '4 години'),
        (5, '5 годин')
    ]
    duration = forms.ChoiceField(choices=DURATION_CHOICES, label='Тривалість бронювання')

    def get_available_auditoriums(self):
        # Отримайте всі доступні аудиторії, тобто ті, що не мають активних бронювань
        booked_auditoriums = Reservation.objects.filter(status='active').values_list('auditorium', flat=True)
        available_auditoriums = Auditorium.objects.exclude(pk__in=booked_auditoriums)
        return available_auditoriums



# У вашому файлі forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обов\'язкове. Введіть дійсну email адресу.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
