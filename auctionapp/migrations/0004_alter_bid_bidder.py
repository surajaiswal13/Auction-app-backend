# Generated by Django 4.1.6 on 2023-02-14 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0003_alter_item_highest_bid_alter_item_winning_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidder',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]