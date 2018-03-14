import pytest
from selenium import webdriver
import helpers.helpers as utils


# Screenshot in case of any test failure
def pytest_exception_interact(node, report):
    if node and report.failed:
        class_name = node._nodeid.replace(".py::", "_class_")
        name = "{0}_{1}".format(class_name, url)
        utils.save_screenshot(node.funcargs.get("driver"), name)


# Create driver and url command line addoption
def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
    parser.addoption("--url", action="store", default="http://blazedemo.com", help="url")


# Create driver fixture that initiates chrome
@pytest.fixture(scope="module", autouse=True)
def driver(request):
    browser = request.config.getoption("--driver")
    if browser == 'chrome':
        browser = webdriver.Chrome()
        browser.get("about:blank")
        browser.implicitly_wait(10)
        return browser
    else:
        print 'only chrome is supported at the moment'


# Create url fixture
@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")
