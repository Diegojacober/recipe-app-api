from rest_framework import permissions


class IsCreationOrIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        if not request.user.is_authenticated:
            if view.action == 'create':
                return True
            else:
                return False
        else:
            return True
