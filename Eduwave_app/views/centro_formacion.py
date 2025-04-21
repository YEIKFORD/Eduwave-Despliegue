from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse


def centro_formacion_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('codigo')
        and request.POST.get('nombre')
        and request.POST.get('direccion')
        and request.POST.get('telefono')
        and request.POST.get('municipio_id')):
            
            centro_formacion= CentroFormacion()
            
            centro_formacion.codigo = request.POST.get('codigo')
            centro_formacion.nombre = request.POST.get('nombre')
            centro_formacion.direccion = request.POST.get('direccion')
            centro_formacion.telefono = request.POST.get('telefono')
            centro_formacion.municipio = Municipio.objects.get(id=request.POST.get('municipio_id')) 
            
            centro_formacion.save()
            return redirect("centro_formacion_listar")
        
    else:
        municipio = Municipio.objects.all()
        return render(request, 'Admin/Centro_Formacion/insertar.html', {'municipio': municipio})
    

def centro_formacion_listar(request):
    municipios = Municipio.objects.all()
    municipio_id = request.GET.get('municipio_id')
    orden = request.GET.get('orden')
    busqueda = request.GET.get('busqueda', '')

    centros_formacion = CentroFormacion.objects.all()

    if municipio_id:
        centros_formacion = centros_formacion.filter(municipio_id=municipio_id)

    if busqueda:
        centros_formacion = centros_formacion.filter(nombre__icontains=busqueda)

    if orden == 'asc':
        centros_formacion = centros_formacion.order_by('nombre')
    elif orden == 'desc':
        centros_formacion = centros_formacion.order_by('-nombre')

    paginador = Paginator(centros_formacion, 5)  
    pagina = request.GET.get("page")
    centros_formacion = paginador.get_page(pagina)

    return render(request, "Admin/Centro_Formacion/listar.html", {
        'centros_formacion': centros_formacion,
        'municipios': municipios,
        'municipio_id_seleccionada': int(municipio_id) if municipio_id else None,
        'orden': orden,
        'busqueda': busqueda,
    })


def centro_formacion_eliminar_seleccionados(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        if ids:
            CentroFormacion.objects.filter(id__in=ids).delete()
            messages.success(request, "Centros de formación eliminados correctamente.")
    return redirect('centro_formacion_listar')



def centro_formacion_eliminar(request, id):
    centro_formacion=get_object_or_404(CentroFormacion,id=id)
    centro_formacion.delete()
    return redirect("centro_formacion_listar")

def centro_formacion_actualizar(request, id):
    centro_formacion = get_object_or_404(CentroFormacion, id=id)

    if request.method == 'POST':
        campos_obligatorios = ['codigo', 'nombre', 'direccion', 'telefono', 'municipio_id']

        if all(request.POST.get(field) for field in campos_obligatorios):
            centro_formacion.nit = request.POST.get('codigo')
            centro_formacion.municipio = Municipio.objects.get(id=request.POST.get('municipio_id'))  # Corrección aquí
            centro_formacion.nombre = request.POST.get('nombre')
            centro_formacion.direccion = request.POST.get('direccion')
            centro_formacion.telefono = request.POST.get('telefono')

            centro_formacion.save()
            return redirect("centro_formacion_listar")

    municipios = Municipio.objects.all()
    return render(request, 'Admin/Centro_Formacion/actualizar.html', {
        'centro_formacion': centro_formacion,
        'municipios': municipios 
    })
