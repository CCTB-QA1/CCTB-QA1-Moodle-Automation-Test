from selenium.webdriver.common.by import By
from locators.Locators import Locators


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.drop_down_menu = Locators.drop_down_menu
        self.logout_link_text = Locators.logout_link_text

    def click_dropdown_menu(self):
        self.driver.find_element(By.XPATH, self.drop_down_menu).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_text).click()
