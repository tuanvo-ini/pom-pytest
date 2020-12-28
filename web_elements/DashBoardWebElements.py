from selenium.webdriver.common.by import By


class DashBoardWebElements():

    def get_account_page(self):
        account_page = (By.XPATH, '//li[@id="account"]')
        return account_page

    def get_dashboard_menu_button(self):
        dashboard_menu = (By.XPATH, '//ul[@id="social-sidebar-menu"]/li[1]')
        return dashboard_menu

    # Hotel menu
    hotels_menu = '//ul[@id="social-sidebar-menu"]//a[@href="#Hotels"]'
    hotels_hotels_submenu = '//ul[@id="Hotels"]/li[1]'
    hotels_rooms_submenu = '//ul[@id="Hotels"]//a[contains(@href, "rooms")]'
    hotels_extras_submenu = '//ul[@id="Hotels"]//a[contains(@href, "extras")]'
    hotels_reviews_submenu = '//ul[@id="Hotels"]//a[contains(@href, "reviews")]'
    hotels_settings_submenu = '//ul[@id="Hotels"]//a[contains(@href, "settings")]'
    logout_button = '//li[@id="logout"]'