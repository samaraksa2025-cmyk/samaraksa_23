from django.urls import path
from . import views

urlpatterns = [
    path("", views.rp_dashboard, name="rp_dashboard"),
    path("compliance/", views.rp_compliance, name="rp_compliance"),
    path("admin/", views.rp_admin, name="rp_admin"),
    path("inspection/", views.rp_inspection, name="rp_inspection"),
    path("hospital-register/", views.rp_hospital_register, name="rp_hospital_register"),
    path("waste-analytics/", views.rp_waste_analytics, name="rp_waste_analytics"),
]
