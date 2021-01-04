from libraries.BasePage import BasePage
from web_elements import account_page


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.account_web_elements = account_page

    def get_account_page_title(self):
        return self.get_page_title()

    def get_account_type_field(self):
        return self.get_attribute_by_value(self.account_web_elements.account_type)

    def get_first_name_field(self):
        return self.get_attribute_by_value(self.account_web_elements.first_name)

    def get_last_name_field(self):
        return self.get_attribute_by_value(self.account_web_elements.last_name)

    def get_email_field(self):
        return self.get_attribute_by_value(self.account_web_elements.email)

    def get_mobile_number_field(self):
        return self.get_attribute_by_value(self.account_web_elements.mobile_number)

    def get_country_field(self):
        return self.get_element_text(self.account_web_elements.country)

