import pandas as pd

def transform_movie_data(movies_data):
    """
    Transform the movie data into a pandas DataFrame.
    """
    movie_list = []
    
    for movie in movies_data['results']:
        movie_list.append({
            'id': movie['id'],
            'title': movie['title'],
            'release_date': movie['release_date'],
            'popularity': movie['popularity'],
            'vote_average': movie['vote_average'],
            'genre_ids': movie['genre_ids']
        })
    
    return pd.DataFrame(movie_list)

def filter_fall_releases(movies_df):
    """
    Filter the movies DataFrame to only include movies released in the fall (September to December).
    """
    # Convert release_date to a datetime format
    movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')

    # Filter for fall months (September to December)
    fall_movies_df = movies_df[movies_df['release_date'].dt.month.isin([9, 10, 11, 12])]

    return fall_movies_df

def filter_awards_worthy(fall_movies_df):
    """
    Further filter fall movies to highlight awards-worthy ones, based on genre and rating.
    """
    # Example: Define "awards-worthy" genres (you can refine this list)
    awards_genres = [18, 36, 99]  # Drama, Biography, Documentary

    # Filter for high ratings and relevant genres
    awards_worthy_df = fall_movies_df[
        (fall_movies_df['vote_average'] >= 7.5) &
        (fall_movies_df['genre_ids'].apply(lambda genres: any(genre in awards_genres for genre in genres)))
    ]

    return awards_worthy_df

