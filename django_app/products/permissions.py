from rest_framework import permissions


class ReadOnlyPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)


class LogRetrieves(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'log_event'):
            is_admin = bool(request.user and request.user.is_staff)
            if request.method in permissions.SAFE_METHODS and not is_admin:
                obj.log_event
        return True

    def has_permission(self, request, view):
        return True
