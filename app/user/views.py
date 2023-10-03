"""
Views for the user API
"""

from rest_framework import generics, authentication, permissions
from rest_framework_simplejwt import authentication as authenticationJWT
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class IsCreationOrIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, request, view, object):

        if not request.user.is_authenticated():
            print(request.user.is_authenticated(), 'não ta autenticado')
            if view.action == 'create':
                return True
            else:
                return False
        else:
            return True


class ManagerUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [
        authentication.TokenAuthentication,
        authenticationJWT.JWTAuthentication]
    permission_classes = [IsCreationOrIsAuthenticated,
                          permissions.IsAuthenticated]

    def get_object(self):
        """Retrive and return the authenticated user."""
        return self.request.user
