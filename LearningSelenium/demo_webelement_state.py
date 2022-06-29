
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde

class DemoElementState():
    def demo_enable_disable(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://training.openspan.com/login')
        state =  driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys('testname')
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys('testpass')
        state1 =  driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state1)
        time.sleep(3)
    
demostate = DemoElementState()
demostate.demo_enable_disable()

