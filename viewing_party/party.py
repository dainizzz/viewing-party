# ------------- WAVE 1 --------------------
# 1
def create_movie(title, genre, rating):
    """ 
    input: a str title, str genre, and str rating
    output: a dict of the given arguments if the inputs are valid OR None if the input is invalid
    """
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else:
        return None

# part 2
def add_to_watched(user_data, movie):
    """
    user_data: a dictionary with a key "watched" and a value list of dictionaries representing the movies the user watched
    an empty list represents that the user has no movies in their watched list
    movie: a dictionary in this format:
        {
            title": "Title A",
            "genre": "Horror",
            "rating": 3.5
        }
    the function will add movie to the watched list inside of user_data
    then return user_data
    """
    pass

# part 3
def add_to_watchlist(user_data, movie):
    """
    user_data: a dict with the key "watchlist" and value list of dictionaries representing the movies the user wants to watch
    an empty list represents the user has no movies in their watchlist
    movie: a dicitonary in this format:
        {
            title": "Title A",
            "genre": "Horror",
            "rating": 3.5
        }
    this function will add movie to the "watchlist" list inside of user_data
    return user_data
    """
    pass

#part 4
def watch_movie(user_data, title):
    """
    user_data: a dict with keys "watchlist" and "watched"
    title: a str representing the title of the movie the user has watched
    if title in user_data["watchlist"]:
        remove movie from "watchlist"
        add movie to "watched"
        return user_data
    elif title not in user_data["watchlist"]:
        return user_data
    """
    pass
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

