from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class HiddenElement():
    def hidden_element_yatra(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH, "//span[normalize-space()=', 1']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(3)
        age_display = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(age_display)
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
        age_display1 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(age_display1)
hidden_element_wodom = HiddenElement()
hidden_element_wodom.hidden_element_yatra()