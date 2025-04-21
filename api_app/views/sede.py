from rest_framework import viewsets
from Eduwave_app.models.sede import Sede
from api_app.serializers.sede import SedeSerializer

class SedeViewset(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer