from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner or request.user.is_staff


class CommentsDeletePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user == obj.post.owner:
            return True
        return bool(request.user and request.user.is_staff)
