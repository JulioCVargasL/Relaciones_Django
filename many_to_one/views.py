from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article

# Create your views here.

def inicio(request):
  repo1 = Reporter(first_name="Julio", last_name="Vargas", email="Julio_exmple.com")

  repo1.save()

  repo2 = Reporter(first_name="Tulio", last_name="Triviño", email="Tulio_exmple.com")

  repo2.save()


  return HttpResponse('hola esto es de muchos a uno')