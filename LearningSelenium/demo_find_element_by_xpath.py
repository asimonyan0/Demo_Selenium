import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByXpath():
    def locate_by_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://yandex.ru/")
        driver.find_element_by_xpath("//a[@class='home-link desk-notif-card__login-new-item desk-notif-card__login-new-item_mail home-link_black_yes']//div[2]").click()
        time.sleep(7)
findbyid = DemoFindElementByXpath()
findbyid.locate_by_demo()
