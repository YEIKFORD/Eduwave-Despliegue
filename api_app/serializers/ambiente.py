from rest_framework import serializers
from Eduwave_app.models.ambiente import Ambiente

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ambiente
        fields='__all__'
