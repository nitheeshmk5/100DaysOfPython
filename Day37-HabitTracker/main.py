import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

TOKEN = os.getenv('USER_TOKEN')
USER_NAME = os.getenv('USER_NAME')
GRAPH_ID = 'graph01'

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token' : TOKEN,
    'username':USER_NAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# response = requests.post(url=pixela_user,json=user_params)
# print(response.text)

pixela_graph = f'{pixela_endpoint}/{USER_NAME}/graphs'
graph_params ={
    'id' : GRAPH_ID,
    'name' : 'Coding graph',
    'unit' : 'Hrs',
    'type' : 'float',
    'color' : 'momiji'
}

headers = {
    'X-USER-TOKEN' : TOKEN
}

# response = requests.post(url=pixela_graph,json=graph_params,headers=headers)

# print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}'

now = datetime.now()
today_date = now.strftime("%Y%m%d")  #'YYYYMMDD'


pixel_params = {
    'date':today_date,
    'quantity':'5.30',    
}

res = requests.post(url=pixel_creation_endpoint, json=pixel_params,headers=headers)

print(res.text)

