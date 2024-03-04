from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class RadioButton():
    def radio_handling(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        time.sleep(2)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//form[contains(text(),'Your current web browser is:')]//input[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//form[contains(text(),'Your current web browser is:')]//input[1]").click()
        time.sleep(3)
        check = driver.find_element(By.XPATH, "//form[contains(text(),'Your current web browser is:')]//input[2]").is_selected()
        print(check)
        time.sleep(2)
radiorun = RadioButton()
radiorun.radio_handling()