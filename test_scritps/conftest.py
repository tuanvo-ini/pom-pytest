import time
from datetime import datetime
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.test_config import TestConfig


# # set up webdriver fixture
# @pytest.fixture(scope='class')
# def selenium_driver(request):
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.set_window_size(1920, 1080)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#
#     yield driver
#     driver.quit()


@pytest.fixture(scope="class")
def init_driver(request):
    """
    """
    driver = webdriver.Chrome(executable_path=TestConfig.CHROME_EXECUTABLE_PATH)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    """
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['init_driver']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)


def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y_%m_%d_%H_%M")}.png'
    file_name = file_name.replace(".py", "")
    file_name = file_name.replace("/","_")
    file_name = file_name.replace("::","__")
    print("Filename: {}".format(file_name))
    driver.save_screenshot('screenshots/' + file_name)