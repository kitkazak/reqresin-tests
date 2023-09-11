import pytest
from api.requests.users.get_user import GetUserRequest

"""
Positive test data:
    * User ID
    * Expected status code
"""

positive_test_data_params = [
    (2, 200),
    (1, 200),
    (3, 200)
]

@pytest.fixture(params=positive_test_data_params)
def positive_test_data(request):
    return request.param

negative_test_data_params = [
    ('one', 404),
    ('two', 404),
    ('three', 404),
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

        user_id, expected_status_code = positive_test_data
        
        request = GetUserRequest(user_id=user_id)
        request.send()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'
        
    def test_api_get_user_negative(
        self,
        negative_test_data
        ):

        user_id, expected_status_code = negative_test_data
        
        request = GetUserRequest(user_id=user_id)
        request.send()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'
