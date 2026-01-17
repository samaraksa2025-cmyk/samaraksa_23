from django.shortcuts import render

def compliance_view(request):
    return render(request, "compliance.html")
