from cinema_extra import save_movie, get_movie_object, delete_movie, get_movie_database,\
    save_cinema, get_cinema_database,get_cinema_object,delete_cinema,\
    save_salon, get_salon_database,get_salon_object, delete_salon,\
    save_session, get_session_database, get_session_object, delete_session, \
    save_ticket, get_ticket_database, get_ticket_object, delete_ticket, \
    save_user_subscription, get_user_subscription_database, delete_user_subscription, get_user_subscription_object
from bank_account.bank_account import BankAccount
from user.user_extra import get_object, delete,save
from user.user import User, UserRole
from datetime import datetime, timedelta


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
        for id, movies in get_movie_database().items():
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
    def show_which_cinema(movie_id, username):
        birthdate = datetime.strptime(get_object(username)['birthdate'],  "%Y-%m-%d")
        current_date = datetime.now()
        age = current_date - birthdate
        years = age.days // 365
        age_limit = get_movie_object(movie_id)['age_limit']
        if years >= age_limit:
            sessions = list(get_session_database().values())
            for session in sessions:
                if session['movie_id'] == movie_id:
                    cinema = get_cinema_object(session['cinema_id'])
                    print(f"{cinema['cinema_id']} - {cinema['name']}")
                else:
                    print('not found cinema for this movie')
        else:
            print('your age is lower than age limit . you dont take this movie')

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
    def show_which_salon(movie_id, cinema_id):
        sessions = list(get_session_database().values())

        for session in sessions:
            if session['movie_id'] == movie_id and session['cinema_id'] == cinema_id:
                salon = get_salon_object(session['salon_id'])
                print(f"({salon['salon_id']}) - {salon['name']}")
            else:
                print('not found salon for this movie')

    @staticmethod
    def generate_id():
        dicti = get_salon_database()
        try:
            last_id = max(list(map(int, list(dicti.keys()))))
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
    def show_which_session(movie_id, cinema_id, salon_id):
        sessions = list(get_session_database().values())
        for session in sessions:
            if session['movie_id'] == movie_id and\
               session['cinema_id'] == cinema_id and\
               session['salon_id'] == salon_id:

                session = get_session_object(session['session_id'])
                print(f"({session['salon_id']}) - |{session['start_time']} to {session['end_time']} \n      "
                      f"|capacity status : {session['capacity']} empty seats\n      "
                      f"|price : {session['price']}")
            else:
                print('not found session for this movie')

    @staticmethod
    def generate_id():
        dicti = get_session_database()
        try:
            last_id = max(list(map(int, list(dicti.keys()))))
            last_id += 1
        except:
            last_id = 1
        return str(last_id)


