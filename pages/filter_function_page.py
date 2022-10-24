import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Filter_function(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    acer_checkbox = "//label[@for='mfilter-opts-attribs-43-manufacturers-206']"
    apple_checkbox = "//label[@for='mfilter-opts-attribs-43-manufacturers-190']"
    huawei_checkbox = "//label[@for='mfilter-opts-attribs-43-manufacturers-1678']"
    ram_checkbox_16GB = "//label[@for='mfilter-opts-attribs-43-88884-56e3666cd7c5d3804bfb05d9a96cc76b']"

    # getters

    def get_acer_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.acer_checkbox)))

    def get_apple_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.apple_checkbox)))

    def get_huawei_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.huawei_checkbox)))

    def get_ram_checkbox_16gb(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ram_checkbox_16GB)))

    # actions

    def use_acer_checkbox(self):
        self.get_acer_checkbox().click()
        time.sleep(1)
        print("acer filter is used")

    def use_apple_checkbox(self):
        self.get_apple_checkbox().click()
        time.sleep(1)
        print("apple filter is used")

    def use_huawei_checkbox(self):
        self.get_huawei_checkbox().click()
        time.sleep(1)
        print("huawei filter is used")

    def use_ram_checkbox_16gb(self):
        self.get_ram_checkbox_16gb().click()
        time.sleep(5)
        print("16GB RAM filter is used")

    # methods

    def use_filters_of_laptops(self):
        self.use_acer_checkbox()
        self.use_apple_checkbox()
        self.use_huawei_checkbox()
        self.use_ram_checkbox_16gb()
        self.get_screenshot()
