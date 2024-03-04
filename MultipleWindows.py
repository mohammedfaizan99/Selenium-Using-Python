from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class MultipleWindows():
    def multiple_windows(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        parenthandle = driver.current_window_handle
        print(parenthandle)
        driver.find_element(By.XPATH,"//img[@alt='Flat 12% OFF (up to Rs 1,500)']").click()
        allhandles = driver.window_handles
        print(allhandles)
        for handles in allhandles:
            if handles != parenthandle:
                driver.switch_to.window(handles)
                time.sleep(2)
                driver.find_element(By.XPATH,"//a[@id='twtr_yttkd']").click()
                time.sleep(2)
                driver.close()
                time.sleep(2)
                break
execmulti = MultipleWindows()
execmulti.multiple_windows()