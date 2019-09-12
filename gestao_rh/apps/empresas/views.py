from django.shortcuts import render
from django.views.generic.edit import CreateView
from ..empresas.models import Empresa
from django.http import HttpResponse

class CriarEmpresa(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):

        obj = form.save
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()

        return HttpResponse('Salvo')