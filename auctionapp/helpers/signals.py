from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from datetime import datetime
from django.utils import timezone


from auctionapp.models import Bid
from auction_internal.constants import choices


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    try:
        if created:
            Token.objects.create(user=instance)
    except Exception as e:
        print(f"Error creating auth token for user {instance}: {e}")


@receiver(post_save, sender=Bid)
def update_highest_bid(sender, instance=None, created=False, **kwargs):
    try:
        if created:
            now = timezone.now()
            item = instance.item
            if item and getattr(item, 'bidding_status', None == choices.BiddingChoices.open) and \
                getattr(item, 'end_time', None) and now <= item.end_time and \
                (item.highest_bid is None or instance.amount > getattr(item, 'highest_bid', None)):
                item.highest_bid = instance.amount
                item.winning_bid = instance
                item.save()
    except Exception as e:
        print(f"Error updating highest bid for item {instance.item}: {e}")
        raise e