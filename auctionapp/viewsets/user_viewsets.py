# from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from auctionapp.models import User
from auctionapp.serializers.user_serializers import UserSerializer, RegisterUserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for CRUD operations on the User model.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserLoginAPIView(ObtainAuthToken):
    """
    API view to logging in users.
    """

    def post(self, request, *args, **kwargs):
        """
        Customized the post method to return a custom response when after logging in a user
        """

        try:
            serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                return None
            response = {
                'token': token.key,
                'id': user.pk,
                'username': user.username,
                'seller': user.is_seller,
                'bidder': user.is_bidder
            }
            
            return Response(response)
        except Exception as e:
            print(f"Something went wrong while logging in , {e}")
            raise e
    
class RegisterUserAPIView(generics.GenericAPIView):
    """
    API view to register new users.
    """

    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """
        Customized the post method to return a custom response when after registering a user
        """

        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            token = Token.objects.get_or_create(user=user)
            response = {
                'token': token[0].key,
                'id': user.pk,
                'user': user.username,
                'seller': user.is_seller,
                'bidder': user.is_bidder
            }
            
            return Response(response)
        except Exception as e:
            print(f"Something went wrong while registering the user , {e}")
            raise e