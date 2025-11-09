import requests

url = 'https://httpbin.org/post'

login_data = {
    'username': 'username',
    'password': 'password'
}

response = requests.post(url, data=login_data)

print(response.json()['form'])
