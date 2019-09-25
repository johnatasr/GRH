from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from ..funcionarios.models import Funcionario


class FuncionariosList(ListView):

    model = Funcionario
    template_name = 'funcionarios/listar_funcionarios.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioUpdate(UpdateView):

    model = Funcionario
    fields = ['nome', 'departamentos']
    template_name = 'funcionarios/update_funcionarios.html'

class FuncionarioDelete(DeleteView):

    model = Funcionario
    template_name = 'funcionarios/delete_funcionarios.html'
    success_url = reverse_lazy('funcionarios:list_funcionarios')

class FuncionarioCreate(CreateView):

    model = Funcionario
    template_name = 'fncionarios/create_funcionarios.html'

    def form_valid(self, form):

        funcionario = self.form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.usuario = User.objects.create(username=username)
        funcionario.save()

        return super(FuncionarioCreate, self).form_valid(form)