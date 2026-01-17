from django.urls import path
from waste import views

urlpatterns = [
    path("", views.wastelogging_view, name="wastelogging"),
    path("wastedisposal/", views.waste_disposal_view, name="wastedisposal"),
    path("tracking/", views.tracking_view, name="tracking"),
    path("inspection/", views.inspection_view, name="inspection"),
    path("userdashboard/", views.userdashboard_view, name="userdashboard"),
]
