import pytest

from test_POM.Pages.login_page import LoginPage
from test_POM.utils import utils


@pytest.mark.usefixtures("setup")
class BaseClass:

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
