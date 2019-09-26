from django.db import models
from django.shortcuts import redirect

from ..empresas.models import Empresa


class Departamento(models.Model):

    nome = models.CharField(max_length=100, help_text='Nome do Departamento')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return redirect('departamentos:list_departamentos')

    def __str__(self):
        return self.nome