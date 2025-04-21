from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *

def rol_insertar(request):
    if request.method == 'POST':
        if (request.POST.get('nombre')
        and request.POST.get('codigo')
        and request.POST.get('descripcion')):
            
            rol = Rol()
            
            rol.nombre = request.POST.get('nombre')
            rol.codigo = request.POST.get('codigo')
            rol.descripcion = request.POST.get('descripcion')
            
            rol.save()
            return redirect("rol_listar")
        
    else:
        return render(request, 'Admin/Rol/insertar.html')
    
def rol_listar(request):
    roles = Rol.objects.all()
    return render(request, "Admin/Rol/listar.html", {'roles': roles})

def rol_eliminar(request, id):
    rol=get_object_or_404(Rol,id=id)
    rol.delete()
    return redirect("rol_listar")

def rol_actualizar(request, id):
    rol=get_object_or_404(Rol,id=id)
    
    if request.method == 'POST':
        campos_obligatorios = ['nombre','codigo','descripcion']
    
        if all(request.POST.get(field) for field in campos_obligatorios):
            rol.codigo = request.POST.get('codigo')
            rol.nombre = request.POST.get('nombre')
            rol.descripcion = request.POST.get('descripcion')
            
            rol.save()
            return redirect("rol_listar")
    
    else:
        return render(request, 'Admin/Rol/actualizar.html', {'rol':rol})
    
    