from rest_framework import serializers
from Eduwave_app.models.novedad import Novedad


class NovedadSerializer(serializers.ModelSerializer):
    apto = serializers.SerializerMethodField()
    evidencia = serializers.SerializerMethodField()
    tipo_novedad = serializers.CharField(source='tipo_novedad.nombre')
    creado_por = serializers.SerializerMethodField()
    numero_ambiente = serializers.SerializerMethodField()  # <-- Aquí lo agregas

    class Meta:
        model = Novedad
        fields = '__all__'
        extra_fields = ['numero_ambiente']  # por si usas esto en otro lado

    def get_apto(self, obj):
        if obj.ambiente:
            return obj.ambiente.get_estado_display()
        return None

    def get_evidencia(self, obj):
        if obj.evidencia:
            return {
                'nombre': obj.evidencia.name.split('/')[-1],
                'url': obj.evidencia.url
            }
        return None

    def get_creado_por(self, obj):
        if obj.creado_por:
            return obj.creado_por.get_full_name() or obj.creado_por.username
        return 'Desconocido'

    def get_numero_ambiente(self, obj):
        if obj.ambiente:
            return obj.ambiente.numero_ambiente  # asegúrate que el modelo Ambiente tenga este campo
        return None