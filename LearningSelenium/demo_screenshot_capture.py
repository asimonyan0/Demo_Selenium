
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde




class DemoScreenshot():
    def demo_screen_capture(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        
        continuedemo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continuedemo.screenshot("./test.png")
        continuedemo.click()
        time.sleep(2)
        driver.get_screenshot_as_file("/home/armen/Рабочий стол/error.png")
        time.sleep(2)
        driver.save_screenshot("./test1.png")
        time.sleep(2)

ddscreenshot = DemoScreenshot()
ddscreenshot.demo_screen_capture()