import time
from libraries.BasePage import BasePage
from web_elements import hotel_page
from selenium.webdriver.common.keys import Keys


class HotelPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.hotel_web_elements = hotel_page

    def do_click_add_button(self):
        self.do_click(self.hotel_web_elements.add_button)

    def enter_hotel_name(self, hotel_name):
        self.do_send_keys(self.hotel_web_elements.name, hotel_name)

    def enter_hotel_description(self, desc):
        self.driver.switch_to.frame(0)
        self.do_send_keys(self.hotel_web_elements.description, desc)
        self.back_to_parent_frame()

    def do_select_hotel_status(self, option):
        self.do_select_by_visible_text(self.hotel_web_elements.status, option)

    def do_config_featured(self, featured_from, featured_to, is_enable="Yes"):
        if is_enable == "Yes":
            self.do_select_by_visible_text(self.hotel_web_elements.featured_enable, is_enable)
            self.do_send_keys(self.hotel_web_elements.featured_from, featured_from)
            self.do_click(self.hotel_web_elements.featured_from)
            self.do_send_keys(self.hotel_web_elements.featured_to, featured_to)
            self.do_click(self.hotel_web_elements.featured_to)
        else:
            self.do_select_by_visible_text(self.hotel_web_elements.featured_enable, is_enable)

    def do_select_type(self, hotel_type):
        self.do_select_by_visible_text(self.hotel_web_elements.hotel_type, hotel_type)

    def do_config_deposit(self, deposit_type, deposit_value):
        self.do_select_by_visible_text(self.hotel_web_elements.deposit_type, deposit_type)
        self.do_send_keys(self.hotel_web_elements.deposit_value, deposit_value)

    def do_config_vat_tax(self, vat_type, vat_value):
        self.do_select_by_visible_text(self.hotel_web_elements.vat_tax_type, vat_type)
        self.do_send_keys(self.hotel_web_elements.vat_tax_value, vat_value)

    def do_select_hotel_star(self, stars):
        self.do_select_by_value(self.hotel_web_elements.stars, stars)

    def enter_hotel_location(self, location):
        self.do_click(self.hotel_web_elements.location)
        self.do_click(self.hotel_web_elements.location_enter)
        self.do_send_keys(self.hotel_web_elements.location_enter, location)
        time.sleep(5)
        self.do_send_keys(self.hotel_web_elements.location_enter, Keys.ENTER)

    def do_submit_button(self):
        self.do_click(self.hotel_web_elements.submit_button)

    def verify_new_hotel_is_created(self, hotel_name):
        return self.is_visible(self.hotel_web_elements.new_hotel.format(hotel_name))