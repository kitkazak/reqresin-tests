import pytest
import time
from api.requests.users.delay import DelayRequest

"""
Test data:
    * Given delay
    * min Actual delay
    * max Actual delay
    * Expected status code
"""

positive_test_data_params = [
    (3, 2.25, 3.75, 200),
    (5, 4.25, 5.75, 200),
    (1, 0.25, 1.75, 200),
]

@pytest.fixture(params=positive_test_data_params)
def positive_test_data(request):
    return request.param

negative_test_data_params = [
    ('Hello', None, None, 400),
]

@pytest.fixture(params=negative_test_data_params)
def negative_test_data(request):
    return request.param

"""
Tests
"""

class TestAPIDelay():

    def test_api_delay_positive(
        self,
        positive_test_data
        ):

        given_delay, min, \
        max, expected_status_code = positive_test_data
        
        request = DelayRequest(delay=given_delay)
        start = time.time()
        request.send()
        end = time.time()
        actual_delay = end - start

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'
        
        assert actual_delay >= min and actual_delay <= max, \
            "Actual delay is not close to given delay"
        
    @pytest.mark.xfail
    def test_api_delay_negative(
        self,
        negative_test_data
        ):

        given_delay, min, \
        max, expected_status_code = negative_test_data
        
        request = DelayRequest(delay=given_delay)
        request.send()

        assert request.response.status_code == expected_status_code, \
            f'\nExpected status code: {expected_status_code}' \
            f'\nActual status code: {request.response.status_code}'  \
            f'\nResponse body: {request.response.content}'