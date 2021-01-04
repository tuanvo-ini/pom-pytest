import time
from test_scritps.test_base import BaseTest
from libraries.HotelPage import HotelPage
from libraries.LoginPage import LoginPage
from libraries.DashBoardPage import DashBoardPage
from utilities import utils


class TestHotelPage(BaseTest):
    test_data = utils.parse_test_data("new_hotel.json")

    def setup_method(self):
        login_page = LoginPage(self.driver)
        login_page.do_login(self.test_data["account"]["email"], self.test_data["account"]["password"])

    def teardown_method(self):
        dashboard_page = DashBoardPage(self.driver)
        dashboard_page.do_click_logout_button()

    def test_add_new_hotel(self):
        hotel_page = HotelPage(self.driver)
        dashboard_page = DashBoardPage(self.driver)

        # Go to Hotel Page
        dashboard_page.do_click_hotel_menu()
        dashboard_page.do_click_hotel_hotel_submenu()
        time.sleep(10)
        title = hotel_page.get_page_title()
        assert title in "Hotels Management", "Invalid Title"

        # Add a new hotel
        hotel_page = HotelPage(self.driver)
        hotel_page.do_click_add_button()
        hotel_page.enter_hotel_name(self.test_data["hotel"]["name"])
        hotel_page.do_select_hotel_status(self.test_data["hotel"]["status"])
        hotel_page.do_select_hotel_star(self.test_data["hotel"]["stars"])
        hotel_page.do_select_type(self.test_data["hotel"]["type"])
        hotel_page.do_config_featured(self.test_data["hotel"]["featured"]["from"],\
                                      self.test_data["hotel"]["featured"]["to"],\
                                      self.test_data["hotel"]["featured"]["is_featured"])
        hotel_page.do_config_deposit(self.test_data["hotel"]["deposit"]["type"],\
                                     self.test_data["hotel"]["deposit"]["value"])
        hotel_page.do_config_vat_tax(self.test_data["hotel"]["vat_tax"]["type"],\
                                     self.test_data["hotel"]["vat_tax"]["value"])
        hotel_page.enter_hotel_location(self.test_data["hotel"]["location"])
        hotel_page.enter_hotel_description(self.test_data["hotel"]["description"])
        hotel_page.do_submit_button()

        # Verify a new hotel is created successfully
        new_hotel = hotel_page.verify_new_hotel_is_created(self.test_data["hotel"]["name"])