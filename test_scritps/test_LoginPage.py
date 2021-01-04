from test_scritps.test_base import BaseTest
from libraries.LoginPage import LoginPage
from utilities import utils


class TestLoginPage(BaseTest):
    test_data = utils.parse_test_data("account.json")

    def test_home_page_title(self):
        login_page = LoginPage(self.driver)
        title = login_page.get_page_title()
        assert title in "Administator Login", "Invalid Title"

    def test_do_login(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(self.test_data["account"]["email"], self.test_data["account"]["password"])
        dashboard_title = login_page.get_page_title()
        assert dashboard_title in "Dashboard", "Invalid Dashboard Page title"
