import json

#-----------------------------------------Cinema------------------------------------------


def get_cinema_database() -> dict:
    try:
        with open("cinema.json", "r") as fp:
            # Load the dictionary from the file
            return json.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_cinema(cinema: dict) -> None:
    dic = get_cinema_database()
    cinema_id = cinema['cinema_id']
    dic.update({cinema_id: cinema})
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_cinema(cinema_id: str) -> None:
    dic = get_cinema_database()
    del dic[cinema_id]
    try:
        with open("cinema.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_cinema_object(cinema_id: str) -> dict | None:
    try:
        with open("cinema.json", "r") as fp:
            # Load the dictionary from the file
            cinema_dict = json.load(fp)
            cinema = cinema_dict[cinema_id]
            return cinema
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
        with open("salon.json", "r") as fp:
            # Load the dictionary from the file
            return json.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_salon(salon: dict) -> None:
    dic = get_salon_database()
    salon_id = salon['salon_id']
    dic.update({salon_id: salon})
    try:
        with open("salon.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_salon(salon_id: str) -> None:
    dic = get_salon_database()
    del dic[salon_id]
    try:
        with open("salon.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_salon_object(salon_id: str) -> dict | None:
    try:
        with open("salon.json", "r") as fp:
            # Load the dictionary from the file
            salon_dict = json.load(fp)
            salon = salon_dict[salon_id]
            return salon
    except Exception:
        return None

#-----------------------------------------Session------------------------------------------


def get_session_database() -> dict:
    """
    gets database content
    :return: dictionary of user accounts
    """
    try:
        with open("session.json", "r") as fp:
            # Load the dictionary from the file
            return json.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_session(season: dict) -> None:
    dic = get_session_database()
    season_id = season['season_id']
    dic.update({season_id: season})
    try:
        with open("session.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_session(session_id: str) -> None:
    dic = get_session_database()
    del dic[session_id]
    try:
        with open("session.json", "w") as fp:
            json.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_session_object(session_id: str) -> dict | None:
    try:
        with open("session.json", "r") as fp:
            # Load the dictionary from the file
            season_dict = json.load(fp)
            season = season_dict[session_id]
            return season
    except Exception:
        return None
