from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
class MouseOver():
    def mouse_over(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        more = driver.find_element(By.XPATH,"//span[@class='more-arr']")
        myacc = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
        action = ActionChains(driver)
        action.move_to_element(myacc).perform()
        time.sleep(2)
        action.move_to_element(more).perform()
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
        time.sleep(2)

execmouse_over = MouseOver()
execmouse_over.mouse_over()