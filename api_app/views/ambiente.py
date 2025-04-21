from rest_framework import viewsets
from Eduwave_app.models.ambiente import Ambiente
from api_app.serializers.ambiente import AmbienteSerializer

class AmbienteViewset(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer