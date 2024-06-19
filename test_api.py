import sys
import requests
import json

url = 'http://127.0.0.1:8000/villagers'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Pretty-print JSON with indentation for readability
    print(json.dumps(data, indent=4))
else:
    print(f"Error fetching data. Status code: {response.status_code}")
