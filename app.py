from flask import Flask, render_template
import pandas as pd
import plotly.express as px
from scripts.data_ingestion import get_movies_by_year
from scripts.data_transformation import transform_movie_data, filter_fall_releases, filter_awards_worthy

app = Flask(__name__)

# Route for displaying fall and awards-worthy movies
@app.route('/fall-awards')
def fall_awards():
    # Fetch movies from 2023
    movies = get_movies_by_year(2023)
    
    if movies:
        # Transform the raw data into a DataFrame
        movies_df = transform_movie_data(movies)
        
        # Filter for fall releases
        fall_movies_df = filter_fall_releases(movies_df)
        
        # Further filter for awards-worthy movies
        awards_movies_df = filter_awards_worthy(fall_movies_df)
        
        # Convert the DataFrame to HTML for rendering in a browser
        awards_movies_html = awards_movies_df.to_html(classes='table table-striped')

        # Render the data in an HTML page
        return render_template('index.html', table=awards_movies_html)
    else:
        return "No awards-worthy movies data available."

# Route for visualizing awards-worthy movie ratings
@app.route('/fall-awards-plot')
def fall_awards_plot():
    # Fetch movies and apply filtering
    movies = get_movies_by_year(2023)
    movies_df = transform_movie_data(movies)
    fall_movies_df = filter_fall_releases(movies_df)
    awards_movies_df = filter_awards_worthy(fall_movies_df)

    # Create a Plotly figure for the movie ratings
    fig = px.histogram(awards_movies_df, x="vote_average", nbins=10, title="Distribution of Awards-Worthy Movie Ratings")
    
    # Convert the Plotly figure to JSON to render in the template
    graphJSON = fig.to_json()

    return render_template('plot.html', graphJSON=graphJSON)

# Route for displaying the most recent fall releases
@app.route('/new-fall-releases')
def new_fall_releases():
    # Fetch movies and apply filtering for fall and sort by release date
    movies = get_movies_by_year(2023)
    movies_df = transform_movie_data(movies)
    fall_movies_df = filter_fall_releases(movies_df)

    # Sort by most recent release dates
    fall_movies_df = fall_movies_df.sort_values(by="release_date", ascending=False)

    # Convert the DataFrame to HTML for rendering in a browser
    recent_movies_html = fall_movies_df.head(10).to_html(classes='table table-striped')

    return render_template('index.html', table=recent_movies_html)

if __name__ == '__main__':
    app.run(debug=True)

