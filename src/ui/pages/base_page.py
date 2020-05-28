from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.ui.locators import BasePageLocators


class BasePage:

    def __init__(self, driver, url):
        self._driver = driver
        self._url = url

    # common functions for each page

    def count_elements(self, how, what):
        return len(self._driver.find_elements(how, what))

    def open(self):
        self._driver.get(self._url)

    def go_to_basket(self):
        self.is_element_clickable(*BasePageLocators.ITEMS_IN_BASKET)
        self._driver.find_element(*BasePageLocators.ITEMS_IN_BASKET).click()

    # 'is_element' functions

    def is_element_clickable(self, how, what):
        try:
            WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_invisible(self, how, what):
        try:
            WebDriverWait(self._driver, 5).until(EC.invisibility_of_element((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self._driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # get sizes

    def get_element_height(self, how, what):
        element_height = BasePage.get_element_size(self, how, what)["height"]
        return element_height

    def get_element_width(self, how, what):
        element_width = BasePage.get_element_size(self, how, what)["width"]
        return element_width

    def get_element_size(self, how, what):
        element_size = self._driver.find_element(how, what).size
        return element_size

