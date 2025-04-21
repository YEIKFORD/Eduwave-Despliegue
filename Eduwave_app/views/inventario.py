from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *

def inventario_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('nombre')
        and request.POST.get('codigo')
        and request.POST.get('descripcion')
        and request.POST.get('categoria_id')
        and request.POST.get('ambiente_id')
        and request.POST.get('fecha_adquisicion')
        and request.POST.get('num_placa_almacen')
        and request.POST.get('precio_compra')):
            
            inventario = Inventario()
            
            inventario.nombre = request.POST.get('nombre')
            inventario.codigo = request.POST.get('codigo')
            inventario.descripcion = request.POST.get('descripcion')
            inventario.fecha_adquisicion = request.POST.get('fecha_adquisicion')
            inventario.num_placa_almacen = request.POST.get('num_placa_almacen')
            inventario.precio_compra = request.POST.get('precio_compra')
            inventario.categoria = SubCategoria.objects.get(id=request.POST.get('categoria_id'))
            inventario.ambiente = Ambiente.objects.get(id=request.POST.get('ambiente_id'))

            
            inventario.save()
            return redirect("inventario_listar")
        
    else:
        categorias = SubCategoria.objects.all()
        ambientes = Ambiente.objects.all()
        return render(request, 'Admin/Inventario/insertar.html', {'categorias': categorias, 'ambientes': ambientes})
    
def inventario_listar(request):
    inventarios = Inventario.objects.all()
    return render(request, "Admin/Inventario/listar.html", {'inventarios':inventarios})

def inventario_eliminar(request, id):
    inventario=get_object_or_404(Inventario,id=id)
    inventario.delete()
    return redirect("inventario_listar")

def inventario_actualizar(request, id):
    inventario=get_object_or_404(Inventario,id=id)
    
    if request.method == 'POST':
        campos_obligatorios = ['nombre','codigo','descripcion','fecha_adquisicion','num_placa_almacen','precio_compra','categoria_id','ambiente_id']
    
        if all(request.POST.get(field) for field in campos_obligatorios):
            inventario.nombre = request.POST.get('nombre')
            inventario.codigo = request.POST.get('codigo')
            inventario.descripcion = request.POST.get('descripcion')
            inventario.fecha_adquisicion = request.POST.get('fecha_adquisicion')
            inventario.num_placa_almacen = request.POST.get('num_placa_almacen')
            inventario.precio_compra = request.POST.get('precio_compra')
            inventario.categoria = SubCategoria.objects.get(id=request.POST.get('categoria_id'))
            inventario.ambiente = Ambiente.objects.get(id=request.POST.get('ambiente_id'))
            
            inventario.save()
            return redirect("inventario_listar")
    
    else:
        categorias = SubCategoria.objects.all()
        ambientes = Ambiente.objects.all()
        return render(request, 'Admin/Inventario/actualizar.html', {'inventario': inventario, 'categorias': categorias,'ambientes': ambientes})
    