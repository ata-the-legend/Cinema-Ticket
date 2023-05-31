import cinema

#-----------------------------------------Cinema------------------------------------------


def get_cinema_database() -> dict:
    try:
        with open("json/cinema.json", "r") as fp:
            # Load the dictionary from the file
            return cinema.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_cinema(cinema: dict) -> None:
    dic = get_cinema_database()
    cinema_id = cinema['cinema_id']
    dic.update({cinema_id: cinema})
    try:
        with open("json/cinema.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_cinema(cinema_id: str) -> None:
    dic = get_cinema_database()
    del dic[cinema_id]
    try:
        with open("json/cinema.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_cinema_object(cinema_id: str) -> dict | None:
    try:
        with open("json/cinema.json", "r") as fp:
            # Load the dictionary from the file
            cinema_dict = cinema.load(fp)
            cinema = cinema_dict[cinema_id]
            return cinema
    except Exception:
        return None

#-----------------------------------------Movie------------------------------------------


def get_movie_database() -> dict:
    try:
        with open("json/movie.json", "r") as fp:
            # Load the dictionary from the file
            return cinema.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_movie(movie: dict) -> None:
    dic = get_movie_database()
    movie_id = movie['movie_id']
    dic.update({movie_id: movie})
    try:
        with open("json/movie.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_movie(movie_id: str) -> None:
    dic = get_movie_database()
    del dic[movie_id]
    try:
        with open("json/movie.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_movie_object(movie_id: str) -> dict | None:
    """
    get object from database
    :param movie_id: username
    :return: user object
    """
    try:
        with open("json/movie.json", "r") as fp:
            # Load the dictionary from the file
            movie_dict = cinema.load(fp)
            movie = movie_dict[movie_id]
            return movie
    except Exception:
        return None


#-----------------------------------------Salon------------------------------------------


def get_salon_database() -> dict:
    try:
        with open("json/salon.json", "r") as fp:
            # Load the dictionary from the file
            return cinema.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_salon(salon: dict) -> None:
    dic = get_salon_database()
    salon_id = salon['salon_id']
    dic.update({salon_id: salon})
    try:
        with open("json/salon.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_salon(salon_id: str) -> None:
    dic = get_salon_database()
    del dic[salon_id]
    try:
        with open("json/salon.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_salon_object(salon_id: str) -> dict | None:
    try:
        with open("json/salon.json", "r") as fp:
            # Load the dictionary from the file
            salon_dict = cinema.load(fp)
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
        with open("json/session.json", "r") as fp:
            # Load the dictionary from the file
            return cinema.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_session(session: dict) -> None:
    dic = get_session_database()
    session_id = session['session_id']
    dic.update({session_id: session})
    try:
        with open("json/session.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_session(session_id: str) -> None:
    dic = get_session_database()
    del dic[session_id]
    try:
        with open("json/session.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_session_object(session_id: str) -> dict | None:
    try:
        with open("json/session.json", "r") as fp:
            # Load the dictionary from the file
            season_dict = cinema.load(fp)
            season = season_dict[session_id]
            return season
    except Exception:
        return None


#-----------------------------------------Ticket------------------------------------------


def get_ticket_database() -> dict:
    try:
        with open("json/ticket.json", "r") as fp:
            # Load the dictionary from the file
            return cinema.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_ticket(ticket: dict) -> None:
    dic = get_ticket_database()
    ticket_id = ticket['ticket_id']
    dic.update({ticket_id: ticket})
    try:
        with open("json/ticket.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_ticket(ticket_id: str) -> None:
    dic = get_ticket_database()
    del dic[ticket_id]
    try:
        with open("json/ticket.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_ticket_object(ticket_id: str) -> dict | None:
    try:
        with open("json/ticket.json", "r") as fp:
            # Load the dictionary from the file
            ticket_dict = cinema.load(fp)
            ticket = ticket_dict[ticket_id]
            return ticket
    except Exception:
        return None


#-----------------------------------------sub------------------------------------------


def get_user_subscription_database() -> dict:
    try:
        with open("json/user_subscription.json", "r") as fp:
            # Load the dictionary from the file
            return cinema.load(fp)
    except Exception as ex:
        print('You have error in get cinema-database', ex)


def save_user_subscription(user_subscription: dict) -> None:
    dic = get_user_subscription_database()
    owner_username = user_subscription['owner_username']
    dic.update({owner_username: user_subscription})
    try:
        with open("json/user_subscription.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def delete_user_subscription(owner_username: str) -> None:
    dic = get_user_subscription_database()
    del dic[owner_username]
    try:
        with open("json/user_subscription.json", "w") as fp:
            cinema.dump(dic, fp, indent=4)  # encode dict into JSON
    except Exception as ex:
        print('You have error', ex)


def get_user_subscription_object(owner_username: str) -> dict | None:
    try:
        with open("json/user_subscription.json", "r") as fp:
            # Load the dictionary from the file
            user_subscription_dict = cinema.load(fp)
            user_subscription = user_subscription_dict[owner_username]
            return user_subscription
    except Exception:
        return None

