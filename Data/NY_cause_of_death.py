# Data set: New York City Leading Causes of Death
# https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam
url = 'http://data.cityofnewyork.us/api/views/jb7j-dtam/rows.json'
results = requests.get(url).json()