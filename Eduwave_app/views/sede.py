from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *
from django.core.paginator import Paginator
from django.contrib import messages


def sede_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('nombre')
        and request.POST.get('codigo')
        and request.POST.get('direccion')
        and request.POST.get('telefono')
        and request.POST.get('centro_formacion_id')
        ):
            sede=Sede()

            sede.nombre = request.POST.get('nombre')
            sede.codigo = request.POST.get('codigo')
            sede.direccion = request.POST.get('direccion')
            sede.telefono = request.POST.get('telefono')
            sede.centro_formacion = CentroFormacion.objects.get(id=request.POST.get('centro_formacion_id')) 
        
            sede.save()
            return redirect("sede_listar")
        
    else:
        centro_formacion = CentroFormacion.objects.all()
        return render(request, 'Admin/Sede/insertar.html',{'centro_formacion': centro_formacion})
    
def sede_listar(request):
    centros = CentroFormacion.objects.all()
    centro_id = request.GET.get('centro_id')
    orden = request.GET.get('orden')
    busqueda = request.GET.get('busqueda', '')

    sedes = Sede.objects.all()

    if centro_id:
        sedes = sedes.filter(centro_formacion_id=centro_id)

    if busqueda:
        sedes = sedes.filter(nombre__icontains=busqueda)

    if orden == 'asc':
        sedes = sedes.order_by('nombre')
    elif orden == 'desc':
        sedes = sedes.order_by('-nombre')

    paginador = Paginator(sedes, 5)
    pagina = request.GET.get("page")
    sedes = paginador.get_page(pagina)

    return render(request, "Admin/Sede/listar.html", {
        'sedes': sedes,
        'centros': centros,
        'centro_id_seleccionado': int(centro_id) if centro_id else None,
        'orden': orden,
        'busqueda': busqueda,
    })


def sede_eliminar_seleccionados(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        if ids:
            Sede.objects.filter(id__in=ids).delete()
            messages.success(request, "Sedes eliminadas correctamente.")
    return redirect('sede_listar')


def sede_eliminar(request, id):
    sede=get_object_or_404(Sede,id=id)
    sede.delete()
    return redirect("sede_listar")

def sede_actualizar(request, id):
    sede=get_object_or_404(Sede,id=id)
    
    if request.method == 'POST':
        campos_obligatorios = ['nombre','codigo','direccion','telefono','centro_formacion_id']
    
        if all(request.POST.get(field) for field in campos_obligatorios):
            sede.nombre = request.POST.get('nombre')
            sede.codigo = request.POST.get('codigo')
            sede.ciudad = request.POST.get('ciudad')
            sede.direccion = request.POST.get('direccion')
            sede.centro_formacion = CentroFormacion.objects.get(id=request.POST.get('centro_formacion_id')) 
            
            sede.save()
            return redirect("sede_listar")
    
    else:
        centro_formacion = CentroFormacion.objects.all()
        return render(request, 'Admin/Sede/actualizar.html', {'sede': sede,'centro_formacion': centro_formacion})
