from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ExplicitWait():
    def explicit_wait(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        departfrom = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        departfrom.click()
        departfrom.send_keys("New York")
        departfrom.send_keys(Keys.ENTER)
        arriveto = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        arriveto.send_keys("New")
        search_result = driver.find_elements(By.XPATH,"//div[@class='ac_results dest_ac']//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for results in search_result:
            if "New Delhi (DEL)" in results.text:
                results.click()
                break
        wait = WebDriverWait(driver, 10)
        #for fluent wait : wait = WebDriverWait(driver,10, 2,ignored_exceptions=)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")).find_element(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))
        #driver.find_element(By.CLASS_NAME, "BE_flight_origin_date").click()
        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "20/03/2024":
                date.click()
                break





execexplicitwait = ExplicitWait()
execexplicitwait.explicit_wait()