from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from auctionapp.helpers.permissions import IsSellerUser
from auctionapp.models import Item
from auctionapp.serializers.item_serializers import ItemSerializer
from auctionapp.helpers.custom_filters import ItemFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'category', 'end_time']
    permission_classes = [IsAuthenticated, IsSellerUser]
    filterset_class = ItemFilter

    def get_queryset(self):
        if self.request.query_params.get("user"):
            return super().get_queryset().filter(seller=self.request.user).select_related('seller')
        return super().get_queryset()
    
    def perform_create(self, serializer):
        try:
            serializer.validated_data['seller'] = self.request.user
            return super().perform_create(serializer)
        except Exception as e:
            print(f"Something went wrong while creating an item, {e}")
            raise e