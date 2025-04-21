from rest_framework import serializers
from Eduwave_app.models.tipo_novedad import TipoNovedad

class Tipo_NovedadSerializer(serializers.ModelSerializer):
    class Meta:
        model=TipoNovedad
        fields='__all__'
