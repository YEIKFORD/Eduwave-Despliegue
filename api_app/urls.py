from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app.views.ambiente import AmbienteViewset
from api_app.views.categoria import CategoriaViewset
from api_app.views.centro_formacion import Centro_FormacionViewset
from api_app.views.ficha import FichaViewset
from api_app.views.inventario import InventarioViewset
from api_app.views.municipio import MunicipioViewset
from api_app.views.novedad import NovedadViewset
from api_app.views.programa_formacion import Programa_FormacionViewset
from api_app.views.red import RedViewset
from api_app.views.regional import RegionalViewset
from api_app.views.rol import RolViewset
from api_app.views.sede import SedeViewset
from api_app.views.sub_categoria import Sub_CategoriaViewset
from api_app.views.tipo_ambiente import Tipo_AmbienteViewset
from api_app.views.tipo_novedad import Tipo_NovedadViewset
from api_app.views.usuario import UsuarioViewset


router= DefaultRouter()
router.register(r'ambientes', AmbienteViewset, basename='ambiente')
router.register(r'categorias', CategoriaViewset, basename='categoria')
router.register(r'centros', Centro_FormacionViewset, basename='centro')
router.register(r'fichas', FichaViewset, basename='ficha')
router.register(r'inventarios', InventarioViewset, basename='inventario')
router.register(r'municipios', MunicipioViewset, basename='municipio')
router.register(r'novedades', NovedadViewset, basename='novedad')
router.register(r'programas', Programa_FormacionViewset, basename='programa')
router.register(r'redes', RedViewset, basename='red')
router.register(r'regionales', RegionalViewset, basename='regionales')
router.register(r'roles', RolViewset, basename='rol')
router.register(r'sedes', SedeViewset, basename='sede')
router.register(r'sub_categorias', Sub_CategoriaViewset, basename='sub_categoria')
router.register(r'tipo_ambientes', Tipo_AmbienteViewset, basename='tipo_ambiente')
router.register(r'tipo_novedades', Tipo_NovedadViewset, basename='tipo_novedad')
router.register(r'usuarios', UsuarioViewset, basename='usuario')


urlpatterns = [
    path('', include(router.urls))
]
