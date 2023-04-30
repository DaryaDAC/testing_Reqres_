import requests
import config_path as path
from source.schemas.user_schema import User, Users_list, Not_Users
import json

NUMBER_OF_RESOURCES = (requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_RESOURCE)).json())["total"]

print(NUMBER_OF_RESOURCES)
