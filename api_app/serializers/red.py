from rest_framework import serializers
from Eduwave_app.models.red import Red
class RedSerializer(serializers.ModelSerializer):
    class Meta:
        model=Red
        fields='__all__'
