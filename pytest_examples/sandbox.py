import requests

url = "https://ithillel.ua/n/"

response = requests.get(url)

print(response.status_code)

print(response.elapsed.total_seconds())

with open("index.html", "w+") as f:
    f.write(response.text)