from django.urls import path
from . import views

urlpatterns = [
    path("", views.ts_dashboard, name="ts_dashboard"),
    path("compliance/", views.ts_compliance, name="ts_compliance"),
    path("waste-reception/", views.ts_waste_reception, name="ts_waste_reception"),
    path("disposal-management/", views.ts_disposal_management, name="ts_disposal_management"),
    path("profile/", views.ts_profile, name="ts_profile"),
]
