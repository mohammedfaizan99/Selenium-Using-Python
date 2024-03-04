from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
class Sliders():
    def sliders(self):
        driver = webdriver.Chrome()
        driver.get("https://www.snapdeal.com/products/mobiles-featured-phones?sort=plrty")
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        from_slide = driver.find_element(By.XPATH,"//a[contains(@class, 'left-handle')]")
        to_slide = driver.find_element(By.XPATH,"//a[contains(@class, 'right-handle')]")
        #ActionChains(driver).drag_and_drop_by_offset(from_slide, 40, 0).perform()
        #ActionChains(driver).drag_and_drop_by_offset(to_slide, 60, 0).perform()
        time.sleep(2)
        ActionChains(driver).click_and_hold(from_slide).pause(2).drag_and_drop_by_offset(from_slide,60,0).release().perform()
        time.sleep(2)
        ActionChains(driver).drag_and_drop_by_offset(to_slide,-40, 0).perform()
        time.sleep(2)
execsliders = Sliders()
execsliders.sliders()