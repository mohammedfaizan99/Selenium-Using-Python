from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemofindElementByClass():
    def locate_by(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys("Test@gmail.com")

        time.sleep(2)


findbyid = DemofindElementByClass()
findbyid.locate_by()