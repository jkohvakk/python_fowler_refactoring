

class Customer(object):
    
    def __init__(self, name):
        self._name = name
        self._rentals = []

    def add_rental(self, arg):
        self._rentals.append(arg)
        
    def get_rentals(self):
        return self._rentals

    def get_name(self):
        return self._name

    def statement(self):
        result = 'Rental Record for ' + self.get_name() + '\n'
        for rental in self._rentals:
            # show figures for this rental
            result += '\t' + rental.get_movie().get_title() + '\t' + '{0:.1f}'.format(rental.get_charge()) + '\n'
        # add footer lines
        result += 'Amount owed is ' + '{0:.1f}'.format(self._get_total_charge()) + '\n'
        result += 'You earned ' + str(self._get_total_frequent_renter_points()) + ' frequent renter points'
        return result

    def _get_total_charge(self):
        total_amount = 0
        for rental in self._rentals:
            total_amount += rental.get_charge()
        return total_amount
    
    def _get_total_frequent_renter_points(self):
        frequent_renter_points = 0
        for rental in self._rentals:
            frequent_renter_points+= rental.get_frequent_renter_points()
        return frequent_renter_points
    
    