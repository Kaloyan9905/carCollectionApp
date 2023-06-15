from django.shortcuts import render, redirect

from carCollectionApp.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from carCollectionApp.web.models import Profile, Car
from carCollectionApp.web.utils import get_total_cars_price


def index(request):
    profile = Profile.objects.all()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    cars = Car.objects.all()
    total_cars_price = get_total_cars_price(cars)

    context = {
        'profile': profile,
        'total_cars_price': total_cars_price,
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.get()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('details profile')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    cars = Car.objects.all()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            profile.delete()
            cars.delete()

            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-delete.html', context)


def catalogue(request):
    cars = Car.objects.all()

    context = {
        'cars': cars,
        'profile': Profile.objects.get(),
        'cars_count': Car.objects.count(),
    }

    return render(request, 'catalogue.html', context)


def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'form': form,
        'profile': Profile.objects.all()
    }

    return render(request, 'car-create.html', context)


def details_car(request, car_id):
    car = Car.objects \
        .filter(pk=car_id) \
        .get()

    context = {
        'car': car,
        'profile': Profile.objects.get(),
    }

    return render(request, 'car-details.html', context)


def edit_car(request, car_id):
    car = Car.objects \
        .filter(pk=car_id) \
        .get()

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)

        if form.is_valid():
            form.save()

            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'profile': Profile.objects.all(),
    }

    return render(request, 'car-edit.html', context)


def delete_car(request, car_id):
    car = Car.objects \
        .filter(pk=car_id) \
        .get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)

        if form.is_valid():
            car.delete()

            return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'profile': Profile.objects.get(),
    }

    return render(request, 'car-delete.html', context)
