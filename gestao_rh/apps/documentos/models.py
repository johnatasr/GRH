from django.db import models
from ..funcionarios.models import Funcionario

class Documentos(models.Model):

    descricao = models.CharField(max_length=100, help_text='Descricao do Documento')
    propietario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao