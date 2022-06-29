
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde

class DemoRadio():
    def demo_radio_button(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.sugarcrm.com/au/request-demo/')
        driver.maximize_window()
        time.sleep(3)
        print(driver.find_element(By.ID, "doi0").is_selected)
        driver.find_element(By.ID, "doi0").click()
        time.sleep(7)
        print(driver.find_element(By.ID, "doi0").is_selected)
        driver.find_element(By.ID, "doi1").click()
        time.sleep(7)
        print(driver.find_element(By.ID, "doi0").is_selected)
        print(driver.find_element(By.ID, "doi1").is_selected)

radiodemo = DemoRadio()   
radiodemo.demo_radio_button()