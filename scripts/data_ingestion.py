import requests
from scripts.config import API_KEY, BASE_URL

def get_movies_by_year(year):
    """
    Function to retrieve movies from the TMDb API by a specific year.
    """
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "primary_release_year": year,
        "sort_by": "popularity.desc",
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()  # Return the raw JSON response
    else:
        print(f"Error: {response.status_code}")
        return None

