from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *
from django.core.paginator import Paginator
from django.contrib import messages

def ambiente_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('numero_ambiente')
        and request.POST.get('estado')
        and request.POST.get('tipo_ambiente_id')
        and request.POST.get('sede_id')):
            
            ambiente = Ambiente()
            
            ambiente.numero_ambiente = request.POST.get('numero_ambiente')
            ambiente.estado = request.POST.get('estado')
            ambiente.tipo_ambiente = TipoAmbiente.objects.get(id=request.POST.get('tipo_ambiente_id'))
            ambiente.sede = Sede.objects.get(id=request.POST.get('sede_id'))
            
            ambiente.save()
            return redirect("ambiente_listar")
        
    else:
        tipo_ambientes = TipoAmbiente.objects.all()
        sedes = Sede.objects.all()
        estados = Ambiente.ESTADO
        return render(request, 'Admin/Ambiente/insertar.html',  {'tipo_ambientes': tipo_ambientes, 'sedes': sedes,
        'estados': estados})
    
def ambiente_listar(request):
    ambientes = Ambiente.objects.all()
    sedes = Sede.objects.all()
    tipos_ambiente = TipoAmbiente.objects.all()

    sede_id = request.GET.get('sede_id')
    tipo_id = request.GET.get('tipo_id')
    orden = request.GET.get('orden')
    busqueda = request.GET.get('busqueda', '')

    if busqueda:
        ambientes = ambientes.filter(numero_ambiente__icontains=busqueda)

    if sede_id:
        ambientes = ambientes.filter(sede_id=sede_id)

    if tipo_id:
        ambientes = ambientes.filter(tipo_ambiente_id=tipo_id)

    if orden == 'asc':
        ambientes = ambientes.order_by('numero_ambiente')
    elif orden == 'desc':
        ambientes = ambientes.order_by('-numero_ambiente')

    paginator = Paginator(ambientes, 5)
    page_number = request.GET.get('page')
    ambientes = paginator.get_page(page_number)

    return render(request, "Admin/Ambiente/listar.html", {
        'ambientes': ambientes,
        'sedes': sedes,
        'tipos_ambiente': tipos_ambiente,
        'sede_id': sede_id,
        'tipo_id': tipo_id,
        'orden': orden,
        'busqueda': busqueda
    })

def ambiente_eliminar_varios(request):
    if request.method == 'POST':
        ids = request.POST.getlist('seleccionados')
        if ids:
            Ambiente.objects.filter(id__in=ids).delete()
            messages.success(request, "Ambientes eliminados correctamente.")
        else:
            messages.warning(request, "No se seleccionó ningún ambiente.")
    return redirect('ambiente_listar')

def ambiente_eliminar(request, id):
    ambiente=get_object_or_404(Ambiente,id=id)
    ambiente.delete()
    return redirect("ambiente_listar")

def ambiente_actualizar(request, id):
    ambiente=get_object_or_404(Ambiente,id=id)
    
    if request.method == 'POST':
        campos_obligatorios = ['numero_ambiente','estado','tipo_ambiente_id','sede_id']
    
        if all(request.POST.get(field) for field in campos_obligatorios):
            ambiente.numero_ambiente = request.POST.get('numero_ambiente')
            ambiente.estado = request.POST.get('estado')
            ambiente.tipo_ambiente = TipoAmbiente.objects.get(id=request.POST.get('tipo_ambiente_id'))
            ambiente.sede = Sede.objects.get(id=request.POST.get('sede_id'))
            
            ambiente.save()
            return redirect("ambiente_listar")
    
    else:
        tipo_ambientes = TipoAmbiente.objects.all()
        sedes = Sede.objects.all()
        estados = Ambiente.ESTADO
        return render(request, 'Admin/Ambiente/actualizar.html', {'ambiente': ambiente, 'tipo_ambientes': tipo_ambientes, 'sedes': sedes, 'estados': estados})
    