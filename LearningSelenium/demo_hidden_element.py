
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde

class DemoHiddenElement():
    def demo_is_displayed(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)

        #Second tipe hidden elements
    def demo_is_displayed_Yatra(self):    
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH, "//label[normalize-space()='Traveller and Hotel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        elem2 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(elem2)
        #NoSuchElementException: Message: no such element: ...
        # driver.find_element(By.XPATH, "//span[@class='ddSpinnerMinus disabled']").click()
        # elem3 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        # print(elem3)

    
demoDisplayed = DemoHiddenElement()
# demoDisplayed.demo_is_displayed()
demoDisplayed.demo_is_displayed_Yatra()