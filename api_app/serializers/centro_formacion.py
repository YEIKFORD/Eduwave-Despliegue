from rest_framework import serializers
from Eduwave_app.models.centro_formacion import CentroFormacion

class Centro_FormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=CentroFormacion
        fields='__all__'
