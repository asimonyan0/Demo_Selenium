import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select

class DemoAutosuggest():
    def demo_autosuggest_dropdown(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")

        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        driver.maximize_window()
        depart_from.click()
        time.sleep(3)
        depart_from.send_keys("New Delhi")
        time.sleep(3)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(3)
        going_to.send_keys("New")
        time.sleep(2)
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))

        for results in search_results:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(3)
                break

        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//td[@id='30/06/2022']").click()
        time.sleep(6)

        # all_dates = driver.find_element(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        # for date in all_dates:
        #     if date.get_attribute("data-date") == "30/06/2022":
        #         date.click()
        #         time.sleep(6)
        #         break

dauto = DemoAutosuggest()
dauto.demo_autosuggest_dropdown()