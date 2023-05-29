# from user import User
import uuid
from extra import save_movie, get_movie_object, delete_movie, get_movie_database

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
        movie_id = cls.generate_id()
        movie = cls(movie_id, name, director, duration_time, product_year, age_limit, description)
        save_movie(vars(movie))

    @classmethod
    def edit_movie(cls, movie_id, new_name,  new_director, new_duration_time, new_product_year,
                   new_age_limit, new_description):
        movie = get_movie_object(movie_id)
        delete_movie(movie_id)
        movie = cls(movie_id, new_name,  new_director, new_duration_time, new_product_year,
                   new_age_limit, new_description)
        save_movie(vars(movie))

    @classmethod
    def delete_movie(cls, movie_id):
        # delete(movie_id)
        pass

    @staticmethod
    def generate_id():
        dicti = get_movie_database()
        try:
            last_id = int(list(dicti.keys())[-1])
            last_id += 1
        except:
            last_id = 1
        return str(last_id)

Movie.add_movie('Zakhm kari 2','hasan fathi', '2:00', '1402', '18','description')
Movie.add_movie('Zakhm kari 1','hasan fathi', '2:00', '1402', '18','description')
Movie.add_movie('Zakhm kari 3','hasan fathi', '2:00', '1402', '18','description')

# class Cinema:
#     def __init__(self, name, location, working_hours, cinema_id):
#         self.name = name
#         self.location = location
#         self.working_hours = working_hours
#         self.cinema_id = cinema_id
#
#
#     @classmethod
#     def cinema_add(cls, name, location, working_hours):
#         cinema_id = cls.generate_id()
#         cinema = cls(name, location, working_hours, cinema_id)
#        #save(vars(cinema))
#
#     @classmethod
#     def cinema_edit(cls,cinema_id, new_name, new_location, new_working_hours):
#         # cinema = get_object(cinema_id)
#         # delete(cinema)
#         cinema = cls(new_name, new_location, new_working_hours,cinema_id)
#
#
#     @classmethod
#     def cinema_delete(cls, cinema_id):
#         #delete(cinema_id)
#         pass
#
#
#
#     # def generate_id(self):
#     #     dict = get_database()
#     #     last_id = list(dict.key)[-1]
#     #     id_counter += 1
#     #     return str(id_counter)
#
#
#
# class Salon:
#     def __init__(self, name, seats_no,cinema_id, salon_id):
#         self.name =name
#         self.seats_no = seats_no
#         self.cinema_id = cinema_id
#         self.salon_id = salon_id
#
#
#     @classmethod
#     def add_salon(cls,name, seats_no, cinema_id):
#         salon_id = cls.generate_id()
#         salon = cls(name, seats_no, cinema_id, salon_id)
#         #save(vars(salon))
#
#
#     @classmethod
#     def edit_salon(cls, salon_id, new_name, new_seats_no, new_cinema_id):
#         #salon = get_object(salon_id)
#         #delete(salon_id)
#         salon = cls(new_name, new_seats_no, new_cinema_id, salon_id)
#         #save(vars(salon))
#
#     @classmethod
#     def delete_salon(cls,salon_id):
#         #delete(salon_id)
#         pass
#
#     # def generate_id(self):
#     #     dict = get_database()
#     #     last_id = list(dict.key)[-1]
#     #     id_counter += 1
#     #     return str(id_counter)
#
# class session:
#     data_season = {}
#     user_reserve_season = {}
#     def __init__(self, session_id, movie_id, cinema_id, salon_id, start_time, end_time, price, datetime):
#         self.session_id = session_id
#         self.movie_id = movie_id
#         self.cinema_id = cinema_id
#         self.salon_id = salon_id
#         self.start_time = start_time
#         self.end_time = end_time
#         self.price = price
#         self.datetime = datetime
#
#
#     @classmethod
#     def add_session(cls, session_id, movie_id, cinema_id, salon_id, start_time, end_time, price, datetime):
#          session_id = cls.generate_id()
#          session = cls( session_id, movie_id, cinema_id, salon_id, start_time, end_time, price, datetime)
#         #save(vars(session))
#
#     @classmethod
#     def edit_session(cls, session_id, new_movie_id, new_cinema_id, new_salon_id, new_start_time, new_end_time,
#                      new_price, new_datetime):
#         #session = get_object(session_id)
#         #delete(session_id)
#          session = cls(session_id,new_movie_id, new_cinema_id, new_salon_id, new_start_time, new_end_time,
#                      new_price, new_datetime)
#         #save(vars(session)
#
#     @classmethod
#     def delete_session(cls, session_id):
#         #datetime(session_id)
#
#     # def generate_id(self):
#     #     dict = get_database()
#     #     last_id = list(dict.key)[-1]
#     #     id_counter += 1
#     #     return str(id_counter)
#
#
#
#
#
#
#
#
#
#
# class ticket :
#
#     def __int__(self, session_id, username_owner):
#         self.session_id = session_id
#         self.username_owner = username_owner
#
#
#     def buy_ticket(self, username_owner ,session_id, ):
#         pass
#
#
#
#
#
#
#
#
#









