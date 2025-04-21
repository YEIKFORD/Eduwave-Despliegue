from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import * 
from django.core.paginator import Paginator
from django.contrib import messages


def categoria_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('nombre')):
            
            categoria = Categoria()
            
            categoria.nombre = request.POST.get('nombre')
            
            categoria.save()
            return redirect("categoria_listar")
        
    else:
        return render(request, 'Admin/Categoria/insertar.html')

def categoria_listar(request):
    buscar = request.GET.get('buscar', '')
    orden = request.GET.get('orden')

    categorias = Categoria.objects.all()

    if buscar:
        categorias = categorias.filter(nombre__icontains=buscar)

    if orden == 'asc':
        categorias = categorias.order_by('nombre')
    elif orden == 'desc':
        categorias = categorias.order_by('-nombre')

    paginator = Paginator(categorias, 10)  # 10 categorías por página
    page = request.GET.get('page')
    categorias = paginator.get_page(page)

    return render(request, "Admin/Categoria/listar.html", {
        'categorias': categorias,
        'buscar': buscar,
        'orden': orden
    })

def categoria_eliminar_masivo(request):
    if request.method == 'POST':
        ids = request.POST.getlist('seleccionados')
        if ids:
            Categoria.objects.filter(id__in=ids).delete()
            messages.success(request, "Categorías eliminadas correctamente.")
    return redirect('categoria_listar')

def categoria_eliminar(request, id):
    categoria=get_object_or_404(Categoria,id=id)
    categoria.delete()
    return redirect("categoria_listar")

def categoria_actualizar(request, id):
    categoria=get_object_or_404(Categoria,id=id)
    
    if request.method == 'POST':
        campos_obligatorios = ['nombre']
    
        if all(request.POST.get(field) for field in campos_obligatorios):
            categoria.nombre = request.POST.get('nombre')
            
            categoria.save()
            return redirect("categoria_listar")
    
    else:
        return render(request, 'Admin/Categoria/actualizar.html', {'categoria':categoria})
