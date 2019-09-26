from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ..departamentos.models import Departamento

class ListDepartamentos(ListView):

    model = Departamento
    template_name = 'departamentos/list_departamentos.html'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)

class CreateDepartamento(CreateView):

    model = Departamento
    fields = ['nome', 'empresa']
    template_name = 'departamentos/create_departamento.html'
    success_url = reverse_lazy('departamentos:list_departamentos')

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()

        return super(CreateDepartamento, self).form_valid(form)

class UpdateDepartamento(UpdateView):

    model = Departamento
    fields = ['nome', 'empresa']
    template_name = 'departamentos/update_departamento.html'

class DeleteDepartamento(DeleteView):

    model = Departamento
    template_name = 'departamentos/delete_departamento.html'
    success_url = reverse_lazy('departamentos:list_departamentos')
