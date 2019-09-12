from django.urls import path, include
from ..funcionarios import views

app_name='funcionarios'

urlpatterns = [
    path('', views.func_view),

]
