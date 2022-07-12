'OPEN NOTIFY'
# TASK: Make a call to the API endpoint to get live information about astronauts in space

import requests
from pprint import pprint as pp

endpoint1 = 'http://api.open-notify.org/astros.json' # endpoint
endpoint2 = 'http://api.open-notify.org/iss-qpass.json'

payload = {'lat': 51.507, 'lon': 0.1278}

payload2 = {'lat': 40.71, 'lon': -74}

response = requests.get(endpoint2, params=payload)
print(response.status_code)

data = response.json()
pp(data)