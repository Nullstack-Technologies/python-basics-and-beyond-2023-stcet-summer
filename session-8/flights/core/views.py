from datetime import datetime

from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Flight


def index(request):
    return render(request, "core/index.html")


def new_year(request):
    day = datetime.now().date().day
    month = datetime.now().date().month
    if day == 1 and month == 1:
        return HttpResponse("Happy New Year!!!🎉")    
    else:
        return HttpResponse("Sorry")    
 

def flights(request):
    flights = Flight.objects.all()
    return render(
        request,
        "core/flights.html",
        {'flights': flights, 'name': 'Nauman '}
    )


def flight_add(request):
    return render(
        request,
        "core/flight_add.html",
    )