# Generated by Django 4.1.6 on 2023-02-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0004_alter_bid_bidder'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['name'], name='auctionapp__name_d6e4fa_idx'),
        ),
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['category'], name='auctionapp__categor_28f1de_idx'),
        ),
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['end_time'], name='auctionapp__end_tim_7bed89_idx'),
        ),
    ]
