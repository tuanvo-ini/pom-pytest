from test_scritps.test_base import BaseTest
from libraries.LoginPage.pom import LoginPage


class TestLoginPage(BaseTest):

    def test_home_page_title(self):

        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_login_page_title()
        assert title in "Administator Login", "Invalid Title"