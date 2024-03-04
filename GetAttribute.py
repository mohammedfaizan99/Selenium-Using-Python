from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemoGetAttribute():
    def locate_by(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        attr_value = driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("type")
        print(attr_value)

attrobj = DemoGetAttribute()
attrobj.locate_by()