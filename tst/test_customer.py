import unittest
from customer import Customer
from movie import Movie
from rental import Rental

TEST_MOVIES = (('Gone with the Wind', Movie.REGULAR), 
               ('Star Wars', Movie.NEW_RELEASE),
               ('Madagascar', Movie.CHILDRENS))

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self._customer = Customer('Sallie')
        self._create_movies()
        
    def _create_movies(self):
        self._movies = {}
        for movie in TEST_MOVIES:
            self._movies[movie[0]] = Movie(*movie)

    def test_add_rental(self):
        movie = Movie('Gone with the Wind', Movie.REGULAR)
        rental = Rental(movie, 3) # 3 day rental
        self._customer.add_rental(rental)
        self.assertIn(rental, self._customer.get_rentals())

    def test_get_name(self):
        self.assertEquals('Sallie', self._customer.get_name())

    def rent(self, name, duration):
        rental = Rental(self._movies[name], duration)
        self._customer.add_rental(rental)

    def check_statement(self, expected):
        self.assertEquals(expected, self._customer.statement())

    def test_statement_for_regular_movie(self):
        self.rent('Gone with the Wind', 3)
        self.check_statement("""Rental Record for Sallie
\tGone with the Wind\t3.5
Amount owed is 3.5
You earned 1 frequent renter points""")
    
    def test_statement_for_new_release_movie(self):
        self.rent('Star Wars', 3)
        self.check_statement("""Rental Record for Sallie
\tStar Wars\t9.0
Amount owed is 9.0
You earned 2 frequent renter points""")
    
    def test_statement_for_childrens_movie(self):
        self.rent('Madagascar', 3)
        self.check_statement("""Rental Record for Sallie
\tMadagascar\t1.5
Amount owed is 1.5
You earned 1 frequent renter points""")
    
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