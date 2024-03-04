from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class IFrame():
    def iframe(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame("iframeResult")
        driver.switch_to.frame(0)
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[@id='navbtn_services']").click()
        time.sleep(2)

diframe = IFrame()
diframe.iframe()
