from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.

def inicio(request):
  # repo1 = Reporter(first_name="Julio", last_name="Vargas", email="Julio_exmple.com")
  repo1 = Reporter.objects.get(id=1)
  # repo1.save()

  # repo2 = Reporter(first_name="Tulio", last_name="Triviño", email="Tulio_exmple.com")
  repo2 = Reporter.objects.get(id=2)
  # repo2.save()

  # Article.objects.create(
  #   headline="Primer articulo", 
  #   pub_date= date(2023, 5, 12), 
  #   reporter=repo1
  #   )
  # Article.objects.create(
  #   headline="Segundo Articulo", 
  #   pub_date= date(2024, 5, 12), 
  #   reporter=repo1
  #   )
  # Article.objects.create(
  #   headline="Articulo del Tulio", 
  #   pub_date= date(2024, 2, 29), 
  #   reporter=repo2
  #   )
  # art1.reporter



  return HttpResponse('hola esto es de muchos a uno')