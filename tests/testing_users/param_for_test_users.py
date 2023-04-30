import requests
import config_path as path
from source.schemas.user_schema import User, Users_list, Not_Users
import json

NUMBER_OF_USERS = (requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_USERS)).json())["total"]
page = 1
per_page = 2
Req = requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_USERS + f"?page={page}&per_page={per_page}")).json()
print(Req)
print(NUMBER_OF_USERS)