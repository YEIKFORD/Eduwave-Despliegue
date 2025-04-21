from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import Red, CentroFormacion

def red_insertar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        centro_formacion_id = request.POST.get('centro_formacion_id')

        if nombre and centro_formacion_id:
            centro_formacion = get_object_or_404(CentroFormacion, id=centro_formacion_id)
            
            # Crear una nueva instancia de Red
            red = Red(nombre=nombre, centro_formacion=centro_formacion)
            red.save()

            return redirect("red_listar")

    centros_formacion = CentroFormacion.objects.all()
    return render(request, 'Admin/Red/insertar.html', {'centros_formacion': centros_formacion})

def red_listar(request):
    red = Red.objects.all()
    return render(request, "Admin/Red/listar.html", {'red':red})

def red_eliminar(request, id):
    red=get_object_or_404(Red,id=id)
    red.delete()
    return redirect("red_listar")

def red_actualizar(request, id):
    red = get_object_or_404(Red, id=id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        centro_formacion_id = request.POST.get('centro_formacion_id')

        if nombre and centro_formacion_id:
            red.nombre = nombre
            red.centro_formacion = get_object_or_404(CentroFormacion, id=centro_formacion_id)
            red.save()
            return redirect("red_listar")

    
    centro_formacion = CentroFormacion.objects.all()
    return render(request, 'Admin/Red/actualizar.html', {'red': red, 'centro_formacion': centro_formacion})