from django.shortcuts import render
from .models import Place, star


# Create your views here.
def demo(requests):
   #return render(requests,"index.html")
    obj=Place.objects.all()
    obj1=star.objects.all()
    return render(requests,"index.html",{'result':obj,'result1':obj1})