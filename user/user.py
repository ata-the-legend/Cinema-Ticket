import uuid, hashlib
from extra import save, get_object, delete
from datetime import datetime
from enum import Enum


class DebitCardType(Enum):
    BRONZE = 1
    SILVER = 2
    GOLD = 3


class User:
    def __init__(self, username: str, password: str, birthdate: str, user_id: str, signup_datetime: str, 
                 debit_card_type: DebitCardType, phone_number: str = None) -> None:

        """
        this is initializer for User class
        :param username: input username
        :param password: input password
        :param phone_number: input phone number
        :param user_id: generated auto user_id
        """
        # if user_id is None:
        #     self.user_id = str(uuid.uuid4())
        # else:
        self.user_id = user_id
        self.username = username
        self.phone_number = phone_number
        self.__password = password
        self.birthdate = birthdate
        self.signup_datetime = signup_datetime
        self.cinema_debit_card = 0
        self.bank_accounts = []
        self.debit_card_type = debit_card_type.value

    def show_bank_account(self):
        ...

    @staticmethod
    def validate_pass(password: str) -> None:
        """
        this method validate password
        :param password: password for check
        :return: None if password was correct. or rais error if not valid
        """
        if password == '' or password.isspace():
            raise ValueError('\n--- your password was empty! you must set password ---\n')
        elif len(password) < 4:
            raise ValueError('\n--- The length of the password must be more than 4 characters! ---\n')
        return None  # why wrong with false?

    @staticmethod
    def validate_username(username: str) -> None:
        """
        this method validate username
        :param username:
        :return:
        """
        if len(username) == 0:
            raise ValueError('\n--- your username was empty! you must set password ---\n')
        return None # false?

    @staticmethod
    def build_pass(password: str) -> str:
        """
        this method hashed password by hashlib
        :param password:
        :return: hashed password
        """
        password = password.encode()
        p_hash = hashlib.sha256()
        p_hash.update(password)
        password = p_hash.hexdigest()
        return password
        # return password = hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def authenticated(cls, username: str) -> object | None:
        """
        this method check user is authenticated or not ...
        :param username: username
        :return: if authenticated return user object . if not, return None.
        """
        user = get_object(username)
        if user is not None:
            debit_card_type = DebitCardType(user['debit_card_type'])
            user = cls(user['username'], user['_User__password'], user['birthdate'], user['user_id'], user['signup_datetime'],debit_card_type, user['phone_number']) 
            return user
        else:
            return None ##??

    @classmethod
    def create_user(cls, username: str, password: str, birthdate: str, phone_number:str =None) -> None:
        """
        this method create user and save to database
        :param username: input username
        :param password: input password
        :param phone_number: input phone_number
        :param user_id: user_id
        """
        if User.validate_pass(password): # these are never can be true
            return cls.validate_pass(password) #this line never runs
        elif User.validate_username(username): ####
            return cls.validate_username(username) #####
        elif User.authenticated(username):
            raise ValueError('\n--- Registration failed , This username already exist! ---\n')
        else:
            password = cls.build_pass(password)

            user_id = str(uuid.uuid4())
            signup_datetime = str(datetime.now())
            debit_card_type = DebitCardType.BRONZE
            user = User(username, password, birthdate, user_id, signup_datetime, debit_card_type, phone_number)

            save(vars(user))
        
        ## check phone number

    @classmethod
    def login(cls, username: str, password: str) -> object:
        """
        this method login user
        :param username: input username
        :param password: input password
        :return: user object if is authenticated
        """
        hashed_password = cls.build_pass(password)
        user = User.authenticated(username)
        if user:
            if user._User__password == hashed_password:
                return user
            else:
                raise ValueError('--- incorrect password ---')
        else:
            raise ValueError(f" --- There is no account with this username : {username} ---\n"
                             f" --- Please register and try again. ---")

    @classmethod
    def change_info(cls, username: str, new_username: str, new_phone_number: str) -> object:
        """
        this method change username or phone number
        :param username: old username
        :param new_username: new user-name
        :param new_phone_number: new phone number
        :return: updated user object
        """
        if cls.validate_username(new_username): ####
            return cls.validate_username(new_username) ######
        user = get_object(username) 
        delete(username)
        debit_card_type = DebitCardType(user['debit_card_type'])
        user = cls(new_username, user['_User__password'], user['birthdate'], user['user_id'],
                   user['signup_datetime'], debit_card_type, new_phone_number) 
        save(vars(user))
        return user
    
        ## check phone number or be optional

    def change_password(self, old: str, new: str, confirm_new: str) -> object:
        """
        change password user
        :param old: old password
        :param new: new password
        :param confirm_new: confirm new password
        :return: updated user object
        """
        old = self.build_pass(old)
        if old == self._User__password:
            if self.match_pass(new, confirm_new): ## this could be checked for more safty and diferent messages
                if self.validate_pass(new) is None:
                    new = self.build_pass(new)
                    delete(self.username)
                    debit_card_type = DebitCardType(self.debit_card_type)
                    user = User(self.username, new, self.birthdate, self.user_id, self.signup_datetime, debit_card_type, self.phone_number)
                    save(vars(user))
                    return user
                return self.validate_pass(new)
            else:
                raise ValueError('--- new password and confirm password not mach ---')
        else:
            raise ValueError('--- your old is invalid ---')

    @staticmethod
    def match_pass(p1: str, p2: str) -> bool: 
        """
        passwords matching
        :param p1: password
        :param p2: confirm password
        :return: True if matched. return False if not matched.
        """
        if p1 == p2:
            return True
        return False

    def __str__(self) -> str:
        """
        this is class str for present class object.
        :return: public information.
        """
        user_id, username, phone_number = self.user_id, self.username, self.phone_number
        return f'\nID = {user_id}\n' \
               f'Username = {username}\n' \
               f'Phone_number = {phone_number}\n' \
               f'Birthdate = {self.birthdate}\n' \
               f'Sign up Date = {self.signup_datetime}\n' \
               f'User Level = {self.debit_card_type}'



