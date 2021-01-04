from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_title_visible(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return bool(self.driver.title)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_page_title(self):
        return self.driver.title

    def get_attribute_by_value(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute("value")

    def switch_to_iframe_text_box(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(by_locator))

    def back_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def do_select_by_visible_text(self, by_locator, option):
        status = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        status.select_by_visible_text(option)

    def do_select_by_value(self, by_locator, value):
        status = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        status.select_by_value(value)

    def do_send_key_enter(self):
        self.driver.send_keys(Keys.ENTER)
