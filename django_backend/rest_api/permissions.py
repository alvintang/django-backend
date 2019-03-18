from django.contrib.auth.models import Group
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    # message = 'Admin permission required'

    def has_permission(self, request, view):
    	group_name = 'Owner'
    	try:
        	return Group.objects.get(name=group_name).user_set.filter(id=request.user.id).exists()
    	except Group.DoesNotExist:
	        return None

class IsCustomer(permissions.BasePermission):
    # message = 'Admin permission required'

    def has_permission(self, request, view):
    	group_name = 'Customer'
    	try:
        	return Group.objects.get(name=group_name).user_set.filter(id=request.user.id).exists()
    	except Group.DoesNotExist:
	        return None