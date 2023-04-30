import pytest
import requests
import config_path as path
@pytest.fixture
def get_path_user():
    response = requests.get(path.SERVICE_DOMAIN + path.PATH_SINGLE_USER + '2')
    return response
