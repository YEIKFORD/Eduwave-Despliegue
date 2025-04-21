from rest_framework import viewsets
from Eduwave_app.models.red import Red
from api_app.serializers.red import RedSerializer

class RedViewset(viewsets.ModelViewSet):
    queryset = Red.objects.all()
    serializer_class = RedSerializer