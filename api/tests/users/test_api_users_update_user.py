import pytest
from api.requests.users.update_user import UpdateUserRequest

"""
Positive test data:
    * User ID
    * Name
    * Job
    * Expected status code
    * Expected response name
    * Expected response job
"""

positive_test_data_params = [

    (2,
    'morpheus', 
    'zion resident', 
    200, 
    'morpheus', 
    'zion resident'),

]

@pytest.fixture(params=positive_test_data_params)
def positive_test_data(request):
    return request.param

"""
Negative test data:
    * User ID
    * Expected status code
"""

negative_test_data_params = [

    (2,
    404),

]

@pytest.fixture(params=negative_test_data_params)
def negative_test_data(request):
    return request.param

"""
Tests
"""

class TestApiUpdateUser():

    def test_api_update_user_positive(
        self,
        positive_test_data):

        user_id, name, job, expected_status_code, \
        expected_response_name, expected_response_job = positive_test_data

        body = {
            'name': name,
            'job': job,
        }
        
        request = UpdateUserRequest(user_id=user_id, json=body)
        request.send()

        response_json = request.response.json()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}' \
            f'\nResponse body: {request.response.content}'
        
        assert response_json['name'] == expected_response_name, \
            f'\nExpected value: {expected_response_name}' \
            f'\nActual value: {response_json["name"]}' \
            f'\nResponse body: {request.response.content}'
        
        assert response_json['job'] == expected_response_job, \
            f'\nExpected value: {expected_response_job}' \
            f'\nActual value: {response_json["job"]}' \
            f'\nResponse body: {request.response.content}'
        
    def test_api_update_user_negative(
        self,
        negative_test_data):

        user_id, expected_status_code = negative_test_data

        request = UpdateUserRequest(user_id=user_id, json=None)
        request.send()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}' \
            f'\nResponse body: {request.response.content}'
        