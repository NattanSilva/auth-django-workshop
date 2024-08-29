from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import UserViewset, LoginViewset

router = DefaultRouter()
router.register(r"users", UserViewset)
router.register(r"login", LoginViewset, basename="login")

urlpatterns = [
    path("v1/", include(router.urls)),
]
