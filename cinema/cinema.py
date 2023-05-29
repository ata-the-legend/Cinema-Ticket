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


class Ticket:

    __cinema_account = 0
    @staticmethod
    def change_cinema_account(serial_number: str) -> None:
        """
        Changes the bank account number for cinema to be set for income account.

        Args:
            serial_number (str): A valid bank account number.
        """
        Ticket.__cinema_account = serial_number
    
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