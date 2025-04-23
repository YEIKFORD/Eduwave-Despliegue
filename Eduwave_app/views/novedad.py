from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from Eduwave_app.models import Novedad, Usuario, TipoNovedad, Ambiente, CentroFormacion, Sede
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Eduwave_app.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from api_app.serializers.novedad import NovedadSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

@login_required
def novedad_insertar(request):
    usuario = request.user
    codigo_rol = usuario.rol.codigo if hasattr(usuario, 'rol') else None

    # Lógica de filtro de tipo de novedad según el rol
    if codigo_rol in ['INS', 'ADS', 'COO']:
        tipo_novedades = TipoNovedad.objects.all()
    elif codigo_rol == 'ADE':
        tipo_novedades = TipoNovedad.objects.filter(nombre__iexact='Ambiente')
    elif codigo_rol == 'LDB':
        tipo_novedades = TipoNovedad.objects.filter(nombre__in=['Disciplinaria', 'Ambiente'])
    else:
        tipo_novedades = TipoNovedad.objects.none()

    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        tipo_novedad_id = request.POST.get('tipo_novedad')
        ambiente_id = request.POST.get('ambiente')
        estado_ambiente = request.POST.get('estado_ambiente')
        inventario_ids = request.POST.getlist('inventario[]')

        if descripcion and tipo_novedad_id:
            tipo_novedad = get_object_or_404(TipoNovedad, id=tipo_novedad_id)

            # Verificación de permiso para este tipo de novedad
            if (codigo_rol == 'ADE' and tipo_novedad.nombre != 'Ambiente') or \
            (codigo_rol == 'LDB' and tipo_novedad.nombre not in ['Ambiente', 'Disciplinaria']):
                return HttpResponseForbidden("No tienes permiso para registrar este tipo de novedad.")

            ambiente = get_object_or_404(Ambiente, id=ambiente_id) if ambiente_id else None

            # Crear y guardar la novedad
            novedad = Novedad(
                descripcion=descripcion,
                tipo_novedad=tipo_novedad,
                tipo_falta=request.POST.get('tipo_falta'),
                ambiente=ambiente,
                creado_por=usuario
            )
            novedad.save()

            # Asignar usuarios
            usuarios_ids = request.POST.getlist('usuarios[]')
            if usuarios_ids:
                usuarios = Usuario.objects.filter(id__in=usuarios_ids)
                novedad.usuarios.set(usuarios)

            # Asignar inventarios
            if inventario_ids:
                inventarios = Inventario.objects.filter(id__in=inventario_ids)
                novedad.inventario.set(inventarios)

            # Subir evidencia si existe
            if 'evidencia' in request.FILES:
                novedad.evidencia = request.FILES['evidencia']
                novedad.save()

            # Actualizar estado del ambiente si es una novedad de tipo 'ambiente'
            if tipo_novedad.nombre.lower() == 'Ambiente' and ambiente and estado_ambiente in ['A', 'N']:
                ambiente.estado = estado_ambiente
                ambiente.save()

            # Redirigir según el rol
            if usuario.rol.codigo == 'INS':  # Instructor
                return redirect('novedad_listar')  # Cambia por la URL correspondiente
            elif usuario.rol.codigo == 'COO':  # Coordinador
                return redirect('novedad_listar')
            elif usuario.rol.codigo == 'ADE':  # Administrador de Edificios
                return redirect('administrador_listar')
            elif usuario.rol.codigo == 'APD':  # Aprendiz
                return redirect('novedad_listar')
            elif usuario.rol.codigo == 'ADS':  # Admin Supremo
                return redirect('novedad_listar')
            elif usuario.rol.codigo == 'LDB':  # Líder de Bienestar
                return redirect('novedad_listar')
            else:
                return redirect('home')  

    # Filtrar los usuarios, ambientes e inventarios según el centro de formación del usuario
    ambientes = Ambiente.objects.filter(sede__centro_formacion=usuario.centro)
    usuarios = Usuario.objects.filter(centro=usuario.centro)
    inventarios = Inventario.objects.filter(ambiente__sede__centro_formacion=usuario.centro)

    return render(request, 'Admin/Novedad/insertar.html', {
        'tipo_novedades': tipo_novedades,
        'ambientes': ambientes,
        'usuarios': usuarios,
        'inventarios': inventarios,
    })


