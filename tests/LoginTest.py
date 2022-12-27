import time
import unittest
from locators.Locators import Locators

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    s = Service(executable_path='chromedriver')
    driver = webdriver.Chrome(service=s)

    @classmethod
    # @staticmethod
    def setUpClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get(Locators.login_page_url)
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_username(Locators.username)
        login.enter_password(Locators.password)
        login.click_login()
        homepage = HomePage(driver)
        homepage.click_dropdown_menu()
        time.sleep(2)
        homepage.click_logout()
        time.sleep(3)

    @classmethod
    # @staticmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test successfully completed")
