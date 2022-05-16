from rest_framework import viewsets
from chamados.api import serializers
from chamados import models

class ChamadosViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.ChamadosSerializers
    queryset = models.chamado.objects.all()
    