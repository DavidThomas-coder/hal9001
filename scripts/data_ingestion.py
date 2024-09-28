import requests
from datetime import datetime
from scripts.config import API_KEY, BASE_URL

def get_movies_from_2024():
    """
    Retrieve movies released from January 1, 2024, up to the current date.
    """
    url = f"{BASE_URL}/discover/movie"
    # Get today's date in YYYY-MM-DD format
    today = datetime.today().strftime('%Y-%m-%d')
    
    params = {
        "api_key": API_KEY,
        "primary_release_date.gte": "2024-01-01",
        "primary_release_date.lte": today,  # Set the upper limit to today's date
        "sort_by": "popularity.desc",
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()  # Return the raw JSON response
    else:
        print(f"Error: {response.status_code}")
        return None