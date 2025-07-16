from django.urls import path
from .views import k8s_ingress_view

urlpatterns = [
    path('', k8s_ingress_view, name='k8s_ingress'),
]