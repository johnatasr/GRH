from django.urls import path, include
from ..departamentos import views

app_name='departamentos'

urlpatterns = [
    path('', views.ListDepartamentos.as_view(), name='list_departamentos'),
    path('novo/', views.CreateDepartamento.as_view(), name='create_departamento'),
    path('editar/<int:pk>', views.UpdateDepartamento.as_view(), name='update_departamentos'),
    path('deletar/<int:pk>', views.DeleteDepartamento.as_view(), name='delete_departamentos'),

]
