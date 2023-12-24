import requests
from datetime import datetime
URL = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = ""
GRAPH_ID = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=URL, json=user_params)
# print(response.text)

graph_URL = f"{URL}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_URL, json=graph_params, headers=headers)
# print(response.text)

post_URL = f"{graph_URL}/{GRAPH_ID}"

today = datetime.now()
td = today.strftime("%Y%m%d")
post_params = {
    "date": td,
    "quantity": "10",
}

# response = requests.post(url=post_URL, json=post_params, headers=headers)
# print(response.text)

update_URL = f"{post_URL}/{td}"

update_params = {
    "quantity": "15"
}

# response = requests.put(url=update_URL, json= update_params, headers=headers)
# print(response.text)

response = requests.delete(url=update_URL, headers=headers)
print(response.text)