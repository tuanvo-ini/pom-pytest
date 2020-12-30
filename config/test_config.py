from utilities import utils


class TestConfig:
    CHROME_EXECUTABLE_PATH = utils.get_webdriver_path()
    LOGIN_PAGE_URL = "https://www.phptravels.net/admin"