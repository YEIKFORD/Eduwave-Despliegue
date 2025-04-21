from rest_framework import serializers
from Eduwave_app.models.municipio import Municipio

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Municipio
        fields='__all__'
