from rest_framework import viewsets
from Eduwave_app.models.tipo_ambiente import TipoAmbiente
from api_app.serializers.tipo_ambiente import Tipo_AmbienteSerializer

class Tipo_AmbienteViewset(viewsets.ModelViewSet):
    queryset = TipoAmbiente.objects.all()
    serializer_class = Tipo_AmbienteSerializer


