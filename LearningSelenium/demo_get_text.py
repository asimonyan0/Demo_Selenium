import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde

class DemoFindElementByXpath():
    def locate_by_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.yatra.com/')
        text = driver.find_element(By.XPATH, "//div[normalize-space()='Phuket']").text
    
        print(text)
        time.sleep(3)
    
findbyid = DemoFindElementByXpath()
findbyid.locate_by_demo()
