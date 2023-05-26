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
    season_name = season['season_name']
    dic.update({season_name: season})
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete(season_name: str) -> None:
    """
    delete user object from database
    :param season_name: username of user account
    :return: None
    """
    dic = get_database()
    del dic[season_name]
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_object(season_name: str) -> dict | None:
    """
    get object from database
    :param season_name: username
    :return: user object
    """
    try:
        with open("cinema.json", "r") as fp:
            # Load the dictionary from the file
            season_dict = json.load(fp)
            season = season_dict[season_name]
            return season
    except Exception:
        return None


