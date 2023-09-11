import pytest
from api.requests.login.login_user import LoginUserRequest

"""
Positive test data:
    * Email
    * Password
    * Expected status code
    * Expected response token
"""

positive_test_data_params = [
    ('eve.holt@reqres.in', 
    'cityslicka',
    200,
    'QpwL5tke4Pnpja7X4'),
]

@pytest.fixture(params=positive_test_data_params)
def positive_test_data(request):
    return request.param

"""
Negative test data:
    * Email
    * Expected status code
    * Expected error message
"""

negative_test_data_params = [
    ('peter@klaven', 
    400,
    'Missing password'),
]

@pytest.fixture(params=negative_test_data_params)
def negative_test_data(request):
    return request.param

"""
Tests
"""

class TestApiLoginUser():

    def test_api_login_user_positive(
        self,
        positive_test_data
        ):

        email, password, \
        expected_status_code, expected_response_token = positive_test_data
        
        body = {
            'email': email,
            'password': password,
        }

        request = LoginUserRequest(json=body)
        request.send()

        response_json = request.response.json()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'

        assert response_json['token'] == expected_response_token, \
            f'\nExpected token: {expected_response_token}' \
            f'\nActual token: {response_json["token"]}'  \
            f'\nResponse body: {request.response.content}'
        
    def test_api_login_user_negative(
        self,
        negative_test_data
        ):

        email, \
        expected_status_code, expected_error_message = negative_test_data
        
        body = {
            'email': email,
        }

        request = LoginUserRequest(json=body)
        request.send()

        response_json = request.response.json()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'
        
        assert response_json['error'] == expected_error_message, \
            f'\nExpected error message: {expected_error_message}' \
            f'\nActual error message: {response_json["error"]}'  \
            f'\nResponse body: {request.response.content}'
        