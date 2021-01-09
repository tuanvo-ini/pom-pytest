from selenium.webdriver.common.by import By

add_button = (By.XPATH, '//button[@type="submit"]')

# Elements in Add page
name = (By.XPATH, '//input[@name="hotelname"]')
description = (By.XPATH, '//body')
# description = (By.XPATH, '//iframe[@title="Rich Text Editor, hoteldesc"]')
map_address = (By.XPATH, '//input[@id="mapaddress"]')
latitude = (By.XPATH, '//input[@id="latitude"]')
longitude = (By.XPATH, '//input[@id="longitude"]')
submit_button = (By.XPATH, '//button[@id="add"]')
status = (By.XPATH, '//select[@name="hotelstatus"]')
stars = (By.XPATH, '//select[@name="hotelstars"]')
hotel_type = (By.XPATH, '//select[@name="hoteltype"]')
featured_enable = (By.XPATH, '//select[@name="isfeatured"]')
featured_from = (By.XPATH, '//input[@placeholder="From"]')
featured_to = (By.XPATH, '//input[@placeholder="To"]')
location = (By.XPATH, '//div[@id="s2id_searching"]')
location_enter = (By.XPATH, '//div[@id="select2-drop"]//input')
location_arrow = (By.XPATH, '//span[@class="select2-arrow"]')
location_match_result = (By.XPATH, '//div[@class="select2-result-label"]')
deposit_type = (By.XPATH, '//select[@name="deposittype"]')
deposit_value = (By.XPATH, '//input[@name="depositvalue"]')
vat_tax_type = (By.XPATH, '//select[@name="taxtype"]')
vat_tax_value = (By.XPATH, '//input[@name="taxvalue"]')

new_hotel = '//a[contains(., "{}")]'
