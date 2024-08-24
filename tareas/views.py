from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

# Create your views here.
def crearTarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarTareas')
    form = TareaForm()
    return render(request,'crearTarea.html',{'form':form})

def listarTareas(request):
    estado = request.GET.get('estado')
    if estado:
        tareas = Tarea.objects.filter(estado=estado)
    else:
        tareas = Tarea.objects.all()
    return render(request,'listarTareas.html',{'tareas':tareas})