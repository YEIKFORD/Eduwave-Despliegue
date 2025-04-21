from rest_framework import viewsets
from Eduwave_app.models.programa_formacion import ProgramaFormacion
from api_app.serializers.programa_formacion import Programa_FormacionSerializer

class Programa_FormacionViewset(viewsets.ModelViewSet):
    queryset = ProgramaFormacion.objects.all()
    serializer_class = Programa_FormacionSerializer


