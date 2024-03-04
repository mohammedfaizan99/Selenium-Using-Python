from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class ElementState():
    def Sign_in(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("anonymous")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("123abcd@")
        time.sleep(3)
        demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state)


demostate = ElementState()
demostate.Sign_in()

