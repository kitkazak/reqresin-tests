import pytest
from selenium import webdriver
import urllib3

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

"""
Test data:
    * Data-id of a method button
    * Expected url span text
"""

data_params = [
    ('users', '/api/users?page=2'),
    ('users-single', '/api/users/2'),
    ('users-single-not-found', '/api/users/23'),
    ('patch', '/api/users/2')
]

@pytest.fixture(params=data_params)
def data(request):
    return request.param

class TestUIMainPageMethodURLs():

    def test_method_buttons(
        self,
        driver_handler,
        data):
        
        driver = driver_handler
        driver.get("https://reqres.in/")

        data_id, expected_url_span_text = data

        main_page = MainPOM(driver=driver)
        main_page.scroll_to_console_section()

        element = main_page.get_method_button_by_data_id(data_id=data_id)
        driver.execute_script(
            "arguments[0].scrollIntoView();", 
            element)
        element.click()

        url_span_text = main_page.get_url_span_text()

        assert url_span_text == expected_url_span_text, \
            'Expected and actual texts do not match'