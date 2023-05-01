import pytest
import requests
from tests_req import config_path as path
from source.response import Response
from source.schemas.registration import User_reg_get_info as reg_info, User_reg_error as reg_err, User_get_token as token, User_update, User_create_info as cr_info, User_err
from registration_form import registration_form as rf
from create_form import create_form as cf



@pytest.mark.parametrize("reg_form, status, reg", [(rf[0], 200, reg_info), (rf[1], 200, reg_info), (rf[2], 400, reg_err), (rf[3], 400, reg_err), (rf[4], 400, reg_err), (rf[5], 400, reg_err)])
def test_post_registration(reg_form, status, reg):
    """
    This test checks the status code and response schema for valid and invalid registration data
    """
    response = Response(requests.post(path.SERVICE_DOMAIN + path.PATH_REGISTER, json=reg_form))
    response.assert_status(status).validate(reg)

@pytest.mark.parametrize("reg_form, status, login", [(rf[0], 200, token), (rf[1], 200, token), (rf[2], 400, reg_err), (rf[3], 400, reg_err), (rf[4], 400, reg_err), (rf[5], 400, reg_err)])
def test_post_login(reg_form, status, login):
    """
    This test checks the status code and response schema for a login request
    """
    response = Response(requests.post(path.SERVICE_DOMAIN + path.PATH_LOGIN, json=reg_form))
    response.assert_status(status).validate(login)

@pytest.mark.parametrize("user_form, status, create_form", [(cf[0], 201, cr_info), (cf[1], 201, User_err), (cf[2], 201, User_err), (cf[3], 201, User_err), (cf[4], 201, cr_info), (cf[5], 201, User_err)])
def test_post_create_user(user_form, status, create_form):
    """
    This test checks the status code and response scheme to create a user.
    """
    response = Response(requests.post(path.SERVICE_DOMAIN + path.PATH_CREATE, json=user_form))
    response.assert_status(status).validate(create_form)

@pytest.mark.parametrize("user_form, status, update_form", [(cf[0], 200, User_update), (cf[1], 200, User_err), (cf[2], 200, User_err), (cf[3], 200, User_err), (cf[4], 200, User_update), (cf[5], 200, User_err)])
def test_put_update(user_form, status, update_form):
    """
    This test checks the status code and response scheme for update user.
    """
    response = Response(requests.put(path.SERVICE_DOMAIN + path.PATH_UPDATE_USER, json=user_form))
    response.assert_status(status).validate(update_form)

@pytest.mark.parametrize("user_form, status, update_form", [(cf[0], 200, User_update), (cf[1], 200, User_err), (cf[2], 200, User_err), (cf[3], 200, User_err), (cf[4], 200, User_update), (cf[5], 200, User_err)])
def test_patch_update(user_form, status, update_form):
    response = Response(requests.patch(path.SERVICE_DOMAIN + path.PATH_UPDATE_USER, json=user_form))
    response.assert_status(status).validate(update_form)


