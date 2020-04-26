from django.urls import path

from . import views

urlpatterns = [
    path("main", views.main, name="main"),
    path("register", views.register, name="register"),
    path("login", views.user_login, name="login"),
]
