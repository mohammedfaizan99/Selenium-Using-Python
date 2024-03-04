from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Screenshot():
    def capture_screenshot(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        btn = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        btn.screenshot(".\\loginbtn.png")
        btn.click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\Users\\Mohammed Faizan\\Desktop\\ssbtn.png")
        driver.save_screenshot(".\\ssbtn1.png")

getscreenshot = Screenshot()
getscreenshot.capture_screenshot()