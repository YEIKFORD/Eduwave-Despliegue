from rest_framework import viewsets
from Eduwave_app.models.tipo_novedad import TipoNovedad
from api_app.serializers.tipo_novedad import Tipo_NovedadSerializer

class Tipo_NovedadViewset(viewsets.ModelViewSet):
    queryset = TipoNovedad.objects.all()
    serializer_class = Tipo_NovedadSerializer


