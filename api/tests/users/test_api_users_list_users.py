import pytest
from api.requests.users.list_users import ListUsersRequest

"""
Test data:
    * Page ID
    * Per page ID
    * Expected status code
"""

positive_test_data_params = [
    (1, None, 200),
    (1, 2, 200),
]

@pytest.fixture(params=positive_test_data_params)
def positive_test_data(request):
    return request.param

negative_test_data_params = [
    (-1, None, 400),
    (0, None, 400),
    ('Hello', 'World', 400),
]

@pytest.fixture(params=negative_test_data_params)
def negative_test_data(request):
    return request.param

"""
Tests
"""

class TestApiListUsers():

    def test_api_list_users_positive(
        self,
        positive_test_data
        ):

        page_id, per_page_id, \
        expected_status_code = positive_test_data
        
        request = ListUsersRequest(page_id=page_id, per_page_id=per_page_id)
        request.send()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'
        
    def test_api_list_users_negative(
        self,
        negative_test_data
        ):

        page_id, per_page_id, expected_status_code = negative_test_data
        
        request = ListUsersRequest(page_id=page_id, per_page_id=per_page_id)
        request.send()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'