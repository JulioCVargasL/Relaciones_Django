from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.
def inicio(request):

  # place1 = Place(name="Los Taqueros bros.", address="Calle 14 # 16 -91")
  # place1.save()

  # resto1 = Restaurant(place=place1, employees = 5)
  # resto1.save()

  restaurante = Restaurant.objects.get(place_id=1)
  print(restaurante.place.address)

  return HttpResponse('Se guardo la info')
