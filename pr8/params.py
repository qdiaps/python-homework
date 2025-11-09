import requests

url = 'https://youtube.com/results'

my_params = {
    'search_query': 'python',
}

response = requests.get(url, params=my_params)

print(response)
