from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages

def municipio_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('codigo_DANE')
        and request.POST.get('nombre')
        and request.POST.get('regional_id')):
            
            municipio= Municipio()
            
            municipio.codigo_DANE = request.POST.get('codigo_DANE')
            municipio.nombre = request.POST.get('nombre')
            municipio.regional = Regional.objects.get(id=request.POST.get('regional_id')) 
            
            municipio.save()
            return redirect("municipio_listar")
        
    else:
        regional = Regional.objects.all()
        return render(request, 'Admin/Municipio/insertar.html', {'regional': regional})


def municipio_listar(request):
    regionales = Regional.objects.all()
    regional_id = request.GET.get('regional_id')
    orden = request.GET.get('orden')
    buscar = request.GET.get('buscar', '')

    municipio = Municipio.objects.all()

    if regional_id:
        municipio = municipio.filter(regional_id=regional_id)

    if buscar:
        municipio = municipio.filter(nombre__icontains=buscar)

    if orden == 'asc':
        municipio = municipio.order_by('nombre')
    elif orden == 'desc':
        municipio = municipio.order_by('-nombre')

    paginator = Paginator(municipio, 10)
    page = request.GET.get('page')
    municipio = paginator.get_page(page)

    return render(request, "Admin/Municipio/listar.html", {
        'municipio': municipio,
        'regionales': regionales,
        'regional_id_seleccionada': int(regional_id) if regional_id else None,
        'orden': orden,
        'buscar': buscar
    })

def municipio_eliminar_masivo(request):
    if request.method == 'POST':
        ids = request.POST.getlist('seleccionados')
        if ids:
            Municipio.objects.filter(id__in=ids).delete()
            messages.success(request, "Municipios eliminados correctamente.")
    return redirect('municipio_listar')


def municipio_eliminar(request, id):
    municipio=get_object_or_404(Municipio,id=id)
    municipio.delete()
    return redirect("municipio_listar")

def municipio_actualizar(request, id):
    municipio = get_object_or_404(Municipio, id=id)

    if request.method == 'POST':
        campos_obligatorios = ['codigo_DANE', 'nombre', 'regional']

        if all(request.POST.get(field) for field in campos_obligatorios):
            municipio.codigo_DANE = request.POST.get('codigo_DANE')
            municipio.nombre = request.POST.get('nombre')
            municipio.regional = Regional.objects.get(id=request.POST.get('regional'))

            municipio.save()
            return redirect("municipio_listar")

    regionales = Regional.objects.all()
    return render(request, 'Admin/Municipio/actualizar.html', {
        'municipio': municipio,
        'regionales': regionales
    })
