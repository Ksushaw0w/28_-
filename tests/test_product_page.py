import pytest
from ..pages.product_page import TestProductPage

link = "https://https://www.ozon.ru/product/podguzniki-trusiki-yokosun-l-9-14-kg-44-sht-149724901/?sh=OYQz-uRAdQ"


@pytest.mark.product
def test_can_see_order_price(browser):
    page = TestProductPage(browser, link)
    page.open()
    page.guest_can_see_order_price()
    page.order_price_equal_basket_price()


def test_can_see_add_button(browser):
    page = TestProductPage(browser, link)
    page.open()
    page.guest_can_see_add_button()


def test_can_see_goods_value_in_header(browser):
    page = TestProductPage(browser, link)
    page.open()
    page.guest_can_see_goods_value_in_header()


def test_can_add_goods_to_basket(browser):
    page = TestProductPage(browser, link)
    page.open()
    page.guest_can_add_goods_to_basket()