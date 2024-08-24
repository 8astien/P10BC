from rest_framework.permissions import BasePermission, SAFE_METHODS # type: ignore


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser
