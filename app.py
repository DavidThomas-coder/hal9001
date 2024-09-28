from flask import Flask, render_template
import pandas as pd
import plotly.express as px
from scripts.data_ingestion import get_movies_from_2024
from scripts.data_transformation import transform_movie_data

app = Flask(__name__)

# Route to display movie data from 2024 up to the current date
@app.route('/movies-2024')
def movies_2024():
    # Fetch movies from 2024 up to today
    movies = get_movies_from_2024()
    
    if movies:
        # Transform the raw data into a DataFrame
        movies_df = transform_movie_data(movies)
        
        # Convert the DataFrame to HTML for rendering in a browser
        movies_html = movies_df.to_html(classes='table table-striped')

        # Render the data in an HTML page
        return render_template('index.html', table=movies_html)
    else:
        return "No movie data available."

# Route for visualizing movie ratings
@app.route('/movies-2024-plot')
def movies_2024_plot():
    # Fetch movies and transform the data
    movies = get_movies_from_2024()
    movies_df = transform_movie_data(movies)

    # Create a plotly figure for the movie ratings
    fig = px.histogram(movies_df, x="vote_average", nbins=10, title="Distribution of Movie Ratings (2024)")
    
    # Convert the Plotly figure to JSON to render in the template
    graphJSON = fig.to_json()

    return render_template('plot.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)


