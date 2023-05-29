import json

#-----------------------------------------Cinema------------------------------------------

def get_cinema_database() -> dict:
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


def save_cinema(season: dict) -> None:
    """
    save object in database
    :param season: user object
    :return: None
    """
    dic = get_cinema_database()
    season_name = season['season_name']
    dic.update({season_name: season})
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_cinema(season_name: str) -> None:
    """
    delete user object from database
    :param season_name: username of user account
    :return: None
    """
    dic = get_cinema_database()
    del dic[season_name]
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_cinema_object(season_name: str) -> dict | None:
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

#-----------------------------------------Movie------------------------------------------


def get_movie_database() -> dict:
    try:
        with open("movie.json", "r") as fp:
            # Load the dictionary from the file
            return json.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_movie(movie: dict) -> None:
    dic = get_movie_database()
    movie_id = movie['movie_id']
    dic.update({movie_id: movie})
    try:
        with open("movie.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_movie(movie_id: str) -> None:
    dic = get_movie_database()
    del dic[movie_id]
    try:
        with open("movie.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_movie_object(movie_id: str) -> dict | None:
    """
    get object from database
    :param movie_id: username
    :return: user object
    """
    try:
        with open("movie.json", "r") as fp:
            # Load the dictionary from the file
            movie_dict = json.load(fp)
            movie = movie_dict[movie_id]
            return movie
    except Exception:
        return None


#-----------------------------------------Salon------------------------------------------


def get_salon_database() -> dict:
    try:
        with open("cinema.json", "r") as fp:
            # Load the dictionary from the file
            return json.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_salon(season: dict) -> None:
    dic = get_salon_database()
    season_name = season['season_name']
    dic.update({season_name: season})
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_salon(season_name: str) -> None:
    dic = get_salon_database()
    del dic[season_name]
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_salon_object(season_name: str) -> dict | None:
    try:
        with open("cinema.json", "r") as fp:
            # Load the dictionary from the file
            season_dict = json.load(fp)
            season = season_dict[season_name]
            return season
    except Exception:
        return None


def get_session_database() -> dict:
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


def save_session(season: dict) -> None:
    """
    save object in database
    :param season: user object
    :return: None
    """
    dic = get_session_database()
    season_name = season['season_name']
    dic.update({season_name: season})
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_session(season_name: str) -> None:
    """
    delete user object from database
    :param season_name: username of user account
    :return: None
    """
    dic = get_session_database()
    del dic[season_name]
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_session_object(season_name: str) -> dict | None:
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
