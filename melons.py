"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """ You fill in the rest """

    def __init__(self, species, qty, order_type, tax=0.0):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = 0.0

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
        super(DomesticMelonOrder, self).__init__(species, qty, self.order_type, self.tax)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """ You fill in the rest """

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, self.order_type, tax)
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""
        # print self.country_code
        return self.country_code
