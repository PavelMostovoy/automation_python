import requests

cred  = ("admin", "admin123")
url_0 = "https://www.aqa.science/"
url_1 = "https://www.aqa.science/users/"
url_2 = "https://www.aqa.science/users/3032/"
#
# response = requests.get(url_2, auth = cred)
# print(response.status_code)
# print(response.text)

session = requests.Session()
session.auth = cred

first_resp = session.get(url_1)
second_response = session.get(url_2)

print(first_resp.text)
print(second_response.text)