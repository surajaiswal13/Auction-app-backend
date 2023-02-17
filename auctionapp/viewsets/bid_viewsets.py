from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.utils import timezone

from auctionapp.serializers.bid_serializers import BidSerializer
from auctionapp.models import Bid
from auction_internal.constants import choices


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.query_params.get('user'):
            return super().get_queryset().filter(bidder=self.request.user).select_related('item')
        return super().get_queryset()
    
    def validate_item_status(self, item):
        now = timezone.now()
        try:
            if item and (item.bidding_status != choices.BiddingChoices.open) or \
                now > item.end_time:
                if item.bidding_status  == choices.BiddingChoices.open:
                    item.bidding_status = choices.BiddingChoices.closed
                    item.save()
                raise ValidationError({'error': 'Cannot place bid on a closed item'})
        except Exception as e:
            raise ValidationError({'error': 'An error occurred while validating item status.'})

    def perform_create(self, serializer):
        try:
            item = serializer.validated_data.get('item')
            self.validate_item_status(item)
            serializer.validated_data['bidder'] = self.request.user
            return super().perform_create(serializer)
        except Exception as e:
            print(f"Something went wrong while creating a bid, {e}")
            raise e


    def perform_update(self, serializer):
        try:
            item = serializer.validated_data.get('item')
            self.validate_item_status(item)
            return super().perform_update(serializer)
        except Exception as e:
            print(f"Something went wrong while updating a bid, {e}")
            raise e