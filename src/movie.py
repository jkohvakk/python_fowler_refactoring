

class Movie(object):

    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self.set_price_code(price_code)

    def get_price_code(self):
        return self._price.get_price_code()

    def set_price_code(self, arg):
        self._price = {Movie.REGULAR: RegularPrice,
         Movie.CHILDRENS: ChildrensPrice,
         Movie.NEW_RELEASE: NewReleasePrice}[arg]()
    
    def get_title(self):
        return self._title

    def get_charge(self, days_rented):
        charge = 0
        if self.get_price_code() == Movie.REGULAR:
            charge += 2
            if days_rented > 2:
                charge += (days_rented - 2) * 1.5
        elif self.get_price_code() == Movie.NEW_RELEASE:
            charge += days_rented * 3
        elif self.get_price_code() == Movie.CHILDRENS:
            charge += 1.5
            if days_rented > 3:
                charge += (days_rented - 3) * 1.5
        return charge

class Price(object):
    
    def get_price_code(self):
        raise Exception('Price is an abstract class')
    
class RegularPrice(Price):
    
    def get_price_code(self):
        return Movie.REGULAR

class NewReleasePrice(Price):
    
    def get_price_code(self):
        return Movie.NEW_RELEASE

class ChildrensPrice(Price):

    def get_price_code(self):
        return Movie.CHILDRENS

