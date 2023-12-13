# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import ReservationForm
from .models import Reservation

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Reservation, Auditorium
from .forms import ReservationForm

from datetime import timedelta


def reserve_auditorium(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            auditorium = form.cleaned_data['auditorium']
            duration = int(form.cleaned_data['duration'])  # Перетворення у ціле число
            user = request.user

            if not is_auditorium_available(auditorium, duration):
                return render(request, 'auditorium_not_available.html', {'auditorium': auditorium})

            reservation = Reservation.objects.create(
                user=user,
                auditorium=auditorium,
                start_time=timezone.now(),
                duration=duration
            )

            return redirect('reservation_success')
    else:
        form = ReservationForm()

    return render(request, 'reserve_auditorium.html', {'form': form})


def is_auditorium_available(auditorium, duration):
    reservations = Reservation.objects.filter(auditorium=auditorium, status='active')

    for reservation in reservations:
        if reservation.start_time <= timezone.now() <= reservation.start_time + timedelta(hours=duration):
            return False

    return True


from .models import Auditorium


def available_auditoriums(request):
    # Отримайте всі аудиторії
    all_auditoriums = Auditorium.objects.all()

    # Отримайте всі бронювання
    reservations = Reservation.objects.filter(status='active')

    # Отримайте список номерів аудиторій, які вже заброньовані
    booked_auditorium_numbers = reservations.values_list('auditorium__number', flat=True)

    # Відфільтруйте аудиторії, залиште тільки ті, які не заброньовані
    available_auditoriums = all_auditoriums.exclude(number__in=booked_auditorium_numbers)

    return render(request, 'available_auditoriums.html', {'available_auditoriums': available_auditoriums})


from django.shortcuts import render
from .models import Reservation


def view_reservations(request):
    user = request.user

    reservations = Reservation.objects.filter(status='active', user=user)

    return render(request, 'view_reservations.html', {'reservations': reservations})


from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправити на сторінку входу після успішної реєстрації
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def reservation_success(request):
    return render(request, 'reservation_success.html')


def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view_reservations')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'edit_reservation.html', {'form': form, 'reservation': reservation})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation


def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    if request.method == 'POST':
        # Позначте бронювання як скасоване
        reservation.status = 'cancelled'
        reservation.save()
        return redirect('view_reservations')

    return render(request, 'cancel_reservation.html', {'reservation': reservation})
