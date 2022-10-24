import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    technic_and_electronic = "//a[@class='clearfix']"
    computers_and_laptops = "//a[@href='ru/kompyutery-i-noutbuki']"
    laptops = "//a[@href='ru/noutbuki']"

    # getters

    def get_technic_and_electronic(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.technic_and_electronic)))

    def get_computers_and_laptops(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.computers_and_laptops)))

    def get_laptops(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptops)))

    # actions

    def move_to_technic_and_electronic(self):
        ActionChains(self.driver).move_to_element(self.get_technic_and_electronic()).perform()
        time.sleep(1)
        print("open technic and electronic")

    def move_to_computers_and_laptops(self):
        ActionChains(self.driver).move_to_element(self.get_computers_and_laptops()).perform()
        time.sleep(1)
        print("open computers and laptops")

    def select_laptops(self):
        self.get_laptops().click()
        time.sleep(1)
        print("enter to laptops category")

    # methods

    def come_in_to_shop(self):
        self.move_to_technic_and_electronic()
        self.get_screenshot()
        self.move_to_computers_and_laptops()
        self.get_screenshot()
        self.select_laptops()
        self.get_screenshot()
        self.assert_url("https://vega.am/ru/noutbuki")

