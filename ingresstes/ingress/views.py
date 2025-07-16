from django.shortcuts import render

def k8s_ingress_view(request):
    return render(request, 'k8sinfo.html')
