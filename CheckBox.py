from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class CheckBox():
    def Check_boxes(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        time.sleep(2)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@value='red']").click()

        time.sleep(4)
        driver.find_element(By.XPATH, "// input[ @ value = 'yellow']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@value='red']").click()
        time.sleep(4)
        var1 = driver.find_element(By.XPATH,"//input[@value='red']").is_selected()
        print(var1)
        time.sleep(3)
checkbox = CheckBox()
checkbox.Check_boxes()