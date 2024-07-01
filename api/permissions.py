from rest_framework import permissions

class ProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.type == 1:
                return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class CommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class CheckoutPermission(permissions.BasePermission):
    def has_permission(self, request,view):
        if(request.user.is_authenticated):
            return True
        return False

    def has_object_permission(self,request,view,obj):
        return False
        
class WishlistPermission(permissions.BasePermission):
    def has_permission(self, request,view):
        if(request.user.is_authenticated):
            return True
        return False

    def has_object_permission(self,request,view,obj):
        if(request.user.is_authenticated):
            return True
        return False

class SavedAddressPermission(permissions.BasePermission):
    def has_permission(self, request,view):
        if(request.user.is_authenticated):
            return True
        return False

    def has_object_permission(self,request,view,obj):
        return False

class SavedPaymentPermission(permissions.BasePermission):
    def has_permission(self, request,view):
        if(request.user.is_authenticated):
            return True
        return False

    def has_object_permission(self,request,view,obj):
        return False

