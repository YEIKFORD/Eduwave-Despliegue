from rest_framework import serializers
from Eduwave_app.models.ficha import Ficha

class FichaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ficha
        fields='__all__'
