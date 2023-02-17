from rest_framework.permissions import BasePermission


class IsSellerUser(BasePermission):

    def has_permission(self, request, view):
        try:
            if request.method and request.method != 'GET':
                if not request.user.is_seller:
                    raise PermissionError("You do not have permission to visit here")
        except Exception as e:
            print(f"Some error occured in seller's permission: {e}")
            return False
        return True