from rest_framework import permissions

# custom permissin class for only created person can edit others can view
class IsCreatedByOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user

 # custom permisstion class for only candidate edit or delete candidate work history othes can view
class IsCandidateOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.history_user == request.user