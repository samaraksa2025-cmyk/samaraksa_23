from django.urls import path
from . import views

urlpatterns = [
    path("", views.ca_dashboard, name="ca_dashboard"),
    path("profile/", views.ca_profile, name="ca_profile"),
    path("pickup-assign/", views.ca_pickup_assign, name="ca_pickup_assign"),
    path("pickup-confirm/", views.ca_pickup_confirm, name="ca_pickup_confirm"),
]
