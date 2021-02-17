from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Права, с помощью которых пользователь сможет изменять и получать только собственные объекты"""

    message = 'Not an owner.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
