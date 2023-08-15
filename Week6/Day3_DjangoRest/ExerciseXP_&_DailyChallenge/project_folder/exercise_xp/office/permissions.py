from rest_framework import permissions

class IsAuthenticatedAdmin(permissions.BasePermission):
    def has_permission(self,request,view): 
        if request.method == 'GET':
            return request.user.is_authenticated
        elif request.method in ['POST','PATCH','DELETE']:
            if request.user.is_authenticated:
                return request.user.is_staff
        
    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH','DELETE']:
         return obj.author == request.user 