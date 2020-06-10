import pytest


@pytest.mark.usefixtures("setup")
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_id = "username"
        self.password_id = "password"
        self.login_xpath = "//button[@type='submit']"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_xpath).click()
