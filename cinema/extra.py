import json


def get_database() -> dict:
    """
    gets database content
    :return: dictionary of user accounts
    """
    try:
        with open("cinema.json", "r") as fp:
            # Load the dictionary from the file
            return json.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save(season: dict) -> None:
    """
    save object in database
    :param season: user object
    :return: None
    """
    dic = get_database()
    username = season['username']
    dic.update({username: season})
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete(season: str) -> None:
    """
    delete user object from database
    :param season: username of user account
    :return: None
    """
    dic = get_database()
    del dic[season]
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_object(username: str) -> dict | None:
    """
    get object from database
    :param username: username
    :return: user object
    """
    try:
        with open("cinema.json", "r") as fp:
            # Load the dictionary from the file
            person_dict = json.load(fp)
            user = person_dict[username]
            return user
    except Exception:
        return None


