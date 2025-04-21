from rest_framework import viewsets
from Eduwave_app.models.novedad import Novedad
from api_app.serializers.novedad import NovedadSerializer

class NovedadViewset(viewsets.ModelViewSet):
    queryset = Novedad.objects.all()
    serializer_class = NovedadSerializer