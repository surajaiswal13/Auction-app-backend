from rest_framework import serializers
from auctionapp.models import Bid


class BidSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    item_winning_bid = serializers.CharField(source='item.winning_bid', read_only=True)
    item_end_time = serializers.CharField(source='item.end_time', read_only=True)

    class Meta:
        model = Bid
        fields = ('item_name', 'item_winning_bid', 'item_end_time', 'bidder', 'amount', 'item', )
        read_only_fields = ('bidder', )