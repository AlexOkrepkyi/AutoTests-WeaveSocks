from src.ui.locators import CataloguePageLocators
from src.ui.pages.base_page import BasePage


class CataloguePage(BasePage):

    def select_9_products_per_page(self):
        self.is_element_clickable(*CataloguePageLocators.PRODUCTS_NUMBER_9)
        self._driver.find_element(*CataloguePageLocators.PRODUCTS_NUMBER_9).click()

    def verify_all_9_products_are_present(self):
        actual_len = len(self._driver.find_elements(*CataloguePageLocators.ADD_TO_CART))
        expected_len = CataloguePageLocators.EXPECTED_PRODUCTS_QUANTITY
        assert actual_len == expected_len, f"{actual_len} != {expected_len}"

    def go_to_figueroa_socks(self):
        self._driver.find_element(*CataloguePageLocators.SOCKS_FIGUEROA).click()
