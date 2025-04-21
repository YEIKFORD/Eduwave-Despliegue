from rest_framework import serializers
from Eduwave_app.models.categoria import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'
