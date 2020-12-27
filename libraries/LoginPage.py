from selenium.webdriver.common.by import By
from libraries.BasePage import BasePage
from web_elements.LoginWebElements import LoginWebElements


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_web_elements = LoginWebElements()

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username):
        self.do_send_keys(self.login_web_elements.get_username_text())

