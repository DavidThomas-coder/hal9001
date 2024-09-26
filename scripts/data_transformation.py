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

# Example usage
if __name__ == "__main__":
    # Assuming you have a movies dictionary from the API call
    movies_df = transform_movie_data(movies)
    print(movies_df.head())
