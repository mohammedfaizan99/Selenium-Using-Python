from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class JSPopUp():
    def popup(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame("iframeResult")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("Faizan")
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(2)
        driver.quit()


execJSPopup = JSPopUp()
execJSPopup.popup()