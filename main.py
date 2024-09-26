from scripts.data_ingestion import get_movies_by_year
from scripts.data_transformation import transform_movie_data
from scripts.data_analysis import analyze_movies, plot_movie_ratings
from scripts.db_handler import save_to_postgres

if __name__ == "__main__":
    # Pull movies from 2023
    movies = get_movies_by_year(2023)
    
    if movies:
        # Transform the raw data into a DataFrame
        movies_df = transform_movie_data(movies)
        
        # Analyze and visualize the data
        analyze_movies(movies_df)
        plot_movie_ratings(movies_df)
        
        # Save the transformed data to PostgreSQL
        save_to_postgres(movies_df, "movies_2023")


