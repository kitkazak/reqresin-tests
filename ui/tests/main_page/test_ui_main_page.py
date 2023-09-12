import pytest
from selenium import webdriver
import urllib3
import time

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

class TestUIMainPage():

    def test_ui_main_page(
        self,
        driver_handler):
        
        driver = driver_handler
        driver.get("https://reqres.in/")

        time.sleep(10)