class Ticket:
    def __init__(self, ticket_id, session_id, username_owner):
        self.ticket_id = ticket_id
        self.session_id = session_id
        self.username_owner = username_owner

    @staticmethod
    def is_birthday(birthdate):
        today = datetime.today()
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        if today.month == birthdate.month and today.day == birthdate.day:
            return True
        else:
            return False

    @classmethod
    def subscription_discount(cls,owner_username):
        subscription = get_user_subscription_object(owner_username)
        print(subscription)
        level = subscription['level']

        if level == "bronze":
            return 0
        elif level == "silver":
            transaction_count = subscription['transition_count']
            if transaction_count <= 3:
                delete_user_subscription(owner_username)
                expire_date = None
                transaction_count += 1
                obj = cls('silver', owner_username, expire_date, transaction_count)
                save_user_subscription(vars(obj))
                return 0.2
            else:
                delete_user_subscription(owner_username)
                obj = cls('bronze', owner_username)
                save_user_subscription(vars(obj))
                return 0
        elif level == "gold":
            expire_date = datetime.strptime(subscription['expire_date'], "%Y-%m-%d")
            if datetime.today() <= expire_date:
                return 0.5
            else:
                delete_user_subscription(owner_username)
                obj = cls('bronze', owner_username)
                save_user_subscription(vars(obj))
                return 0

    @classmethod
    def apply_discount(cls, owner_username):
        user = get_object(owner_username)
        discount = 0
        if cls.is_birthday(user['birthdate']):
            discount += 0.5
        discount += cls.subscription_discount(owner_username)
        return discount

    @classmethod
    def show_ticket(cls, owner_username, session_id):
        user = get_object(owner_username)
        session = get_session_object(session_id)
        if int(session['capacity']) >= 1:
            price = int(session['price'])
            discount = cls.apply_discount(owner_username)
            final_price = price * (1-discount)
            if user['cinema_debit_card'] >= final_price:
                movie_name = get_movie_object(session['movie_id'])['name']
                cinema_name = get_cinema_object(session['cinema_id'])['name']
                salon_name = get_salon_object(session['salon_id'])['name']
                session_time = session['start_time'] + ' to ' + session['end_time']
                session_datetime = session['datetime']
                final_price = final_price
                print(f' _________________________ Your Ticket __________________________\n'
                      f'       movie  : {movie_name}\n'
                      f'       cinema : {cinema_name}\n'  
                      f'       salon  : {salon_name} \n'
                      f'       date : {session_datetime}\n'
                      f'       time : {session_time}\n'
                      f'       final price : {final_price}\n'
                      f' __________________________________________________________________')
            else:
                print('Your wallet balance is Not enough')
        else:
            print("this session doesn't have capacity")

    @staticmethod
    def cinema_debit_card_sub(owner_username, amount):
        user = get_object(owner_username)
        inventory = user['cinema_debit_card']
        if inventory >= int(amount):
            new_inventory = inventory - int(amount)
            delete(user['username'])
            obj = User(user['username'], user['_User__password'], user['birthdate'],
                       user['user_id'], user['signup_datetime'], UserRole(user['user_role']),
                       new_inventory, user['phone_number'])
            save(vars(obj))
        else:
            raise 'balance not enough'

    @classmethod
    def buy_ticket(cls, owner_username, session_id):
        session = get_session_object(session_id)
        if int(session['capacity']) >= 1:
            price = int(session['price'])
            user = get_object(owner_username)
            discount = cls.apply_discount(owner_username)
            final_price = price * (1-discount)
            if user['cinema_debit_card'] >= final_price:
                cls.cinema_debit_card_sub(owner_username, final_price)
                ticket_id = cls.generate_id()
                ticket = cls(ticket_id, session_id, owner_username)
                save_ticket(vars(ticket))
            else:
                print('Your wallet balance is Not enough')

    @staticmethod
    def generate_id():
        dicti = get_ticket_database()
        try:
            last_id = max(list(map(int,list(dicti.keys()))))
            last_id += 1
        except:
            last_id = 1
        return str(last_id)


Ticket.buy_ticket('pouriya', '2')
# Ticket.show_ticket('saba', '2')
# Ticket.apply_discount('saba')

class Subscription:
    def __init__(self, level, owner_username, expire_date=None, transition_count=None):
        self.level = level
        self.owner_username = owner_username
        self.expire_date = expire_date
        self.transition_count = transition_count

    @classmethod
    def buy_subscription(cls, choices_subscription, owner_username, serial_bank_account=None, password=None, cvv2=None):
        match choices_subscription:
            case 'gold':
                # if bank transition is success :
                purchase_date = datetime.today()
                expire_date = purchase_date + timedelta(days=30)
                expire_date_str = datetime.strftime(expire_date, '%Y-%m-%d')
                subscription = cls(choices_subscription, owner_username, expire_date, transition_count=None)
                save_user_subscription(vars(subscription))
            case 'silver':
                # if bank transition is success :
                transition_count = 3
                expire_date = None
                subscription = cls(choices_subscription, owner_username, expire_date, transition_count)
                save_user_subscription(vars(subscription))
            case 'bronze':
                expire_date = None
                transition_count = None
                subscription = cls(choices_subscription, owner_username, expire_date, transition_count)
                save_user_subscription(vars(subscription))
