from src.ui.locators import DetailsPageLocators, CataloguePageLocators
from src.ui.pages.base_page import BasePage
from src.ui.pages.catalogue_page import CataloguePage


class DetailsPage(BasePage):

    def add_item_to_cart(self):
        self.is_element_clickable(*DetailsPageLocators.ADD_TO_CART)
        self._driver.find_element(*DetailsPageLocators.ADD_TO_CART).click()
