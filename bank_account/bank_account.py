from uuid import uuid4
from bank_account.bank_extra import save_bank_account,get_bank_database,delete_bank_account, get_bank_account_object

class BankAccount:

    BANK_TRANSFER_FEE = 1_000

    def __init__(self, owner_name: str, bank: str, balance: int, serial_number, cvv2, password):
        self.owner_name = owner_name
        self.bank = bank
        self.serial_number = serial_number 
        self.cvv2 = cvv2 
        self.__password = password 
        self.__balance = balance


    @staticmethod
    def serial_number_creator() -> str:
        """
        create a serial number for bank account

        Returns:
            a 16 digit string serial number
            with ****-****-****-**** shape
        """

        id = (str(uuid4().int))[:16]
        return f"{id[:4]}-{id[4:8]}-{id[8:12]}-{id[12:]}"
    
    @staticmethod
    def cvv2_creator() -> str:
        """
        create a CVV2 for bank account

        Returns:
            a 3 digit number as string
        """

        cvv2 = (str(uuid4().int))[-3:]
        return cvv2

    @staticmethod
    def password_creator() -> str:
        """
        create a CVV2 for bank account

        Returns:
            a 4 digit number as string
        """

        psw = (str(uuid4().int))[:4]
        return psw

    @classmethod
    def create_account(cls,
        input_owner_name: str,
        input_bank: str,
        input_balance: int) -> 'BankAccount':
        """
        create a bank account

        Args:
            input_owner_name (str)
            input_bank (str)
            input_balance (int)

        Returns:
            create a BankAccount instance 
            and return its serial number as string
        """
        if input_balance < 0:
            raise ValueError('Amount of balance should be positive.')
        serial_number = cls.serial_number_creator()
        cvv2 = cls.cvv2_creator()
        password = cls.password_creator()
        account = cls(input_owner_name, input_bank, input_balance, serial_number, cvv2, password)
        save_bank_account(vars(account))
        return account
        #this serial number should save in user_accounts!!!

    def __str__(self) -> str:
        return f"\"{self.bank}\" bank information:\n\
Owner Name    >>>   {self.owner_name}\n\
Serial Number >>>   {self.serial_number}\n\
CVV2          >>>   {self.cvv2}\n\
Password      >>>   {self.__password}\n\
Balance       >>>   {self.__balance:,}"

    @classmethod
    def show_account(cls, serial_number: str) -> 'BankAccount':
        """
        show all information of each bank account

        Args:
            the bank account serial number as string

        Returns:
            str: show all information with an f"string"
        """
        user_dict = get_bank_account_object(serial_number)
        user = cls(user_dict["owner_name"], user_dict["bank"], user_dict["_BankAccount__balance"], user_dict["serial_number"], user_dict["cvv2"], user_dict["_BankAccount__password"])
        return user
    


    def add(self, amount: int) -> int:
        """
        Add a certain amount to the account's balance

        Args:
            amount (int): and must be greater than 0

        Raises:
            ValueError: will raise when the Args condition are not ready

        Returns:
            int: update the account's balance with the int number
        """
        
        if amount < 0:
            raise ValueError("Invalid Amount")
        self.__balance += amount
        delete_bank_account(self.serial_number)
        save_bank_account(vars(self))
        return self.__balance

    def sub(self, amount: int, password: str) -> int:
        """
        Subtracts a certain amount from the account's balance

        Args:
            amount (int): and must be greater than 0

        Raises:
            ValueError: will raise when the Args condition are not ready
            ValueError: will raise when there is not enough amount of money
                        in account's balance for withdrawal

        Returns:
            int: update the account's balance with the int number
        """

        if password != self.__password:
            raise ValueError("Incorrect Password")
        
        if amount < 0:
            raise ValueError("Invalid Amount")
        new_balance = self.__balance - amount
        if new_balance < 0 :
            raise ValueError("Insufficient Inventory")
        self.__balance = new_balance
        delete_bank_account(self.serial_number)
        save_bank_account(vars(self))
        return self.__balance

    def transfer_to_another(self, other: "BankAccount", amount: int,
                            password: str, cvv2: str) -> None:
        """
        Transfer a certain amount of money
        from first object to the second object that mentioned in Args
        ! the first account will pay 1000 more as banking fees

        Args:
            other (BankAccount): an object from BankAccount class
            that its account take the money is deposited
            amount (int): the amount of money that will transfer
            (excluding bank transfer fees)
        """
        if cvv2 != self.cvv2:
            raise ValueError("Incorrect CVV2")
        if amount < 0:
            raise ValueError("Invalid Amount")

        self.sub((amount + self.BANK_TRANSFER_FEE), password)
        other.add(amount)

    @staticmethod
    def is_serial(serial_number: str) -> bool:
        """
        Check if serial number is valid and exist.

        Args:
            serial_number (str): A bank account serial number

        Returns:
            bool: True if serial is valid.
        """
        if get_bank_account_object(serial_number):
            return True
        return False

