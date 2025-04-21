from rest_framework import serializers
from Eduwave_app.models.subcategoria import SubCategoria

class Sub_CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategoria
        fields='__all__'
