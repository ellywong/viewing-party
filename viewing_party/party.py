# Wave 1 
def create_movie(title, genre, rating):
    if bool(title) == True & bool(genre) == True & bool(rating) == True:
        movie_to_watch = {
                "title" : title,
                "genre" : genre,
                "rating" : rating 
                }    
        return movie_to_watch      
    else: 
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    length_list_watchlist = len_list(user_data, "watchlist")
    for i in range(length_list_watchlist):
        if user_data["watchlist"][i]["title"] == title:
            movie_to_be_added = user_data["watchlist"][i]
            add_to_watched(user_data, movie_to_be_added)
            user_data["watchlist"].pop(i)
    return user_data

# helper func (length of list)
def len_list(user_data, key):
    return len(user_data[key])

# Wave 2 
def get_watched_avg_rating(user_data):
    sum_rating = 0 
    avg_rating = 0 
    length_list_watched = len_list(user_data, "watched")
    if length_list_watched != 0:
        for i in range(length_list_watched):
            sum_rating += user_data["watched"][i]["rating"]
        avg_rating = sum_rating / length_list_watched
    return avg_rating

def get_most_watched_genre(user_data):
    length_watched = len_list(user_data, "watched")
    if length_watched == 0:
        return None
    dict_genre = {}
    for i in range(length_watched):
        genre_counted = user_data["watched"][i]["genre"]  #str
        if genre_counted in dict_genre:
            dict_genre[genre_counted] = dict_genre.get(genre_counted) + 1
        else:
            dict_genre[genre_counted] = 1
# get the most genre
    cur_most_genre = user_data["watched"][0]["genre"]
    count_cur_most_genre = dict_genre[cur_most_genre]
    for count in dict_genre.values():
        if count > count_cur_most_genre:
            count_cur_most_genre = count
# get the key
    for key_genre in dict_genre:
        if dict_genre[key_genre] == count_cur_most_genre:
            return key_genre

        

# Wave 3
def get_unique_watched(user_data):
    pass