from django.urls import path

from . import views

urlpatterns = [
    path("", views.viewMap, name="viewMap"),
    path("sharelocation", views.shareLocation, name="shareLocation")
]
