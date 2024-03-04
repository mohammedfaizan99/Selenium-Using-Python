from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class JavaScript():
    def javascript_exe(self):
        driver = webdriver.Chrome()
        driver.execute_script("window.open('https://www.yatra.com/', '_self');")
        time.sleep(4)
        paraele = driver.execute_script("return document.getElementByTagName('p.low_price')[16];")
        driver.execute_script("arguments[0].click();",paraele)
        time.sleep(2)
jsexec = JavaScript()
jsexec.javascript_exe()