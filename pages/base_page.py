import time

from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageHeaderLocators, BasePageBodyLocators, BasePageFooterLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def scroll(self, timeout):
        scroll_pause_time = timeout

        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If heights are the same it will exit the function
                break
            last_height = new_height

    def guest_can_change_currency(self):
        self.browser.find_element(*BasePageHeaderLocators.CHANGE_CURRENCY)
        assert self.is_element_present(*BasePageHeaderLocators.CHANGE_CURRENCY), "Icon with currency is not presented"

    def guest_can_change_area(self):
        self.browser.find_element(*BasePageHeaderLocators.CHANGE_CURRENCY)
        assert self.is_element_present(*BasePageHeaderLocators.CHANGE_AREA), "Icon with area is not presented"

    def guest_can_change_delivery_address(self):
        self.browser.find_element(*BasePageHeaderLocators.CHANGE_DELIVERY_ADDRESS)
        assert self.is_element_present(
            *BasePageHeaderLocators.CHANGE_DELIVERY_ADDRESS), "Icon with delivery address is not presented"

    def guest_can_go_to_mobile_app_link(self):
        self.browser.find_element(*BasePageHeaderLocators.MOBILE_APP_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.MOBILE_APP_LINK), "Mobile app link is not presented"

    def guest_can_go_to_seller_ozon_link(self):
        self.browser.find_element(*BasePageHeaderLocators.SELLER_OZON_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.SELLER_OZON_LINK), "Seller referral link is not presented"

    def guest_can_go_to_referral_program_link(self):
        self.browser.find_element(*BasePageHeaderLocators.REFERRAL_PROGRAM_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.REFERRAL_PROGRAM_LINK), "Referral link is not presented"

    def guest_can_go_to_certificates_link(self):
        self.browser.find_element(*BasePageHeaderLocators.CERTIFICATES_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.CERTIFICATES_LINK), "Certificates link is not presented"

    def guest_can_go_to_help_link(self):
        self.browser.find_element(*BasePageHeaderLocators.HELP_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.CERTIFICATES_LINK), "Help link is not presented"

    def guest_can_go_to_points_of_issue_link(self):
        self.browser.find_element(*BasePageHeaderLocators.POINTS_OF_ISSUE_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.CERTIFICATES_LINK), "Points of issue link is not presented"

    def guest_can_go_to_ozon_icon(self):
        self.browser.find_element(*BasePageHeaderLocators.OZON_ICON)
        assert self.is_element_present(
            *BasePageHeaderLocators.OZON_ICON), "Ozon icon is not presented"

    def guest_can_click_on_the_catalogue_button(self):
        self.browser.find_element(*BasePageHeaderLocators.CATALOGUE_BUTTON).click()
        assert self.is_element_present(
            *BasePageHeaderLocators.CATALOGUE_BUTTON), "Catalogue button is not presented"

    def guest_can_go_to_everywhere_dropdown(self):
        self.browser.find_element(*BasePageHeaderLocators.EVERYWHERE_DROPDOWN)
        assert self.is_element_present(
            *BasePageHeaderLocators.EVERYWHERE_DROPDOWN), "Everywhere dropdown is not presented"

    def guest_can_insert_a_phrase_in_the_input_area(self):
        self.browser.find_element(*BasePageHeaderLocators.INPUT_AREA).send_keys('justSOMEphrase')
        assert self.is_element_present(
            *BasePageHeaderLocators.INPUT_AREA), "Input does not work"

    def guest_can_use_the_search_button(self):
        self.browser.find_element(*BasePageHeaderLocators.INPUT_AREA).send_keys('justSOMEphrase')
        assert self.is_element_present(
            *BasePageHeaderLocators.SEARCH_BUTTON), "Search button does not work"

    def guest_can_go_to_login_icon(self):
        self.browser.find_element(*BasePageHeaderLocators.LOGIN_ICON)
        assert self.is_element_present(
            *BasePageHeaderLocators.LOGIN_ICON), "Login icon is not presented"

    def guest_can_go_to_orders_icon(self):
        self.browser.find_element(*BasePageHeaderLocators.ORDERS_ICON)
        assert self.is_element_present(
            *BasePageHeaderLocators.ORDERS_ICON), "Orders icon is not presented"

    def guest_can_go_to_favorites_icon(self):
        self.browser.find_element(*BasePageHeaderLocators.FAVORITES_ICON)
        assert self.is_element_present(
            *BasePageHeaderLocators.FAVORITES_ICON), "Favorites icon is not presented"

    def guest_can_go_to_basket_icon(self):
        self.browser.find_element(*BasePageHeaderLocators.BASKET_ICON)
        assert self.is_element_present(
            *BasePageHeaderLocators.BASKET_ICON), "Basket icon is not presented"

    def guest_can_go_to_top_fashion_link(self):
        self.browser.find_element(*BasePageHeaderLocators.TOP_FASHION_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.TOP_FASHION_LINK), "Top fashion link is not presented"

    def guest_can_go_to_actions_link(self):
        self.browser.find_element(*BasePageHeaderLocators.ACTIONS_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.ACTIONS_LINK), "Actions link is not presented"

    def guest_can_go_to_brands_link(self):
        self.browser.find_element(*BasePageHeaderLocators.BRANDS_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.BRANDS_LINK), "Brands link is not presented"

    def guest_can_go_to_electronic_link(self):
        self.browser.find_element(*BasePageHeaderLocators.ELECTRONIC_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.ELECTRONIC_LINK), "Electronic link is not presented"

    def guest_can_go_to_technic_link(self):
        self.browser.find_element(*BasePageHeaderLocators.TECHNIC_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.TECHNIC_LINK), "Technic link is not presented"

    def guest_can_go_to_clothes_and_shoes_link(self):
        self.browser.find_element(*BasePageHeaderLocators.CLOTHES_AND_SHOES_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.CLOTHES_AND_SHOES_LINK), "Clothes and shoes link is not presented"

    def guest_can_go_to_beauty_and_health_link(self):
        self.browser.find_element(*BasePageHeaderLocators.BEAUTY_AND_HEALTH_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.BEAUTY_AND_HEALTH_LINK), "Beauty and health link is not presented"

    def guest_can_go_to_sport_and_relax_link(self):
        self.browser.find_element(*BasePageHeaderLocators.SPORT_AND_RELAX_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.SPORT_AND_RELAX_LINK), "Sport and relax link is not presented"

    def guest_can_go_to_house_and_garden_link(self):
        self.browser.find_element(*BasePageHeaderLocators.HOUSE_AND_GARDEN_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.HOUSE_AND_GARDEN_LINK), "House and garden link is not presented"

    def guest_can_go_to_kids_toys_link(self):
        self.browser.find_element(*BasePageHeaderLocators.KIDS_TOYS_LINK)
        assert self.is_element_present(
            *BasePageHeaderLocators.KIDS_TOYS_LINK), "Kids toys link is not presented"

    def guest_can_see_ozon_banner(self):
        self.browser.find_element(*BasePageBodyLocators.OZON_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.OZON_BANNER), "Ozon banner is not presented"

    def guest_can_see_input_area(self):
        self.browser.find_element(*BasePageBodyLocators.INPUT_AREA)
        assert self.is_element_present(
            *BasePageBodyLocators.INPUT_AREA), "Input area is not presented"

    def guest_can_see_enter_button(self):
        self.browser.find_element(*BasePageBodyLocators.ENTER_BUTTON)
        assert self.is_element_present(
            *BasePageBodyLocators.ENTER_BUTTON), "Enter button is not presented"

    def guest_can_see_all_actions_link(self):
        self.browser.find_element(*BasePageBodyLocators.ALL_ACTIONS_LINK)
        assert self.is_element_present(
            *BasePageBodyLocators.ALL_ACTIONS_LINK), "All actions link is not presented"

    def guest_can_see_login_button(self):
        self.browser.find_element(*BasePageBodyLocators.LOGIN_BUTTON)
        assert self.is_element_present(
            *BasePageBodyLocators.LOGIN_BUTTON), "Login button is not presented"

    def guest_can_see_school_things_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SCHOOL_THINGS_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SCHOOL_THINGS_BANNER), "School things is not presented"

    def guest_can_see_school_and_sport_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SCHOOL_AND_SPORT_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SCHOOL_AND_SPORT_BANNER), "School and sport is not presented"

    def guest_can_see_backpacks_banner(self):
        self.browser.find_element(*BasePageBodyLocators.BACKPACKS_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.BACKPACKS_BANNER), "Backpacks banner is not presented"

    def guest_can_see_sales_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SALES_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SALES_BANNER), "Backpacks banner is not presented"

    def guest_can_see_mega_sales_banner(self):
        self.browser.find_element(*BasePageBodyLocators.MEGA_SALES_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.MEGA_SALES_BANNER), "Mega sales banner is not presented"

    def guest_can_see_super_sales_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SUPER_SALES_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SUPER_SALES_BANNER), "Super sales banner is not presented"

    def guest_can_see_save_vitamins_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SAVE_VITAMINS_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SAVE_VITAMINS_BANNER), "Save vitamins banner is not presented"

    def guest_can_go_to_your_goods_link(self):
        self.scroll(1)
        assert self.is_element_present(
            *BasePageFooterLocators.YOUR_GOODS_LINK), "Your goods link is not presented"

    def guest_can_go_to_sell_on_ozon_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.SELL_ON_OZON_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.SELL_ON_OZON_LINK), "Sell on Ozon link is not presented"

    def guest_can_go_to_referral_footer_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.REFERRAL_PROGRAM_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.REFERRAL_PROGRAM_LINK), "Referral program link in footer is not presented"

    def guest_can_go_to_ozon_box_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.SET_OZON_BOX_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.SET_OZON_BOX_LINK), "Ozon box link in footer is not presented"

    def guest_can_go_to_open_on_ozon_point_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.OPEN_ON_OZON_POINT_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.OPEN_ON_OZON_POINT_LINK), "Open on Ozon point link in footer is not presented"

    def guest_can_go_to_become_deliver_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.BECOME_DELIVER_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.BECOME_DELIVER_LINK), "Become deliver link in footer is not presented"

    def guest_can_go_to_what_sell_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.WHAT_SELL_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.WHAT_SELL_LINK), "What sell link in footer is not presented"

    def guest_can_go_to_selling_on_ozon_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.SELLING_ON_OZON_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.SELLING_ON_OZON_LINK), "Selling on Ozon link in footer is not presented"

    def guest_can_go_to_about_ozon_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.ABOUT_OZON_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.ABOUT_OZON_LINK), "About Ozon link in footer is not presented"

    def guest_can_go_to_become_courier_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.BECOME_COURIER_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.BECOME_COURIER_LINK), "Become courier link in footer is not presented"

    def guest_can_go_to_press_contracts_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.PRESS_CONTACTS_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.PRESS_CONTACTS_LINK), "Press contracts link in footer is not presented"

    def guest_can_go_to_requisites_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.REQUISITES_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.REQUISITES_LINK), "Requisites link in footer is not presented"

    def guest_can_go_to_ozon_ballon_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.OZON_BALLON_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.OZON_BALLON_LINK), "Ozon ballon link in footer is not presented"

    def guest_can_go_to_ozon_brand_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.OZON_BRAND_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.OZON_BRAND_LINK), "Ozon brand link in footer is not presented"

    def guest_can_go_to_hot_line_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.HOT_LINE_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.HOT_LINE_LINK), "Hot line link in footer is not presented"

    def guest_can_go_to_stable_development_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.STABLE_DEVELOPMENT_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.STABLE_DEVELOPMENT_LINK), "Stable development link in footer is not presented"

    def guest_can_go_to_ozon_care_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.OZON_CARE_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.OZON_CARE_LINK), "Ozon care link in footer is not presented"

    def guest_can_go_to_personal_data_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.PERSONAL_DATA_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.PERSONAL_DATA_LINK), "Personal data link in footer is not presented"

    def guest_can_go_to_how_order_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.HOW_ORDER_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.HOW_ORDER_LINK), "How order link in footer is not presented"

    def guest_can_go_to_delivery_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.DELIVERY_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.DELIVERY_LINK), "Delivery link in footer is not presented"

    def guest_can_go_to_payment_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.PAYMENT_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.PAYMENT_LINK), "Payment link in footer is not presented"

    def guest_can_go_to_contacts_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.CONTACTS_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.CONTACTS_LINK), "Contacts link in footer is not presented"

    def guest_can_go_to_safety_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.SAFETY_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.SAFETY_LINK), "Safety link in footer is not presented"

    def guest_can_go_to_all_rights_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.ALL_RIGHTS_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.ALL_RIGHTS_LINK), "All rights link in footer is not presented"

    def guest_can_go_to_vk_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.VK_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.VK_LINK), "VK link in footer is not presented"

    def guest_can_go_to_ok_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.OK_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.OK_LINK), "OK link in footer is not presented"

    def guest_can_go_to_tg_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.TG_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.TG_LINK), "TG link in footer is not presented"

    def guest_can_go_to_better_vision_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.BETTER_VISION)
        assert self.is_element_present(
            *BasePageFooterLocators.BETTER_VISION), "Better vision link in footer is not presented"

    def guest_can_go_to_stop_covid_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.STOP_COVID_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.STOP_COVID_LINK), "Stop covid link in footer is not presented"

    def guest_can_go_to_ozon_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.OZON_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.OZON_LINK), "Ozon link in footer is not presented"

    def guest_can_go_to_ozon_vacancies_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.OZON_VACANCIES_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.OZON_VACANCIES_LINK), "Ozon vacancies link in footer is not presented"

    def guest_can_go_to_route_256_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.ROUTE_256_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.ROUTE_256_LINK), "Route 256 link in footer is not presented"

    def guest_can_go_to_litres_ru_link(self):
        self.scroll(1)
        self.browser.find_element(*BasePageFooterLocators.LITRES_RU_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.LITRES_RU_LINK), "Litres.ru link in footer is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False