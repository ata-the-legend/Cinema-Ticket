from uuid import uuid4


class BankAccount:
    accounts_dict = {}

    def __init__(self, owner_name: str, bank: str, balance: int):
        self.owner_name = owner_name
        self.bank = bank
        self.serial_number = self.serial_number_creator()
        self.cvv2 = self.cvv2_creator()
        self.__password = self.password_creator()
        self.__balance = balance
        self.accounts_dict[self.serial_number] = vars(self)

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
        input_balance: int) -> str:
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
        usr = cls(input_owner_name, input_bank, input_balance)
        
        return usr.serial_number
        #this serial number should save in user_accounts!!!

    @classmethod
    def show_account(cls, serial_number: str) -> str:
        """
        show all information of each bank account

        Args:
            the bank account serial number as string

        Returns:
            str: show all information with an f"string"
        """

        info = cls.accounts_dict[serial_number]
        owner_name = info["owner_name"]
        bank = info["bank"]
        serial_number = info["serial_number"]
        cvv2 = info["cvv2"]
        password = info["_BankAccount__password"]
        balance = info["_BankAccount__balance"]

        return f"\"{bank}\" bank information:\n\
Owner Name    >>>   {owner_name}\n\
Serial Number >>>   {serial_number}\n\
CVV2          >>>   {cvv2}\n\
Password      >>>   {password}\n\
Balance       >>>   {balance:,}"
