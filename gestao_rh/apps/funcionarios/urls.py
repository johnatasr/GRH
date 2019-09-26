from django.urls import path, include
from ..funcionarios import views

app_name='funcionarios'

urlpatterns = [
    path('', views.FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', views.FuncionarioCreate.as_view(), name='create_funcionarios'),
    path('editar/<int:pk>', views.FuncionarioUpdate.as_view(), name='update_funcionarios'),
    path('deletar/<int:pk>', views.FuncionarioDelete.as_view(), name='delete_funcionarios'),

]
