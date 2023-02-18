from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token
from auctionapp.viewsets.user_viewsets import UserLoginAPIView, UserViewSet, RegisterUserAPIView
from auctionapp.viewsets.item_viewsets import ItemViewSet
from auctionapp.viewsets.bid_viewsets import BidViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('items', ItemViewSet)
router.register('bids', BidViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', UserLoginAPIView.as_view(), name='login'),
    path('auth/register/', RegisterUserAPIView.as_view(), name='register'),
]