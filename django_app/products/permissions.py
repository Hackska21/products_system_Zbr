from rest_framework import permissions


class ReadOnlyPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)


class LogRetrieves(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        is_admin = bool(request.user and request.user.is_staff)
        if not is_admin and hasattr(obj, 'log_event'):
            if request.method in permissions.SAFE_METHODS:
                obj.log_event
        return True

    def has_permission(self, request, view):
        return True
