from django.urls import path, include
from ..empresas import views

app_name='empresas'

urlpatterns = [
    path('criar/', views.CriarEmpresa.as_view(), name='criar_empresa'),
    path('editar/<int:pk>', views.EditaEmpresa.as_view(), name='editar_empresa'),

]
