from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class AppUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ["user_phone", "username"]
    fieldsets = UserAdmin.fieldsets + (("Location", {"fields": ("zipcode",)}),)


admin.site.register(CustomUser, AppUserAdmin)
