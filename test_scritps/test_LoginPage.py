from test_scritps.test_base import BaseTest
from libraries.LoginPage.pom import LoginPage
from utilities import utils


class TestLoginPage(BaseTest):

    test_data = utils.parse_test_data("test_login_page")

    def test_home_page_title(self):

        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_login_page_title()
        assert title in "Administator Login", "Invalid Title"

    def test_do_login(self):
        self.login_page.do_login(self)