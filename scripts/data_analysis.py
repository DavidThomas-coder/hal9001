import matplotlib.pyplot as plt

def analyze_movies(movies_df):
    """
    Perform some basic analysis, such as average rating and most popular genres.
    """
    print("Average Rating:", movies_df['vote_average'].mean())
    print("Most Popular Movie:", movies_df.loc[movies_df['popularity'].idxmax()]['title'])

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
