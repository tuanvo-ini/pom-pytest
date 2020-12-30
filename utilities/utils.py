import os
import time
import datetime
import platform
import pytest
from selenium import webdriver
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def setup_webdriver():
    # Get url
    driver = webdriver.Chrome(get_webdriver_path())
    driver.get("https://www.phptravels.net/admin")
    driver.maximize_window()
    assert "Administator Login" in driver.title
    yield driver
    # Close webdriver
    # driver.quit()


def get_webdriver_path(webdriver_type="chrome"):
    """
    :param webdriver_type: chrome/firefox/safari/...
    :return: webdriver_path - the path of the webdriver
    """
    webdriver_path = os.path.join(get_project_root(), "resource")
    if platform.system() == "Darwin":
        webdriver_path = os.path.join(webdriver_path, "webdriver_mac")
    elif platform.system() == "Windows":
        webdriver_path = os.path.join(webdriver_path, "webdriver_window")
    else:
        raise Exception("Unsupported {} OS".format(platform.system()))

    if webdriver_type == "chrome":
        web_drivers = [filename for filename in os.listdir(webdriver_path) if filename.startswith("chromedriver")]
        webdriver_path = os.path.join(webdriver_path, web_drivers[0])
    elif webdriver_type == "firefox":
        pass
    else:
        raise Exception("Don't support {} webdriver".format(webdriver_type))
    return webdriver_path


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Set up a hook to be able to check if a test has failed
    """
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    """
    Check if a test has failed
    Call take screenshot function to save the failure screen
    :param request:
    :return:
    """
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['setup_webdriver']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)


def take_screenshot(driver, nodeid):
    """
    Make a screenshot with a name of the test, date and time
    :param driver: webdriver
    :param nodeid: name of the test - get from
    :return:
    """
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y_%m_%d_%H_%M")}.png'
    file_name = file_name.replace(".py", "")
    file_name = file_name.replace("/","_")
    file_name = file_name.replace("::","__")
    print("Filename: {}".format(file_name))
    driver.save_screenshot('screenshots/' + file_name)


if __name__ == "__main__":
    tmp = "Hello"
    tmp = get_webdriver_path("chrome")
    print(tmp)