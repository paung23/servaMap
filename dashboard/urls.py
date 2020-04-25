from django.urls import path

from . import views

urlpatterns = [
    path("", views.viewMap, name="viewDashboard"),
    path("sharelocation", views.shareLocation, name="shareLocation")
]
