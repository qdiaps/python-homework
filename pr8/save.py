import requests

url = 'https://httpbin.org/html'
filename = 'result.html'

response = requests.get(url)
response.raise_for_status() 

with open(filename, 'w', encoding='utf-8') as file:
    file.write(response.text)
        
print(f"Вміст збережено у файл {filename}")

