from django.db import models
from django.urls import reverse

from ..funcionarios.models import Funcionario

class Documento(models.Model):

    descricao = models.CharField(max_length=100, help_text='Descricao do Documento')
    propietario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('funcionarios:update_funcionarios', args=[self.pertence.id])

    def __str__(self):
        return self.descricao