@login_required
def novedad_academica_listar(request):
    aprendiz = request.user

    fecha = request.GET.get('fecha')
    nombre_instructor = request.GET.get('nombre_instructor')
    tipo_novedad = request.GET.get('tipo_novedad')

    novedades_aca = Novedad.objects.all()

    if fecha:
        try:
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
            novedades_aca = novedades_aca.filter(fecha__date=fecha)
        except ValueError:
            pass  

    if nombre_instructor:
        novedades_aca = novedades_aca.filter(creado_por__first_name__icontains=nombre_instructor)

    if tipo_novedad == 'Academica':
        novedades_aca = novedades_aca.filter(tipo_novedad__nombre='Académica', usuarios=aprendiz)
    
    elif not tipo_novedad:
        novedades_aca = novedades_aca.filter(usuarios=aprendiz)

    return render(request, "Aprendiz/academica.html", {'novedades_aca': novedades_aca})

@login_required
def novedad_listar(request):
    usuarios = Usuario.objects.all()
    tipos_novedad = TipoNovedad.objects.all()
    estado = request.GET.get('estado')
    tipo_novedad_id = request.GET.get('tipo_novedad')
    gravedad = request.GET.get('gravedad')
    aprendiz_id = request.GET.get('aprendiz')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    orden = request.GET.get('orden')
    buscar = request.GET.get('buscar', '')

    # Filtrar todas las novedades
    novedades = Novedad.objects.all()

    # Condiciones de filtrado comunes
    if tipo_novedad_id:
        novedades = novedades.filter(tipo_novedad_id=tipo_novedad_id)
    
    if gravedad:
        novedades = novedades.filter(tipo_falta=gravedad)

    if estado:
        novedades = novedades.filter(estado=estado)

    if aprendiz_id:
        novedades = novedades.filter(usuarios__id=aprendiz_id)

    if fecha_inicio and fecha_fin:
        novedades = novedades.filter(fecha__range=[fecha_inicio, fecha_fin])

    if buscar:
        novedades = novedades.filter(descripcion__icontains=buscar)

    # Ordenar según la fecha
    if orden == 'desc':
        novedades = novedades.order_by('-fecha')
    else:
        novedades = novedades.order_by('fecha')

    # Paginación
    paginator = Paginator(novedades, 10)
    page = request.GET.get('page')
    novedades = paginator.get_page(page)

    return render(request, "Admin/Novedad/listar.html", {
        'novedades': novedades,
        'usuarios': usuarios,
        'tipos_novedad': tipos_novedad,
        'estado': estado,
        'tipo_novedad_id': tipo_novedad_id,
        'gravedad': gravedad,
        'aprendiz_id': aprendiz_id,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'orden': orden,
        'buscar': buscar
    })


def novedad_eliminar_masivo(request):
    if request.method == 'POST':
        ids = request.POST.getlist('seleccionados')
        if ids:
            Novedad.objects.filter(id__in=ids).delete()
            messages.success(request, "Novedades eliminadas correctamente.")
    return redirect('novedad_listar')


@login_required
def novedad_eliminar(request, id):
    novedad = get_object_or_404(Novedad, id=id)
    novedad.delete()
    return redirect("novedad_listar")

