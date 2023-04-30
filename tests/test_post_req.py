import pytest
import requests
import config_path as path
from source.response import Response
from source.schemas.user_schema import User, Users_list, User_update
from source.schemas.resource import Resource, Resources_list

my_obj = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

my_obj2 = {
    "name": "morpheus",
    "job": "leader"
}

@pytest.mark.parametrize()
def test_post_register():
    response = Response(requests.post(path.SERVICE_DOMAIN + path.PATH_REGISTER, json=my_obj))
    response.assert_status(200)


def test_post_login():
    response = Response(requests.post(path.SERVICE_DOMAIN + path.PATH_LOGIN, json=my_obj))
    response.assert_status(200)

def test_post_create_user():
    response = Response(requests.post(path.SERVICE_DOMAIN + path.PATH_CREATE, json=my_obj2))
    response.assert_status(201)

def test_put_update():
    response = Response(requests.put(path.SERVICE_DOMAIN + path.PATH_SINGLE_USER, json=my_obj2))
    response.assert_status(200).validate(User_update)


