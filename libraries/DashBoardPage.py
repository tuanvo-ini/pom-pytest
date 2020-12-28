from libraries.BasePage import BasePage
from web_elements import DashBoardWebElements


class DashBoardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard_web_elements = DashBoardWebElements()