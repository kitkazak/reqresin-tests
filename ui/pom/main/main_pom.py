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
        
        self.url_span = driver.find_element(
            By.XPATH,
            MainPageLocators.url_span)

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
    END Click methond buttons
    """

    def scroll_to_console_section(self):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", 
            self.console_section)
        
    def get_url_span_text(self):
        return self.url_span.text
    
    def get_method_button_by_data_id(self, data_id: int):
        element = None
        
        match data_id:
            case 'users':
                element = self.list_users_button
            case 'users-single':
                element = self.get_user_button
            case 'users-single-not-found':
                element = self.get_user_not_found_button
            
        return element

