import http.client
import json 
from urllib.parse import quote_plus


base_url = 'https://nominatim.openstreetmap.org/search'
url_path = '{}?q={}&format=json'.format(base_url,'taipei')
headers = {'User-agent':'Demo'}
conection = http.client.HTTPSConnection('nominatim.openstreetmap.org')



reply = 1
print(reply[0]['display_name'])
print(reply[0]['lon'])
print(reply[0]['lat'])