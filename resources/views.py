from django.shortcuts import render
from .models import ResourcesCategory,profiles
from .serializers import ResourcesCategorySerializer,ProfilesSerializer
from rest_framework import viewsets
# Create your views here.
class ResourceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ResourcesCategory.objects.all()
    serializer_class = ResourcesCategorySerializer

class ProfilesViewSet(viewsets.ModelViewSet):
    queryset = profiles.objects.all()
    serializer_class = ProfilesSerializer