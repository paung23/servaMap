from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser
from .forms import UserCreationForm, LoginForm


def main(request):
    template = loader.get_template("mainpage.html")
    context = {}
    return HttpResponse(template.render(context, request))


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(request.POST.get("password1"))
            user.save()
            return HttpResponseRedirect("login")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        if email and password:
            login_user = CustomUser.objects.filter(email=email).first()
            if login_user is not None:
                username = login_user.username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("/")
            messages.error(request, "Invalid email or password")
            return HttpResponseRedirect("login")
        else:
            messages.error(request, "Please, write email and password")
            return HttpResponseRedirect("login")

    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form})
