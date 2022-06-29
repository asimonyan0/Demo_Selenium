
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde

from selenium.webdriver.support.select import Select

# --it doesn't work well
# class DemoDropdownSingleSelect():
#     def demo_dropdown(self):
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         driver.get('https://www.sugarcrm.com/uk/request-demo/?utm_source=yandex.ru&utm_medium=organic')
#         driver.maximize_window()
#         dropdown = driver.find_element(By.NAME, "employees_c")
#         dd = Select(dropdown)
        
#         dd.select_by_index(1)
#         time.sleep(3)
#         dd.select_by_visible_text("51 - 100 employees")
#         time.sleep(3)
#         dd.select_by_value("level4")
#         time.sleep(4)
        
class DemoDropdownSingleSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        driver.maximize_window()
        dropdown = driver.find_element(By.ID, "select-demo")
        dd = Select(dropdown)
        
        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_visible_text("Monday")
        time.sleep(3)
        dd.select_by_value("Tuesday")
        time.sleep(4)
               


dddemo1 = DemoDropdownSingleSelect()  
dddemo1.demo_dropdown()