from django.shortcuts import render, redirect, get_object_or_404
from laboratorio.models import Laboratorio
from .forms import LaboratorioForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'laboratorio/index.html')

def mostrar(request):
    laboratorios = Laboratorio.objects.all()
    
    return render(request, 'laboratorio/mostrar.html', {'laboratorios': laboratorios})
    

def insertar(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/insertar.html', {'form':form})

def editar(request, laboratorio_name):
    laboratorio = get_object_or_404(Laboratorio, nombre=laboratorio_name)  
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('mostrar')  
    else:
        form = LaboratorioForm(instance=laboratorio) 

    return render(request, 'laboratorio/editar.html', {'form': form})

def eliminar(request, laboratorio_name):
    laboratorio = get_object_or_404(Laboratorio, nombre=laboratorio_name)  
    
    if request.method == 'POST':
        laboratorio.delete()  
        messages.success(request, 'Laboratorio eliminado con éxito.')
        return redirect('mostrar') 

    return render(request, 'laboratorio/eliminar_confirmar.html', {'laboratorio': laboratorio})
