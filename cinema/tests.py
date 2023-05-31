import unittest
from cinema import *


class TestMovie(unittest.TestCase):
    def test_add_movie(self):
        # Test adding a new movie
        Movie.add_movie('The Shawshank Redemption', 'Frank Darabont', '2h 22min', 1994, 18)
        self.assertIn('The Shawshank Redemption', [movie['name'] for movie in get_movie_database().values()])

        # Test adding an existing movie
        with self.assertRaises(ValueError):
            Movie.add_movie('The Shawshank Redemption', 'Frank Darabont', '2h 22min', 1994, 18)

    def test_edit_movie(self):
        # Test editing an existing movie
        movie = get_movie_database()['1']
        Movie.edit_movie('1', 'The Godfather', 'Francis Ford Coppola', '2h 55min', 1972, 18, 'A classic mafia movie')
        edited_movie = get_movie_database()['1']
        self.assertNotEqual(movie['name'], edited_movie['name'])
        self.assertEqual(edited_movie['name'], 'The Godfather')
        self.assertEqual(edited_movie['director'], 'Francis Ford Coppola')
        self.assertEqual(edited_movie['duration_time'], '2h 55min')
        self.assertEqual(edited_movie['product_year'], 1972)
        self.assertEqual(edited_movie['age_limit'], 18)
        self.assertEqual(edited_movie['description'], 'A classic mafia movie')

        # Test editing a non-existing movie
        with self.assertRaises(KeyError):
            Movie.edit_movie('10', 'The Shawshank Redemption', 'Frank Darabont', '2h 22min', 1994, 18, 'so sexsi')

    def test_delete_movie(self):
        # Test deleting an existing movie
        Movie.delete_movie('1')
        self.assertNotIn('1', get_movie_database().keys())

        # Test deleting a non-existing movie
        with self.assertRaises(KeyError):
            Movie.delete_movie('10')

    def test_show_movie(self):
        # Test showing all movies        # Redirect print output to a variable
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output

        Movie.show_movie()

        # Reset print output
        sys.stdout = sys.__stdout__

        # Check if the output matches
        self.assertEqual(captured_output.getvalue(), '(2) - The Shawshank Redemption\n')

    def test_generate_id(self):
        # Test generating a new movie id
        movie_id = Movie.generate_id()
        self.assertIsInstance(movie_id, str)
        self.assertGreater(int(movie_id), 1)



class TestCinema(unittest.TestCase):

        def test_show_which_cinema(self):
            # create a user and add their birthdate to the database
            user = {'username': 'test_user', 'birthdate': '1990-01-01', 'cinema_debit_card': 0}
            save(user)

            # create a movie and add its age limit and cinema sessions to the database
            movie = {'movie_id': '1', 'age_limit': 16}
            save_movie(movie)
            cinema1 = {'cinema_id': '1', 'name': 'Cinema A', 'location': 'City A', 'working_hours': '9AM-10PM'}
            save_cinema(cinema1)
            session1 = {'session_id': '1', 'cinema_id': '1', 'movie_id': '1', 'start_time': '10AM'}
            session2 = {'session_id': '2', 'cinema_id': '1', 'movie_id': '2', 'start_time': '2PM'}
            save_session(session1)
            save_session(session2)

            # test with valid user and movie_id, should print the cinema name
            result = Cinema.show_which_cinema('1', 'test_user')
            expected_output = '1 - Cinema A'
            self.assertEqual(result, expected_output)

            # test with invalid user, should print an error message
            result = Cinema.show_which_cinema('1', 'nonexistent_user')
            expected_output = 'User not found'
            self.assertEqual(result, expected_output)

            # test with user under age limit, should print an error message
            user['birthdate'] = '2010-01-01'
            save(user)
            result = Cinema.show_which_cinema('1', 'test_user')
            expected_output = 'Your age is lower than age limit. You cannot watch this movie.'
            self.assertEqual(result, expected_output)

        def test_charge_debit_card(self):
            # create a user and add their debit card info to the database
            user = {'username': 'test_user', 'birthdate': '1990-01-01', 'cinema_debit_card': 100}
            save(user)

            # create a cinema bank account and add somemoney to it
            cinema_bank_account = '123456789'
            BankAccount.create_account(cinema_bank_account)
            BankAccount.deposit(cinema_bank_account, 1000)

            # test with valid inputs, should transfer money and update user's debit card balance
            result = Cinema.charge_debit_card('test_user', '500', cinema_bank_account, 'password', '123')
            expected_output = None
            self.assertEqual(result, expected_output)
            user = get_object('test_user')
            self.assertEqual(user['cinema_debit_card'], 600)

            # test with invalid serial number, should raise an error
            with self.assertRaises(Exception):
                Cinema.charge_debit_card('test_user', '500', 'invalid_serial', 'password', '123')

        def test_cinema_add_and_edit(self):
            # test adding a cinema to the database
            Cinema.cinema_add('Cinema B', 'City B', '10AM-11PM')
            cinema = get_cinema_object('2')
            self.assertEqual(cinema['name'], 'Cinema B')
            self.assertEqual(cinema['location'], 'City B')
            self.assertEqual(cinema['working_hours'], '10AM-11PM')

            # test editing a cinema in the database
            Cinema.cinema_edit('2', 'Cinema C', 'City C', '11AM-12PM')
            cinema = get_cinema_object('2')
