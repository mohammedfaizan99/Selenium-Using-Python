from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemofindElementByLT():
    def locate_by(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.PARTIAL_LINK_TEXT, "Yatra for").click()

        time.sleep(2)


findbyid = DemofindElementByLT()
findbyid.locate_by()