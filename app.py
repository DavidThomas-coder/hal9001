from flask import Flask, render_template
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN
from scripts.data_ingestion import get_movies_from_2024
from scripts.data_transformation import transform_movie_data

app = Flask(__name__)

# Base route to display movie data and Bokeh plot for 2024
@app.route('/')
def index():
    # Fetch movies from 2024 up to today
    movies = get_movies_from_2024()
    
    if movies:
        # Transform the raw data into a DataFrame
        movies_df = transform_movie_data(movies)
        
        # Convert the DataFrame to HTML for rendering in a browser
        movies_html = movies_df.to_html(classes='table-auto w-full border-collapse')

        # Create Bokeh plot for movie ratings
        p = figure(title="Distribution of Movie Ratings (2024)",
                   x_axis_label='Rating', y_axis_label='Number of Movies', 
                   height=350, width=800)  # Use 'height' and 'width' instead of 'plot_height' and 'plot_width'

        # Create a histogram of vote_average
        hist, edges = pd.cut(movies_df['vote_average'], bins=10, retbins=True)
        ratings = hist.value_counts(sort=False)

        # Add the histogram to the Bokeh plot
        p.quad(top=ratings, bottom=0, left=edges[:-1], right=edges[1:], 
               fill_color="navy", line_color="white", alpha=0.7)

        # Get the components (script and div) to embed the plot
        script, div = components(p, CDN)

        # Render the HTML template with the table and Bokeh plot
        return render_template('index.html', table=movies_html, bokeh_script=script, bokeh_div=div)
    else:
        return "No movie data available."

if __name__ == '__main__':
    app.run(debug=True)
