from extra import save_movie, get_movie_object, delete_movie, get_movie_database,\
    save_cinema, get_cinema_database,get_cinema_object,delete_cinema,\
    save_salon, get_salon_database,get_salon_object, delete_salon,\
    save_session, get_session_database, get_session_object, delete_session, \
    save_ticket, get_ticket_database, get_ticket_object, delete_ticket
from bank_account.bank_account import BankAccount


class Movie:
    def __init__(self, movie_id, name:str, director:str, duration_time:str, product_year,
                 age_limit, description:str = None):
        self.movie_id = movie_id
        self.name = name
        self.director = director
        self.description = description
        self.duration_time = duration_time
        self.age_limit = age_limit
        self.product_year = product_year

    @classmethod
    def add_movie(cls,name:str, director:str, duration_time:str, product_year, age_limit, description:str=None):
        dict_m = list(get_movie_database().values())
        for movie in dict_m:
            if movie['name'] == name:
                raise ValueError(f'this movie already exist with id {movie["movie_id"]}')
        movie_id = cls.generate_id()
        movie = cls(movie_id, name, director, duration_time, product_year, age_limit, description)
        save_movie(vars(movie))

    @classmethod
    def edit_movie(cls, movie_id, new_name,  new_director, new_duration_time, new_product_year,
                   new_age_limit, new_description):
        delete_movie(movie_id)
        movie = cls(movie_id, new_name,  new_director, new_duration_time, new_product_year,
                    new_age_limit, new_description)
        save_movie(vars(movie))

    @staticmethod
    def delete_movie(movie_id:str):
        delete_movie(movie_id)

    @staticmethod
    def show_movie():
        for id, movies in get_movie_database().items() :
            print(f'({id}) - {movies["name"]}')




    @staticmethod
    def generate_id():
        dicti = get_movie_database()
        try:
            last_id = max(list(map(int,list(dicti.keys()))))
            last_id += 1
        except:
            last_id = 1
        return str(last_id)

# Movie.add_movie("star wars", 'babllll', '3:00', '2007', '12', 'description....')
# Movie.show_movie()

class Cinema:
    def __init__(self,cinema_id, name, location, working_hours):
        self.name = name
        self.location = location
        self.working_hours = working_hours
        self.cinema_id = cinema_id
        # BankAccount.create_account(name, 'dd',0000)
        # self.cinema_serial_bank_account = ...

    @staticmethod
    def show_which_cinema(movie_id):
        sessions = list(get_session_database().values())
        for session in sessions:
            if session['movie_id'] == movie_id:
                cinema = get_cinema_object(session['cinema_id'])
                print(f"{cinema['cinema_id']} - {cinema['name']}")
            else:
                print('not found ')



    @staticmethod
    def change_cinema_account(serial_number: str) -> None:
        """
        Changes the bank account number for cinema to be set for income account.

        Args:
            serial_number (str): A valid bank account number.
        """
        Ticket.cinema_account = serial_number

    @classmethod
    def is_cinema_account(cls) -> bool:
        """
        It will check is admin defined a bank account?

        Returns:
            bool: True if there is a defined accaount for cinema
        """
        if cls.__cinema_account:
            return True
        return False

    @classmethod
    def cinema_add(cls, name, location, working_hours):
        cinema_id = cls.generate_id()
        cinema = cls(cinema_id, name, location, working_hours)
        save_cinema(vars(cinema))

    @classmethod
    def cinema_edit(cls, cinema_id, new_name, new_location, new_working_hours):
        delete_cinema(cinema_id)
        cinema = cls(cinema_id, new_name, new_location, new_working_hours)
        save_cinema(vars(cinema))

    @staticmethod
    def delete_cinema(cinema_id):
        delete_cinema(cinema_id)

    @staticmethod
    def generate_id():
        dicti = get_cinema_database()
        try:
            last_id = max(list(map(int,list(dicti.keys()))))
            last_id += 1
        except:
            last_id = 1
        return str(last_id)

class Salon:
    def __init__(self, salon_id, name, seats_no, cinema_id):
        self.name = name
        self.seats_no = seats_no
        self.cinema_id = cinema_id
        self.salon_id = salon_id

    @classmethod
    def add_salon(cls, name, seats_no, cinema_id):
        salon_id = cls.generate_id()
        salon = cls(salon_id, name, seats_no, cinema_id)
        save_salon(vars(salon))

    @classmethod
    def edit_salon(cls, salon_id, new_name, new_seats_no, new_cinema_id):
        delete_salon(salon_id)
        salon = cls(salon_id, new_name, new_seats_no, new_cinema_id)
        save_salon(vars(salon))

    @staticmethod
    def delete_salon(salon_id):
        delete_salon(salon_id)

    @staticmethod
    def generate_id():
        dicti = get_salon_database()
        try:
            last_id = max(list(map(int,list(dicti.keys()))))
            last_id += 1
        except :
            last_id = 1
        return str(last_id)


class Session:
    def __init__(self, session_id, movie_id, cinema_id, salon_id, start_time, end_time, price, datetime):
        self.session_id = session_id
        self.movie_id = movie_id
        self.cinema_id = cinema_id
        self.salon_id = salon_id
        self.start_time = start_time
        self.end_time = end_time
        self.price = price
        self.datetime = datetime
        salon = get_salon_object(salon_id)
        self.capacity = salon['seats_no']

    @classmethod
    def add_session(cls, movie_id, cinema_id, salon_id, start_time, end_time, price, datetime):
        session_id = cls.generate_id()
        session = cls(session_id, movie_id, cinema_id, salon_id, start_time, end_time, price, datetime)
        save_session(vars(session))

    @classmethod
    def edit_session(cls, session_id, new_movie_id, new_cinema_id, new_salon_id, new_start_time, new_end_time,
                     new_price, new_datetime):
        delete_session(session_id)
        session = cls(session_id, new_movie_id, new_cinema_id, new_salon_id, new_start_time, new_end_time,
                      new_price, new_datetime)
        save_session(vars(session))

    @staticmethod
    def delete_session(session_id):
        delete_session(session_id)

    @staticmethod
    def generate_id():
        dicti = get_session_database()
        try:
            last_id = max(list(map(int,list(dicti.keys()))))
            last_id += 1
        except:
            last_id = 1
        return str(last_id)


class Ticket:
    def __init__(self, ticket_id, session_id, username_owner):
        self.ticket_id = ticket_id
        self.session_id = session_id
        self.username_owner = username_owner

    @classmethod
    def buy_ticket(cls, username_owner, session_id):
        ticket_id = cls.generate_id()
        ticket = cls(ticket_id, session_id, username_owner)
        save_ticket(vars(ticket))

    @staticmethod
    def generate_id():
        dicti = get_ticket_database()
        try:
            last_id = max(list(map(int,list(dicti.keys()))))
            last_id += 1
        except:
            last_id = 1
        return str(last_id)

