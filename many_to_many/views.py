from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article
# Create your views here.

def create(request):
#   art1 = Article(headline="Test Art 1")
#   art2 = Article(headline="Test Art 2")
#   art3 = Article(headline="Test Art 3")
#   art4 = Article(headline="Test Art 4")
#   art5 = Article(headline="Test Art 5")
#   art6 = Article(headline="Test Art 6")
#   art7 = Article(headline="Test Art 7")
#   art8 = Article(headline="Test Art 8")

#   art1.save()
#   art2.save()
#   art3.save()
#   art4.save()
#   art5.save()
  
#   pub1 = Publication(title="Test Title 1")
#   pub2 = Publication(title="Test Title 2")
#   pub3 = Publication(title="Test Title 3")
#   pub4 = Publication(title="Test Title 4")
#   pub5 = Publication(title="Test Title 5")
#   pub6 = Publication(title="Test Title 6")
#   pub7 = Publication(title="Test Title 7")
#   pub8 = Publication(title="Test Title 8")
#   pub9 = Publication(title="Test Title 9")
#   pub10 = Publication(title="Test Title 10")
#   pub11 = Publication(title="Test Title 11")

#   pub1.save()
#   pub2.save()
#   pub3.save()
#   pub4.save()
#   pub5.save()
#   pub6.save()
#   pub7.save()
#   pub8.save()
#   pub9.save()
#   pub10.save()
#   pub11.save()

#   art1.publications.add(pub1)
#   art1.publications.add(pub2)
#   art1.publications.add(pub3)
#   art2.publications.add(pub4)
#   art3.publications.add(pub5)
#   art3.publications.add(pub6)
#   art4.publications.add(pub6)
#   art4.publications.add(pub7)
#   art4.publications.add(pub7)
#   art4.publications.add(pub8)
#   art5.publications.add(pub9)
#   art5.publications.add(pub11)

  return HttpResponse('Muchos a Muchos')


