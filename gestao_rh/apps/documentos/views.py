from django.shortcuts import render
from django.views.generic import CreateView
from ..documentos.models import Documento


class CreateDocumento(CreateView):

    model = Documento
    fields = ['descricao', 'arquivo']
    template_name = 'documentos/create_document.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

