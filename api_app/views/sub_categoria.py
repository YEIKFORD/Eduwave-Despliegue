from rest_framework import viewsets
from Eduwave_app.models.subcategoria import SubCategoria
from api_app.serializers.sub_categoria import Sub_CategoriaSerializer

class Sub_CategoriaViewset(viewsets.ModelViewSet):
    queryset = SubCategoria.objects.all()
    serializer_class = Sub_CategoriaSerializer


