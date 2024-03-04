from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemofindElementByID():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.html")
        driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys('test@test.com')
        time.sleep(2)


findbyid = DemofindElementByID()
findbyid.locate_by_id()