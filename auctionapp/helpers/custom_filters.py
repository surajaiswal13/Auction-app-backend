from django_filters import rest_framework as filters
from auctionapp.models import Item


class ItemFilter(filters.FilterSet):
    category = filters.CharFilter(lookup_expr='iexact')
    end_time = filters.DateTimeFilter(lookup_expr='gte')
    bidding_status = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Item
        fields = ['category', 'end_time', 'bidding_status']