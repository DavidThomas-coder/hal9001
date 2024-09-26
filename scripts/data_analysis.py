import matplotlib.pyplot as plt

def analyze_movies(movies_df):
    """
    Perform some detailed analysis for movies from 2023.
    """
    # Basic summaries
    print(f"Number of Movies: {len(movies_df)}")
    print(f"Average Rating: {movies_df['vote_average'].mean():.2f}")
    print(f"Most Popular Movie (by popularity): {movies_df.loc[movies_df['popularity'].idxmax()]['title']}")
    print(f"Highest Rated Movie: {movies_df.loc[movies_df['vote_average'].idxmax()]['title']}")

    # Genre IDs need to mapped to actual genre names
    print("Sample of Genre IDs (first 5 movies):")
    print(movies_df[['title', 'genre_ids']].head())


def plot_movie_ratings(movies_df):
    """
    Plot the distribution of movie ratings.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(movies_df['vote_average'], bins=10, color='blue', edgecolor='black')
    plt.title('Distribution of Movie Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Number of Movies')
    plt.show()

    

# Example usage
if __name__ == "__main__":
    # Assuming you have a transformed DataFrame
    analyze_movies(movies_df)
    plot_movie_ratings(movies_df)
