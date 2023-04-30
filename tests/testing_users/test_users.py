import pytest
import requests
import config_path as path
from source.response import Response
from source.schemas.user_schema import User, Users_list, Not_Users, Not_Users_list
from param_for_test_users import NUMBER_OF_USERS



@pytest.mark.parametrize("num_id, status, user", [(NUMBER_OF_USERS + 1, 404, Not_Users), (NUMBER_OF_USERS, 200, User), (0, 404, Not_Users), (-5, 404, Not_Users)])
def test_get_user(num_id, status, user):
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_SINGLE_USER + str(num_id))))
    response.assert_status(status).validate(user)

@pytest.mark.parametrize("page, per_page, status, users_list", [(NUMBER_OF_USERS, 1, 200, Users_list), (NUMBER_OF_USERS + 1, 1, 200, Not_Users_list)])
def test_get_list_users(page, per_page, status, users_list):
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_USERS + f"?page={page}&per_page={per_page}")))
    response.assert_status(status).validate(users_list)

def test_delayed_resource():
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_DELAYED_RESOURCED)))
    response.assert_status(200).validate(Users_list)

def test_delete_users():
    response = requests.delete(url = (path.SERVICE_DOMAIN + path.PATH_SINGLE_USER))
    assert response.status_code == 204


