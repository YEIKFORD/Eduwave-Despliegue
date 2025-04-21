from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *

def ficha_insertar(request):
    if request.method == 'POST':
        num_ficha = request.POST.get('num_ficha')
        programa_id = request.POST.get('programa_id')

        if num_ficha and programa_id:
            programa = ProgramaFormacion.objects.get(id=programa_id)
            ficha = Ficha.objects.create(num_ficha=num_ficha, programa=programa)
            return redirect("ficha_listar")

    programas = ProgramaFormacion.objects.all()
    return render(request, 'Admin/Ficha/insertar.html', {'programas': programas})


def ficha_listar(request):
    fichas = Ficha.objects.all()
    return render(request, "Admin/Ficha/listar.html", {'fichas': fichas})


def ficha_eliminar(request, id):
    ficha = get_object_or_404(Ficha, id=id)
    ficha.delete()
    return redirect("ficha_listar")


def ficha_actualizar(request, id):
    ficha = get_object_or_404(Ficha, id=id)

    if request.method == 'POST':
        num_ficha = request.POST.get('num_ficha')
        programa_id = request.POST.get('programa_id')

        if num_ficha and programa_id:
            ficha.num_ficha = num_ficha
            ficha.programa = ProgramaFormacion.objects.get(id=programa_id)
            ficha.save()
            return redirect("ficha_listar")

    programas = ProgramaFormacion.objects.all()
    return render(request, 'Admin/Ficha/actualizar.html', {
        'ficha': ficha,
        'programas': programas
    })
