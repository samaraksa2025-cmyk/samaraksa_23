from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),        
    path("compliance/", include("compliance.urls")),
    path("waste/", include("waste.urls")),
    path("rp/",include("rp.urls")),
    path("tf/", include("tf.urls")),
    path("ca/", include("ca.urls")),

]
