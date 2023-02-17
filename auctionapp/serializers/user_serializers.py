from rest_framework import serializers
from auctionapp.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_seller', 'is_bidder', )
        extra_kwargs = {
            'password': {'write_only': True}
        }

class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_seller', 'is_bidder', )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        try:
            user = User.objects.create_user(validated_data['username'], validated_data['email'], 
                                            validated_data['password'], is_seller=validated_data['is_seller'], 
                                            is_bidder=validated_data['is_bidder'])
            return user
        except Exception as e:
            print(f"Something went wrong while creating user, {e}")
            raise e