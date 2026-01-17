from django.shortcuts import render

def wastelogging_view(request):
    return render(request, "wastelogging.html")

def waste_disposal_view(request):
    return render(request, "waste_disposal.html")

def tracking_view(request):
    return render(request, "tracking.html")

def inspection_view(request):
    return render(request, "inspection.html")

def userdashboard_view(request):
    return render(request, "user_dashboard.html")