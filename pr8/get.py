import requests

url = 'https://youtube.com'

response = requests.get(url)

print("--- Вміст сторінки (відповідь сервера) ---")
print(response.text)
