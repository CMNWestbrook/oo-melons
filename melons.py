"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """ You fill in the rest """

    def __init__(self, species, qty, order_type):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = None

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """ You fill in the rest """

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, order_type="domestic", tax=0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """ You fill in the rest """

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, order_type="international", tax=0.17)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
