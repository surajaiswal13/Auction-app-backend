from rest_framework.permissions import BasePermission


class IsSellerUser(BasePermission):
    """
    A custom permission class to allow access to seller users only.
    """

    def has_permission(self, request, view):
        """
        Check if the user is a seller.

        Args:
            request: The HTTP request being made.
            view: The view requesting access.

        Returns:
            bool: True if the user is a seller and the request method is not GET, False otherwise.
        """
        
        try:
            if request.method and request.method != 'GET':
                if not request.user.is_seller:
                    raise PermissionError("You do not have permission to visit here")
        except Exception as e:
            print(f"Some error occured in seller's permission: {e}")
            return False
        return True