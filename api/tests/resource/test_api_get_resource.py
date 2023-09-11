import pytest
from api.requests.resource.get_resource import GetResourceRequest

"""
Positive test data:
    * Resource ID
    * Expected status code
    * Expected name
"""

positive_test_data_params = [
    (1, 200, "cerulean"),
    (2, 200, "fuchsia rose"),
    (3, 200, "true red")
]

@pytest.fixture(params=positive_test_data_params)
def positive_test_data(request):
    return request.param

negative_test_data_params = [
    (23, 404),
    (24, 404),
]

@pytest.fixture(params=negative_test_data_params)
def negative_test_data(request):
    return request.param

"""
Tests
"""

class TestApiGetUser():

    def test_api_get_user_positive(
        self,
        positive_test_data
        ):

        resource_id, expected_status_code, \
        expected_name = positive_test_data
        
        request = GetResourceRequest(resource_id=resource_id)
        request.send()

        response_json = request.response.json()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'
        
        assert response_json['data']['name'] == expected_name, \
            f'\nExpected value: {expected_name}' \
            f'\nActual value: {response_json["data"]["name"]}'  \
            f'\nResponse body: {request.response.content}'
        
        
    def test_api_get_user_negative(
        self,
        negative_test_data
        ):

        resource_id, expected_status_code = negative_test_data
        
        request = GetResourceRequest(resource_id==resource_id)
        request.send()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'
