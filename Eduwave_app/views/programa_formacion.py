from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *

def programa_formacion_insertar(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        modalidad = request.POST.get('modalidad')
        red_id = request.POST.get('red_id')

        if nombre and modalidad and red_id:
            programa_formacion = ProgramaFormacion(
                nombre=nombre,
                modalidad=modalidad,
                red=get_object_or_404(Red, id=red_id)
            )
            programa_formacion.save()
            return redirect("programa_formacion_listar")
    
    redes = Red.objects.all()
    modalidades = ProgramaFormacion.MODALIDAD 
    return render(request, 'Admin/Programa_Formacion/insertar.html', {'redes': redes, 'modalidades': modalidades})


def programa_formacion_listar(request):
    programa_formacion = ProgramaFormacion.objects.all()
    return render(request, "Admin/Programa_Formacion/listar.html", {'programa_formacion':programa_formacion})

def programa_formacion_eliminar(request, id):
    programa_formacion=get_object_or_404(ProgramaFormacion,id=id)
    programa_formacion.delete()
    return redirect("programa_formacion_listar")

def programa_formacion_actualizar(request, id):
    programa_formacion = get_object_or_404(ProgramaFormacion, id=id)

    if request.method == 'POST':
        campos_obligatorios = ['nombre', 'modalidad', 'red_id']

        if all(request.POST.get(field) for field in campos_obligatorios):
            programa_formacion.nombre = request.POST.get('nombre')
            programa_formacion.red_id = Regional.objects.get(id=request.POST.get('red_id'))  # Corrección aquí
            programa_formacion.modalidad = request.POST.get('modalidad')

            programa_formacion.save()
            return redirect("programa_formacion_listar")

    red = Red.objects.all()
    modalidades = ProgramaFormacion.MODALIDAD 
    return render(request, 'Admin/Programa_Formacion/actualizar.html', {
        'programa_formacion': programa_formacion,
        'red': red,
        'modalidades': modalidades
    })