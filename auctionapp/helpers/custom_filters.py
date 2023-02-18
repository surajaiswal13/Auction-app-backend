from django_filters import rest_framework as filters
from auctionapp.models import Item


class ItemFilter(filters.FilterSet):
    """
    A filter for the Item model that filters by category, end_time, and bidding_status.

    Attributes:
    - category: A case-insensitive filter for the item category.
    - end_time: A filter that only returns items with end times greater than or equal to the provided value.
    - bidding_status: A case-insensitive filter for the bidding status of the item.
    """

    category = filters.CharFilter(lookup_expr='iexact')
    end_time = filters.DateTimeFilter(lookup_expr='gte')
    bidding_status = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Item
        fields = ['category', 'end_time', 'bidding_status']