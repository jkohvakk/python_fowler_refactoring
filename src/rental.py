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
        return self.get_movie().get_charge(self.get_days_rented())

    def get_frequent_renter_points(self):
        return self.get_movie().get_frequent_renter_points(self.get_days_rented())







