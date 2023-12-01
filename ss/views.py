from django.shortcuts import render
from .models import *
# Create your views here.

def all(request):
    persons=Person.objects.all()
    art=Articale.objects.all()
    context={'person':persons,'art':art}

    return render(request,'index.html',context)