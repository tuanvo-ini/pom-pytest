from libraries.BasePage import BasePage
from libraries.LoginPage import web_elements
from config.test_config import TestConfig
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_web_elements = web_elements
        self.driver.get(TestConfig.LOGIN_PAGE_URL)

    def get_login_page_title(self):
        return self.get_title("Administator Login")

    def do_login(self, username, password):
        self.do_send_keys((By.XPATH, self.login_web_elements.email), username)
        self.do_send_keys((By.XPATH, self.login_web_elements.password), password)
        self.do_click((By.XPATH, self.login_web_elements.submit_button))

