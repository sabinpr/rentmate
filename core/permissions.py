from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role in ['admin', 'superadmin']


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Safe methods: allow read-only access for everyone
        if request.method in SAFE_METHODS:
            return True
        
        # Only the owner or admin/superadmin can modify
        return (
            request.user.is_authenticated and (
                obj.owner == request.user or 
                request.user.role in ['admin', 'superadmin']
            )
        )


class IsSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Tenants and Admins can view; only Admin can update
        return (
            request.user == obj.user or
            request.user.role in ['admin', 'superadmin']
        )
