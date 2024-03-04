from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemofindElementByTN():
    def locate_by(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.TAG_NAME, "input").send_keys("Test@gmail.com")

        time.sleep(2)


findbyid = DemofindElementByTN()
findbyid.locate_by()