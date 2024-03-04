from selenium import webdriver
import time
class DemofindElementByID():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.html")
        driver.find_element('name','login-input').send_keys('test@test.com')
        time.sleep(2)


findbyid = DemofindElementByID()
findbyid.locate_by_id()