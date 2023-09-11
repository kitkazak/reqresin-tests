import pytest
from api.requests.resource.list_resources import ListResourcesRequest

"""
Test data:
    * Expected status code
    * Expected response total
"""

positive_test_data_params = [
    (200, 12)
]

@pytest.fixture(params=positive_test_data_params)
def positive_test_data(request):
    return request.param

"""
Tests
"""

class TestApiListResources():

    def test_api_list_users_positive(
        self,
        positive_test_data
        ):

        expected_status_code, expected_total = positive_test_data
        
        request = ListResourcesRequest()
        request.send()

        response_json = request.response.json()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'
        
        assert response_json['total'] == expected_total, \
            f'\nExpected value: {expected_total}' \
            f'\nActual status code: {response_json["total"]}'  \
            f'\nResponse body: {request.response.content}'
        