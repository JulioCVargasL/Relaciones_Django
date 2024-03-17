from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.
def inicio(request):
#CRUD 
  #---- Create -----

  # place1 = Place(name="Los Taqueros bros.", address="Calle 14 # 16 -91")
  # place1.save()
  place1 = Place.objects.get(id=1)
  # resto1 = Restaurant(place=place1, employees = 5)
  # resto1.save()
  # place2 = Place(name="Resto Sushi", address="Car 33 # 45 -91")
  # place2.save()
  # resto2 = Restaurant(place=place1, employees = 10)
  # resto2.save()

  # place3 = Place(name="Hamburguess", address="Car 36 # 55 - 4")
  # place3.save()
  # resto3 = Restaurant(place=place1, employees = 6)
  # resto3.save()
  
  # place4 = Place(name="Empanaditas", address="Calle 15 # 32 - 7")
  # place4.save()
  # resto4 = Restaurant(place=place1, employees = 3)
  # resto4.save()

  restaurante = Restaurant.objects.get(place_id=1)
  print(restaurante.place.address)

#---- List ----
  
  def listOTO(request):
    places = Place.objects.all()
    return HttpResponse(print(restaurante.place.address))
  
#----Delete----
  
  # eliminar = Place.objects.get(id=2)
  # eliminar.delete()
  
#----Update----
  
def update(request, id, name):
  pla = Place.objects.get(id = id)
  pla.name = name
  pla.save()
  return HttpResponse('Se guardo la info')
