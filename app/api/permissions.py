from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from rest_framework.views import Request, View


class IsAccountOwner(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if (
            request.method in SAFE_METHODS
            or request.method == "POST"
            or request.user.is_authenticated
        ):
            return True

    def has_object_permission(self, request: Request, view: View, obj: object) -> bool:
        if request.method in "GET":
            return True

        if request.user.is_superuser:
            return True

        if request.user.is_authenticated and obj.id == request.user.id:
            return True

        return False
