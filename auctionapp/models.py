from django.contrib.auth.models import AbstractUser
from django.db import models
from auction_internal.constants import choices

# Create your models here.

class User(AbstractUser):
    """
    Custom User model with additional fields for seller and bidder flags
    """

    is_seller = models.BooleanField(default=False)
    is_bidder = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Item(models.Model):
    """
    Model representing an auction item
    """

    name = models.CharField(max_length=244)
    description = models.TextField()
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    end_time = models.DateTimeField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items', blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bidding_status = models.CharField(max_length=10, choices=choices.BiddingChoices.choices)
    winning_bid = models.ForeignKey('Bid', on_delete=models.CASCADE, related_name='item_won', blank=True, null=True)
    category = models.CharField(max_length=10, choices=choices.CategoryChoices.choices)
    is_updated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
    class Meta:
        indexes = [
            models.Index(fields=['name',]),
            models.Index(fields=['category',]),
            models.Index(fields=['end_time',])
        ]

class Bid(models.Model):
    """
    Model representing a bid on an auction item
    """

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder.username} bid {self.amount} on {self.item.name}"


class Notification(models.Model):
    """
    Model representing a notification message to a user
    """

    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.recipient.username}"