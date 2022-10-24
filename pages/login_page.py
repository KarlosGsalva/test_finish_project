import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    url = "https://vega.am/ru"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    sign_in = "//a[@class='my-account']"
    user_name = "//input[@id='input-email']"
    password = "//input[@id='input-password']"
    login_button = "//input[@class='btn btn-primary']"

    # getters

    def get_link_sign_in(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.sign_in)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # actions

    def click_sign_in(self):
        self.get_link_sign_in().click()
        print("open login form")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user name")
        time.sleep(1)

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password")
        time.sleep(1)

    def click_login_button(self):
        self.get_login_button().click()
        print("click login button")
        time.sleep(1)

    # methods

    def authorization(self):

        Logger.add_start_step(method="authorization")
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_sign_in()
        self.input_user_name('4014837@mail.ru')
        self.input_password('9689963salva')
        self.click_login_button()
        Logger.add_end_step(url=self.driver.current_url, method="authorization")
