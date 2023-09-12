class MainPageLocators:

    """
    Method buttons
    """

    list_users_button = '//li[@data-id="users"]'
    get_user_button = '//li[@data-id="users-single"]'
    get_user_not_found_button = '//li[@data-id="users-single-not-found"]'
    list_resources_button = '//li[@data-id="unknown"]'
    get_resource_button = '//li[@data-id="unknown-single"]'
    get_resource_not_found_button = '//li[@data-id="unknown-single-not-found"]'
    post_button = '//li[@data-id="post"]'
    put_button = '//li[@data-id="put"]'
    patch_button = '//li[@data-id="patch"]'
    delete_button = '//li[@data-id="delete"]'
    register_successful_button = '//li[@data-id="register-successful"]'
    register_unsuccessful_button = '//li[@data-id="register-unsuccessful"]'
    login_successful_button = '//li[@data-id="login-successful"]'
    login_unsuccessful_button = '//li[@data-id="login-unsuccessful"]'
    delay_button = '//li[@data-id="delay"]'


    """
    END Method buttons
    """

    console_section = '//section[@id="console"]'
    url_span = '//span[@data-key="url"]'
    output_response = '//pre[@data-key="output-response"]'
    response_code = '//span[@data-key="response-code"]'