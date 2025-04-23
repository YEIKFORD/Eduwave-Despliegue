from django.shortcuts import render, redirect, get_object_or_404
from Eduwave_app.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.http import JsonResponse
from django.core.paginator import Paginator


def usuario_insertar(request):
    if request.method == 'POST':
        tipo_doc = request.POST.get('tipo_doc')
        numero_doc = request.POST.get('numero_doc')
        telefono = request.POST.get('telefono')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rol_id = request.POST.get('rol_id')
        centro_id = request.POST.get('centro_id')
        fichas_ids = request.POST.getlist('fichas')  # Múltiples fichas

        if not all([tipo_doc, numero_doc, telefono, first_name, last_name, username, email, password, rol_id, centro_id]):
            messages.error(request, "Todos los campos obligatorios deben ser diligenciados.")
            return redirect('usuario_insertar')

        if not telefono.isdigit() or len(telefono) != 10:
            messages.error(request, "El número de teléfono debe tener exactamente 10 dígitos.")
            return redirect('usuario_insertar')

        if Usuario.objects.filter(numero_doc=numero_doc).exists():
            messages.error(request, "El número de documento ya está registrado.")
            return redirect('usuario_insertar')

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return redirect('usuario_insertar')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está registrado.")
            return redirect('usuario_insertar')

        try:
            with transaction.atomic():
                usuario = Usuario.objects.create(
                    tipo_doc=tipo_doc,
                    numero_doc=numero_doc,
                    telefono=telefono,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=make_password(password),
                    rol_id=rol_id,
                    centro_id=centro_id,
                )
                if fichas_ids:
                    usuario.fichas.set(fichas_ids)  # Relación many-to-many si aplica
                messages.success(request, "Usuario registrado exitosamente.")
                return redirect('login_usuario')
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect('usuario_insertar')

    roles = Rol.objects.all()
    centros = CentroFormacion.objects.all()
    fichas = Ficha.objects.all()
    codigos_roles = {rol.id: rol.codigo for rol in roles}

    return render(request, "Usuario/insertar.html", {
        'roles': roles,
        'centros': centros,
        'fichas': fichas,
        'codigos_roles': codigos_roles,
    })

def usuario_listar(request):
    usuarios = Usuario.objects.all()
    return render(request, "Usuario/listar.html", {'usuarios': usuarios})

def usuario_eliminar(request, id):
    usuario=get_object_or_404(Usuario,id=id)
    usuario.delete()
    return redirect("usuario_listar")


def usuario_actualizar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    roles = Rol.objects.all()
    centros = CentroFormacion.objects.all()
    fichas = Ficha.objects.all()

    if request.method == 'POST':
        tipo_doc = request.POST.get('tipo_doc', '').strip()
        numero_doc = request.POST.get('numero_doc', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        rol_id = request.POST.get('rol_id', '').strip()
        centro_id = request.POST.get('centro_id', '').strip()
        ficha_input = request.POST.get('ficha', '').strip()  # Input por datalist

        if not all([tipo_doc, numero_doc, first_name, last_name, username, email, rol_id, centro_id]):
            messages.error(request, "Todos los campos obligatorios deben ser diligenciados.")
        elif not telefono.isdigit() or len(telefono) != 10:
            messages.error(request, "El teléfono debe tener exactamente 10 dígitos.")
        elif Usuario.objects.filter(numero_doc=numero_doc).exclude(id=usuario.id).exists():
            messages.error(request, "El número de documento ya está registrado por otro usuario.")
        elif Usuario.objects.filter(username=username).exclude(id=usuario.id).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
        elif Usuario.objects.filter(email=email).exclude(id=usuario.id).exists():
            messages.error(request, "El correo electrónico ya está registrado por otro usuario.")
        else:
            usuario.tipo_doc = tipo_doc
            usuario.numero_doc = numero_doc
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.username = username
            usuario.email = email
            usuario.telefono = telefono
            usuario.rol_id = rol_id
            usuario.centro_id = centro_id

            if password:
                usuario.set_password(password)

            usuario.save()

            # Actualizar fichas (ManyToMany)
            if ficha_input:
                try:
                    ficha = Ficha.objects.get(codigo=ficha_input)
                    usuario.fichas.set([ficha])
                except Ficha.DoesNotExist:
                    usuario.fichas.clear()
            else:
                usuario.fichas.clear()

            messages.success(request, "Usuario actualizado correctamente.")
            return redirect("usuario_listar")

    # Obtener el código de la primera ficha asociada (si existe)
    ficha_codigo = usuario.fichas.first().codigo if usuario.fichas.exists() else ''

    return render(request, "Usuario/actualizar.html", {
        'usuario': usuario,
        'roles': roles,
        'centros': centros,
        'fichas': fichas,
        'ficha_codigo': ficha_codigo,
    })
def buscar_fichas(request):
    query = request.GET.get('q', '')
    fichas = Ficha.objects.filter(numero__icontains=query)  # O cualquier filtro adecuado para tu caso
    resultados = [
        {'id': ficha.id, 'text': f'{ficha.numero} - {ficha.programa.nombre}'}  # Ajusta según tu modelo
        for ficha in fichas
    ]
    return JsonResponse({'results': resultados})
    
def login_usuario(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '').strip()

            # Validar campos vacíos
            if not username or not password:
                messages.error(request, "Por favor, ingrese usuario y contraseña.")
                return render(request, 'Usuario/login.html')

            # Intentar autenticar
            usuario = authenticate(username=username, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('redireccion_usuario')
            else:
                messages.error(request, "Credenciales incorrectas. Verifique su usuario y contraseña.")

        except ValidationError as e:
            messages.error(request, f"Error de validación: {e}")
        except Exception as e:
            # Captura cualquier error inesperado
            messages.error(request, "Ha ocurrido un error inesperado. Intente de nuevo más tarde.")

    return render(request, 'Usuario/login.html')

    
def logout_usuario(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('home')

@login_required
def redireccionar_usuario(request):
    usuario = request.user

    if usuario.rol.codigo == 'INS':  # Instructor
        return render(request, 'Instructor/instructor.html', {'usuario': usuario})
    
    elif usuario.rol.codigo == 'COO':  # Coordinador
        return redirect('coordinador_listar')
    
    elif usuario.rol.codigo == 'ADE':  # Administrador de Edificios
        return render(request, 'Administrador/listar.html', {'usuario': usuario})
    
    elif usuario.rol.codigo == 'APD':  # Aprendiz
        return render(request, 'Aprendiz/aprendiz.html', {'usuario': usuario})

    elif usuario.rol.codigo == 'ADS':  # Admin supremo
        return render(request, 'Admin/admin.html', {'usuario': usuario})
    
    elif usuario.rol.codigo == 'LDB':  # Lider de Bienestar
        return render(request, 'Admin/admin.html', {'usuario': usuario})

    else:
        return render(request, 'home.html', {'usuario': usuario})  # Para roles no definidos

