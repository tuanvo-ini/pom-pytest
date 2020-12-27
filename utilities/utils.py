import os
import platform
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_webdriver_path(webdriver_type="chrome"):
    """
    :param webdriver_type: chrome/firefox/safari/...
    :return: webdriver_path - the path of the webdriver
    """
    webdriver_path = str(get_project_root()) + '/resource/'
    if platform.system() == "Darwin":
        webdriver_path += 'webdriver_mac/'
    elif platform.system() == "Windowns":
        webdriver_path += webdriver_path + 'webdriver_window/'
    else:
        raise Exception("Unsupported {} OS".format(platform.system()))

    if webdriver_type == "chrome":
        web_drivers = [filename for filename in os.listdir(webdriver_path) if filename.startswith("chromedriver")]
        webdriver_path += web_drivers[0]
    elif webdriver_type == "firefox":
        pass
    else:
        raise Exception("Don't support {} webdriver".format(webdriver_type))
    return webdriver_path


if __name__ == "__main__":
    tmp = get_webdriver_path()
    print(tmp)