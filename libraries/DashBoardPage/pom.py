from libraries.BasePage import BasePage
from libraries.DashBoardPage import web_elements


class DashBoardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard_web_elements = web_elements

    def get_dashboard_page_title(self):
        return self.get_page_title()
