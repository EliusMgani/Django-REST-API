from rest_framework import permissions

class IsOwnerOrReadyOnly(permissions.BasePermission):
    # Custom Permissions to only allow Owners of an Object to Edit it

    def has_object_permission(self, request, view, obj):
        # Read Permissions are allowed to any request,
        # So we will always allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the Owner of the Snippet
        return obj.owner == request.user