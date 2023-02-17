from djchoices import ChoiceItem, DjangoChoices
from typing import Final


class BiddingChoices(DjangoChoices):

    open: Final = ChoiceItem("OPEN", "open")
    closed: Final = ChoiceItem("CLOSED", "closed")
    # coming_soon = ChoiceItem("CS", "Coming Soon")

class CategoryChoices(DjangoChoices):

    cars: Final = ChoiceItem("CARS", "cars")
    bikes: Final = ChoiceItem("BIKES", "bikes")
    property: Final = ChoiceItem("PROPERTY", "property")