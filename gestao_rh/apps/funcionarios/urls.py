from django.urls import path, include
from ..funcionarios import views

urlpatterns = [
    path('', views.func_view),

]
