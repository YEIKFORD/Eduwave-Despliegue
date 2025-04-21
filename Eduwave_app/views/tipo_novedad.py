from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *

def tipo_novedad_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('nombre')):
            
            tipo_novedad=TipoNovedad()

            tipo_novedad.nombre=request.POST.get('nombre')

            tipo_novedad.save()
            return redirect('tipo_novedad_listar')
    else:
        return render(request,'Admin/Tipo_Novedad/insertar.html')
    
def tipo_novedad_listar(request):
    tipo_novedad = TipoNovedad.objects.all()
    return render(request,'Admin/Tipo_Novedad/listar.html',{'tipo_novedad':tipo_novedad})

def tipo_novedad_actualizar(request, id):
    tipo_novedad= get_object_or_404(TipoNovedad,id=id)
    if request.method == 'POST':
        campos_obligatorios=['nombre']
        if all(request.POST.get(field) for field in campos_obligatorios):

            tipo_novedad.nombre=request.POST.get('nombre')
            tipo_novedad.save()
            return redirect('tipo_novedad_listar')
    else: 
        return render(request,'Admin/Tipo_Novedad/actualizar.html',{'tipo_novedad':tipo_novedad})
    
def tipo_novedad_eliminar( request, id):
    tipo_novedad= get_object_or_404(TipoNovedad,id=id)
    tipo_novedad.delete()
    return redirect('tipo_novedad_listar')