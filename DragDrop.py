from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
class DragDrop():
    def drag_drop(self):
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(2)
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        fromdrag = driver.find_element(By.ID,"draggable")
        todrop = driver.find_element(By.ID,"droppable")
        ActionChains(driver).drag_and_drop(fromdrag,todrop).perform()
        time.sleep(2)
execdragdrop = DragDrop()
execdragdrop.drag_drop()