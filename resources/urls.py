from django.urls import path, include

from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register('ResourceCategory',ResourceCategoryViewSet)
router.register('Profiles',ProfilesViewSet)

urlpatterns = [
    
    
    # path('', ResourceCategoryViewSet.as_view({'get': 'list'}) ,name="resources"),
    # path('current_datetime/', current_datetime),
    path('', include(router.urls)),

]
