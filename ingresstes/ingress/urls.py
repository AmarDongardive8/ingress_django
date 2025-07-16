from django.urls import path
from .views import k8s_ingress_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', k8s_ingress_view, name='k8s_ingress')
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)