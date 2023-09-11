import pytest
from api.requests.register.register_user import RegisterUserRequest

"""
Positive test data:
    * Username
    * Email
    * Password
    * Expected status code
    * Expected response id
"""

positive_test_data_params = [

    (None, 
    'eve.holt@reqres.in', 
    'pistol', 
    200,
    4),

]

@pytest.fixture(params=positive_test_data_params)
def positive_test_data(request):
    return request.param

"""
Negative test data:
    * Username
    * Email
    * Password
    * Expected status code
    * Expected error message
"""

negative_test_data_params = [

    (None, 
    None, 
    'pistol', 
    400,
    'Missing email or username'),

]

@pytest.fixture(params=negative_test_data_params)
def negative_test_data(request):
    return request.param

"""
Tests
"""

class TestApiRegisterUser():

    def test_api_register_user_positive(
        self,
        positive_test_data):

        username, email, \
        password, expected_status_code, \
        expected_response_id = positive_test_data

        body = {
            'username': username,
            'email': email,
            'password': password,
        }
        
        request = RegisterUserRequest(json=body)
        request.send()

        response_json = request.response.json()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}' \
            f'\nResponse body: {request.response.content}'
        
        assert response_json['id'] == expected_response_id, \
            f'\nExpected value: {expected_response_id}' \
            f'\nActual value: {response_json["id"]}' \
            f'\nResponse body: {request.response.content}'
        
    def test_api_register_user_negative(
        self,
        negative_test_data):

        username, email, \
        password, expected_status_code, \
        expected_error_message = negative_test_data

        body = {
            'username': username,
            'email': email,
            'password': password,
        }
        
        request = RegisterUserRequest(json=body)
        request.send()

        response_json = request.response.json()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}' \
            f'\nResponse body: {request.response.content}'
        
        assert response_json['error'] == expected_error_message, \
            f'\nExpected value: {expected_error_message}' \
            f'\nActual value: {response_json["error"]}' \
            f'\nResponse body: {request.response.content}'