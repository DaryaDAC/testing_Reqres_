import requests
from tests_req import config_path as path
from source.schemas.user_schema import Users_list, Not_Users_list
from allure_combine import combine_allure

NUMBER_OF_USERS = (requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_USERS)).json())["total"]
if NUMBER_OF_USERS > 0:
    MIN_NUMBER_OF_USERS = 1
    STATUS_MIN = 200
    USER = Users_list
else:
    STATUS_MIN = 404
    MIN_NUMBER_OF_USERS = -1
    USER = Not_Users_list
