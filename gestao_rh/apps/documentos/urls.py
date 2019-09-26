from ..documentos import views
from django.urls import path, include

app_name = 'documentos'

urlpatterns = [
    path('novo/<int:funcionario_id>', views.CreateDocumento.as_view(), name='create_documento'),

]