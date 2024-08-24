from rest_framework.permissions import BasePermission
from .models import Issue, Comment


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsContributor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' or request.method == 'PATCH':
            return False
        if request.method == 'GET':
            if isinstance(obj, Issue):
                return request.user in obj.project.contributors.all()
            if isinstance(obj, Comment):
                return request.user in obj.issue.project.contributors.all()
        return request.user in obj.contributors.all()
