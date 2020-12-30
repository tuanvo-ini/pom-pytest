import os
import json
import platform
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


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


def parse_test_data(file_name):
    # Input data
    data_path = os.path.join(get_project_root(), "test_data")
    data_path = os.path.join(data_path, file_name)
    data_file = open(data_path, "r")
    test_data = json.load(data_file)
    data_file.close()
    return test_data


if __name__ == "__main__":
    tmp = "Hello"
    tmp = get_webdriver_path("chrome")
    print(tmp)