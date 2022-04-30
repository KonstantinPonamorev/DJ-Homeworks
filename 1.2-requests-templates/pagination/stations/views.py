from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    stations = []
    with open(BUS_STATION_CSV) as csvfile:
        with open(BUS_STATION_CSV, encoding='UTF-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                stations.append(row)
    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': stations[(page_number-1)*10:page_number*10],
        'page': page,
    }
    return render(request, 'stations/index.html', context)
