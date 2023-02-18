from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.utils import timezone

from auctionapp.serializers.bid_serializers import BidSerializer
from auctionapp.models import Bid
from auction_internal.constants import choices


class BidViewSet(viewsets.ModelViewSet):
    """
    A viewset for CRUD operations on the Bid model.

    Attributes:
        queryset (QuerySet): A QuerySet containing all Bid objects.
        serializer_class (Serializer): A serializer class for Bid objects.
        permission_classes (list): A list of permission classes for the viewset.
    """

    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns a filtered queryset for Bids based on query parameters.
        If 'user' parameter is passed, returns Bids placed by the requesting user,
        else all bids are returned.
        """

        if self.request.query_params.get('user'):
            return super().get_queryset().filter(bidder=self.request.user).select_related('item')
        return super().get_queryset()
    
    def validate_item_status(self, item):
        """
        Validates the status of an item and raises a ValidationError if the item is closed or the bidding is over.
        If the item is open, updates its status to closed and saves it.

        Args:
            item (Item): An Item object to validate.

        Raises:
            ValidationError: If the item is closed or the bidding is over.
        """

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
        """
        Overrides the default perform_create method to validate the item status before creating a new Bid object.

        Args:
            serializer (BidSerializer): A serializer instance containing validated data for the new Bid object.

        Returns:
            A new Bid object.
        """

        try:
            item = serializer.validated_data.get('item')
            self.validate_item_status(item)
            serializer.validated_data['bidder'] = self.request.user
            return super().perform_create(serializer)
        except Exception as e:
            print(f"Something went wrong while creating a bid, {e}")
            raise e


    def perform_update(self, serializer):
        """
        Overrides the default perform_update method to validate the item status before updating an existing Bid object.

        Args:
            serializer (BidSerializer): A serializer instance containing validated data for the updated Bid object.

        Returns:
            An updated Bid object.
        """
        
        try:
            item = serializer.validated_data.get('item')
            self.validate_item_status(item)
            return super().perform_update(serializer)
        except Exception as e:
            print(f"Something went wrong while updating a bid, {e}")
            raise e