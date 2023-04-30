import requests
import config_path as path
from source.response import Response
from source.schemas.user_schema import User, Users_list
from source.schemas.resource import Resource


def test_get_user_nf():
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_SINGLE_USER_NF)))
    print(response)
    response.assert_status(404)

def test_get_user():
    response = requests.get(url=(path.SERVICE_DOMAIN + path.PATH_SINGLE_USER))
    test_obj = Response(response)
    test_obj.assert_status(200).validate(User)

def test_get_list_users():
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_USERS)))
    response.assert_status(200).validate(Users_list)

def test_get_list_resources():
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_RESOURCE)))
    response.assert_status(200)

def test_get_resource():
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_SINGLE_RESOURCE)))
    response.assert_status(200).validate(Resource)

def test_get_resource_nf():
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_SINGLE_RESOURCE_NF)))
    response.assert_status(404)

def test_delayed_resource():
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_DELAYED_RESOURCED)))
    response.assert_status(200)


