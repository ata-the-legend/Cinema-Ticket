class Movie:
    def __init__(self, name:str, director:str, description:str, duration_time:str, id=None):
        ...


class Cinema:
    def __init__(self, name, location, working_hours, id=None):
        ...


class Salon:
    def __init__(self, name, seats_no, id=None):
        ...


class Season:
    def __init__(self, movie, cinema, salon, start_time, end_time, price, datetime, capacity):
        ...

    def create_season(self, movie, cinema, salon, start_time, end_time, price, datetime, capacity):
        ...

    def edit_season(self, ):
        ...

    def delete_season(self):
        ...

    def get_list_of_season(self):
        ...

    def reserve_season(self):
        ...


