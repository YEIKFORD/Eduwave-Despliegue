from rest_framework import serializers
from Eduwave_app.models.inventario import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inventario
        fields='__all__'
