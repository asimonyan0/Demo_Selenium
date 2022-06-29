
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde

class DemoCheckboxes():
    def demo_checkbox(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.sugarcrm.com/au/request-demo/')
        driver.maximize_window()
        time.sleep(6)
        driver.find_element(By.ID, "interest_market_c0").click()
        var1 =driver.find_element(By.ID, "interest_market_c0").is_selected()
        print(var1)
        var2 =driver.find_element(By.ID, "interest_sell_c0").is_selected()
        print(var2)
        time.sleep(4)

checkbox = DemoCheckboxes()
checkbox.demo_checkbox()
       