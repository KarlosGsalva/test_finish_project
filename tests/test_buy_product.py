from selenium import webdriver
import pytest
from pages.filter_function_page import Filter_function
from pages.login_page import Login_page
from pages.product_page import Product_page
from pages.put_products_in_cart import Put_products_in_cart
from pages.put_products_in_cart_2 import Put_products_in_cart_2
import time


@pytest.mark.run(order=2)
def test_buy_product(set_up):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Karlen\\PycharmProjects\\QA_project\\chromedriver.exe")

    print("start test 1")

    """authorization"""
    login = Login_page(driver)
    login.authorization()

    """come in to laptop catalog"""
    get_catalog = Product_page(driver)
    get_catalog.come_in_to_shop()

    """use filters"""
    use_filters = Filter_function(driver)
    use_filters.use_filters_of_laptops()

    """chose products"""
    chose_product = Put_products_in_cart(driver)
    chose_product.put_product_in_cart()

    print("finish test 1")
    time.sleep(3)
    driver.quit()


@pytest.mark.run(order=1)
def test_buy_product_2(set_group):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Karlen\\PycharmProjects\\QA_project\\chromedriver.exe")

    print("start test 2")

    """authorization"""
    login = Login_page(driver)
    login.authorization()

    """come in to laptop catalog"""
    get_catalog = Product_page(driver)
    get_catalog.come_in_to_shop()

    """chose products"""
    choose_product = Put_products_in_cart_2(driver)
    choose_product.put_product_in_cart_2()

    print("finish test 2")
    time.sleep(3)
    driver.quit()
