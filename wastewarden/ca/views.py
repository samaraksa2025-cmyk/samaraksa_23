from django.shortcuts import render

def ca_dashboard(request):
    return render(request, "CA_dashB.html")

def ca_profile(request):
    return render(request, "CA_profilepg.html")

def ca_pickup_assign(request):
    return render(request, "CA_pickupassn.html")

def ca_pickup_confirm(request):
    return render(request, "CA_pickupcnfrm.html")
