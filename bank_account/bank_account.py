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
