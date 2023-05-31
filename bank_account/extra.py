import json


def get_database() -> dict:
    """
    gets database content
    :return: dictionary of user accounts
    """
    try:
        with open("bank_accounts.json", "r") as fp:
            # Load the dictionary from the file
            return json.load(fp)
    except Exception as ex:
        print('You have error in get bank accounts-database', ex)


def save(bank_account: dict) -> None:
    """
    save object in database
    :param bank_account: user object
    :return: None
    """
    dic = get_database()
    serial_number = bank_account['serial_number']
    dic.update({serial_number: bank_account})
    try:
        with open("bank_account.py", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete(serial_number: str) -> None:
    """
    delete user object from database
    :param serial_number: username of user account
    :return: None
    """
    dic = get_database()
    del dic[serial_number]
    try:
        with open("bank_accounts.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_object(serial_number: str) -> dict | None:
    """
    get object from database
    :param serial_number: username
    :return: user object
    """
    try:
        with open("bank_accounts.json", "r") as fp:
            # Load the dictionary from the file
            bank_accounts = json.load(fp)
            bank_account = bank_accounts[serial_number]
            return bank_account
    except Exception:
        return None


