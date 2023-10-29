from urllib import response
import requests

base_url = 'https://nominatim.openstreetmap.org/search'
parameters = {'q':'taipei','format':'json'}
headers = {'User-agent':'Demo'}
response = requests.get(base_url, params=parameters, headers=headers)
reply = response.json()

print(reply[0]['display_name'])
print(reply[0]['lon'])
print(reply[0]['lat'])