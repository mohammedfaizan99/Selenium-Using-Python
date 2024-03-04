from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
class ImplicitWait():
    def implicit_wait(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.XPATH,"//input[@id='usernae']").send_keys("Faizan")

execimplicitwait = ImplicitWait()
execimplicitwait.implicit_wait()