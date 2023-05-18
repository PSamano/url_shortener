import requests
import json

url = "http://localhost:5000/shorten"
data = {'url': 'https://www.example.com'}

response = requests.post(url, json=data)
print(response.text)
print(type(response.text))

json_data = json.loads(response.text)
print(json_data)
print(json_data['shortcode'])

shortcode = json_data['shortcode']
shortcode = "sNEOSc"
url = "http://localhost:5000/" + shortcode

response_get = requests.get(url)

print(response_get.url)
