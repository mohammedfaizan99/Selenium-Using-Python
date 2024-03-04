from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemogetText():
    def locate_by(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/hotels")
        text = driver.find_element(By.XPATH,"//p[contains(text(),'We are back in the post-pandemic world with a bouq')]").text
        print(text)


findbyid = DemogetText()
findbyid.locate_by()