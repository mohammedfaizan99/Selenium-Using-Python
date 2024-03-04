from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Dropdown():
    def dropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
        drp1 = driver.find_element(By.NAME,"UserTitle")
        dd = Select(drp1)
        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_visible_text("IT Manager")
        time.sleep(3)
        dd.select_by_value("CxO_General_Manager_ANZ")
        time.sleep(3)


dropdownlist = Dropdown()
dropdownlist.dropdown()