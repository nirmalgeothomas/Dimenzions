from django.shortcuts import redirect, render
from .models import *

# Create your views here.


def addmodel(request):
    return render(request, "addmodel.html")


def createmodel(request):
    if request.method == 'POST':

        modelname = request.POST['modelname']
        description = request.POST['description']
        gib = request.FILES['gib']
        price = request.POST['price']
        types = request.POST['types']
        format = request.POST['format']
        modeltype = request.POST['modeltype']
        category = request.POST['category']
        fbx = request.FILES['fbx']

        item = items(modelname=modelname, description=description, gib=gib, price=price, types=types, format=format, modeltype=modeltype, category=category,
                     fbx=fbx)
        item.save()
        return redirect('addmodel')
    else:
        return redirect('createmodel')
