from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemoBrowserMethods():
    def locate_by(self):
        driver = webdriver.Chrome()
        driver.get("https://www.dsce.edu.in/")
        print(driver.current_url)
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.XPATH, "//span[@class='menu-title'][normalize-space()='Admissions']").click()
        driver.back()
        time.sleep(5)
        driver.forward()
        time.sleep(5)
        driver.minimize_window()
        time.sleep(2)
        driver.quit()


findbyid = DemoBrowserMethods()
findbyid.locate_by()