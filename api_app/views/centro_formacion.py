from rest_framework import viewsets
from Eduwave_app.models.centro_formacion import CentroFormacion
from api_app.serializers.centro_formacion import Centro_FormacionSerializer

class Centro_FormacionViewset(viewsets.ModelViewSet):
    queryset = CentroFormacion.objects.all()
    serializer_class = Centro_FormacionSerializer


