from djchoices import ChoiceItem, DjangoChoices
from typing import Final


class BiddingChoices(DjangoChoices):
    """
    A class representing the different bidding status choices for an auction item.
    """

    open: Final = ChoiceItem("OPEN", "open")
    closed: Final = ChoiceItem("CLOSED", "closed")
    # coming_soon = ChoiceItem("CS", "Coming Soon")

class CategoryChoices(DjangoChoices):
    """
    A class representing the different category choices for an auction item.
    """

    cars: Final = ChoiceItem("CARS", "cars")
    bikes: Final = ChoiceItem("BIKES", "bikes")
    property: Final = ChoiceItem("PROPERTY", "property")