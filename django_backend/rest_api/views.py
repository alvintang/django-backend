from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, permissions, serializers
from rest_api.serializers import UserSerializer, GroupSerializer
from rest_api.permissions import IsOwner

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = []
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser, TokenHasScope]
    required_scopes = ['groups']

# class SignupViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# Create the API views
# class UserList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetails(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class GroupList(generics.ListAPIView):
#     permission_classes = [permissions.IsAdminUser, TokenHasScope]
#     required_scopes = ['groups']
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer



