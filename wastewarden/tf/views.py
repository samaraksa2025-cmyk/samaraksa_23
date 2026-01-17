from django.shortcuts import render

def ts_dashboard(request):
    return render(request, "tf_dashboard.html")

def ts_compliance(request):
    return render(request, "tf_compliance.html")

def ts_waste_reception(request):
    return render(request, "tf_waste_reception.html")

def ts_disposal_management(request):
    return render(request, "tf_disposal_management.html")

def ts_profile(request):
    return render(request, "tf_profile_page.html")
