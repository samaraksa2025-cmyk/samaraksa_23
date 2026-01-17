from django.urls import path
from compliance import views

urlpatterns = [
    path("", views.compliance_view, name="compliance"),
]
