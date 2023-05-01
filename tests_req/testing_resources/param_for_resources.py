import requests
from tests_req import config_path as path


NUMBER_OF_RESOURCES = (requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_RESOURCE)).json())["total"]

print(NUMBER_OF_RESOURCES)
