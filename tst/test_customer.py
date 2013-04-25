import unittest
from customer import Customer
from movie import Movie
from rental import Rental


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self._customer = Customer('Sallie')

    def test_add_rental(self):
        movie = Movie('Gone with the Wind', Movie.REGULAR)
        rental = Rental(movie, 3) # 3 day rental
        self._customer.add_rental(rental)
        # not possible to verify because no public interface for that

    def test_get_name(self):
        self.assertEquals('Sallie', self._customer.get_name())

    def test_statement_for_regular_movie(self):
        movie = Movie('Gone with the Wind', Movie.REGULAR)
        rental = Rental(movie, 3) # 3 day rental
        self._customer.add_rental(rental)
        expected = """Rental Record for Sallie
\tGone with the Wind\t3.5
Amount owed is 3.5
You earned 1 frequent renter points"""
        statement = self._customer.statement()
        self.assertEquals(expected, statement)
    
    def test_statement_for_new_release_movie(self):
        movie = Movie('Star Wars', Movie.NEW_RELEASE)
        rental = Rental(movie, 3) # 3 day rental
        self._customer.add_rental(rental)
        expected = """Rental Record for Sallie
\tStar Wars\t9.0
Amount owed is 9.0
You earned 2 frequent renter points"""
        statement = self._customer.statement()
        self.assertEquals(expected, statement)
    
    def test_statement_for_childrens_movie(self):
        movie = Movie('Madagascar', Movie.CHILDRENS)
        rental = Rental(movie, 3) # 3 day rental
        self._customer.add_rental(rental)
        expected = """Rental Record for Sallie
\tMadagascar\t1.5
Amount owed is 1.5
You earned 1 frequent renter points"""
        statement = self._customer.statement()
        self.assertEquals(expected, statement)
    
    def test_statement_for_many_movies_and_rentals(self):
        customer1 = Customer('David')
        movie1 = Movie('Madagascar', Movie.CHILDRENS)
        rental1 = Rental(movie1, 6) # 6 day rental
        movie2 = Movie('Star Wars', Movie.NEW_RELEASE)
        rental2 = Rental(movie2, 2) # 2 day rental
        movie3 = Movie('Gone with the Wind', Movie.REGULAR)
        rental3 = Rental(movie3, 8) # 8 day rental
        customer1.add_rental(rental1)
        customer1.add_rental(rental2)
        customer1.add_rental(rental3)
        expected = """Rental Record for David
\tMadagascar\t6.0
\tStar Wars\t6.0
\tGone with the Wind\t11.0
Amount owed is 23.0
You earned 4 frequent renter points"""
        statement = customer1.statement()
        self.assertEquals(expected, statement)
    
    # TODO make test for price breaks in code.


if __name__ == '__main__':
    #import sys; sys.argv = ['', 'Test.testName']
    unittest.main()