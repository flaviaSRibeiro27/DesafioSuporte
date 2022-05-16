from rest_framework import serializers
from chamados import models

class ChamadosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.chamado
        fields = '__all__'