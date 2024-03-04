from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class DemofindElements():
    def locate_by(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(4)
        list_a=driver.find_elements(By.TAG_NAME, "a")
        print(len(list_a))
        for i in list_a:
            print(i.text)

        time.sleep(2)


findbyid = DemofindElements()
findbyid.locate_by()