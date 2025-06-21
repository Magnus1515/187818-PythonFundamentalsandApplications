import requests 

response  = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
data_json = response.text

data = json.loads(data_json)

print(data)