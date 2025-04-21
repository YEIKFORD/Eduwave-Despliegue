from rest_framework import serializers
from Eduwave_app.models.tipo_ambiente import TipoAmbiente

class Tipo_AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoAmbiente
        fields='__all__'
