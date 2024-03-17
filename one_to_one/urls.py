from django.urls import path
from . import views

urlpatterns = [
  path('', views.inicio, name='uno'),
  path('update/<int:id>/<str:name>/', views.update, name="update")
]

