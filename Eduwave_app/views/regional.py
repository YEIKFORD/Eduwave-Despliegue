from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')

def regional_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('codigo')
        and request.POST.get('nombre')

        ):
            
            regional=Regional()

            regional.codigo=request.POST.get('codigo')
            regional.nombre=request.POST.get('nombre')

            regional.save()
            return redirect('regional_listar')
    else:
        return render(request,'Admin/Regional/insertar.html')
    

def regional_listar(request):
    regional = Regional.objects.all()

    buscar_nombre = request.GET.get('buscar_nombre', '')
    orden = request.GET.get('orden', '')

    if buscar_nombre:
        regional = regional.filter(nombre__icontains=buscar_nombre)

    if orden:
        regional = regional.order_by(orden)

    paginator = Paginator(regional, 20)
    page = request.GET.get('page')
    regional = paginator.get_page(page)

    return render(request, 'Admin/Regional/listar.html', {
        'regional': regional,
        'buscar_nombre': buscar_nombre,
        'orden': orden
    })

def regional_eliminar_masivo(request):
    if request.method == 'POST':
        ids = request.POST.getlist('seleccionados')
        if ids:
            Regional.objects.filter(id__in=ids).delete()
            messages.success(request, "Regionales eliminadas correctamente.")
    return redirect('regional_listar')


def regional_actualizar(request, id):
    regional= get_object_or_404(Regional,id=id)
    if request.method == 'POST':
        campos_obligatorios=['codigo','nombre']
        if all(request.POST.get(field) for field in campos_obligatorios):

            regional.codigo=request.POST.get('codigo')
            regional.nombre=request.POST.get('nombre')
            regional.save()
            return redirect('regional_listar')
    else:
        return render(request,'Admin/Regional/actualizar.html',{'regional':regional})
    
def regional_eliminar( request, id):
    regional= get_object_or_404(Regional,id=id)
    regional.delete()
    return redirect('regional_listar')