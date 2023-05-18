import requests
import json

url = "https://4o6ybihyw3.execute-api.us-east-2.amazonaws.com/dev/shorten/"
data = {'url': 'https://www.example.com'}

# Realizar una solicitud POST para acortar la URL
response = requests.post(url, json=data)
print(response.text)
print(type(response.text))

# Convertir la respuesta en JSON
json_data = json.loads(response.text)
print(json_data)
print(json_data['shortcode'])

# Realizar una solicitud GET para redirigir a la URL original
shortcode = json_data['shortcode']
url = "https://4o6ybihyw3.execute-api.us-east-2.amazonaws.com/dev/shortcode/" + shortcode

response_get = requests.get(url)

# Imprimir la URL redirigida
print(response_get.url)
