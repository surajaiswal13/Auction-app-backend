from rest_framework import serializers
from auctionapp.models import Item, User


class UserItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        read_only_fields = ('id', 'username', 'email')

class ItemSerializer(serializers.ModelSerializer):
    seller = UserItemSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'starting_price', 
                  'end_time', 'highest_bid', 'bidding_status', 'category', 'image', 'seller')
        read_only_fields = ('highest_bid', )