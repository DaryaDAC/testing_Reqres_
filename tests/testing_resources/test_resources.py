import pytest
import requests
import config_path as path
from source.response import Response
from source.schemas.resource import Resource, Resources_list, Not_Resource, Not_Resources_list
from param_for_resources import NUMBER_OF_RESOURCES



@pytest.mark.parametrize("page, per_page, status, resources_list", [(NUMBER_OF_RESOURCES, 1, 200, Resources_list), (NUMBER_OF_RESOURCES+1, 1, 200, Not_Resources_list), (-13, 1, 200, Not_Resources_list)])
def test_get_list_resources(page, per_page, status, resources_list):
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_LIST_RESOURCE + f"?page={page}&per_page={per_page}")))
    response.assert_status(status).validate(resources_list)

@pytest.mark.parametrize("num_id, status, resource", [(NUMBER_OF_RESOURCES + 1, 404, Not_Resource), (NUMBER_OF_RESOURCES, 200, Resource), (0, 404, Not_Resource), (-5, 404, Not_Resource)])
def test_get_resource(num_id, status, resource):
    response = Response(requests.get(url=(path.SERVICE_DOMAIN + path.PATH_SINGLE_RESOURCE + str(num_id))))
    response.assert_status(status).validate(resource)

