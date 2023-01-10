from django.db import models


'''
Abstract User -- user already created by django, we can change them
AbstractBaseUser -- empty model is provided with basic functionality but super staff, staff this type of functionalities are not provided

'''
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
from .managers import UserProfileManager


class UserProfile(AbstractUser):
    username = None
    email = models.EmailField(("Email Addresss"), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserProfileManager()
    
    def __str__(self):
        return self.email



