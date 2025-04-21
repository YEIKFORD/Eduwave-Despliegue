from rest_framework import viewsets
from Eduwave_app.models.rol import Rol
from api_app.serializers.rol import RolSerializer

class RolViewset(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer