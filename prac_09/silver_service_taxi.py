from prac_09.taxi import Taxi
class SilverServiceTaxi(Taxi):
    flagfall = 4.50    # Extra charge for each new fare
    def __init__(self, name, fuel, price_per_km, fanciness):
        super().__init__(name, fuel, price_per_km)
        self.price_per_km *= fanciness
        self.fanciness = fanciness


    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.fanciness
    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"