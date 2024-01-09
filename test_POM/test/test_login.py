import pytest
from test_POM.Pages.login_page import LoginPage
from test_POM.Pages.logout_page import Logout
from test_POM.utils import utils as utils


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
        assert LoginPage.flash_message, 'You logged into a secure area!'

    def test_logout(self):
        driver = self.driver
        driver.get(utils.XURL)
        logout = Logout(driver)
        logout.test_logout()
        assert LoginPage.flash_message, ' You logged out of the secure area!'
