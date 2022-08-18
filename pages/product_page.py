from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import ProductPageLocators
from base_page import BasePage


class TestProductPage(BasePage):

    def guest_can_see_add_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        assert self.is_element_present(
            *ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def guest_can_see_goods_value_in_header(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.is_element_present(*ProductPageLocators.GOODS_VALUE_IN_HEADER)
        assert self.is_element_present(
            *ProductPageLocators.GOODS_VALUE_IN_HEADER), "Goods value in header is not presented"

    def guest_can_add_goods_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.browser.implicitly_wait(4)
        self.browser.find_element(*ProductPageLocators.BASKET).click()
        value = self.browser.find_element(*ProductPageLocators.GODS_VALUE_IN_BASKET).text
        assert value

    def guest_can_see_order_price(self):
        assert self.is_element_present(*ProductPageLocators.ORDER_PRICE), 'Order price is not presented'

    def order_price_equal_basket_price(self):
        order_price = self.browser.find_element(*ProductPageLocators.ORDER_PRICE).text
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.browser.implicitly_wait(4)
        self.browser.find_element(*ProductPageLocators.BASKET).click()
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.m2c button > span svg"))).click()
        self.browser.implicitly_wait(3)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert order_price == basket_price, f'{order_price} not equal {basket_price}'