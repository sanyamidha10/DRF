import requests

URL = 'http://127.0.0.1:8000/stuinfo/2'
r = requests.get(url=URL)

json_data = r.json()

print (json_data)