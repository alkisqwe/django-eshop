from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "profileimage",
        "certified",
        "type",
        "plan",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("profileimage","certified","type","plan",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("profileimage","certified","type","plan",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
