from django.contrib.auth.decorators import permission_required
from rest_framework import permissions
from django.contrib.auth.models import User

class Userpermissions(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def checkid(self, request, pk):
        if pk == request.user.Login_id:
            return True
        return False