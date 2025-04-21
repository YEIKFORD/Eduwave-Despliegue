from rest_framework import viewsets
from Eduwave_app.models.usuario import Usuario
from api_app.serializers.usuario import UsuarioSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer