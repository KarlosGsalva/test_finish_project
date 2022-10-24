import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Put_products_in_cart_2(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators

    PRESTIGIO_SmartBook_141_C7 = "//*[@id='product-184327']/div[2]/div[1]"
    LENOVO_V15_IGL = "//*[@id='product-165787']/div[2]/div[1]"

    laptop_1_name = PRESTIGIO_SmartBook_141_C7
    laptop_1_buy = "//a[@class='btn-add-to-cart']"

    laptop_2_name = LENOVO_V15_IGL
    laptop_2_buy = "//*[@id='product-165787']/div[1]/div[3]/div[2]/a"

    continue_to_buy = "//*[@id='modalAddToCartProduct']/div/div/div[2]/div[2]/div/div[2]/a[1]"
    desktop_cart = "//div[@id='cart_block']"
    execute_order = "//*[@id='cart_content_ajax']/div[3]/a"

    delete_cart_button = "//*[@id='cart_content_ajax']/div[1]/table/tbody/tr/td[5]/a"

    # getters

    def get_laptop_1_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_1_name)))

    def get_laptop_1_buy(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_1_buy)))

    def get_laptop_2_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_2_name)))

    def get_laptop_2_buy(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.laptop_2_buy)))

    def get_continue_to_buy(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_to_buy)))

    def get_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.desktop_cart)))

    def get_delete_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.delete_cart_button)))

    def get_execute_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.execute_order)))

    # actions

    """delete first position in cart"""
    def delete_1_position_in_cart(self):
        self.get_delete_cart_button().click()
        print("position 1 in cart deleted")
        time.sleep(1)

    """put used laptop in the cart"""
    def put_laptop_1_in_cart(self):
        ActionChains(self.driver).move_to_element(self.get_laptop_1_name()).perform()
        self.get_laptop_1_buy().click()
        print("select laptop_1 and throw to cart")
        time.sleep(1)

    """put used second laptop in the cart"""
    def put_laptop_2_in_cart(self):
        ActionChains(self.driver).move_to_element(self.get_laptop_2_name()).perform()
        self.get_laptop_2_buy().click()
        print("select laptop_2 and throw to cart")
        time.sleep(1)

    """push button continue to buy in opened window after add product"""
    def go_continue_to_buy(self):
        self.get_continue_to_buy().click()
        print("buy something else")
        time.sleep(1)

    """come in to the cart"""
    def go_to_cart(self):
        self.get_to_cart().click()
        print("go to cart")
        time.sleep(5)

    """come in to the execute stage"""
    def go_to_execute_order(self):
        self.get_execute_order().click()
        print("come in payment stage")
        time.sleep(5)

    # methods

    def put_product_in_cart_2(self):
        """put laptop 1 to the cart"""
        self.put_laptop_1_in_cart()
        """push continue button"""
        self.go_continue_to_buy()
        """get screenshot"""
        self.get_screenshot()
        """put laptop 2 to the cart"""
        self.put_laptop_2_in_cart()
        """push continue button"""
        self.go_continue_to_buy()
        """get screenshot"""
        self.get_screenshot()
        """come in to the cart"""
        self.go_to_cart()
        """get screenshot"""
        self.get_screenshot()
        """delete first position in the cart"""
        self.delete_1_position_in_cart()
        """get screenshot"""
        self.get_screenshot()
        """come in to execute stage"""
        self.go_to_execute_order()
        """get screenshot"""
        self.get_screenshot()
        """check url"""
        self.assert_url("https://vega.am/ru/checkout-ru")



