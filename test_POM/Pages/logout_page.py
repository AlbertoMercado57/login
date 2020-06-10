import pytest


@pytest.mark.usefixtures("setup")
class Logout:

    def __init__(self, driver):
        self.driver = driver

        self.logout_xpath = "//i[@class='icon-2x icon-signout']"

    def test_logout(self):
        return self.driver.find_element_by_xpath(self.logout_xpath).click()
