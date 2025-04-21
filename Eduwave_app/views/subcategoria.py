from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages


def sub_categoria_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('nombre')
        and request.POST.get('categoria_id')):
            
            sub_categoria = SubCategoria()
            
            sub_categoria.nombre = request.POST.get('nombre')
            sub_categoria.categoria = Categoria.objects.get(id=request.POST.get('categoria_id'))
            
            sub_categoria.save()
            return redirect("sub_categoria_listar")
        
    else:
        categoria = Categoria.objects.all()
        return render(request, 'Admin/SubCategoria/insertar.html',  {'categoria': categoria})
    
def sub_categoria_listar(request):
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria_id')
    orden = request.GET.get('orden')
    buscar = request.GET.get('buscar', '')

    sub_categorias = SubCategoria.objects.all()

    if categoria_id:
        sub_categorias = sub_categorias.filter(categoria_id=categoria_id)

    if buscar:
        sub_categorias = sub_categorias.filter(nombre__icontains=buscar)

    if orden == 'asc':
        sub_categorias = sub_categorias.order_by('nombre')
    elif orden == 'desc':
        sub_categorias = sub_categorias.order_by('-nombre')

    paginator = Paginator(sub_categorias, 10)
    page = request.GET.get('page')
    sub_categorias = paginator.get_page(page)

    return render(request, "Admin/SubCategoria/listar.html", {
        'sub_categorias': sub_categorias,
        'categorias': categorias,
        'categoria_id_seleccionada': int(categoria_id) if categoria_id else None,
        'orden': orden,
        'buscar': buscar,
    })

def sub_categoria_eliminar_masivo(request):
    if request.method == 'POST':
        ids = request.POST.getlist('seleccionados')
        if ids:
            SubCategoria.objects.filter(id__in=ids).delete()
            messages.success(request, "Sub categorías eliminadas correctamente.")
    return redirect('sub_categoria_listar')

def sub_categoria_eliminar(request, id):
    sub_categoria=get_object_or_404(SubCategoria,id=id)
    sub_categoria.delete()
    return redirect("sub_categoria_listar")

def sub_categoria_actualizar(request, id):
    sub_categoria = get_object_or_404(SubCategoria, id=id)
    
    if request.method == 'POST':
        campos_obligatorios = ['nombre', 'categoria_id']
    
        if all(request.POST.get(field) for field in campos_obligatorios):
            sub_categoria.nombre = request.POST.get('nombre')
            sub_categoria.categoria = Categoria.objects.get(id=request.POST.get('categoria_id'))
            sub_categoria.save()
            return redirect("sub_categoria_listar")
    
    categorias = Categoria.objects.all()
    return render(request, 'Admin/SubCategoria/actualizar.html', {'sub_categoria': sub_categoria, 'categorias': categorias})
