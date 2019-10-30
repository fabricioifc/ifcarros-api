from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import DjangoModelPermissions

from api.models import User, Car
from api.serializers import *
# Also add these imports
from api.permissions import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (DjangoModelPermissions, )

    # Add this code block
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (DjangoModelPermissions, )
    # permission_classes = [HasGroupPermission]
    # permission_groups = {
    #     'create': ['DIRETOR', 'GESTOR'],
    #     'destroy': ['DIRETOR', 'GESTOR'],
    #     'update': ['DIRETOR', 'GESTOR'],
    #     'partial_update': ['DIRETOR', 'GESTOR'],
    #     'retrieve': ['DIRETOR', 'GESTOR'],
    #     'list': ['_Public'],
    # }

    # Add this code block
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [IsDiretorOrGestorUser]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]
