from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response

from api.models import User, Car
from api.serializers import *
# Also add these imports
from api.permissions import *

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('profile')
    serializer_class = UserSerializer
    permission_classes = (DjangoModelPermissions, )
    # def list(self, request):
    #     queryset = User.objects.all().select_related('profile')
    #     serializer_class = UserSerializer
    #     permission_classes = (DjangoModelPermissions, )

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all().select_related('profile')
    #     permission_classes = (DjangoModelPermissions, )
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    

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
