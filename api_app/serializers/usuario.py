from rest_framework import serializers
from Eduwave_app.models.usuario import Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields='__all__'
