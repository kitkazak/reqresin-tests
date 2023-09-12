from selenium import webdriver
from selenium.webdriver.common.by import By
from ui.pom.main.main_locators import MainPageLocators

class MainPOM:

    def __init__(
        self,
        driver: webdriver):
        
        self.driver = driver

        self.list_users_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.list_users_button)
        
        self.get_user_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.get_user_button) 
            
        self.get_user_not_found_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.get_user_not_found_button) 

        self.list_resources_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.list_resources_button) 

        self.get_resource_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.get_resource_button) 

        self.get_resource_not_found_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.get_resource_not_found_button)
        
        self.console_section = driver.find_element(
            By.XPATH,
            MainPageLocators.console_section)

    """
    Click method buttons
    """

    def click_list_users_button(self):
        self.list_users_button.click()

    def click_get_user_button(self):
        self.get_user_button.click()

    def click_get_user_not_found_button(self):
        self.get_user_not_found_button.click()

    def click_list_resources_button(self):
        self.list_resources_button.click()

    def click_get_resource_button(self):
        self.get_resource_button.click()

    def click_get_resource_not_found_button(self):
        self.get_resource_not_found_button.click()

    """
    Scroll to console section
    """

    def scroll_to_console_section(self):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", 
            self.console_section)

