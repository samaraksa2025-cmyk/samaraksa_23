from django.shortcuts import render

def rp_dashboard(request):
    return render(request, "rp_dashboard.html")

def rp_compliance(request):
    return render(request, "rp_compliance.html")

def rp_admin(request):
    return render(request, "rp_admin.html")

def rp_inspection(request):
    return render(request, "rp_inspection.html")

def rp_hospital_register(request):
    return render(request, "rp_hospital_register.html")

def rp_waste_analytics(request):
    return render(request, "rp_waste_analytics.html")
