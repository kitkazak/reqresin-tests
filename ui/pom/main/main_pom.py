from selenium import webdriver
from selenium.webdriver.common.by import By
from ui.pom.main.main_locators import MainPageLocators

class MainPOM:

    def __init__(
        self,
        driver: webdriver):
        
        self.driver = driver

        """
        Method buttons
        """

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
        
        self.post_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.post_button) 

        self.put_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.put_button) 

        self.patch_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.patch_button)
        
        self.delete_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.delete_button)
        
        self.register_successful_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.register_successful_button)
        
        self.register_unsuccessful_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.register_unsuccessful_button)
        
        self.login_successful_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.login_successful_button)
        
        self.login_unsuccessful_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.login_unsuccessful_button)
        
        self.delay_button = driver.find_element(
            By.XPATH, 
            MainPageLocators.delay_button)
        
        """
        END Method buttons
        """
        
        self.console_section = driver.find_element(
            By.XPATH,
            MainPageLocators.console_section)
        
        self.url_span = driver.find_element(
            By.XPATH,
            MainPageLocators.url_span)

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
            case 'unknown':
                element = self.list_resources_button
            case 'unknown-single':
                element = self.get_resource_button
            case 'unknown-single-not-found':
                element = self.get_resource_not_found_button
            case 'post':
                element = self.post_button
            case 'put':
                element = self.put_button
            case 'patch':
                element = self.patch_button
            case 'delete':
                element = self.delete_button
            case 'register-successful':
                element = self.register_successful_button
            case 'register-unsuccessful':
                element = self.register_unsuccessful_button
            case 'login-successful':
                element = self.register_successful_button
            case 'login-unsuccessful':
                element = self.login_unsuccessful_button
            case 'delay':
                element = self.delay_button
            case _:
                raise BaseException('No such data-id')

        return element

