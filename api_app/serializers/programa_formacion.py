from rest_framework import serializers
from Eduwave_app.models.programa_formacion import ProgramaFormacion

class Programa_FormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProgramaFormacion
        fields='__all__'
