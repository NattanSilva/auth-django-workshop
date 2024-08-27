from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import UserViewset

router = DefaultRouter()
router.register(r"users", UserViewset)

urlpatterns = [
    path("v1/", include(router.urls)),
]
