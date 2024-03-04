from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemofindElementByXP():
    def locate_by(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.html")
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys('test@test.com')
        time.sleep(2)


findbyid = DemofindElementByXP()
findbyid.locate_by()