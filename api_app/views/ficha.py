from rest_framework import viewsets
from Eduwave_app.models.ficha import Ficha
from api_app.serializers.ficha import FichaSerializer

class FichaViewset(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer