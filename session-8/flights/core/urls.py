from django.urls import path, include

from . import views

urlpatterns = [
    
    path('', views.index, name="index"),
    path('new-year', views.new_year, name="new-year"),
    path('flights', views.flights, name="flights"),
    path('flight-add', views.flight_add, name="flight-add"),
]
