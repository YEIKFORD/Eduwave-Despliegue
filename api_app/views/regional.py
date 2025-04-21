from rest_framework import viewsets
from Eduwave_app.models.regional import Regional
from api_app.serializers.regional import RegionalSerializer

class RegionalViewset(viewsets.ModelViewSet):
    queryset = Regional.objects.all()
    serializer_class = RegionalSerializer