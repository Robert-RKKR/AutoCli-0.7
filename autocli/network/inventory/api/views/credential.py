# Rest framework import:
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets

# Django import:
from django.shortcuts import get_object_or_404

# Model import:
from network.inventory.models.credential import Credential

# Serializer import:
from ..serializers.credential import CredentialSerializer


class CredentialView(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
