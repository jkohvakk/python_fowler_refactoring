from movie import Movie

class Rental(object): 
    
    def __init__(self, movie, days_rented):
        self._movie = movie
        self._days_rented = days_rented

    def get_days_rented(self):
        return self._days_rented

    def get_movie(self):
        return self._movie

    def get_charge(self):
        amount = 0
        if self.get_movie().get_price_code() == Movie.REGULAR:
            amount += 2
            if self.get_days_rented() > 2:
                amount += (self.get_days_rented() - 2) * 1.5
        elif self.get_movie().get_price_code() == Movie.NEW_RELEASE:
            amount += self.get_days_rented() * 3
        elif self.get_movie().get_price_code() == Movie.CHILDRENS:
            amount += 1.5
            if self.get_days_rented() > 3:
                amount += (self.get_days_rented() - 3) * 1.5
        return amount







