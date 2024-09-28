from flask import Flask, render_template
import pandas as pd
import plotly.express as px
from scripts.data_ingestion import get_movies_from_2024
from scripts.data_transformation import transform_movie_data

app = Flask(__name__)

# Base route to display movie data and rating distribution for 2024
@app.route('/')
def index():
    # Fetch movies from 2024 up to today
    movies = get_movies_from_2024()
    
    if movies:
        # Transform the raw data into a DataFrame
        movies_df = transform_movie_data(movies)
        
        # Convert the DataFrame to HTML for rendering in a browser
        movies_html = movies_df.to_html(classes='table table-striped')

        # Create a Plotly figure for the movie ratings
        fig = px.histogram(movies_df, x="vote_average", nbins=10, title="Distribution of Movie Ratings (2024)")
        
        # Convert the Plotly figure to JSON for rendering
        graphJSON = fig.to_json()

        # Render the data and the plot in an HTML page
        return render_template('index.html', table=movies_html, graphJSON=graphJSON)
    else:
        return "No movie data available."

if __name__ == '__main__':
    app.run(debug=True)


