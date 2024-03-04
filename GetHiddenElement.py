from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class HiddenElement():
    def hide_ele(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        element_displayed = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(element_displayed)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        time.sleep(2)
        element_displayed1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        time.sleep(2)
        print(element_displayed1)



web_element = HiddenElement()
web_element.hide_ele()

