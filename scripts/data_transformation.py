import pandas as pd

def transform_movie_data(movies_data):
    """
    Transform the movie data into a pandas DataFrame.
    """
    movie_list = []
    
    for movie in movies_data['results']:
        movie_list.append({
            'title': movie['title'],
            'release_date': movie['release_date'],
            'popularity': movie['popularity'],
            'vote_average': movie['vote_average'],
            'genre_ids': movie['genre_ids']
        })
    
    return pd.DataFrame(movie_list)


