import requests as rq 
from datetime import datetime

BASE_URL = 'https://dulithaction1.pythonanywhere.com/'
payload = {'input': 'test'}
response = rq.get(BASE_URL, params=payload)
json_value = response.json()

print(f"Response: {json_value}")