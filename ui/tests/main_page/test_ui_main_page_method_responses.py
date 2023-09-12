import pytest
import urllib3
import json
import time
from selenium import webdriver

from api.requests.users.list_users import ListUsersRequest
from api.requests.users.get_user import GetUserRequest
from api.requests.resource.list_resources import ListResourcesRequest
from api.requests.resource.get_resource import GetResourceRequest
from api.requests.users.update_user import UpdateUserRequest

from ui.pom.main.main_pom import MainPOM

def setup():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

def teardown(driver: webdriver):
    if (driver != None):
        driver.close()
        driver.quit()

@pytest.fixture(autouse=True)
def driver_handler():
    driver = setup()
    yield driver
    teardown(driver=driver)

class TestUIMainPageMethodRespones():

    def test_ui_main_page_method_responses(
        self,
        driver_handler):
        
        driver = driver_handler
        driver.get("https://reqres.in/")

        main_page = MainPOM(driver=driver)
        main_page.scroll_to_console_section()

        """
        List users
        """

        element = main_page.list_users_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        # Не понимаю почему, 
        # но без паузы json не всегда конверится в dict :(
        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # List users Request

        request = ListUsersRequest(page_id=2, per_page_id=None)
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'
        
        """
        Get single user
        """

        element = main_page.get_user_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # Get user Request

        request = GetUserRequest(user_id=2)
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'
        
        """
        Get single user not found
        """

        element = main_page.get_user_not_found_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # Get user not found Request

        request = GetUserRequest(user_id=23)
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'
        
        """
        List resource
        """

        element = main_page.list_resources_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # List resource Request

        request = ListResourcesRequest()
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'
        
        """
        Get resource
        """

        element = main_page.get_resource_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # Get resource Request

        request = GetResourceRequest(resource_id=2)
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'
        
        """
        Get resource not found
        """

        element = main_page.get_resource_not_found_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # Get resource not found Request

        request = GetResourceRequest(resource_id=23)
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'
        
        """
        Update user
        """

        element = main_page.put_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # Update user Request

        body = {
            "name": "morpheus",
            "job": "zion resident"
        }

        request = UpdateUserRequest(user_id=2, json=body)
        request.send()

        response_json = request.response.json()

        assert output_response['name'] == response_json['name'] and \
            output_response['job'] == response_json['job'], \
            'UI Output response and API Response json do not match'
        