@login_required
def novedad_actualizar(request, id):
    usuario = request.user
    codigo_rol = usuario.rol.codigo if hasattr(usuario, 'rol') else None

    # Lógica de filtro de tipo de novedad según el rol
    if codigo_rol in ['INS', 'ADS', 'COO']:
        tipo_novedades = TipoNovedad.objects.all()
    elif codigo_rol == 'ADE':
        tipo_novedades = TipoNovedad.objects.filter(nombre__iexact='Ambiente')
    elif codigo_rol == 'LDB':
        tipo_novedades = TipoNovedad.objects.filter(nombre__in=['Disciplinaria', 'Ambiente'])
    else:
        tipo_novedades = TipoNovedad.objects.none()

    # Obtener la novedad desde la base de datos
    novedad = get_object_or_404(Novedad, id=id)

    # Verificación de permisos
    if novedad.creado_por != usuario and codigo_rol != 'ADM':
        return HttpResponseForbidden("No tienes permiso para editar esta novedad.")

    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        tipo_novedad_id = request.POST.get('tipo_novedad')
        ambiente_id = request.POST.get('ambiente')
        estado_ambiente = request.POST.get('estado_ambiente')
        inventario_ids = request.POST.getlist('inventario[]')

        if descripcion and tipo_novedad_id:
            tipo_novedad = get_object_or_404(TipoNovedad, id=tipo_novedad_id)

            # Verificación de permiso para este tipo de novedad
            if (codigo_rol == 'ADM' and tipo_novedad.nombre != 'Ambiente') or \
            (codigo_rol == 'LDB' and tipo_novedad.nombre not in ['Ambiente', 'Disciplinaria']):
                return HttpResponseForbidden("No tienes permiso para actualizar este tipo de novedad.")

            ambiente = get_object_or_404(Ambiente, id=ambiente_id) if ambiente_id else None

            # Actualizar los valores de la novedad
            novedad.descripcion = descripcion
            novedad.tipo_novedad = tipo_novedad
            novedad.tipo_falta = request.POST.get('tipo_falta')
            novedad.ambiente = ambiente

            # Actualizar usuarios seleccionados
            usuarios_ids = request.POST.getlist('usuarios[]')
            if usuarios_ids:
                usuarios_seleccionados = Usuario.objects.filter(id__in=usuarios_ids)
                novedad.usuarios.set(usuarios_seleccionados)

            # Actualizar inventarios seleccionados
            if inventario_ids:
                inventarios = Inventario.objects.filter(id__in=inventario_ids)
                novedad.inventario.set(inventarios)

            # Subir evidencia si existe
            if 'evidencia' in request.FILES:
                novedad.evidencia = request.FILES['evidencia']

            # Cambiar estado del ambiente si aplica
            if tipo_novedad.nombre.lower() == 'ambiente' and ambiente and estado_ambiente in ['A', 'N']:
                ambiente.estado = estado_ambiente
                ambiente.save()

            novedad.save()

            # Redirección según el rol
            if codigo_rol in ['INS', 'COO', 'APD', 'ADS', 'LDB']:
                return redirect('novedad_listar')
            elif codigo_rol == 'ADE':
                return redirect('administrador_listar')
            else:
                return redirect('home')

    # Datos necesarios para la plantilla
    ambientes = Ambiente.objects.filter(sede__centro_formacion=usuario.centro)
    usuarios = Usuario.objects.filter(centro=usuario.centro)
    inventarios = Inventario.objects.filter(ambiente__sede__centro_formacion=usuario.centro)

    # Obtener IDs de usuarios seleccionados para marcar como "selected" en la plantilla
    usuarios_seleccionados_ids = list(novedad.usuarios.values_list('id', flat=True))

    return render(request, 'Admin/Novedad/actualizar.html', {
        'tipo_novedades': tipo_novedades,
        'ambientes': ambientes,
        'usuarios': usuarios,
        'inventarios': inventarios,
        'novedad': novedad,
        'usuarios_seleccionados_ids': usuarios_seleccionados_ids,
    })


def usuario_search(request):
    term = request.GET.get('q', '')
    print(f"Buscando usuarios con el término: {term}")

    # Obtener el centro del usuario que está haciendo la búsqueda
    usuario = request.user
    centro_usuario = usuario.centro  # Asegúrate de que 'centro' es la relación correcta en el modelo

    # Filtrar usuarios por el término de búsqueda y por el centro
    users = Usuario.objects.filter(
        Q(centro=centro_usuario) & (
            Q(username__icontains=term) |
            Q(first_name__icontains=term) |
            Q(last_name__icontains=term) |
            Q(numero_doc__icontains=term)
        )
    )

    # Paginación de resultados
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Preparar los resultados para el frontend
    results = [
        {"id": user.id, "text": user.get_full_name() or user.username}
        for user in page_obj
    ]

    # Información de paginación
    pagination = {
        "more": page_obj.has_next()
    }

    return JsonResponse({"results": results, "pagination": pagination})



@login_required
def coordinador_listar(request):
    novedades = Novedad.objects.filter(estado='P')[:3]
    return render(request, 'Coordinador/listar.html', {
        'novedades': novedades
    })

@login_required
def aprobar_novedad(request, id):
    novedad = get_object_or_404(Novedad, id=id)
    novedad.estado = 'A'  
    novedad.save()
    return redirect('coordinador_listar')


@login_required
def administrador_listar(request):#Listar Novedades Administrador de Edificios
    novedades = Novedad.objects.filter(estado='P', tipo_novedad_id='3')[:3]
    return render(request, 'Administrador/listar.html', {
        'novedades': novedades
    })


@login_required
def evaluar_novedad(request, id):
    novedad = get_object_or_404(Novedad, id=id)
    novedad.estado = 'A'  
    novedad.save()
    return redirect('administrador_listar')

class NovedadDetailView(APIView):
    def get(self, request, novedad_id, format=None):
        try:
            # Obtenemos la novedad por el id
            novedad = Novedad.objects.get(id=novedad_id)
        except Novedad.DoesNotExist:
            return Response({'error': 'Novedad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        # Serializamos la novedad y la devolvemos como respuesta
        serializer = NovedadSerializer(novedad)
        return Response(serializer.data)