from django.shortcuts import render
from .forms import FormRemedio
from .models import Remedio

# Create your views here.

def index(request):
    return render(request, 'index.html')


def listadoRemedios(request):
    remedios=Remedio.objects.all()
    data={'remedios':remedios}
    return render(request, 'remedios.html',data)

def agregarRemedios(request):
    form=FormRemedio()
    if request.method=='POST':
        form =FormRemedio(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render(request, 'agregarRemedios.html',data)