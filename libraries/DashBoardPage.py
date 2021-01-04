from libraries.BasePage import BasePage
from web_elements import dashboard_page


class DashBoardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dashboard_web_elements = dashboard_page

    def get_dashboard_page_title(self):
        return self.get_page_title()

    def do_click_hotel_menu(self):
        self.do_click(self.dashboard_web_elements.hotels_menu)

    def do_click_hotel_hotel_submenu(self):
        self.do_click(self.dashboard_web_elements.hotels_hotels_submenu)

    def do_click_logout_button(self):
        self.do_click(self.dashboard_web_elements.logout_button)