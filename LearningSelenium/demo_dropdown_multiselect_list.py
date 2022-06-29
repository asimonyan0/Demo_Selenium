
from select import select
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde

from selenium.webdriver.support.select import Select

class DemoDropdownMultileSelect():
    def demo_dropdown(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        dd_demo = driver.find_element(By.ID, "multi-select")
        dd_multi = Select(dd_demo)
        
        dd_multi.select_by_index(0)
        dd_multi.select_by_value("New Jersey")
        dd_multi.select_by_visible_text("Florida")
        dd_multi.select_by_index(3)
        dd_multi.select_by_value("Ohio")
        dd_multi.select_by_visible_text("Texas")
        time.sleep(4)
        dd_multi.deselect_by_index(0)                  #--DEACTIVATION 
        dd_multi.deselect_by_value("New Jersey")
        dd_multi.deselect_by_visible_text("Florida")
        time.sleep(4)
        dd_multi.deselect_all()
        time.sleep(5)


demo_multiselect = DemoDropdownMultileSelect()  
demo_multiselect.demo_dropdown()