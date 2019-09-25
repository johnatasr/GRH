from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from ..empresas.models import Empresa
from django.http import HttpResponse
from ..funcionarios.models import Funcionario

class CriarEmpresa(CreateView):

    model = Empresa
    fields = ['nome']

    def form_valid(self, form):

        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()

        return HttpResponse('Salvo')

class EditaEmpresa(UpdateView):

    model = Empresa
    fields = ['nome']

