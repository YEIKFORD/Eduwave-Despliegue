from rest_framework import serializers
from Eduwave_app.models.rol import Rol
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rol
        fields='__all__'
