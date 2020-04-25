from django.http import HttpResponse
from django.shortcuts import render


def viewMap(request):
    return render(request, "dashboard/map.html")


def shareLocation(request):
    if request.method == "POST":
        user_location_latitude = request.POST.get("user_location_latitude")
        user_location_longitude = request.POST.get("user_location_longitude")

        return HttpResponse("Thank you for sharing your location!")
    else:
        return HttpResponse("Request method is not a GET")
