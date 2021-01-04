import requests



url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}

r = requests.post(url, json=payload)
print(r.text)