from rest_framework import viewsets
from Eduwave_app.models.municipio import Municipio
from api_app.serializers.municipio import MunicipioSerializer

class MunicipioViewset(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer