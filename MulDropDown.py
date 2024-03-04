from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class MulDropdown():
    def muldropdown(self):
        driver = webdriver.Chrome()
        driver.get("https://html.com/attributes/select-multiple/")
        time.sleep(2)
        multdro = driver.find_element(By.XPATH,"//div[@class='render']//select")
        time.sleep(2)
        md = Select(multdro)
        md.select_by_index(1)
        time.sleep(2)
        md.select_by_value("Andean")
        md.select_by_visible_text("Chilean flamingo")
        md.select_by_index(4)
        md.select_by_value("James's")
        time.sleep(2)
        md.select_by_visible_text("Lesser flamingo")
        time.sleep(2)
        md.deselect_all()
        time.sleep(2)



multidropdown = MulDropdown()
multidropdown.muldropdown()