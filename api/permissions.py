from api.models import User
from django.contrib.auth.models import Group
from rest_framework import permissions


def is_in_group(user, group_name):
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return False


class HasGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        required_groups = view.permission_groups.get(view.action)
        if required_groups == None:
            return False
        elif '_Public' in required_groups:
            return True
        else:
            return any([is_in_group(request.user, group_name) for group_name in required_groups])


class IsLoggedInUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsLoggedInUserOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser


class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_superuser


class IsDiretorUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_diretor

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_diretor


class IsGestorUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_gestor

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_gestor


class IsDiretorOrGestorUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and (request.user.is_gestor or request.user.is_diretor)


class IsServidorUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_servidor

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_servidor
