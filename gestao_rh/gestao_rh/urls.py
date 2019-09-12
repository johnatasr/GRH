from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('apps.funcionarios.urls', namespace='funcionarios')),
    path('', include('apps.core.urls', namespace='core')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('departamentos/', include('apps.departamentos.urls')),
    path('empresa/', include('apps.empresas.urls', namespace='empresa')),
]
