from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
class DoubleCLick():
    def double_click(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        action = ActionChains(driver)
        rightclick = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        copyele = driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")
        time.sleep(2)
        action.context_click(rightclick).perform()
        time.sleep(2)
        copyele.click()
        time.sleep(2)
        Alert(driver).accept()

        actionchains = ActionChains(driver)
        doubleclick = driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")

        time.sleep(2)
        actionchains.double_click(doubleclick).perform()
        time.sleep(2)
        Alert(driver).accept()
        time.sleep(2)

execdoubleclick = DoubleCLick()
execdoubleclick.double_click()