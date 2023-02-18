from rest_framework import serializers
from auctionapp.models import Item, User


class UserItemSerializer(serializers.ModelSerializer):
    """
    Serializer for User model used in ItemSerializer
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'email', )
        read_only_fields = ('id', 'username', 'email', )

class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for Item model.

    Includes a nested UserItemSerializer to serialize the seller field of the Item model.
    Only the 'highest_bid' and 'seller' field is read-only.
    """

    seller = UserItemSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'starting_price', 
                  'end_time', 'highest_bid', 'bidding_status', 'category', 'image', 'seller', )
        read_only_fields = ('highest_bid', )