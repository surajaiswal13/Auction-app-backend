from django.apps import AppConfig


class AuctionappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auctionapp'

    def ready(self):
        import auctionapp.helpers.signals
