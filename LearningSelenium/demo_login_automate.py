
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # NEW Metod for finde
from selenium.webdriver.common.keys import Keys



class DemoLogin():
    def demo_login_auto(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://yandex.ru/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@class='home-link desk-notif-card__login-new-item desk-notif-card__login-new-item_enter home-link_black_yes home-link_hover_inherit']").click()
        time.sleep(2)
        email_input = driver.find_element(By.XPATH, "//input[@id='passp-field-login']")
        email_input.clear()
        email_input.send_keys("asimonyan0")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@id='passp:sign-in']").click()
        time.sleep(2)
        password_input = driver.find_element(By.XPATH, "//input[@id='passp-field-passwd']")
        time.sleep(2)
        password_input.send_keys("12345")
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)


ddscreenshot = DemoLogin()
ddscreenshot.demo_login_auto()