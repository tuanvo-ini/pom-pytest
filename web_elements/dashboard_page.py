from selenium.webdriver.common.by import By

account_page = (By.XPATH, '//li[@id="account"]')
dashboard_menu = (By.XPATH, '//ul[@id="social-sidebar-menu"]/li[1]')
# Hotel menu
hotels_menu = (By.XPATH, '//ul[@id="social-sidebar-menu"]//a[@href="#Hotels"]')
hotels_hotels_submenu = (By.XPATH, '//ul[@id="Hotels"]/li[1]')
hotels_rooms_submenu = (By.XPATH, '//ul[@id="Hotels"]//a[contains(@href, "rooms")]')
hotels_extras_submenu = (By.XPATH, '//ul[@id="Hotels"]//a[contains(@href, "extras")]')
hotels_reviews_submenu = (By.XPATH, '//ul[@id="Hotels"]//a[contains(@href, "reviews")]')
hotels_settings_submenu = (By.XPATH, '//ul[@id="Hotels"]//a[contains(@href, "settings")]')
logout_button = (By.XPATH, '//li[@id="logout"]')