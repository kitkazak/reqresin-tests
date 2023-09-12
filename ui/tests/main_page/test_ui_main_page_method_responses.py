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
from api.requests.users.delete_user import DeleteUserRequest
from api.requests.register.register_user import RegisterUserRequest
from api.requests.login.login_user import LoginUserRequest  

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
        
        """
        Delete user
        """

        element = main_page.delete_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_code = int(main_page.response_code.text)

        # Delete user Request

        request = DeleteUserRequest(user_id=2)
        request.send()

        response_code = request.response.status_code

        assert output_code == response_code, \
            'UI Output status code and API status code json do not match'
        
        """
        Register user successsful
        """

        element = main_page.register_successful_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # Register user successful Request

        body = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        request = RegisterUserRequest(json=body)
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'

        """
        Register user unsuccesssful
        """

        element = main_page.register_unsuccessful_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # Register user unsuccessful Request

        body = {
            "email": "ydney@fife",
        }

        request = RegisterUserRequest(json=body)
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'
        
        """
        Login user successsful
        """

        element = main_page.login_successful_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # Login user successful Request

        body = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        request = LoginUserRequest(json=body)
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'

        """
        Login user unsuccesssful
        """

        element = main_page.login_unsuccessful_button
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        time.sleep(0.5)
        output_response = json.loads(main_page.output_response.text)

        # Login user unsuccessful Request

        body = {
            "email": "ydney@fife",
        }

        request = LoginUserRequest(json=body)
        request.send()

        response_json = request.response.json()

        assert output_response == response_json, \
            'UI Output response and API Response json do not match'
