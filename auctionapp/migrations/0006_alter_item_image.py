# Generated by Django 4.1.6 on 2023-02-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0005_item_auctionapp__name_d6e4fa_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]