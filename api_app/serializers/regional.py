from rest_framework import serializers
from Eduwave_app.models.regional import Regional
class RegionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Regional
        fields='__all__'
