import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "gulab"
TOKEN = "thisthetoken"
GRAPH_ID = "graph2"

parameters = {
    "token": "thisthetoken",
    "username":"gulab",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# reponse = requests.post(url=pixela_endpoint,json=parameters)
# print(reponse.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":"graph2",
    "name":"cycling",
    "unit":"km",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# response =requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")
pixel_data = {
    "date":today,
    "quantity":input("How many km did you cycle today?")
}


print(today)
response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
put_data = {
    "quantity" : "11"
}
# response = requests.put(url=put_endpoint,json=put_data,headers=headers)
# print(response.text)