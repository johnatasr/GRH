from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('funcionarios/', include('apps.funcionarios.urls', namespace='funcionarios')),
    path('', include('apps.core.urls', namespace='core')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('departamentos/', include('apps.departamentos.urls', namespace='departamentos')),
    path('documentos/', include('apps.documentos.urls', namespace='documentos')),
    path('empresa/', include('apps.empresas.urls', namespace='empresa')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
