from django.db import models
from uuid import uuid4

# Create your models here.


class chamado(models.Model):
    id_chamado = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    assunto = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    data_chamado = models.DateField(auto_now_add=True)
    horas_chamado = models.TimeField(auto_now_add=True)