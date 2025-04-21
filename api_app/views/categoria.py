from rest_framework import viewsets
from Eduwave_app.models.categoria import Categoria
from api_app.serializers.categoria import CategoriaSerializer

class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer