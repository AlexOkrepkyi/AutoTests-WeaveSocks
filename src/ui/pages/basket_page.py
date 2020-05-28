from src.ui.locators import BasketPageLocators
from src.ui.pages.base_page import BasePage


class BasketPage(BasePage):

    def verify_quantity_is_one(self):
        self.is_element_present(*BasketPageLocators.QUANTITY_FIELD)
        quantity = self._driver.find_element(*BasketPageLocators.QUANTITY_FIELD).get_attribute("value")
        assert quantity == str(1), f"{quantity} != 1"

    def proceed_to_checkout(self):
        self._driver.find_element(*BasketPageLocators.ORDER_BUTTON).click()

    def verify_is_present_alert_message_order_not_placed(self):
        alert_message = BasketPageLocators.ALERT_MESSAGE_COULD_NOT_SEND_ORDER
        assert alert_message in self._driver.page_source, f"'{alert_message}' not in page source, however it should be"
