
from pytest import xfail
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver
    print("Test Start")
    yield
    driver.close()
    driver.quit()
    print("Test Complete")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s"> alt="screenshot" style="width:304px;height:228px;" onclick="window.open(' \
                       'this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extra.html(html))
        report.extra = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
