import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByXpath():
    def locate_by_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.find_element_by_link_text("Yatra for Business").click()
        time.sleep(6)
findbyid = DemoFindElementByXpath()
findbyid.locate_by_demo()