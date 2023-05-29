from uuid import uuid4


class BankAccount:
    accounts_dict = {}
    BANK_TRANSFER_FEE = 1_000

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
        self.__balance -= amount
        if self.__balance < 0 :
            raise ValueError("Insufficient Inventory")
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

        self.sub((amount + self.BANK_TRANSFER_FEE), password)
        other.add(amount)


