import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.ui.locators import IndexPageLocators, CataloguePageLocators
from src.ui.pages.base_page import BasePage


class IndexPage(BasePage):

    # def __init__(self, driver, url, driver_index_page):
    #     super().__init__(driver, url)
    #     self._driver_index_page = driver_index_page

    # verify elements are present

    def verify_is_present_log_in_form_button(self):
        assert self.is_element_present(*IndexPageLocators.LOGIN_FORM_BUTTON), \
            f"\n--- {IndexPageLocators.LOGIN_FORM_BUTTON} is not present ---"

    def verify_is_present_logo(self):
        assert self.is_element_present(*IndexPageLocators.LOGO), \
            f"\n--- {IndexPageLocators.LOGO} is not present ---"

    def verify_is_present_register_button(self):
        assert self.is_element_present(*IndexPageLocators.REGISTER_FORM_BUTTON), \
            f"\n--- {IndexPageLocators.REGISTER_FORM_BUTTON} is not present ---"

    def verify_is_present_tab_catalogue(self):
        assert self.is_element_present(*IndexPageLocators.TAB_CATALOGUE),\
            f"\n--- {IndexPageLocators.TAB_CATALOGUE} is not present ---"

    # footer

    def verify_footer_pages_has_expected_number_of_elements(self):
        actual_footer_pages_qty = self.count_elements(*IndexPageLocators.FOOTER_PAGES_LI)
        assert actual_footer_pages_qty == IndexPageLocators.FOOTER_PAGES_LEN,\
            f"Total elements in footer pages {actual_footer_pages_qty} " \
            f"!= expected quantity {IndexPageLocators.FOOTER_PAGES_LEN}"

    # verify sizes

    def verify_logo_has_expected_height(self):
        actual_logo_height = self.get_element_height(*IndexPageLocators.LOGO)
        expected_logo_height = IndexPageLocators.LOGO_SIZE["height"]
        assert actual_logo_height == expected_logo_height,\
            f"\n--- Actual logo size {actual_logo_height} != expected logo size {expected_logo_height}"

    def verify_logo_has_expected_width(self):
        actual_logo_width = self.get_element_width(*IndexPageLocators.LOGO)
        expected_logo_width = IndexPageLocators.LOGO_SIZE["width"]
        assert actual_logo_width == expected_logo_width,\
            f"\n--- Actual logo size {actual_logo_width} != expected logo size {expected_logo_width}"

    # to-do functions

    def click_login_button(self):
        self._driver.find_element(*IndexPageLocators.LOG_IN_BUTTON).click()

    def go_to_catalogue(self):
        self.is_element_invisible(*IndexPageLocators.LOGIN_FORM)
        self._driver.find_element(*IndexPageLocators.CATALOGUE).click()

    def login_registered_user(self, username, password):
        self.send_registered_username(username)
        self.send_registered_password(password)
        self.click_login_button()
        self.is_present_successful_login_message()

    def open_login_window(self):
        self._driver.find_element(*IndexPageLocators.LOGIN_FORM_BUTTON).click()

    def should_be_login_form(self):
        self.is_element_clickable(*IndexPageLocators.USERNAME_FIELD),\
            f"\n--- {IndexPageLocators.USERNAME_FIELD} is not clickable ---"
        self.is_element_clickable(*IndexPageLocators.PASSWORD_FIELD),\
            f"\n--- {IndexPageLocators.PASSWORD_FIELD} is not clickable ---"

    def send_registered_password(self, password):
        self._driver.find_element(*IndexPageLocators.PASSWORD_FIELD).send_keys(password)

    def send_registered_username(self, username):
        self._driver.find_element(*IndexPageLocators.USERNAME_FIELD).send_keys(username)

    # assertions - text

    def is_present_successful_login_message(self):
        actual_text = (self._driver.find_element(*IndexPageLocators.LOGIN_MESSAGE)).text
        expected_text = IndexPageLocators.LOGIN_SUCCESSFUL_TEXT
        assert actual_text == expected_text, f"\n--- '{actual_text}' != '{expected_text}' ---"

    def is_present_invalid_login_credentials_text(self):
        actual_text = (self._driver.find_element(*IndexPageLocators.LOGIN_MESSAGE)).text
        expected_text = IndexPageLocators.INVALID_LOGIN_CREDENTIALS_TEXT
        assert actual_text == expected_text, f"\n--- '{actual_text}' != '{expected_text}' ---"
