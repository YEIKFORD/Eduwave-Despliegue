from rest_framework import viewsets
from Eduwave_app.models.inventario import Inventario
from api_app.serializers.inventario import InventarioSerializer

class InventarioViewset(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer