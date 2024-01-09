import pytest
from test_POM.Pages.login_page import LoginPage
from test_POM.utils import utils as utils


@pytest.mark.usefixtures("setup")
class TestErrLogin():

    def test_ErrUser(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.BAD_USER)
        login.enter_password(utils.PASSWORD)
        login.click_login()
        assert LoginPage.flash_message, ' Your username is invalid!'

    def test_ErrPass(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.BAD_PASS)
        login.click_login()
        assert LoginPage.flash_message, ' Your password is invalid!'
