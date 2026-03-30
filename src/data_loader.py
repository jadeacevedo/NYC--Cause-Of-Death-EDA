import requests
import json

def fetch_data_from_api(url='http://data.cityofnewyork.us/api/views/jb7j-dtam/rows.json'):
    """Fetches the dataset from NYC Open Data API."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def load_local_data(filepath="/workspaces/NYC--Cause-Of-Death-EDA/Data/NY_cause_of_death.py"):
    """Loads dataset from a local JSON file (useful for large files)."""
    with open(filepath, 'r') as file:
        return json.load(file)