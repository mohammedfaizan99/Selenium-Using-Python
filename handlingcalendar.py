from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
class AutoSuggest():
    def auto_suggestcal(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        departfrom = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        departfrom.click()
        time.sleep(2)
        departfrom.send_keys("New York")
        time.sleep(2)
        departfrom.send_keys(Keys.ENTER)
        time.sleep(2)
        arriveto = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        arriveto.send_keys("New")
        time.sleep(2)
        search_result = driver.find_elements(By.XPATH, "//div[@class='ac_results dest_ac']//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        time.sleep(2)
        for results in search_result:
            if "New Delhi (DEL)" in results.text:
                time.sleep(2)
                results.click()
                break

        driver.find_element(By.CLASS_NAME, "BE_flight_origin_date").click()
        time.sleep(2)
        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "20/03/2024":
                date.click()
                time.sleep(2)
                break
        driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
suggest = AutoSuggest()
suggest.auto_suggestcal()
