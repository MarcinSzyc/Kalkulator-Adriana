from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('products', ProductView)

urlpatterns = [
    path('', include(router.urls)),
]