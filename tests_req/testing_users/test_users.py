import pytest
import requests
from tests_req import config_path as path
from source.response import Response
from source.schemas.user_schema import User, Users_list, Not_Users, Not_Users_list
from param_for_test_users import NUMBER_OF_USERS, MIN_NUMBER_OF_USERS, STATUS_MIN, USER



@pytest.mark.parametrize("num_id, status, user", [(NUMBER_OF_USERS + 1, 404, Not_Users), (NUMBER_OF_USERS, 200, User), (0, 404, Not_Users), (-5, 404, Not_Users)])
def test_get_user(num_id, status, user):
    """
    This test checks status code and schema for single users (user found/user not found)
    """
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_SINGLE_USER + str(num_id))))
    response.assert_status(status).validate(user)

@pytest.mark.parametrize("page, per_page, status, users_list", [(NUMBER_OF_USERS, 1, 200, Users_list), (NUMBER_OF_USERS + 1, 1, 200, Not_Users_list), (MIN_NUMBER_OF_USERS, 1, STATUS_MIN, USER)])
def test_get_list_users(page, per_page, status, users_list):
    """
    This test checks status code and schema for list users.
    Id exists - information about the user is displayed
    Id does not exist - empty information about user is displayed
    """
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_USERS + f"?page={page}&per_page={per_page}")))
    response.assert_status(status).validate(users_list)

@pytest.mark.parametrize("delay, status", [(3, 200), (0, 200), (-1, 200), (5, 200), ("b", 200), ("", 200), ("-1n", 200)])
def test_delayed_resource(delay, status):
    """
    This test checks the status code and schema for pending requests on valid and invalid data.
    """
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_DELAYED_RESOURCED + str(delay))))
    response.assert_status(status).validate(Users_list)

@pytest.mark.parametrize("deleted_users, status", [(NUMBER_OF_USERS, 204), (-1, 204), ("b", 204)])
def test_delete_users(deleted_users, status):
    """
    This test checks status code and schema when deleting user.
    """
    response = requests.delete(url=path.SERVICE_DOMAIN + path.PATH_DELAYED_RESOURCED + str(deleted_users))
    assert response.status_code == status

