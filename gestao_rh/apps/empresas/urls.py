from django.urls import path, include
from ..empresas import views

app_name='empresas'

urlpatterns = [
    path('criar/', views.CriarEmpresa.as_view(), name='criar'),

]
