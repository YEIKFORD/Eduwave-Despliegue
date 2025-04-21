from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *


def tipo_ambiente_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('nombre')
        and request.POST.get('descripcion')):
            
            tipo_ambiente=TipoAmbiente()

            tipo_ambiente.nombre=request.POST.get('nombre')
            tipo_ambiente.descripcion=request.POST.get('descripcion')

            tipo_ambiente.save()
            return redirect('tipo_ambiente_listar')
    else:
        return render(request,'Admin/Tipo_Ambiente/insertar.html')
    
def tipo_ambiente_listar(request):
    orden = request.GET.get('orden')

    tipo_ambiente = TipoAmbiente.objects.all()

    if orden == 'asc':
        tipo_ambiente = tipo_ambiente.order_by('nombre')
    elif orden == 'desc':
        tipo_ambiente = tipo_ambiente.order_by('-nombre')

    return render(request, 'Admin/Tipo_Ambiente/listar.html', {
        'tipo_ambiente': tipo_ambiente,
        'orden': orden
    })


def tipo_ambiente_actualizar(request, id):
    tipo_ambiente= get_object_or_404(TipoAmbiente,id=id)
    if request.method == 'POST':
        campos_obligatorios=['nombre','descripcion']
        if all(request.POST.get(field) for field in campos_obligatorios):

            tipo_ambiente.nombre=request.POST.get('nombre')
            tipo_ambiente.descripcion=request.POST.get('descripcion')
            tipo_ambiente.save()
            return redirect('tipo_ambiente_listar')
    else: 
        return render(request,'Admin/Tipo_Ambiente/actualizar.html',{'tipo_ambiente':tipo_ambiente})
    
def tipo_ambiente_eliminar( request, id):
    tipo_ambiente= get_object_or_404(TipoAmbiente,id=id)
    tipo_ambiente.delete()
    return redirect('tipo_ambiente_listar')