import requests

url = 'https://httpbin.org/get'
response = requests.get(url)

print(response.status_code)

print("\nЗаголовки:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

print(response.text)
