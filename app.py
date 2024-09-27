from flask import Flask, render_template
import pandas as pd
from scripts.data_ingestion import get_movies_by_year
from scripts.data_transformation import transform_movie_data

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch movies from 2023
    movies = get_movies_by_year(2023)
    
    if movies:
        # Transform the raw data into a DataFrame
        movies_df = transform_movie_data(movies)
        
        # Convert the DataFrame to HTML for rendering in a browser
        movies_html = movies_df.to_html(classes='table table-striped')
        
        # Render the data in an HTML page
        return render_template('index.html', table=movies_html)
    else:
        return "No movies data available."

if __name__ == '__main__':
    app.run(debug=True)
