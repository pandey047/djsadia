from django.contrib import admin
from .models import *
'''
for custom user
'''
from django.contrib.auth.admin import UserAdmin
from .form import UserProfileChangeForm, UserProfileCreationForm

class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ('email', 'is_staff', "is_active")
    list_filter = ('email', "is_staff", "is_active")
    fieldsets = (
        (None, {"fields":("email", "password")}),
        ("Permissions", {"fields":("is_staff", "is_active")})
    )
    add_fieldsets = (
        (None, {
          "classes":("wide",),
          "fields":("email", "password", "is_staff", "is_active")  
        },),
    )
    search_fields = ("email",)
    ordering = ("email",)
    
admin.site.register(UserProfile, UserProfileAdmin)


