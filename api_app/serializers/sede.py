from rest_framework import serializers
from Eduwave_app.models.sede import Sede
class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sede
        fields='__all__'
