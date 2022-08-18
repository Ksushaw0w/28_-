from locators import ParametrizePageLocators
from base_page import BasePage


class TestParametrizePage(BasePage):
    def checking_search_field(self):
        self.browser.find_element(*ParametrizePageLocators.SEARCH_STRING)
        assert self.is_element_present(*ParametrizePageLocators.SEARCH_STRING), "Search field is not presented"

    def checking_parametrize_data(self, string):
        self.browser.find_element(*ParametrizePageLocators.SEARCH_STRING).send_keys(string)
        self.browser.find_element(*ParametrizePageLocators.SEARCH_BUTTON).click()
        assert self.is_element_present(*ParametrizePageLocators.SUCCESS_MESSAGE), 'Success message is not presented'