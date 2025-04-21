from django.contrib import admin
from django.urls import path, include
from Eduwave_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from Eduwave_app import views  


urlpatterns = [
    path('', home, name='home'),
    path('rol/insertar/', rol_insertar, name='rol_insertar'),
    path('rol/listar/', rol_listar, name='rol_listar'),
    path('rol/actualizar/<int:id>/', rol_actualizar, name='rol_actualizar'),
    path('rol/eliminar/<int:id>/', rol_eliminar, name='rol_eliminar'),

    path('coordinador/listar/', coordinador_listar, name='coordinador_listar'),
    path('aprobar_novedad/<int:id>/', aprobar_novedad, name='aprobar_novedad'),

    path('administrador/listar/', administrador_listar, name='administrador_listar'),
    path('evaluar_novedad/<int:id>/', evaluar_novedad, name='evaluar_novedad'),


    path('usuario/insertar/', usuario_insertar, name='usuario_insertar'),
    path('usuario/listar/', usuario_listar, name='usuario_listar'),
    path('usuario/eliminar/<int:id>/', usuario_eliminar, name='usuario_eliminar'),
    path('usuario/actualizar/<int:id>/', usuario_actualizar, name='usuario_actualizar'),
    path('buscar-fichas/', buscar_fichas, name='buscar_fichas'),


    path('usuario/login/', login_usuario, name='login_usuario'),
    path('logout_usuario', logout_usuario, name='logout_usuario'),

    path('inventario/insertar', inventario_insertar, name='inventario_insertar'),
    path('inventario/listar/', inventario_listar, name='inventario_listar'),
    path('inventario/eliminar/<int:id>', inventario_eliminar, name='inventario_eliminar'),
    path('inventario/actualizar/<int:id>', inventario_actualizar, name='inventario_actualizar'),

    path('sede/insertar', sede_insertar, name='sede_insertar'),
    path('sede/listar/', sede_listar, name='sede_listar'),
    path('sede/eliminar/<int:id>', sede_eliminar, name='sede_eliminar'),
    path('sede/actualizar/<int:id>', sede_actualizar, name='sede_actualizar'),
    path('sede/eliminar_seleccionados/', sede_eliminar_seleccionados, name='sede_eliminar_seleccionados'),


    path('categoria/insertar', categoria_insertar, name='categoria_insertar'),
    path('categoria/listar/', categoria_listar, name='categoria_listar'),
    path('categoria/eliminar/<int:id>', categoria_eliminar, name='categoria_eliminar'),
    path('categoria/actualizar/<int:id>', categoria_actualizar, name='categoria_actualizar'),
    path('categorias/eliminar-masivo/', categoria_eliminar_masivo, name='categoria_eliminar_masivo'),

    path('regional/listar',regional_listar , name='regional_listar'),
    path('regional/insertar',regional_insertar , name='regional_insertar'),
    path('regional/eliminar/<int:id>',  regional_eliminar , name='regional_eliminar'),
    path('regional/actualizar/<int:id>', regional_actualizar , name='regional_actualizar'),
    path('regional/eliminar_masivo/', regional_eliminar_masivo, name='regional_eliminar_masivo'),

    
    path('centro_formacion/insertar', centro_formacion_insertar, name='centro_formacion_insertar'),
    path('centro_formacion/listar/', centro_formacion_listar, name='centro_formacion_listar'),
    path('centro_formacion/eliminar/<int:id>', centro_formacion_eliminar, name='centro_formacion_eliminar'),
    path('centro_formacion/actualizar/<int:id>', centro_formacion_actualizar, name='centro_formacion_actualizar'),
    path('centro/eliminar_seleccionados/', centro_formacion_eliminar_seleccionados, name='centro_formacion_eliminar_seleccionados'),


    path('tipo_ambiente/insertar', tipo_ambiente_insertar, name='tipo_ambiente_insertar'),
    path('tipo_ambiente/listar/', tipo_ambiente_listar, name='tipo_ambiente_listar'),
    path('tipo_ambiente/eliminar/<int:id>', tipo_ambiente_eliminar, name='tipo_ambiente_eliminar'),
    path('tipo_ambiente/actualizar/<int:id>', tipo_ambiente_actualizar, name='tipo_ambiente_actualizar'),

    path('ambiente/insertar', ambiente_insertar, name='ambiente_insertar'),
    path('ambiente/listar/', ambiente_listar, name='ambiente_listar'),
    path('ambiente/eliminar/<int:id>', ambiente_eliminar, name='ambiente_eliminar'),
    path('ambiente/actualizar/<int:id>', ambiente_actualizar, name='ambiente_actualizar'),
    path('ambiente/eliminar-varios/', views.ambiente_eliminar_varios, name='ambiente_eliminar_varios'),

    path('sub_categoria/insertar', sub_categoria_insertar, name='sub_categoria_insertar'),
    path('sub_categoria/listar/', sub_categoria_listar, name='sub_categoria_listar'),
    path('sub_categoria/eliminar/<int:id>', sub_categoria_eliminar, name='sub_categoria_eliminar'),
    path('sub_categoria/actualizar/<int:id>', sub_categoria_actualizar, name='sub_categoria_actualizar'),
    path('sub-categorias/', sub_categoria_listar, name='sub_categoria_listar'),

    path('red/insertar', red_insertar, name='red_insertar'),
    path('red/listar/', red_listar, name='red_listar'),
    path('red/eliminar/<int:id>', red_eliminar, name='red_eliminar'),
    path('red/actualizar/<int:id>', red_actualizar, name='red_actualizar'),

    path('programa_formacion/insertar', programa_formacion_insertar, name='programa_formacion_insertar'),
    path('programa_formacion/listar/', programa_formacion_listar, name='programa_formacion_listar'),
    path('programa_formacion/eliminar/<int:id>', programa_formacion_eliminar, name='programa_formacion_eliminar'),
    path('programa_formacion/actualizar/<int:id>', programa_formacion_actualizar, name='programa_formacion_actualizar'),

    path('ficha/insertar', ficha_insertar, name='ficha_insertar'),
    path('ficha/listar/', ficha_listar, name='ficha_listar'),
    path('ficha/eliminar/<int:id>', ficha_eliminar, name='ficha_eliminar'),
    path('ficha/actualizar/<int:id>', ficha_actualizar, name='ficha_actualizar'),

    path('tipo_novedad/insertar', tipo_novedad_insertar, name='tipo_novedad_insertar'),
    path('tipo_novedad/listar/', tipo_novedad_listar, name='tipo_novedad_listar'),
    path('tipo_novedad/eliminar/<int:id>', tipo_novedad_eliminar, name='tipo_novedad_eliminar'),
    path('tipo_novedad/actualizar/<int:id>', tipo_novedad_actualizar, name='tipo_novedad_actualizar'),

    path('municipio/insertar', municipio_insertar, name='municipio_insertar'),
    path('municipio/listar/', municipio_listar, name='municipio_listar'),
    path('municipio/eliminar/<int:id>', municipio_eliminar, name='municipio_eliminar'),
    path('municipio/actualizar/<int:id>', municipio_actualizar, name='municipio_actualizar'),
    path('municipio/eliminar_masivo/', municipio_eliminar_masivo, name='municipio_eliminar_masivo'),

    path('novedad/insertar/', novedad_insertar, name='novedad_insertar'),
    path('novedad/listar/', novedad_listar, name='novedad_listar'),
    path('novedad/actualizar/<int:id>/', novedad_actualizar, name='novedad_actualizar'),
    path('novedad/eliminar/<int:id>/', novedad_eliminar, name='novedad_eliminar'),
    path('api/usuarios/', usuario_search, name='usuario_search'),
    path('novedades/eliminar_masivo/', novedad_eliminar_masivo, name='novedad_eliminar_masivo'),
    path('novedades/academica/', novedad_academica_listar, name='novedad_academica_listar'),



    path('redireccion/', redireccionar_usuario, name='redireccion_usuario'),

    path('novedad/<int:novedad_id>/detalle/', NovedadDetailView.as_view(), name='novedad-detalle'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

